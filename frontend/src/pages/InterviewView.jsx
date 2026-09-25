import React, { useState, useEffect, useRef } from 'react';
import { Mic, MicOff, Send, Sparkles, RefreshCw, Award, ArrowRight, CheckCircle, AlertCircle, HelpCircle, Volume2, Video, VideoOff, ShieldAlert, Maximize, Smartphone, UserX, Eye, FileCheck, Activity, Gauge, Users, Code, Terminal, Play, Cpu, Check, X, BookOpen, Calculator, Lightbulb, LogOut, Lock, ShieldCheck, Upload, FileText } from 'lucide-react';
import * as tf from '@tensorflow/tfjs';
import * as cocoSsd from '@tensorflow-models/coco-ssd';
import CodeEditor from '../components/CodeEditor';
import CodingPracticeSection from '../components/CodingPracticeSection';
import AptitudeSection from '../components/AptitudeSection';
import CodingTestSection from '../components/CodingTestSection';

export default function InterviewView({ parsedData, onInterviewCompleted, onSessionStateChange }) {
  const [activeTabMode, setActiveTabMode] = useState('practice'); // 'practice' | 'voice' | 'coding_test' | 'aptitude'
  
  // Resume Tailored Preparation States
  const [activeResume, setActiveResume] = useState(parsedData || null);
  const [resumeLoading, setResumeLoading] = useState(false);
  const [resumeUploading, setResumeUploading] = useState(false);
  const [uploadError, setUploadError] = useState('');
  const [isResumeTailoredMode, setIsResumeTailoredMode] = useState(true);
  const resumeFileInputRef = useRef(null);

  // Voice Mode States
  const [category, setCategory] = useState('INFORMATION-TECHNOLOGY');
  const [targetRole, setTargetRole] = useState('Software Engineer');
  const [difficulty, setDifficulty] = useState('Medium');

  // Load candidate resume if not provided via props
  useEffect(() => {
    if (parsedData) {
      setActiveResume(parsedData);
      if (parsedData.predicted_category) setCategory(parsedData.predicted_category);
    } else {
      setResumeLoading(true);
      fetch('/api/interview/resume-profile')
        .then(res => res.json())
        .then(data => {
          if (data.has_resume && data.resume) {
            setActiveResume(data.resume);
            if (data.resume.predicted_category) setCategory(data.resume.predicted_category);
          }
        })
        .catch(err => console.warn('Could not load resume profile:', err))
        .finally(() => setResumeLoading(false));
    }
  }, [parsedData]);

  const handleResumeUpload = async (e) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setResumeUploading(true);
    setUploadError('');
    const formData = new FormData();
    formData.append('file', file);
    formData.append('engine', 'local');

    try {
      const res = await fetch('/api/resume/parse', {
        method: 'POST',
        body: formData
      });
      const data = await res.json();
      if (res.ok && data.data) {
        setActiveResume({
          ...data.data,
          filename: file.name
        });
        if (data.data.predicted_category) {
          setCategory(data.data.predicted_category);
        }
      } else {
        setUploadError(data.error || 'Failed to parse resume file.');
      }
    } catch (err) {
      setUploadError('Network error uploading resume: ' + err.message);
    } finally {
      setResumeUploading(false);
      if (resumeFileInputRef.current) resumeFileInputRef.current.value = '';
    }
  };

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
  const [gazeStatus, setGazeStatus] = useState('Candidate Focus: 50%');
  const [noPhoneDetected, setNoPhoneDetected] = useState(true);
  const [audioLevel, setAudioLevel] = useState(0);
  const [gazeScore, setGazeScore] = useState(50);
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
  const deviceViolationTimerRef = useRef(0);
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
        let model;
        try {
          model = await cocoSsd.load({ base: 'mobilenet_v1' });
        } catch (e1) {
          model = await cocoSsd.load({ base: 'lite_mobilenet_v2' });
        }
        if (isMounted && model) {
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

  // Anti-Escape & Anti-Tab Switch Event Listeners (100% Secure Module: Switching tabs terminates session)
  useEffect(() => {
    if (!sessionActive) return;

    const handleFullscreenChange = () => {
      if (!document.fullscreenElement) {
        console.log("Candidate full-screen toggled. Focus preserved at 50%.");
      }
    };

    const handleVisibilityChange = () => {
      if (document.hidden) {
        handleEndSession("AI Ethical Proctor Security Alert: Switching tabs or opening external applications violates the 100% secure testing policy. Session terminated.");
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
      deviceViolationTimerRef.current = 0;

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
    let electronicDeviceFound = false;
    let electronicDeviceLabel = 'Mobile Phone';

    // 1. TENSORFLOW.JS COCO-SSD MODEL DETECTION (STRICT ELECTRONIC DEVICE FINDER)
    if (cocoModelRef.current) {
      try {
        const predictions = await cocoModelRef.current.detect(video);
        const personDetections = predictions.filter(p => 
          p.class.toLowerCase() === 'person' && p.score > 0.35
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

        // Strict electronic devices & mobile phone classes
        const prohibitedElectronics = [
          'cell phone', 'mobile phone', 'phone', 'remote', 
          'telephone', 'laptop', 'tablet', 'electronic', 'book'
        ];
        
        const detectedForbidden = predictions.find(p => 
          prohibitedElectronics.includes(p.class.toLowerCase()) && p.score > 0.22
        );

        if (detectedForbidden) {
          electronicDeviceFound = true;
          electronicDeviceLabel = detectedForbidden.class.toUpperCase();
          console.warn("Prohibited electronic device detected by AI model:", detectedForbidden);
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
    let highGlowPixels = 0;

    for (let i = 0; i < data.length; i += 4) {
      const r = data[i];
      const g = data[i + 1];
      const b = data[i + 2];

      const lum = 0.299 * r + 0.587 * g + 0.114 * b;
      totalLuminance += lum;

      if (r > 60 && g > 30 && b > 15 && r > g && r > b && (Math.max(r, g, b) - Math.min(r, g, b)) > 12) {
        skinPixelCount++;
      }

      // Compact dark rectangular screen or back of phone
      if (r < 40 && g < 40 && b < 40) darkRectangularPixels++;
      // Active phone screen backlight glare
      if (r > 210 && g > 210 && b > 210 && lum > 210) highGlowPixels++;
    }

    const totalPixels = data.length / 4;
    const avgLuminance = totalLuminance / totalPixels;
    const skinRatio = skinPixelCount / totalPixels;

    // Fast Canvas Secondary Device Fallback:
    if (!electronicDeviceFound) {
      const darkRatio = darkRectangularPixels / totalPixels;
      const glowRatio = highGlowPixels / totalPixels;
      if ((darkRatio > 0.05 && darkRatio < 0.35 && glowRatio > 0.008) || (glowRatio > 0.04 && darkRatio > 0.04)) {
        electronicDeviceFound = true;
        electronicDeviceLabel = 'HANDHELD MOBILE DEVICE';
      }
    }

    // Candidate Face Visibility: Kept steady without false dropouts
    if (avgLuminance < 6 || skinRatio < 0.015) {
      setFaceDetected(false);
    } else {
      noFaceTimerRef.current = 0;
      setFaceDetected(true);
    }

    // Candidate Focus on screen: Maintained at 50% without terminating session when moving out or looking away
    setGazeScore(50);
    setGazeStatus('Candidate Focus: 50%');

    // 3. STRICT ELECTRONIC DEVICE DETECTION & AUTO-EXIT
    if (electronicDeviceFound) {
      deviceViolationTimerRef.current += 1;
      setNoPhoneDetected(false);

      if (deviceViolationTimerRef.current >= 2) {
        handleEndSession(`AI Ethical Proctor Security Violation: Prohibited electronic device (${electronicDeviceLabel}) detected in video feed! 100% secure testing standards strictly forbid secondary devices. Session terminated.`);
        return;
      }
    } else {
      deviceViolationTimerRef.current = 0;
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
          resume_skills: isResumeTailoredMode ? (activeResume?.skills || []) : [],
          candidate_name: activeResume?.candidate_name || 'Candidate',
          filename: activeResume?.filename || ''
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
      try {
        recognitionRef.current.stop();
      } catch (e) {}
    }
    setIsRecording(false);
    setUserResponse('');
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
          question: currentQuestion.question,
          question_text: currentQuestion.question,
          target_keywords: currentQuestion.target_keywords || currentQuestion.keywords || [],
          user_response: userResponse,
          user_answer: userResponse,
          candidate_name: activeResume?.candidate_name || 'Candidate',
          target_role: targetRole,
          current_difficulty: difficulty,
          asked_questions: askedQuestions,
          resume_skills: isResumeTailoredMode ? (activeResume?.skills || []) : []
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

  // FULL STRICT INTERVIEW LOCKDOWN OVERLAY - When interview starts, no other options or headers are visible
  if (sessionActive) {
    return (
      <div style={{
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100vw',
        height: '100vh',
        zIndex: 99999,
        background: '#0b0f17',
        overflowY: 'auto',
        padding: '24px 32px',
        boxSizing: 'border-box',
        display: 'flex',
        flexDirection: 'column',
        gap: '20px'
      }}>
        {/* STRICT PROCTORED INTERVIEW TOP STATUS BAR */}
        <div className="glass-card" style={{
          padding: '14px 24px',
          background: 'rgba(15, 23, 42, 0.95)',
          border: '1px solid rgba(239, 68, 68, 0.4)',
          borderRadius: '16px',
          boxShadow: '0 8px 30px rgba(0, 0, 0, 0.6)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          flexWrap: 'wrap',
          gap: '12px'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
            <div style={{
              width: '38px',
              height: '38px',
              borderRadius: '10px',
              background: 'linear-gradient(135deg, #ef4444, #f43f5e)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              boxShadow: '0 0 15px rgba(239, 68, 68, 0.5)',
              flexShrink: 0
            }}>
              <Lock size={18} color="#fff" />
            </div>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                <span style={{ fontSize: '1rem', fontWeight: 800, color: '#fff', letterSpacing: '-0.01em' }}>
                  PrepWise AI <span style={{ color: '#ef4444' }}>• Strict Proctored Interview</span>
                </span>
                <span className="badge badge-rose" style={{ fontSize: '0.68rem', padding: '2px 8px', fontWeight: 700 }}>
                  LOCKDOWN ACTIVE
                </span>
                {isResumeTailoredMode && activeResume && (
                  <span className="badge badge-emerald" style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', fontSize: '0.68rem', padding: '2px 8px' }}>
                    <Sparkles size={11} /> Resume Tailored
                  </span>
                )}
              </div>
              <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>
                Candidate: <strong style={{ color: '#fff' }}>{activeResume?.candidate_name || 'Candidate'}</strong> • Role: <strong style={{ color: '#fff' }}>{targetRole}</strong> • Navigation Strictly Restricted
              </span>
            </div>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
            <span className="badge badge-emerald" style={{ display: 'flex', alignItems: 'center', gap: '5px', padding: '6px 12px', fontSize: '0.8rem' }}>
              <ShieldCheck size={14} /> Full Anti-Cheat Proctoring Active
            </span>
            <button
              type="button"
              onClick={() => {
                if (window.confirm("Are you sure you want to exit the Strict Proctored Interview Session? All session text and active test monitoring will be closed.")) {
                  handleEndSession("Candidate formally exited the strict proctored interview session.");
                }
              }}
              className="btn-danger"
              style={{
                padding: '8px 16px',
                fontSize: '0.82rem',
                fontWeight: 700,
                display: 'flex',
                alignItems: 'center',
                gap: '6px',
                borderRadius: '8px',
                cursor: 'pointer'
              }}
              title="Exit interview and restore standard navigation"
            >
              <LogOut size={14} /> Exit Strict Interview
            </button>
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

        {/* PROCTORED INTERVIEW WORKSPACE */}
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 340px', gap: '24px', flex: 1 }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
            <div className="glass-card" style={{ padding: '28px', display: 'flex', flexDirection: 'column', gap: '20px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
                <div style={{ display: 'flex', gap: '8px', alignItems: 'center', flexWrap: 'wrap' }}>
                  <span className="badge badge-indigo">{currentQuestion?.category || 'Technical Question'}</span>
                  {currentQuestion?.is_resume_tailored && (
                    <span className="badge badge-emerald" style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                      <Sparkles size={13} /> Resume-Tailored Question
                    </span>
                  )}
                  <span className={difficulty === 'Hard' ? 'badge badge-rose' : difficulty === 'Medium' ? 'badge badge-amber' : 'badge badge-emerald'}>
                    Difficulty: {difficulty}
                  </span>
                  <span className="badge badge-emerald" style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                    <ShieldCheck size={13} /> 100% Strict Lockdown
                  </span>
                </div>

                <button
                  type="button"
                  onClick={() => {
                    if (window.confirm("Are you sure you want to exit the Strict Proctored Interview Session? All session text and active test monitoring will be closed.")) {
                      handleEndSession("Candidate formally exited the strict proctored interview session.");
                    }
                  }}
                  className="btn-danger"
                  style={{
                    padding: '7px 16px',
                    fontSize: '0.84rem',
                    fontWeight: 700,
                    display: 'flex',
                    alignItems: 'center',
                    gap: '6px',
                    borderRadius: '8px',
                    cursor: 'pointer'
                  }}
                  title="Exit interview and restore standard navigation"
                >
                  <LogOut size={15} /> Exit Strict Interview
                </button>
              </div>

              <div style={{ background: 'rgba(15, 23, 42, 0.6)', border: '1px solid var(--border-glow)', borderRadius: '12px', padding: '20px' }}>
                <h3 style={{ fontSize: '1.25rem', color: '#fff', lineHeight: 1.4 }}>"{currentQuestion?.question}"</h3>
              </div>

              <div>
                <textarea
                  placeholder="Click microphone to speak or type response..."
                  value={userResponse}
                  onChange={(e) => setUserResponse(e.target.value)}
                  onCopy={(e) => e.preventDefault()}
                  onPaste={(e) => e.preventDefault()}
                  onContextMenu={(e) => e.preventDefault()}
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

            {/* Evaluation Feedback Card */}
            {evaluation && (
              <div className="glass-card" style={{ padding: '20px', background: 'rgba(99, 102, 241, 0.1)', border: '1px solid rgba(99, 102, 241, 0.3)', marginTop: '8px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
                  <h4 style={{ color: '#fff', fontSize: '1rem', margin: 0, display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <Sparkles size={18} color="var(--primary-light)" /> AI Answer Evaluation
                  </h4>
                  <span className="badge badge-emerald">
                    Score: {evaluation.overall_score}% ({evaluation.performance_tier || 'Good'})
                  </span>
                </div>

                <p style={{ color: 'var(--text-muted)', fontSize: '0.88rem', marginBottom: '12px' }}>
                  {evaluation.feedback}
                </p>

                {evaluation.vocal_metrics && (
                  <div style={{
                    background: 'rgba(99, 102, 241, 0.12)',
                    border: '1px solid rgba(99, 102, 241, 0.3)',
                    padding: '10px 14px',
                    borderRadius: '8px',
                    marginBottom: '10px',
                    display: 'flex',
                    flexWrap: 'wrap',
                    gap: '12px',
                    alignItems: 'center',
                    fontSize: '0.8rem'
                  }}>
                    <span style={{ color: '#fff', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '4px' }}>
                      <Activity size={14} color="var(--primary-light)" /> Vocal Delivery:
                    </span>
                    <span className="badge badge-emerald">Tone: {evaluation.vocal_metrics.vocal_tone}</span>
                    <span className="badge badge-indigo">Speed: {evaluation.vocal_metrics.wpm} WPM</span>
                    <span className={evaluation.vocal_metrics.filler_count > 2 ? 'badge badge-rose' : 'badge badge-emerald'}>
                      Hesitations: {evaluation.vocal_metrics.filler_count} Filler(s)
                    </span>
                  </div>
                )}

                {evaluation.strengths && evaluation.strengths.length > 0 && (
                  <div style={{ fontSize: '0.82rem', color: '#6ee7b7', marginBottom: '4px' }}>
                    ✓ Strength: {evaluation.strengths[0]}
                  </div>
                )}

                {evaluation.areas_for_improvement && evaluation.areas_for_improvement.length > 0 && (
                  <div style={{ fontSize: '0.82rem', color: '#fbcfe8', marginTop: '4px' }}>
                    💡 Tip: {evaluation.areas_for_improvement[0]}
                  </div>
                )}
              </div>
            )}
          </div>

          {/* Right Column: Webcam Live Feed & Proctoring Panel */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <div className="glass-card" style={{ padding: '16px', textAlign: 'center', position: 'relative' }}>
              <div style={{
                position: 'relative',
                width: '100%',
                aspectRatio: '16/9',
                background: '#090d16',
                borderRadius: '12px',
                overflow: 'hidden',
                border: faceDetected ? '2px solid rgba(16, 185, 129, 0.6)' : '2px solid rgba(99, 102, 241, 0.6)'
              }}>
                <video
                  ref={videoRef}
                  autoPlay
                  playsInline
                  muted
                  style={{ width: '100%', height: '100%', objectFit: 'cover', transform: 'scaleX(-1)' }}
                />
                <canvas ref={canvasRef} style={{ display: 'none' }} />

                {/* Status Badge */}
                <div style={{
                  position: 'absolute',
                  top: '10px',
                  left: '10px',
                  background: 'rgba(15, 23, 42, 0.85)',
                  padding: '4px 10px',
                  borderRadius: '20px',
                  fontSize: '0.72rem',
                  fontWeight: 700,
                  color: !noPhoneDetected ? '#ef4444' : '#10b981',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px',
                  backdropFilter: 'blur(4px)'
                }}>
                  <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: !noPhoneDetected ? '#ef4444' : '#10b981', boxShadow: !noPhoneDetected ? '0 0 8px #ef4444' : '0 0 8px #10b981' }} />
                  {!noPhoneDetected ? 'MOBILE DEVICE FOUND' : 'CANDIDATE ACTIVE'}
                </div>

                {/* Audio Level Indicator */}
                <div style={{
                  position: 'absolute',
                  bottom: '10px',
                  left: '10px',
                  background: 'rgba(15, 23, 42, 0.85)',
                  padding: '4px 10px',
                  borderRadius: '12px',
                  fontSize: '0.72rem',
                  color: '#fff',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px',
                  backdropFilter: 'blur(4px)'
                }}>
                  <Volume2 size={12} color="#818cf8" />
                  <span>Mic: {audioLevel}%</span>
                  <div style={{ width: '40px', height: '4px', background: 'rgba(255,255,255,0.2)', borderRadius: '2px', overflow: 'hidden' }}>
                    <div style={{ width: `${audioLevel}%`, height: '100%', background: '#6366f1' }} />
                  </div>
                </div>
              </div>

              <div style={{ marginTop: '12px', textAlign: 'left' }}>
                <span style={{ fontSize: '0.84rem', fontWeight: 700, color: '#fff', display: 'block', marginBottom: '2px' }}>
                  Candidate: {activeResume?.candidate_name || 'Active Candidate'}
                </span>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                  Video & Audio Feed Live • Candidate Focus: 50%
                </span>
              </div>
            </div>

            {/* Ethical Security & Gaze Status Cards */}
            <div className="glass-card" style={{ padding: '18px', background: 'rgba(15, 23, 42, 0.65)' }}>
              <h5 style={{ color: '#fff', fontSize: '0.88rem', marginBottom: '12px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                <ShieldAlert size={16} color="#f59e0b" />
                AI Ethical & Vision Audit Panel
              </h5>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', fontSize: '0.8rem' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', color: 'var(--text-muted)' }}>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <Eye size={14} /> Candidate Focus on Screen
                  </span>
                  <span style={{ color: '#10b981', fontWeight: 700 }}>
                    50% (Standard)
                  </span>
                </div>

                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', color: 'var(--text-muted)' }}>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <Smartphone size={14} /> Mobile Phone / Device
                  </span>
                  <span style={{ color: noPhoneDetected ? '#10b981' : '#ef4444', fontWeight: 700 }}>
                    {noPhoneDetected ? 'Zero Detected' : 'Mobile Device Found'}
                  </span>
                </div>

                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', color: 'var(--text-muted)' }}>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <Volume2 size={14} /> Microphone Stream
                  </span>
                  <span style={{ color: '#10b981', fontWeight: 700 }}>Active ({audioLevel}%)</span>
                </div>

                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', color: 'var(--text-muted)' }}>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <Maximize size={14} /> Fullscreen Focus Mode
                  </span>
                  <span style={{ color: '#818cf8', fontWeight: 700 }}>Active</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      {/* Header Banner & Mode Switcher */}
      <div className="glass-card" style={{ padding: '24px 32px', background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(236, 72, 153, 0.08) 100%)' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px' }}>
          <div>
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', marginBottom: '8px' }}>
              <span className="badge badge-indigo">Module 3</span>
              <span className="badge badge-emerald">Comprehensive Preparation Suite</span>
            </div>
            <h1 style={{ fontSize: '1.8rem', fontWeight: 700, color: '#fff' }}>Preparation & Mock Interview Hub</h1>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.92rem', marginTop: '4px' }}>
              Select between <strong>Coding Practice</strong>, <strong>Voice AI Mock Interview</strong>, <strong>Timed Coding Tests</strong> or <strong>Aptitude Reasoning</strong>.
            </p>
          </div>

          {/* Mode Switcher Tabs */}
          <div style={{ display: 'flex', gap: '6px', background: 'rgba(15, 23, 42, 0.8)', padding: '6px', borderRadius: '12px', border: '1px solid var(--border-glass)', flexWrap: 'wrap' }}>
            <button
              onClick={() => setActiveTabMode('practice')}
              className={activeTabMode === 'practice' ? 'btn-primary' : 'btn-secondary'}
              style={{ padding: '8px 16px', fontSize: '0.86rem' }}
            >
              🎯 Coding Practice
            </button>
            <button
              onClick={() => setActiveTabMode('voice')}
              className={activeTabMode === 'voice' ? 'btn-primary' : 'btn-secondary'}
              style={{ padding: '8px 16px', fontSize: '0.86rem' }}
            >
              🎙️ AI Mock Interview
            </button>
            <button
              onClick={() => setActiveTabMode('coding_test')}
              className={activeTabMode === 'coding_test' || activeTabMode === 'coding' ? 'btn-primary' : 'btn-secondary'}
              style={{ padding: '8px 16px', fontSize: '0.86rem' }}
            >
              💻 Coding Test
            </button>
            <button
              onClick={() => setActiveTabMode('aptitude')}
              className={activeTabMode === 'aptitude' ? 'btn-primary' : 'btn-secondary'}
              style={{ padding: '8px 16px', fontSize: '0.86rem' }}
            >
              🧠 Aptitude Test
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
        <div className="glass-card" style={{ padding: '36px' }}>
            <div style={{ maxWidth: '680px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '22px' }}>
              <div style={{ textAlign: 'center' }}>
                <h2 style={{ fontSize: '1.45rem', fontWeight: 700, color: '#fff', marginBottom: '6px' }}>
                  Configure Your Proctored Voice Interview Session
                </h2>
                <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', margin: 0 }}>
                  Practice real-time technical and behavioral interview questions with AI evaluation.
                </p>
              </div>

              {/* RESUME-TAILORED INTERVIEW INTELLIGENCE CARD */}
              <div style={{
                background: activeResume 
                  ? 'linear-gradient(135deg, rgba(16, 185, 129, 0.12) 0%, rgba(99, 102, 241, 0.12) 100%)' 
                  : 'rgba(15, 23, 42, 0.6)',
                border: activeResume ? '1px solid rgba(16, 185, 129, 0.45)' : '1px dashed var(--border-glass)',
                borderRadius: '16px',
                padding: '20px 24px',
                boxShadow: activeResume ? '0 8px 24px -6px rgba(16, 185, 129, 0.15)' : 'none'
              }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '12px', marginBottom: activeResume ? '14px' : '0' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                    <div style={{
                      width: '42px',
                      height: '42px',
                      borderRadius: '10px',
                      background: activeResume ? 'rgba(16, 185, 129, 0.2)' : 'rgba(99, 102, 241, 0.2)',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      color: activeResume ? '#10b981' : '#818cf8',
                      flexShrink: 0
                    }}>
                      <FileText size={22} />
                    </div>
                    <div>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                        <span style={{ fontSize: '0.96rem', fontWeight: 700, color: '#fff' }}>
                          {activeResume ? 'Resume-Powered Question Mode' : 'Practice with Your Resume'}
                        </span>
                        {activeResume ? (
                          <span className="badge badge-emerald" style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', fontSize: '0.72rem', padding: '2px 8px' }}>
                            <Sparkles size={11} /> 100% Tailored
                          </span>
                        ) : (
                          <span className="badge badge-amber" style={{ fontSize: '0.72rem' }}>
                            Standard Questions
                          </span>
                        )}
                      </div>
                      <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', display: 'block', marginTop: '2px' }}>
                        {activeResume 
                          ? `Questions customized for ${activeResume.candidate_name || 'Candidate'} • ${activeResume.filename || 'Uploaded Resume'}`
                          : 'Upload your candidate resume to receive interview questions tailored to your skills & projects.'}
                      </span>
                    </div>
                  </div>

                  <div>
                    <input
                      type="file"
                      ref={resumeFileInputRef}
                      onChange={handleResumeUpload}
                      accept=".pdf,.docx,.txt"
                      style={{ display: 'none' }}
                    />
                    <button
                      type="button"
                      onClick={() => resumeFileInputRef.current?.click()}
                      disabled={resumeUploading}
                      className={activeResume ? "btn-secondary" : "btn-primary"}
                      style={{ padding: '8px 14px', fontSize: '0.82rem', display: 'flex', alignItems: 'center', gap: '6px' }}
                    >
                      <Upload size={14} />
                      {resumeUploading ? 'Parsing Resume...' : activeResume ? 'Change Resume' : 'Upload Resume'}
                    </button>
                  </div>
                </div>

                {uploadError && (
                  <div style={{ color: '#ef4444', fontSize: '0.82rem', marginTop: '10px' }}>
                    {uploadError}
                  </div>
                )}

                {activeResume && activeResume.skills && activeResume.skills.length > 0 && (
                  <div style={{ borderTop: '1px solid rgba(255, 255, 255, 0.08)', paddingTop: '12px', marginTop: '4px' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                      <span style={{ fontSize: '0.75rem', fontWeight: 600, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                        Interview Topics from Resume ({activeResume.skills.length} skills recognized)
                      </span>
                      <label style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.8rem', color: '#10b981', cursor: 'pointer', fontWeight: 600 }}>
                        <input
                          type="checkbox"
                          checked={isResumeTailoredMode}
                          onChange={(e) => setIsResumeTailoredMode(e.target.checked)}
                          style={{ accentColor: '#10b981', cursor: 'pointer' }}
                        />
                        Ask questions based on resume
                      </label>
                    </div>

                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px', maxHeight: '90px', overflowY: 'auto' }}>
                      {activeResume.skills.slice(0, 16).map((skill, idx) => (
                        <span
                          key={idx}
                          style={{
                            fontSize: '0.74rem',
                            padding: '3px 9px',
                            borderRadius: '16px',
                            background: 'rgba(16, 185, 129, 0.15)',
                            border: '1px solid rgba(16, 185, 129, 0.35)',
                            color: '#a7f3d0',
                            fontWeight: 500
                          }}
                        >
                          {skill}
                        </span>
                      ))}
                      {activeResume.skills.length > 16 && (
                        <span style={{ fontSize: '0.74rem', padding: '3px 8px', color: 'var(--text-muted)' }}>
                          +{activeResume.skills.length - 16} more
                        </span>
                      )}
                    </div>
                  </div>
                )}
              </div>

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
                  <option value="ENGINEERING" style={{ background: '#0f172a' }}>Engineering & Systems Design</option>
                  <option value="FINANCE" style={{ background: '#0f172a' }}>Finance & Quantitative Analytics</option>
                  <option value="HR" style={{ background: '#0f172a' }}>Human Resources & Talent</option>
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
                  placeholder="e.g. Senior Full-Stack Engineer, AI/ML Specialist"
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
                {loading ? 'Initializing Ethical Session...' : (activeResume && isResumeTailoredMode ? '🚀 Enter Resume-Tailored AI Voice Interview' : 'Enter Proctored AI Voice Interview')}
              </button>
            </div>
          </div>
      )}

      {/* MODE 1: CODING PRACTICE (SCREENSHOT REPLICA & RICH SOLVING STUDIO) */}
      {activeTabMode === 'practice' && (
        <CodingPracticeSection />
      )}

      {/* MODE 3: OFFICIAL TIMED CODING ASSESSMENT TEST */}
      {(activeTabMode === 'coding_test' || activeTabMode === 'coding') && (
        <CodingTestSection onTestCompleted={onInterviewCompleted} />
      )}

      {/* MODE 4: APTITUDE & REASONING TEST */}
      {activeTabMode === 'aptitude' && (
        <AptitudeSection />
      )}
    </div>
  );
}
