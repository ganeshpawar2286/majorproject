import React, { useState, useEffect } from 'react';
import {
  Code, Terminal, Play, Check, X, Sparkles, Clock, CheckCircle2,
  Award, AlertCircle, ChevronRight, ChevronLeft, RotateCcw, ArrowRight
} from 'lucide-react';
import CodeEditor from './CodeEditor';

export default function CodingTestSection({ onTestCompleted }) {
  const [testActive, setTestActive] = useState(false);
  const [loading, setLoading] = useState(false);

  // Configuration
  const [config, setConfig] = useState({
    language: 'python',
    difficulty: 'Medium',
    questionCount: 3,
    durationMinutes: 45
  });

  // Active Test State
  const [sessionId, setSessionId] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [currentQIndex, setCurrentQIndex] = useState(0);
  const [userCodes, setUserCodes] = useState({}); // { [qId]: codeString }
  const [questionSubmissions, setQuestionSubmissions] = useState({}); // { [qId]: submissionResult }
  const [secondsRemaining, setSecondsRemaining] = useState(2700);

  // Results State
  const [finalScorecard, setFinalScorecard] = useState(null);
  const [executionResult, setExecutionResult] = useState(null);
  const [executing, setExecuting] = useState(false);

  // Timer Effect
  useEffect(() => {
    if (!testActive || secondsRemaining <= 0) return;

    const timer = setInterval(() => {
      setSecondsRemaining((prev) => {
        if (prev <= 1) {
          clearInterval(timer);
          handleFinishAssessment();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [testActive, secondsRemaining]);

  const handleStartTest = async () => {
    setLoading(true);
    try {
      const res = await fetch('/api/coding/interview/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          language: config.language,
          difficulty: config.difficulty,
          topic: 'All',
          question_count: config.questionCount
        })
      });
      const data = await res.json();
      if (res.ok && data.questions && data.questions.length > 0) {
        setSessionId(data.session_id);
        setQuestions(data.questions);
        setCurrentQIndex(0);

        // Prepopulate starter codes
        const initialCodes = {};
        data.questions.forEach((q) => {
          const qid = q.id || q.questionId;
          const stubs = q.starter_code || q.starterCode || {};
          initialCodes[qid] = stubs[config.language] || stubs['python'] || Object.values(stubs)[0] || '';
        });
        setUserCodes(initialCodes);
        setQuestionSubmissions({});
        setExecutionResult(null);
        setSecondsRemaining(config.durationMinutes * 60);
        setFinalScorecard(null);
        setTestActive(true);
      }
    } catch (err) {
      console.error('Start coding assessment error:', err);
    } finally {
      setLoading(false);
    }
  };

  const currentQ = questions[currentQIndex];
  const currentQId = currentQ ? (currentQ.id || currentQ.questionId) : '';
  const currentUserCode = userCodes[currentQId] || '';

  const handleRunCode = async () => {
    if (!currentUserCode.trim() || !currentQ) return;
    setExecuting(true);
    setExecutionResult(null);

    try {
      const res = await fetch('/api/coding/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          language: config.language,
          code: currentUserCode,
          problem_id: currentQId
        })
      });
      const data = await res.json();
      if (res.ok) {
        setExecutionResult(data);
      }
    } catch (err) {
      console.error('Run code error:', err);
    } finally {
      setExecuting(false);
    }
  };

  const handleSubmitProblem = async () => {
    if (!currentUserCode.trim() || !currentQ) return;
    setExecuting(true);

    try {
      const res = await fetch('/api/coding/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          session_id: sessionId,
          question_id: currentQId,
          language: config.language,
          code: currentUserCode
        })
      });
      const data = await res.json();
      if (res.ok) {
        setQuestionSubmissions((prev) => ({
          ...prev,
          [currentQId]: data
        }));
        setExecutionResult(data);
      }
    } catch (err) {
      console.error('Submit problem error:', err);
    } finally {
      setExecuting(false);
    }
  };

  const handleFinishAssessment = () => {
    // Tally results
    let totalScore = 0;
    let totalPassed = 0;
    let totalCases = 0;

    questions.forEach((q) => {
      const qid = q.id || q.questionId;
      const sub = questionSubmissions[qid];
      if (sub) {
        totalScore += (sub.status === 'Accepted' ? 100 : (sub.score || 50));
        totalPassed += (sub.passed_test_cases || 0);
        totalCases += (sub.total_test_cases || 0);
      }
    });

    const avgScore = questions.length > 0 ? Math.round(totalScore / questions.length) : 0;
    const accuracy = totalCases > 0 ? Math.round((totalPassed / totalCases) * 100) : 0;

    const report = {
      overallScore: avgScore,
      accuracy,
      totalPassed,
      totalCases,
      questionsCount: questions.length,
      solvedCount: Object.values(questionSubmissions).filter(s => s.status === 'Accepted').length,
      timeTakenMinutes: Math.round((config.durationMinutes * 60 - secondsRemaining) / 60)
    };

    setFinalScorecard(report);
    setTestActive(false);
    if (onTestCompleted) onTestCompleted(report);
  };

  const formatTime = (secs) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  // -------------------------------------------------------------
  // VIEW: COMPLETED ASSESSMENT SCORECARD
  // -------------------------------------------------------------
  if (finalScorecard) {
    return (
      <div className="glass-card" style={{ padding: '40px', maxWidth: '780px', margin: '0 auto', textAlign: 'center' }}>
        <div style={{ display: 'inline-flex', padding: '16px', borderRadius: '50%', background: 'rgba(99, 102, 241, 0.2)', marginBottom: '14px' }}>
          <Award size={48} color="var(--primary-light)" />
        </div>

        <h2 style={{ fontSize: '2rem', color: '#fff', margin: 0 }}>Coding Assessment Complete</h2>
        <p style={{ color: 'var(--text-muted)', fontSize: '0.94rem', marginTop: '6px' }}>
          Your algorithmic submissions have been sandboxed and evaluated.
        </p>

        <div style={{ display: 'flex', justifyContent: 'center', gap: '24px', margin: '32px 0', flexWrap: 'wrap' }}>
          <div style={{ padding: '18px 26px', background: 'rgba(15, 23, 42, 0.7)', borderRadius: '14px', border: '1px solid var(--border-glass)' }}>
            <span style={{ fontSize: '0.76rem', color: 'var(--text-muted)', display: 'block' }}>OVERALL SCORE</span>
            <strong style={{ fontSize: '2.4rem', color: finalScorecard.overallScore >= 70 ? '#34d399' : '#f59e0b' }}>
              {finalScorecard.overallScore}%
            </strong>
          </div>

          <div style={{ padding: '18px 26px', background: 'rgba(15, 23, 42, 0.7)', borderRadius: '14px', border: '1px solid var(--border-glass)' }}>
            <span style={{ fontSize: '0.76rem', color: 'var(--text-muted)', display: 'block' }}>PROBLEMS SOLVED</span>
            <strong style={{ fontSize: '2.4rem', color: '#818cf8' }}>
              {finalScorecard.solvedCount} / {finalScorecard.questionsCount}
            </strong>
          </div>

          <div style={{ padding: '18px 26px', background: 'rgba(15, 23, 42, 0.7)', borderRadius: '14px', border: '1px solid var(--border-glass)' }}>
            <span style={{ fontSize: '0.76rem', color: 'var(--text-muted)', display: 'block' }}>TEST CASES PASSED</span>
            <strong style={{ fontSize: '2.4rem', color: '#34d399' }}>
              {finalScorecard.totalPassed} / {finalScorecard.totalCases}
            </strong>
          </div>
        </div>

        <div style={{ display: 'flex', justifyContent: 'center', gap: '14px' }}>
          <button
            onClick={() => {
              setFinalScorecard(null);
            }}
            className="btn-primary"
            style={{ padding: '12px 28px' }}
          >
            <RotateCcw size={16} /> Take Another Coding Assessment
          </button>
        </div>
      </div>
    );
  }

  // -------------------------------------------------------------
  // VIEW: ACTIVE CODING ASSESSMENT WORKSPACE
  // -------------------------------------------------------------
  if (testActive && currentQ) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
        {/* Test HUD Header */}
        <div className="glass-card" style={{ padding: '16px 24px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '14px' }}>
          {/* Question Switcher Tabs */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
            <span style={{ fontSize: '0.84rem', color: 'var(--text-muted)', fontWeight: 700 }}>
              TASKS:
            </span>
            {questions.map((q, idx) => {
              const qid = q.id || q.questionId;
              const sub = questionSubmissions[qid];
              const isCur = idx === currentQIndex;
              const isAccepted = sub?.status === 'Accepted';

              return (
                <button
                  key={qid}
                  onClick={() => {
                    setCurrentQIndex(idx);
                    setExecutionResult(null);
                  }}
                  style={{
                    padding: '8px 16px',
                    borderRadius: '10px',
                    background: isCur ? 'rgba(99, 102, 241, 0.3)' : 'rgba(15, 23, 42, 0.7)',
                    border: isCur ? '2px solid var(--primary-light)' : '1px solid var(--border-glass)',
                    color: isCur ? '#fff' : 'var(--text-muted)',
                    fontWeight: 700,
                    fontSize: '0.84rem',
                    cursor: 'pointer',
                    display: 'inline-flex',
                    alignItems: 'center',
                    gap: '6px'
                  }}
                >
                  {isAccepted && <Check size={14} color="#34d399" />}
                  Problem {idx + 1}
                </button>
              );
            })}
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
            {/* Timer */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              padding: '8px 18px',
              borderRadius: '12px',
              background: secondsRemaining < 300 ? 'rgba(239, 68, 68, 0.2)' : 'rgba(99, 102, 241, 0.15)',
              border: secondsRemaining < 300 ? '1px solid #ef4444' : '1px solid var(--border-glass)',
              color: secondsRemaining < 300 ? '#f87171' : '#818cf8',
              fontWeight: 800,
              fontSize: '1.05rem'
            }}>
              <Clock size={16} /> {formatTime(secondsRemaining)}
            </div>

            <button
              onClick={() => {
                if (window.confirm('Are you ready to finalize and submit all coding solutions for assessment?')) {
                  handleFinishAssessment();
                }
              }}
              className="btn-success"
              style={{ padding: '8px 20px', fontSize: '0.86rem' }}
            >
              Finish Assessment
            </button>
          </div>
        </div>

        {/* Coding Assessment Grid */}
        <div style={{ display: 'grid', gridTemplateColumns: '420px 1fr', gap: '20px' }}>
          {/* Left Column: Problem Details */}
          <div className="glass-card" style={{ padding: '24px', display: 'flex', flexDirection: 'column', gap: '16px', maxHeight: '720px', overflowY: 'auto' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span className="badge badge-indigo">{currentQ.topic || 'DSA'}</span>
              <span className={currentQ.difficulty === 'Easy' ? 'badge badge-emerald' : currentQ.difficulty === 'Hard' ? 'badge badge-rose' : 'badge badge-amber'}>
                {currentQ.difficulty}
              </span>
            </div>

            <h3 style={{ color: '#fff', fontSize: '1.25rem', margin: 0 }}>
              {currentQ.title}
            </h3>

            <p style={{ color: 'var(--text-muted)', fontSize: '0.88rem', lineHeight: 1.6, margin: 0, whiteSpace: 'pre-line' }}>
              {currentQ.description}
            </p>

            {currentQ.constraints && (
              <div style={{ background: 'rgba(15, 23, 42, 0.6)', padding: '10px 14px', borderRadius: '8px', border: '1px solid var(--border-glass)', fontSize: '0.8rem' }}>
                <strong style={{ color: '#f59e0b', display: 'block', marginBottom: '2px' }}>Constraints:</strong>
                <code>{currentQ.constraints}</code>
              </div>
            )}

            {currentQ.examples && currentQ.examples.length > 0 && (
              <div>
                <span style={{ fontSize: '0.82rem', fontWeight: 700, color: '#fff', display: 'block', marginBottom: '8px' }}>
                  Sample Example:
                </span>
                <div style={{ background: 'rgba(15, 23, 42, 0.7)', padding: '12px', borderRadius: '8px', border: '1px solid var(--border-glass)', fontSize: '0.82rem' }}>
                  <div style={{ color: '#818cf8', marginBottom: '4px' }}>Input: <code>{currentQ.examples[0].input}</code></div>
                  <div style={{ color: '#34d399' }}>Output: <code>{currentQ.examples[0].output}</code></div>
                </div>
              </div>
            )}
          </div>

          {/* Right Column: Code Editor & Execution */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
            <CodeEditor
              code={currentUserCode}
              setCode={(newCode) => setUserCodes({ ...userCodes, [currentQId]: newCode })}
              language={config.language}
              setLanguage={() => {}}
              onRunCode={handleRunCode}
              onEvaluateAi={() => {}}
              loading={executing}
            />

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px' }}>
              <button
                onClick={handleRunCode}
                disabled={executing}
                className="btn-secondary"
                style={{ padding: '8px 20px', fontSize: '0.86rem' }}
              >
                <Play size={14} /> Run Test Cases
              </button>
              <button
                onClick={handleSubmitProblem}
                disabled={executing}
                className="btn-primary"
                style={{ padding: '8px 22px', fontSize: '0.86rem' }}
              >
                <Check size={16} /> Submit Task {currentQIndex + 1}
              </button>
            </div>

            {/* Execution Status Console */}
            {executionResult && (
              <div className="glass-card" style={{ padding: '16px', background: executionResult.status === 'Accepted' ? 'rgba(16, 185, 129, 0.08)' : 'rgba(239, 68, 68, 0.08)' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span style={{ fontSize: '0.88rem', fontWeight: 700, color: executionResult.status === 'Accepted' ? '#34d399' : '#fca5a5' }}>
                    Status: {executionResult.status} ({executionResult.execution_time_ms || 0} ms)
                  </span>
                  {executionResult.total_test_cases > 0 && (
                    <span className="badge badge-emerald">
                      Cases Passed: {executionResult.passed_test_cases} / {executionResult.total_test_cases}
                    </span>
                  )}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    );
  }

  // -------------------------------------------------------------
  // DEFAULT VIEW: CONFIGURATION / START ASSESSMENT
  // -------------------------------------------------------------
  return (
    <div className="glass-card" style={{ padding: '40px', maxWidth: '680px', margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: '28px' }}>
        <div style={{ display: 'inline-flex', padding: '14px', borderRadius: '50%', background: 'rgba(99, 102, 241, 0.2)', marginBottom: '14px' }}>
          <Code size={36} color="var(--primary-light)" />
        </div>
        <h2 style={{ fontSize: '1.6rem', color: '#fff', margin: 0 }}>Configure Coding Assessment Test</h2>
        <p style={{ color: 'var(--text-muted)', fontSize: '0.88rem', marginTop: '6px' }}>
          Select language, target difficulty, and question count to launch an official timed coding test.
        </p>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
        {/* Language */}
        <div>
          <label style={{ fontSize: '0.84rem', color: 'var(--text-muted)', fontWeight: 600, display: 'block', marginBottom: '8px' }}>
            PROGRAMMING LANGUAGE
          </label>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '10px' }}>
            {['python', 'javascript', 'java', 'cpp'].map((lang) => (
              <button
                key={lang}
                onClick={() => setConfig({ ...config, language: lang })}
                style={{
                  padding: '10px',
                  borderRadius: '10px',
                  background: config.language === lang ? 'rgba(99, 102, 241, 0.25)' : 'rgba(15, 23, 42, 0.7)',
                  border: config.language === lang ? '2px solid var(--primary-light)' : '1px solid var(--border-glass)',
                  color: '#fff',
                  fontWeight: 700,
                  fontSize: '0.84rem',
                  textTransform: 'uppercase',
                  cursor: 'pointer'
                }}
              >
                {lang === 'cpp' ? 'C++' : lang}
              </button>
            ))}
          </div>
        </div>

        {/* Difficulty */}
        <div>
          <label style={{ fontSize: '0.84rem', color: 'var(--text-muted)', fontWeight: 600, display: 'block', marginBottom: '8px' }}>
            DIFFICULTY TIER
          </label>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '10px' }}>
            {['Easy', 'Medium', 'Hard'].map((diff) => (
              <button
                key={diff}
                onClick={() => setConfig({ ...config, difficulty: diff })}
                style={{
                  padding: '10px',
                  borderRadius: '10px',
                  background: config.difficulty === diff ? 'rgba(99, 102, 241, 0.25)' : 'rgba(15, 23, 42, 0.7)',
                  border: config.difficulty === diff ? '2px solid var(--primary-light)' : '1px solid var(--border-glass)',
                  color: '#fff',
                  fontWeight: 700,
                  fontSize: '0.84rem',
                  cursor: 'pointer'
                }}
              >
                {diff}
              </button>
            ))}
          </div>
        </div>

        {/* Question Count & Time */}
        <div>
          <label style={{ fontSize: '0.84rem', color: 'var(--text-muted)', fontWeight: 600, display: 'block', marginBottom: '8px' }}>
            ASSESSMENT FORMAT
          </label>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '10px' }}>
            {[
              { count: 1, mins: 25, label: '1 Problem (25m)' },
              { count: 3, mins: 45, label: '3 Problems (45m)' },
              { count: 5, mins: 75, label: '5 Problems (75m)' }
            ].map((fmt) => (
              <button
                key={fmt.count}
                onClick={() => setConfig({ ...config, questionCount: fmt.count, durationMinutes: fmt.mins })}
                style={{
                  padding: '12px 10px',
                  borderRadius: '10px',
                  background: config.questionCount === fmt.count ? 'rgba(99, 102, 241, 0.25)' : 'rgba(15, 23, 42, 0.7)',
                  border: config.questionCount === fmt.count ? '2px solid var(--primary-light)' : '1px solid var(--border-glass)',
                  color: '#fff',
                  fontWeight: 700,
                  fontSize: '0.82rem',
                  cursor: 'pointer'
                }}
              >
                {fmt.label}
              </button>
            ))}
          </div>
        </div>

        <button
          onClick={handleStartTest}
          disabled={loading}
          className="btn-primary"
          style={{ width: '100%', padding: '14px', justifyContent: 'center', fontSize: '1rem', marginTop: '12px' }}
        >
          <Play size={18} /> Launch Coding Assessment Test
        </button>
      </div>
    </div>
  );
}
