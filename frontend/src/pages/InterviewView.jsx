import React, { useState, useEffect, useRef } from 'react';
import { Mic, MicOff, Send, Sparkles, RefreshCw, Award, ArrowRight, CheckCircle, AlertCircle, HelpCircle, Volume2, Video, VideoOff, ShieldAlert, Maximize, Smartphone, UserX, Eye, FileCheck, Activity, Gauge, Users, Code, Terminal, Play, Cpu, Check, X } from 'lucide-react';
import * as tf from '@tensorflow/tfjs';
import * as cocoSsd from '@tensorflow-models/coco-ssd';
import CodeEditor from '../components/CodeEditor';

export default function InterviewView({ parsedData, onInterviewCompleted }) {
  const [activeTabMode, setActiveTabMode] = useState('voice'); // 'voice' | 'coding'
  
  // Voice Mode States
  const [category, setCategory] = useState('INFORMATION-TECHNOLOGY');
  const [targetRole, setTargetRole] = useState('Software Engineer');
  const [difficulty, setDifficulty] = useState('Medium');

  // Coding Test Mode States
  const [codingSubject, setCodingSubject] = useState('All');
  const [codingDifficulty, setCodingDifficulty] = useState('All');
  const [problemsList, setProblemsList] = useState([]);
  const [selectedProblem, setSelectedProblem] = useState(null);
  const [codeLanguage, setCodeLanguage] = useState('python');
  const [userCode, setUserCode] = useState('');
  const [executionResult, setExecutionResult] = useState(null);
  const [testCasesPassed, setTestCasesPassed] = useState(null);
  const [aiCodeAudit, setAiCodeAudit] = useState(null);
  const [codingLoading, setCodingLoading] = useState(false);

  // Common Interview States
  const [sessionActive, setSessionActive] = useState(false);
  const [sessionId, setSessionId] = useState(null);
  const [currentQuestion, setCurrentQuestion] = useState(null);
  const [askedQuestions, setAskedQuestions] = useState([]);
  
  const [userResponse, setUserResponse] = useState('');
  const [isRecording, setIsRecording] = useState(false);
  const [evaluation, setEvaluation] = useState(null);
  const [loading, setLoading] = useState(false);
  const [securityAlert, setSecurityAlert] = useState('');

  // Ethical Proctoring & Gaze Tracker Indicators
  const [faceDetected, setFaceDetected] = useState(true);
  const [personCount, setPersonCount] = useState(1);
  const [gazeStatus, setGazeStatus] = useState('Focused');
  const [noPhoneDetected, setNoPhoneDetected] = useState(true);
  const [audioLevel, setAudioLevel] = useState(0);
  const [gazeScore, setGazeScore] = useState(95);
  const [aiModelLoading, setAiModelLoading] = useState(false);

  // References
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const mediaStreamRef = useRef(null);
  const recognitionRef = useRef(null);
  const audioContextRef = useRef(null);
  const proctorIntervalRef = useRef(null);
  const noFaceTimerRef = useRef(0);
  const lookingAwayTimerRef = useRef(0);
  const multiPersonTimerRef = useRef(0);
  const cocoModelRef = useRef(null);

  // Load Coding Problems on Mount / Filter Change
  useEffect(() => {
    fetchCodingProblems();
  }, [codingSubject, codingDifficulty]);

  const fetchCodingProblems = async () => {
    try {
      const res = await fetch('/api/coding/problems', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ subject: codingSubject, difficulty: codingDifficulty })
      });
      const data = await res.json();
      if (res.ok && data.problems) {
        setProblemsList(data.problems);
        if (data.problems.length > 0) {
          const firstProb = data.problems[0];
          setSelectedProblem(firstProb);
          updateCodeStubForLanguage(firstProb, codeLanguage);
        }
      }
    } catch (err) {
      console.warn("Fetch coding problems error:", err);
    }
  };

  const updateCodeStubForLanguage = (problem, lang) => {
    if (!problem || !problem.starter_code) return;
    const stubs = problem.starter_code;
    const key = lang.toLowerCase();
    if (stubs[key]) {
      setUserCode(stubs[key]);
    } else if (stubs['python']) {
      setUserCode(stubs['python']);
    } else {
      setUserCode(Object.values(stubs)[0] || '');
    }
  };

  const handleLanguageChange = (newLang) => {
    setCodeLanguage(newLang);
    if (selectedProblem) {
      updateCodeStubForLanguage(selectedProblem, newLang);
    }
  };

  const handleSelectProblem = (prob) => {
    setSelectedProblem(prob);
    setExecutionResult(null);
    setTestCasesPassed(null);
    setAiCodeAudit(null);
    updateCodeStubForLanguage(prob, codeLanguage);
  };

  // Run Code Execution
  const handleRunCode = async () => {
    if (!userCode.trim()) return;
    setCodingLoading(true);
    setExecutionResult(null);
    setTestCasesPassed(null);

    try {
      const res = await fetch('/api/coding/execute', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          language: codeLanguage,
          code: userCode,
          problem_id: selectedProblem?.id
        })
      });
      const data = await res.json();
      if (res.ok) {
        setExecutionResult(data.execution_result);
        setTestCasesPassed(data.test_cases);
      }
    } catch (err) {
      console.error("Run code error:", err);
    } finally {
      setCodingLoading(false);
    }
  };

  // AI Big-O & Quality Audit
  const handleEvaluateAiCode = async () => {
    if (!userCode.trim()) return;
    setCodingLoading(true);
    try {
      const res = await fetch('/api/coding/evaluate-ai', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          language: codeLanguage,
          code: userCode,
          problem_title: selectedProblem?.title || 'Coding Problem'
        })
      });
      const data = await res.json();
      if (res.ok) {
        setAiCodeAudit(data.evaluation);
      }
    } catch (err) {
      console.error("AI Code Audit error:", err);
    } finally {
      setCodingLoading(false);
    }
  };

  // Load TensorFlow COCO-SSD Object Detection Model
  useEffect(() => {
    let isMounted = true;
    const loadAiModel = async () => {
      try {
        setAiModelLoading(true);
        await tf.ready();
        const model = await cocoSsd.load({ base: 'lite_mobilenet_v2' });
        if (isMounted) {
          cocoModelRef.current = model;
          console.log("TensorFlow.js COCO-SSD AI Model Loaded Successfully.");
        }
      } catch (err) {
        console.warn("TFJS Model load error (will use Canvas Vision fallback):", err);
      } finally {
        if (isMounted) setAiModelLoading(false);
      }
    };
    loadAiModel();

    return () => {
      isMounted = false;
    };
  }, []);

  // Initialize Web Speech API & Resume Context
  useEffect(() => {
    if (parsedData) {
      if (parsedData.predicted_category) setCategory(parsedData.predicted_category);
      if (parsedData.candidate_name) setTargetRole(`${parsedData.predicted_category.replace('-', ' ').toLowerCase()} Role`);
    }

    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      recognitionRef.current = new SpeechRecognition();
      recognitionRef.current.continuous = true;
      recognitionRef.current.interimResults = true;
      recognitionRef.current.lang = 'en-US';

      recognitionRef.current.onresult = (event) => {
        let finalTranscript = '';
        let interimTranscript = '';

        for (let i = 0; i < event.results.length; i++) {
          const chunk = event.results[i][0].transcript;
          if (event.results[i].isFinal) {
            finalTranscript += chunk + ' ';
          } else {
            interimTranscript += chunk;
          }
        }

        const fullText = (finalTranscript + interimTranscript).trim();
        if (fullText) {
          setUserResponse(fullText);
        }
      };

      recognitionRef.current.onerror = (err) => {
        console.error('Speech recognition error:', err);
        setIsRecording(false);
      };

      recognitionRef.current.onend = () => {
        setIsRecording(false);
      };
    }

    return () => {
      stopWebcamStream();
    };
  }, [parsedData]);

  // Anti-Escape & Anti-Tab Switch Event Listeners
  useEffect(() => {
    if (!sessionActive) return;

    const handleFullscreenChange = () => {
      if (!document.fullscreenElement) {
        handleEndSession("AI Ethical Proctor Security Alert: Exiting full-screen focus mode violates ethical interview policies. Session terminated.");
      }
    };

    const handleVisibilityChange = () => {
      if (document.hidden) {
        handleEndSession("AI Ethical Proctor Security Alert: Switching tabs or opening external applications violates ethical interview policies. Session terminated.");
      }
    };

    document.addEventListener('fullscreenchange', handleFullscreenChange);
    document.addEventListener('visibilitychange', handleVisibilityChange);

    return () => {
      document.removeEventListener('fullscreenchange', handleFullscreenChange);
      document.removeEventListener('visibilitychange', handleVisibilityChange);
    };
  }, [sessionActive]);

  // Start Webcam Stream + Vision Proctoring Loop (Every 300ms)
  const startWebcamStream = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { width: 1280, height: 720 },
        audio: true
      });
      mediaStreamRef.current = stream;

      if (videoRef.current) {
        videoRef.current.srcObject = stream;
      }

      // Audio Level Analyzer
      try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        audioContextRef.current = new AudioCtx();
        const source = audioContextRef.current.createMediaStreamSource(stream);
        const analyser = audioContextRef.current.createAnalyser();
        analyser.fftSize = 64;
        source.connect(analyser);

        const dataArray = new Uint8Array(analyser.frequencyBinCount);
        const checkAudio = () => {
          if (!mediaStreamRef.current) return;
          analyser.getByteFrequencyData(dataArray);
          let sum = 0;
          for (let i = 0; i < dataArray.length; i++) sum += dataArray[i];
          const avg = sum / dataArray.length;
          setAudioLevel(Math.min(100, Math.round((avg / 128) * 100)));
          if (sessionActive) requestAnimationFrame(checkAudio);
        };
        checkAudio();
      } catch (audioErr) {
        console.warn("Audio Context init error:", audioErr);
      }

      noFaceTimerRef.current = 0;
      lookingAwayTimerRef.current = 0;
      multiPersonTimerRef.current = 0;

      proctorIntervalRef.current = setInterval(() => {
        analyzeWebcamFrame();
      }, 300);

    } catch (err) {
      console.error("Camera/Mic access error:", err);
      setSecurityAlert("Ethical Proctor Requirement: Webcam video and microphone audio access are mandatory for ethical interview evaluation.");
    }
  };

  // Real-Time Frame Analysis: Balanced Gaze, Movement & Multi-Person Detector
  const analyzeWebcamFrame = async () => {
    if (!videoRef.current || !canvasRef.current) return;
    const video = videoRef.current;
    const canvas = canvasRef.current;

    if (video.readyState !== 4 || video.paused || video.ended) {
      noFaceTimerRef.current += 1;
      setFaceDetected(false);
      if (noFaceTimerRef.current >= 4) {
        handleEndSession("AI Ethical Proctor Alert: Camera feed was disabled or not transmitting video! Candidate face must remain visible throughout the interview.");
      }
      return;
    }

    let detectedPersonCount = 1;

    // 1. TENSORFLOW.JS COCO-SSD MODEL DETECTION
    if (cocoModelRef.current) {
      try {
        const predictions = await cocoModelRef.current.detect(video);
        const personDetections = predictions.filter(p => 
          p.class.toLowerCase() === 'person' && p.score > 0.38
        );
        
        detectedPersonCount = Math.max(1, personDetections.length);
        setPersonCount(detectedPersonCount);

        if (personDetections.length >= 2) {
          multiPersonTimerRef.current += 1;
          if (multiPersonTimerRef.current >= 3) {
            handleEndSession(`AI Ethical Proctor Security Violation: Multiple People Detected (${personDetections.length} people detected on screen)! Ethical interview policies strictly require only one candidate on screen. Session terminated.`);
            return;
          }
        } else {
          multiPersonTimerRef.current = 0;
        }

        const forbiddenClasses = ['cell phone', 'mobile phone', 'phone', 'laptop', 'remote'];
        const detectedForbidden = predictions.find(p => 
          forbiddenClasses.includes(p.class.toLowerCase()) && p.score > 0.45
        );

        if (detectedForbidden) {
          setNoPhoneDetected(false);
          handleEndSession(`AI Ethical Proctor Violation: Prohibited electronic device (${detectedForbidden.class.toUpperCase()}) detected in camera feed! Ethical interview standards strictly forbid secondary devices.`);
          return;
        }
      } catch (tfErr) {
        console.warn("TFJS detection frame skip:", tfErr);
      }
    }

    // 2. CANVAS COMPUTER VISION HEURISTICS
    const ctx = canvas.getContext('2d');
    canvas.width = 160;
    canvas.height = 90;
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    const frameData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const data = frameData.data;

    let totalLuminance = 0;
    let skinPixelCount = 0;
    let darkRectangularPixels = 0;
    let lensCirclePixels = 0;

    let leftHalfSkin = 0;
    let rightHalfSkin = 0;
    let skinSumX = 0;
    let skinSumY = 0;

    const midX = canvas.width / 2;

    for (let i = 0; i < data.length; i += 4) {
      const pixelIndex = i / 4;
      const x = pixelIndex % canvas.width;
      const y = Math.floor(pixelIndex / canvas.width);

      const r = data[i];
      const g = data[i + 1];
      const b = data[i + 2];

      const lum = 0.299 * r + 0.587 * g + 0.114 * b;
      totalLuminance += lum;

      if (r > 60 && g > 30 && b > 15 && r > g && r > b && (Math.max(r, g, b) - Math.min(r, g, b)) > 12) {
        skinPixelCount++;
        skinSumX += x;
        skinSumY += y;

        if (x < midX - 10) leftHalfSkin++;
        else if (x > midX + 10) rightHalfSkin++;
      }

      if (r < 45 && g < 45 && b < 45) darkRectangularPixels++;
      if (r > 160 && g > 160 && b > 160 && lum > 160) lensCirclePixels++;
    }

    const totalPixels = data.length / 4;
    const avgLuminance = totalLuminance / totalPixels;
    const skinRatio = skinPixelCount / totalPixels;
    const darkRatio = darkRectangularPixels / totalPixels;
    const lensRatio = lensCirclePixels / totalPixels;

    const leftSkinRatio = leftHalfSkin / totalPixels;
    const rightSkinRatio = rightHalfSkin / totalPixels;

    if (leftSkinRatio > 0.09 && rightSkinRatio > 0.09) {
      multiPersonTimerRef.current += 1;
      setPersonCount(2);
      if (multiPersonTimerRef.current >= 3) {
        handleEndSession("AI Ethical Proctor Security Violation: Multiple People Detected (2+ persons detected in camera feed)! Ethical interview policies strictly require only one candidate on screen. Session terminated.");
        return;
      }
    }

    if (avgLuminance < 6 || skinRatio < 0.015) {
      noFaceTimerRef.current += 1;
      setFaceDetected(false);
      setGazeScore(0);
      setGazeStatus('Missing / Exited Camera');

      if (noFaceTimerRef.current >= 4) {
        handleEndSession("AI Ethical Proctor Security Violation: Candidate moved off-screen or exited camera view! Candidate face must remain visible in camera throughout the interview. Session terminated.");
        return;
      }
    } else {
      noFaceTimerRef.current = 0;
      setFaceDetected(true);
    }

    const avgX = skinPixelCount > 0 ? (skinSumX / skinPixelCount) : (canvas.width / 2);
    const avgY = skinPixelCount > 0 ? (skinSumY / skinPixelCount) : (canvas.height / 2);

    const normalizedCenterX = avgX / canvas.width;
    const normalizedCenterY = avgY / canvas.height;

    const isUnfocused = (
      normalizedCenterX < 0.22 || 
      normalizedCenterX > 0.78 || 
      normalizedCenterY < 0.15 || 
      normalizedCenterY > 0.80 || 
      (leftSkinRatio > 0.80 * skinRatio) || 
      (rightSkinRatio > 0.80 * skinRatio)
    );

    if (isUnfocused) {
      lookingAwayTimerRef.current += 1;
      setGazeStatus('⚠️ Unfocused / Looking Away');
      setGazeScore(Math.max(30, 85 - (lookingAwayTimerRef.current * 12)));

      if (lookingAwayTimerRef.current >= 5) {
        handleEndSession("AI Ethical Proctor Security Violation: Candidate looking away or moving off-screen for an extended period! Candidate must maintain focus on the screen throughout the interview. Session terminated.");
        return;
      }
    } else {
      lookingAwayTimerRef.current = 0;
      setGazeStatus('Focused');
      setGazeScore(Math.min(99, Math.max(88, Math.round(skinRatio * 360))));
    }

    if (darkRatio > 0.15 && lensRatio > 0.010 && skinRatio > 0.02) {
      setNoPhoneDetected(false);
      handleEndSession("AI Ethical Proctor Violation: Prohibited electronic device (Mobile Phone / Handheld Device) detected in video feed! Ethical interview standards strictly forbid secondary devices.");
    } else {
      setNoPhoneDetected(true);
    }
  };

  const stopWebcamStream = () => {
    if (proctorIntervalRef.current) {
      clearInterval(proctorIntervalRef.current);
      proctorIntervalRef.current = null;
    }
    if (audioContextRef.current) {
      audioContextRef.current.close().catch(() => {});
      audioContextRef.current = null;
    }
    if (mediaStreamRef.current) {
      mediaStreamRef.current.getTracks().forEach(track => track.stop());
      mediaStreamRef.current = null;
    }
    if (videoRef.current) {
      videoRef.current.srcObject = null;
    }
  };

  const enterFullscreenLock = () => {
    if (document.documentElement.requestFullscreen) {
      document.documentElement.requestFullscreen().catch(err => {
        console.warn("Fullscreen request error:", err);
      });
    }
  };

  const exitFullscreenLock = () => {
    if (document.fullscreenElement && document.exitFullscreen) {
      document.exitFullscreen().catch(err => {
        console.warn("Exit fullscreen error:", err);
      });
    }
  };

  const toggleRecording = () => {
    if (!recognitionRef.current) {
      alert('Speech recognition is not supported in your browser. You can type your response in the text area.');
      return;
    }

    if (isRecording) {
      recognitionRef.current.stop();
      setIsRecording(false);
    } else {
      try {
        setUserResponse('');
        recognitionRef.current.start();
        setIsRecording(true);
      } catch (e) {
        console.error('Failed to start speech recognition:', e);
      }
    }
  };

  const handleStartSession = async () => {
    setLoading(true);
    setEvaluation(null);
    setUserResponse('');
    setAskedQuestions([]);
    setSecurityAlert('');

    try {
      const res = await fetch('/api/interview/start-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          category,
          target_role: targetRole,
          difficulty,
          resume_skills: parsedData?.skills || [],
          candidate_name: parsedData?.candidate_name || 'Candidate'
        })
      });
      const data = await res.json();
      if (res.ok) {
        setSessionId(data.session_id);
        setCurrentQuestion(data.question);
        setAskedQuestions([data.question.question]);
        setSessionActive(true);

        enterFullscreenLock();
        setTimeout(() => {
          startWebcamStream();
        }, 300);
      }
    } catch (err) {
      console.error('Start interview session error:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleEndSession = (reasonMessage) => {
    if (recognitionRef.current) {
      recognitionRef.current.stop();
    }
    setIsRecording(false);
    stopWebcamStream();
    exitFullscreenLock();
    setSessionActive(false);
    
    if (reasonMessage) {
      setSecurityAlert(reasonMessage);
    }
  };

  const handleSubmitAnswer = async () => {
    if (!userResponse.trim() || !currentQuestion) return;
    if (isRecording && recognitionRef.current) {
      recognitionRef.current.stop();
      setIsRecording(false);
    }

    setLoading(true);
    try {
      const res = await fetch('/api/interview/evaluate-answer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          session_id: sessionId,
          question_id: currentQuestion.id,
          user_answer: userResponse,
          candidate_name: parsedData?.candidate_name || 'Candidate',
          target_role: targetRole,
          asked_questions: askedQuestions
        })
      });
      const data = await res.json();
      if (res.ok) {
        setEvaluation(data.evaluation);
        if (data.next_question) {
          setCurrentQuestion(data.next_question);
          setAskedQuestions(prev => [...prev, data.next_question.question]);
          setUserResponse('');
        }
      }
    } catch (err) {
      console.error('Submit answer error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      {/* Header Banner & Mode Switcher */}
      <div className="glass-card" style={{ padding: '24px 32px', background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(236, 72, 153, 0.08) 100%)' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px' }}>
          <div>
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', marginBottom: '8px' }}>
              <span className="badge badge-indigo">Module 3</span>
              <span className="badge badge-emerald">Proctored AI Technical Suite</span>
            </div>
            <h1 style={{ fontSize: '1.8rem', fontWeight: 700, color: '#fff' }}>Proctored AI Interview & Coding Test</h1>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.92rem', marginTop: '4px' }}>
              Select between <strong>Proctored Voice AI Interviewer</strong> or <strong>Interactive Multi-Language AI Coding Test</strong>.
            </p>
          </div>

          {/* Mode Switcher Tabs */}
          <div style={{ display: 'flex', gap: '8px', background: 'rgba(15, 23, 42, 0.8)', padding: '6px', borderRadius: '12px', border: '1px solid var(--border-glass)' }}>
            <button
              onClick={() => setActiveTabMode('voice')}
              className={activeTabMode === 'voice' ? 'btn-primary' : 'btn-secondary'}
              style={{ padding: '8px 16px', fontSize: '0.86rem' }}
            >
              🎙️ Voice Interview
            </button>
            <button
              onClick={() => setActiveTabMode('coding')}
              className={activeTabMode === 'coding' ? 'btn-primary' : 'btn-secondary'}
              style={{ padding: '8px 16px', fontSize: '0.86rem' }}
            >
              💻 AI Coding Test
            </button>
          </div>
        </div>
      </div>

      {/* SECURITY VIOLATION / TERMINATION MODAL ALERT */}
      {securityAlert && (
        <div className="glass-card" style={{ padding: '24px', background: 'rgba(239, 68, 68, 0.12)', border: '2px solid rgba(239, 68, 68, 0.5)', display: 'flex', alignItems: 'flex-start', gap: '16px' }}>
          <div style={{ padding: '10px', borderRadius: '12px', background: 'rgba(239, 68, 68, 0.2)' }}>
            <ShieldAlert size={28} color="#ef4444" />
          </div>
          <div style={{ flex: 1 }}>
            <h3 style={{ color: '#ef4444', fontSize: '1.15rem', fontWeight: 700, marginBottom: '6px' }}>
              PROCTORING SECURITY VIOLATION — SESSION EXIT
            </h3>
            <p style={{ color: '#fca5a5', fontSize: '0.92rem', lineHeight: 1.5, margin: 0 }}>
              {securityAlert}
            </p>
          </div>
          <button onClick={() => setSecurityAlert('')} className="btn-secondary" style={{ padding: '6px 14px', fontSize: '0.8rem' }}>
            Dismiss Notice
          </button>
        </div>
      )}

      {/* MODE 1: PROCTORED VOICE INTERVIEW */}
      {activeTabMode === 'voice' && (
        !sessionActive ? (
          <div className="glass-card" style={{ padding: '36px' }}>
            <div style={{ maxWidth: '640px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '20px' }}>
              <h2 style={{ fontSize: '1.4rem', fontWeight: 700, color: '#fff', textAlign: 'center' }}>
                Configure Your Proctored Voice Interview Session
              </h2>

              <div>
                <label style={{ fontSize: '0.86rem', fontWeight: 600, color: 'var(--text-muted)', display: 'block', marginBottom: '8px' }}>
                  TARGET INDUSTRY DOMAIN
                </label>
                <select
                  value={category}
                  onChange={(e) => setCategory(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '12px 16px',
                    background: 'rgba(15, 23, 42, 0.7)',
                    border: '1px solid var(--border-glass)',
                    borderRadius: '10px',
                    color: '#fff',
                    outline: 'none',
                    fontSize: '0.92rem'
                  }}
                >
                  <option value="INFORMATION-TECHNOLOGY" style={{ background: '#0f172a' }}>Information Technology (IT)</option>
                  <option value="SOFTWARE-DEVELOPMENT" style={{ background: '#0f172a' }}>Software Development & Full-Stack</option>
                  <option value="DATA-SCIENCE" style={{ background: '#0f172a' }}>Data Science, AI & Machine Learning</option>
                  <option value="DEVOPS-CLOUD" style={{ background: '#0f172a' }}>DevOps & Cloud Engineering</option>
                  <option value="CYBER-SECURITY" style={{ background: '#0f172a' }}>Cybersecurity & Networking</option>
                </select>
              </div>

              <div>
                <label style={{ fontSize: '0.86rem', fontWeight: 600, color: 'var(--text-muted)', display: 'block', marginBottom: '8px' }}>
                  TARGET POSITION / ROLE TITLE
                </label>
                <input
                  type="text"
                  value={targetRole}
                  onChange={(e) => setTargetRole(e.target.value)}
                  placeholder="e.g. Senior React Developer, Python Data Engineer"
                  style={{
                    width: '100%',
                    padding: '12px 16px',
                    background: 'rgba(15, 23, 42, 0.7)',
                    border: '1px solid var(--border-glass)',
                    borderRadius: '10px',
                    color: '#fff',
                    outline: 'none',
                    fontSize: '0.92rem'
                  }}
                />
              </div>

              <div>
                <label style={{ fontSize: '0.86rem', fontWeight: 600, color: 'var(--text-muted)', display: 'block', marginBottom: '8px' }}>
                  INTERVIEW DIFFICULTY LEVEL
                </label>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '12px' }}>
                  {['Easy', 'Medium', 'Hard'].map((level) => (
                    <button
                      key={level}
                      type="button"
                      onClick={() => setDifficulty(level)}
                      className={difficulty === level ? 'btn-primary' : 'btn-secondary'}
                      style={{ padding: '10px', fontSize: '0.88rem' }}
                    >
                      {level}
                    </button>
                  ))}
                </div>
              </div>

              <button
                onClick={handleStartSession}
                disabled={loading}
                className="btn-primary"
                style={{ width: '100%', justifyContent: 'center', padding: '14px', marginTop: '12px', fontSize: '1rem' }}
              >
                {loading ? 'Initializing Ethical Session...' : 'Enter Proctored AI Voice Interview'}
              </button>
            </div>
          </div>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 340px', gap: '24px' }}>
            <div className="glass-card" style={{ padding: '28px', display: 'flex', flexDirection: 'column', gap: '20px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span className="badge badge-indigo">{currentQuestion?.category || 'Technical Question'}</span>
                <span className={difficulty === 'Hard' ? 'badge badge-rose' : difficulty === 'Medium' ? 'badge badge-amber' : 'badge badge-emerald'}>
                  Difficulty: {difficulty}
                </span>
              </div>

              <div style={{ background: 'rgba(15, 23, 42, 0.6)', border: '1px solid var(--border-glow)', borderRadius: '12px', padding: '20px' }}>
                <h3 style={{ fontSize: '1.25rem', color: '#fff', lineHeight: 1.4 }}>"{currentQuestion?.question}"</h3>
              </div>

              <div>
                <textarea
                  placeholder="Click microphone to speak or type response..."
                  value={userResponse}
                  onChange={(e) => setUserResponse(e.target.value)}
                  rows={6}
                  style={{ width: '100%', padding: '14px', background: 'rgba(15, 23, 42, 0.7)', border: '1px solid var(--border-glass)', borderRadius: '10px', color: '#fff' }}
                />
              </div>

              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <button type="button" onClick={toggleRecording} className={isRecording ? 'btn-danger' : 'btn-secondary'}>
                  {isRecording ? <MicOff size={18} /> : <Mic size={18} color="var(--primary-light)" />}
                  {isRecording ? 'Stop Recording' : 'Voice Input (STT)'}
                </button>

                <button type="button" onClick={handleSubmitAnswer} disabled={loading || !userResponse.trim()} className="btn-success">
                  {loading ? 'Evaluating...' : 'Submit Response'} <Send size={16} />
                </button>
              </div>
            </div>

            {/* Webcam Live Feed Box */}
            <div className="glass-card" style={{ padding: '16px', textAlign: 'center' }}>
              <div style={{ position: 'relative', width: '100%', aspectRatio: '16/9', background: '#090d16', borderRadius: '12px', overflow: 'hidden' }}>
                <video ref={videoRef} autoPlay playsInline muted style={{ width: '100%', height: '100%', objectFit: 'cover', transform: 'scaleX(-1)' }} />
                <canvas ref={canvasRef} style={{ display: 'none' }} />
              </div>
            </div>
          </div>
        )
      )}

      {/* MODE 2: INTERACTIVE PROCTORED AI CODING TEST */}
      {activeTabMode === 'coding' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          {/* Subject & Difficulty Selector Bar */}
          <div className="glass-card" style={{ padding: '18px 24px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '16px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '16px', flexWrap: 'wrap' }}>
              <span style={{ fontSize: '0.88rem', fontWeight: 700, color: '#fff', display: 'flex', alignItems: 'center', gap: '6px' }}>
                <Code size={18} color="var(--primary-light)" /> SUBJECT / LANGUAGE:
              </span>
              <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
                {['All', 'Python', 'Java', 'C', 'C++', 'SQL', 'DSA'].map((subj) => (
                  <button
                    key={subj}
                    onClick={() => setCodingSubject(subj)}
                    className={codingSubject === subj ? 'btn-primary' : 'btn-secondary'}
                    style={{ padding: '6px 14px', fontSize: '0.8rem' }}
                  >
                    {subj}
                  </button>
                ))}
              </div>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
              <span style={{ fontSize: '0.82rem', color: 'var(--text-muted)', fontWeight: 600 }}>DIFFICULTY:</span>
              <select
                value={codingDifficulty}
                onChange={(e) => setCodingDifficulty(e.target.value)}
                style={{ padding: '6px 12px', background: 'rgba(15, 23, 42, 0.8)', border: '1px solid var(--border-glass)', borderRadius: '6px', color: '#fff', fontSize: '0.82rem' }}
              >
                <option value="All">All Levels</option>
                <option value="Easy">Easy</option>
                <option value="Medium">Medium</option>
                <option value="Hard">Hard</option>
              </select>
            </div>
          </div>

          {/* Main Coding Workspace Grid */}
          <div style={{ display: 'grid', gridTemplateColumns: '360px 1fr', gap: '20px' }}>
            {/* Left Column: Problem Bank & Statement */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
              {/* Problem Selection List */}
              <div className="glass-card" style={{ padding: '16px' }}>
                <h4 style={{ color: '#fff', fontSize: '0.9rem', marginBottom: '12px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <Terminal size={16} color="var(--primary-light)" /> Select Problem Task ({problemsList.length})
                </h4>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', maxHeight: '180px', overflowY: 'auto' }}>
                  {problemsList.map(prob => (
                    <button
                      key={prob.id}
                      onClick={() => handleSelectProblem(prob)}
                      style={{
                        padding: '10px 14px',
                        borderRadius: '8px',
                        background: selectedProblem?.id === prob.id ? 'rgba(99, 102, 241, 0.2)' : 'rgba(15, 23, 42, 0.6)',
                        border: selectedProblem?.id === prob.id ? '1px solid var(--primary-light)' : '1px solid var(--border-glass)',
                        textAlign: 'left',
                        cursor: 'pointer',
                        display: 'flex',
                        justify: 'space-between',
                        alignItems: 'center'
                      }}
                    >
                      <div>
                        <span style={{ fontSize: '0.84rem', fontWeight: 700, color: '#fff', display: 'block' }}>{prob.title}</span>
                        <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>{prob.subject} • {prob.category}</span>
                      </div>
                      <span className={prob.difficulty === 'Easy' ? 'badge badge-emerald' : 'badge badge-amber'}>{prob.difficulty}</span>
                    </button>
                  ))}
                </div>
              </div>

              {/* Selected Problem Description Card */}
              {selectedProblem && (
                <div className="glass-card" style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <span className="badge badge-indigo">{selectedProblem.subject}</span>
                    <span className="badge badge-purple">{selectedProblem.difficulty}</span>
                  </div>

                  <h3 style={{ color: '#fff', fontSize: '1.1rem', margin: 0 }}>{selectedProblem.title}</h3>
                  <p style={{ color: 'var(--text-muted)', fontSize: '0.86rem', lineHeight: 1.5, margin: 0 }}>
                    {selectedProblem.description}
                  </p>

                  <div style={{ background: 'rgba(15, 23, 42, 0.7)', padding: '10px 14px', borderRadius: '8px', border: '1px solid var(--border-glass)', fontSize: '0.8rem' }}>
                    <strong style={{ color: '#818cf8', display: 'block', marginBottom: '2px' }}>Input Format:</strong>
                    <code style={{ color: '#e2e8f0' }}>{selectedProblem.input_format}</code>
                  </div>

                  <div style={{ background: 'rgba(15, 23, 42, 0.7)', padding: '10px 14px', borderRadius: '8px', border: '1px solid var(--border-glass)', fontSize: '0.8rem' }}>
                    <strong style={{ color: '#34d399', display: 'block', marginBottom: '2px' }}>Expected Output:</strong>
                    <code style={{ color: '#e2e8f0' }}>{selectedProblem.output_format}</code>
                  </div>
                </div>
              )}
            </div>

            {/* Right Column: Code Editor & Execution Results */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
              <CodeEditor
                code={userCode}
                setCode={setUserCode}
                language={codeLanguage}
                setLanguage={handleLanguageChange}
                onRunCode={handleRunCode}
                onEvaluateAi={handleEvaluateAiCode}
                loading={codingLoading}
              />

              {/* Execution Console & Test Case Status */}
              {executionResult && (
                <div className="glass-card" style={{ padding: '20px', background: executionResult.success ? 'rgba(16, 185, 129, 0.08)' : 'rgba(239, 68, 68, 0.08)' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
                    <span style={{ fontSize: '0.88rem', fontWeight: 700, color: executionResult.success ? '#34d399' : '#fca5a5', display: 'flex', alignItems: 'center', gap: '6px' }}>
                      {executionResult.success ? <Check size={16} /> : <X size={16} />}
                      {executionResult.success ? 'Execution Successful' : 'Execution Error'} ({executionResult.execution_time_ms} ms)
                    </span>

                    {testCasesPassed && (
                      <span className={testCasesPassed.passed === testCasesPassed.total ? 'badge badge-emerald' : 'badge badge-rose'}>
                        Test Cases Passed: {testCasesPassed.passed} / {testCasesPassed.total}
                      </span>
                    )}
                  </div>

                  {executionResult.stdout && (
                    <div style={{ background: '#090d16', padding: '12px', borderRadius: '8px', fontFamily: 'monospace', fontSize: '0.84rem', color: '#6ee7b7', whiteSpace: 'pre-wrap' }}>
                      {executionResult.stdout}
                    </div>
                  )}

                  {executionResult.stderr && (
                    <div style={{ background: '#090d16', padding: '12px', borderRadius: '8px', fontFamily: 'monospace', fontSize: '0.84rem', color: '#fca5a5', whiteSpace: 'pre-wrap' }}>
                      {executionResult.stderr}
                    </div>
                  )}
                </div>
              )}

              {/* AI Big-O Complexity & Quality Report */}
              {aiCodeAudit && (
                <div className="glass-card" style={{ padding: '20px', background: 'rgba(99, 102, 241, 0.1)', border: '1px solid rgba(99, 102, 241, 0.3)' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                    <h4 style={{ color: '#fff', fontSize: '1rem', margin: 0, display: 'flex', alignItems: 'center', gap: '6px' }}>
                      <Sparkles size={18} color="var(--primary-light)" /> AI Code Quality & Big-O Complexity Audit
                    </h4>
                    <span className="badge badge-emerald">Code Score: {aiCodeAudit.overall_code_score}%</span>
                  </div>

                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '12px', marginBottom: '12px' }}>
                    <div style={{ background: 'rgba(15, 23, 42, 0.7)', padding: '10px', borderRadius: '8px', border: '1px solid var(--border-glass)', textAlign: 'center' }}>
                      <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', display: 'block' }}>TIME COMPLEXITY</span>
                      <strong style={{ fontSize: '1.1rem', color: '#818cf8' }}>{aiCodeAudit.time_complexity}</strong>
                    </div>
                    <div style={{ background: 'rgba(15, 23, 42, 0.7)', padding: '10px', borderRadius: '8px', border: '1px solid var(--border-glass)', textAlign: 'center' }}>
                      <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', display: 'block' }}>SPACE COMPLEXITY</span>
                      <strong style={{ fontSize: '1.1rem', color: '#34d399' }}>{aiCodeAudit.space_complexity}</strong>
                    </div>
                  </div>

                  <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem', marginBottom: '10px' }}>
                    {aiCodeAudit.summary_feedback}
                  </p>

                  {aiCodeAudit.code_strengths && aiCodeAudit.code_strengths.length > 0 && (
                    <div style={{ fontSize: '0.8rem', color: '#6ee7b7', marginBottom: '4px' }}>
                      ✓ Strength: {aiCodeAudit.code_strengths[0]}
                    </div>
                  )}

                  {aiCodeAudit.refactoring_tips && aiCodeAudit.refactoring_tips.length > 0 && (
                    <div style={{ fontSize: '0.8rem', color: '#fbcfe8', marginTop: '4px' }}>
                      💡 Tip: {aiCodeAudit.refactoring_tips[0]}
                    </div>
                  )}
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
