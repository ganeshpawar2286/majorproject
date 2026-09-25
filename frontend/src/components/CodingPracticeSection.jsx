import React, { useState, useEffect } from 'react';
import {
  Code, Terminal, Play, Check, X, Sparkles, Search, ChevronDown, ChevronUp,
  RotateCcw, ArrowLeft, ExternalLink, Filter, Award, CheckCircle2, Circle
} from 'lucide-react';
import CodeEditor from './CodeEditor';

export default function CodingPracticeSection() {
  const [problems, setProblems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedProblem, setSelectedProblem] = useState(null);
  
  // Filters
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedTrack, setSelectedTrack] = useState('All');
  const [selectedTag, setSelectedTag] = useState('All');
  const [selectedDifficulty, setSelectedDifficulty] = useState('All');
  const [selectedStatus, setSelectedStatus] = useState('All');
  const [isTagsExpanded, setIsTagsExpanded] = useState(false);

  // Solved state tracking in localStorage
  const [solvedIds, setSolvedIds] = useState(() => {
    try {
      const saved = localStorage.getItem('prepwise_solved_coding_problems');
      return saved ? JSON.parse(saved) : [];
    } catch (e) {
      return [];
    }
  });

  // Code editor & execution states
  const [codeLanguage, setCodeLanguage] = useState('python');
  const [userCode, setUserCode] = useState('');
  const [customInput, setCustomInput] = useState('');
  const [showCustomInput, setShowCustomInput] = useState(false);
  const [executionResult, setExecutionResult] = useState(null);
  const [submissionResult, setSubmissionResult] = useState(null);
  const [aiCodeAudit, setAiCodeAudit] = useState(null);
  const [codeExecuting, setCodeExecuting] = useState(false);

  // Predefined Tags from Screenshot
  const ALL_TAGS = [
    '1-d Array', '2-d Array', 'Advanced Algorithms', 'Advanced Data Structures',
    'Algebra', 'Algorithms', 'Approximate', 'Arithmetic Progression', 'Arrays',
    'Backtracking', 'Basic Programming', 'Bellman Ford Algorithm', 'Binary Search',
    'Bit Manipulation', 'Dynamic Programming', 'Graph', 'Greedy', 'Hash Tables',
    'Math', 'Recursion', 'Sliding Window', 'Sorting', 'Stack', 'Trees'
  ];

  // 6 Domain Track Cards matching screenshot styling and SVG watermarks
  const TRACK_CARDS = [
    {
      id: 'Codemonk',
      title: 'Codemonk',
      gradient: 'linear-gradient(135deg, #064e3b 0%, #065f46 50%, #047857 100%)',
      glow: 'rgba(5, 150, 105, 0.4)',
      iconType: 'monkey'
    },
    {
      id: 'Basic Programming',
      title: 'Basic\nProgramming',
      gradient: 'linear-gradient(135deg, #1e3a8a 0%, #1e40af 50%, #2563eb 100%)',
      glow: 'rgba(37, 99, 235, 0.4)',
      iconType: 'brackets'
    },
    {
      id: 'Data Structures',
      title: 'Data Structures',
      gradient: 'linear-gradient(135deg, #083344 0%, #0e7490 50%, #0f766e 100%)',
      glow: 'rgba(14, 116, 144, 0.4)',
      iconType: 'tree'
    },
    {
      id: 'Algorithms',
      title: 'Algorithms',
      gradient: 'linear-gradient(135deg, #831843 0%, #9d174d 50%, #be123c 100%)',
      glow: 'rgba(190, 18, 60, 0.4)',
      iconType: 'flowchart'
    },
    {
      id: 'Math',
      title: 'Math',
      gradient: 'linear-gradient(135deg, #78350f 0%, #9a3412 50%, #b45309 100%)',
      glow: 'rgba(180, 83, 9, 0.4)',
      iconType: 'math'
    },
    {
      id: 'Mock Assessments',
      title: 'Mock\nAssessments',
      gradient: 'linear-gradient(135deg, #4c1d95 0%, #581c87 50%, #6d28d9 100%)',
      glow: 'rgba(109, 40, 217, 0.4)',
      iconType: 'checklist'
    }
  ];

  useEffect(() => {
    fetchProblems();
  }, []);

  const fetchProblems = async () => {
    try {
      setLoading(true);
      const res = await fetch('/api/coding/problems', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic: 'All', difficulty: 'All' })
      });
      const data = await res.json();
      if (res.ok && data.problems) {
        setProblems(data.problems);
      }
    } catch (err) {
      console.error('Fetch problems error:', err);
    } finally {
      setLoading(false);
    }
  };

  const updateCodeStub = (prob, lang) => {
    if (!prob) return;
    const stubs = prob.starter_code || prob.starterCode || {};
    const key = lang.toLowerCase();
    if (stubs[key]) {
      setUserCode(stubs[key]);
    } else if (stubs['python']) {
      setUserCode(stubs['python']);
    } else {
      const first = Object.values(stubs)[0];
      setUserCode(first || '# Write your solution here\n');
    }
  };

  const handleOpenProblem = (prob) => {
    setSelectedProblem(prob);
    setExecutionResult(null);
    setSubmissionResult(null);
    setAiCodeAudit(null);
    updateCodeStub(prob, codeLanguage);
  };

  const handleLanguageChange = (newLang) => {
    setCodeLanguage(newLang);
    if (selectedProblem) {
      updateCodeStub(selectedProblem, newLang);
    }
  };

  const handleRunCode = async () => {
    if (!userCode.trim() || !selectedProblem) return;
    setCodeExecuting(true);
    setExecutionResult(null);

    try {
      const res = await fetch('/api/coding/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          language: codeLanguage,
          code: userCode,
          problem_id: selectedProblem.id || selectedProblem.questionId,
          custom_input: showCustomInput ? customInput : null
        })
      });
      const data = await res.json();
      if (res.ok) {
        setExecutionResult(data);
      }
    } catch (err) {
      console.error('Run code error:', err);
    } finally {
      setCodeExecuting(false);
    }
  };

  const handleSubmitSolution = async () => {
    if (!userCode.trim() || !selectedProblem) return;
    setCodeExecuting(true);
    setSubmissionResult(null);

    try {
      const qid = selectedProblem.id || selectedProblem.questionId;
      const res = await fetch('/api/coding/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          language: codeLanguage,
          code: userCode,
          question_id: qid
        })
      });
      const data = await res.json();
      if (res.ok) {
        setSubmissionResult(data);
        if (data.status === 'Accepted' || (data.passed_test_cases && data.passed_test_cases === data.total_test_cases)) {
          // Mark as solved
          if (!solvedIds.includes(qid)) {
            const updated = [...solvedIds, qid];
            setSolvedIds(updated);
            localStorage.setItem('prepwise_solved_coding_problems', JSON.stringify(updated));
          }
        }
        if (data.ai_evaluation) {
          setAiCodeAudit(data.ai_evaluation);
        }
      }
    } catch (err) {
      console.error('Submit code error:', err);
    } finally {
      setCodeExecuting(false);
    }
  };

  const handleEvaluateAi = async () => {
    if (!userCode.trim() || !selectedProblem) return;
    setCodeExecuting(true);
    try {
      const res = await fetch('/api/coding/evaluate-ai', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          language: codeLanguage,
          code: userCode,
          problem_title: selectedProblem.title,
          problem_desc: selectedProblem.description
        })
      });
      const data = await res.json();
      if (res.ok) {
        setAiCodeAudit(data.evaluation);
      }
    } catch (err) {
      console.error('AI code audit error:', err);
    } finally {
      setCodeExecuting(false);
    }
  };

  // Filter Problem List
  const filteredProblems = problems.filter((prob) => {
    const qid = prob.id || prob.questionId;
    const isSolved = solvedIds.includes(qid);

    // Track filter
    if (selectedTrack !== 'All' && prob.track !== selectedTrack) {
      return false;
    }

    // Status filter
    if (selectedStatus === 'Solved' && !isSolved) return false;
    if (selectedStatus === 'Unsolved' && isSolved) return false;

    // Difficulty filter
    if (selectedDifficulty !== 'All') {
      const diffMap = { 'Easy': 'Easy', 'Med.': 'Medium', 'Medium': 'Medium', 'Hard': 'Hard' };
      const targetDiff = diffMap[selectedDifficulty] || selectedDifficulty;
      if (prob.difficulty !== targetDiff) return false;
    }

    // Tag filter
    if (selectedTag !== 'All') {
      const pTags = prob.tags || [];
      const matchesTag = pTags.some(t => t.toLowerCase() === selectedTag.toLowerCase()) ||
                         (prob.topic && prob.topic.toLowerCase() === selectedTag.toLowerCase());
      if (!matchesTag) return false;
    }

    // Search query
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase().trim();
      const matchTitle = prob.title && prob.title.toLowerCase().includes(q);
      const matchTopic = prob.topic && prob.topic.toLowerCase().includes(q);
      const matchTag = (prob.tags || []).some(t => t.toLowerCase().includes(q));
      if (!matchTitle && !matchTopic && !matchTag) return false;
    }

    return true;
  });

  const visibleTags = isTagsExpanded ? ALL_TAGS : ALL_TAGS.slice(0, 12);

  // SVG Watermark Renderer
  const renderCardWatermark = (type) => {
    if (type === 'monkey') {
      return (
        <svg width="88" height="88" viewBox="0 0 100 100" fill="none" opacity="0.18" style={{ position: 'absolute', right: '14px', bottom: '12px' }}>
          <circle cx="50" cy="50" r="32" stroke="#fff" strokeWidth="4" />
          <circle cx="24" cy="40" r="12" stroke="#fff" strokeWidth="4" />
          <circle cx="76" cy="40" r="12" stroke="#fff" strokeWidth="4" />
          <circle cx="42" cy="46" r="4" fill="#fff" />
          <circle cx="58" cy="46" r="4" fill="#fff" />
          <path d="M42 62 C46 68, 54 68, 58 62" stroke="#fff" strokeWidth="4" strokeLinecap="round" />
        </svg>
      );
    }
    if (type === 'brackets') {
      return (
        <svg width="88" height="88" viewBox="0 0 100 100" fill="none" opacity="0.22" style={{ position: 'absolute', right: '14px', bottom: '12px' }}>
          <path d="M36 28 C28 28, 28 36, 28 44 C28 50, 22 50, 22 50 C22 50, 28 50, 28 56 C28 64, 28 72, 36 72" stroke="#fff" strokeWidth="4" strokeLinecap="round" fill="none" />
          <path d="M64 28 C72 28, 72 36, 72 44 C72 50, 78 50, 78 50 C78 50, 72 50, 72 56 C72 64, 72 72, 64 72" stroke="#fff" strokeWidth="4" strokeLinecap="round" fill="none" />
          <path d="M45 42 L40 50 L45 58" stroke="#fff" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round" />
          <path d="M55 42 L60 50 L55 58" stroke="#fff" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      );
    }
    if (type === 'tree') {
      return (
        <svg width="88" height="88" viewBox="0 0 100 100" fill="none" opacity="0.22" style={{ position: 'absolute', right: '14px', bottom: '12px' }}>
          <circle cx="50" cy="24" r="8" stroke="#fff" strokeWidth="4" />
          <circle cx="28" cy="68" r="8" stroke="#fff" strokeWidth="4" />
          <circle cx="72" cy="68" r="8" stroke="#fff" strokeWidth="4" />
          <line x1="45" y1="31" x2="33" y2="61" stroke="#fff" strokeWidth="3" />
          <line x1="55" y1="31" x2="67" y2="61" stroke="#fff" strokeWidth="3" />
        </svg>
      );
    }
    if (type === 'flowchart') {
      return (
        <svg width="88" height="88" viewBox="0 0 100 100" fill="none" opacity="0.22" style={{ position: 'absolute', right: '14px', bottom: '12px' }}>
          <rect x="34" y="16" width="32" height="18" rx="4" stroke="#fff" strokeWidth="3" />
          <line x1="50" y1="34" x2="50" y2="48" stroke="#fff" strokeWidth="3" />
          <line x1="26" y1="48" x2="74" y2="48" stroke="#fff" strokeWidth="3" />
          <line x1="26" y1="48" x2="26" y2="60" stroke="#fff" strokeWidth="3" />
          <line x1="74" y1="48" x2="74" y2="60" stroke="#fff" strokeWidth="3" />
          <rect x="14" y="60" width="24" height="16" rx="3" stroke="#fff" strokeWidth="3" />
          <rect x="62" y="60" width="24" height="16" rx="3" stroke="#fff" strokeWidth="3" />
        </svg>
      );
    }
    if (type === 'math') {
      return (
        <svg width="88" height="88" viewBox="0 0 100 100" fill="none" opacity="0.22" style={{ position: 'absolute', right: '14px', bottom: '12px' }}>
          <line x1="20" y1="80" x2="80" y2="80" stroke="#fff" strokeWidth="4" />
          <line x1="20" y1="80" x2="20" y2="20" stroke="#fff" strokeWidth="4" />
          <line x1="20" y1="20" x2="80" y2="80" stroke="#fff" strokeWidth="3" strokeDasharray="5 5" />
          <path d="M56 46 A 24 24 0 0 0 76 76" stroke="#fff" strokeWidth="3" fill="none" />
          <circle cx="76" cy="46" r="3" fill="#fff" />
        </svg>
      );
    }
    return (
      <svg width="88" height="88" viewBox="0 0 100 100" fill="none" opacity="0.22" style={{ position: 'absolute', right: '14px', bottom: '12px' }}>
        <rect x="26" y="24" width="48" height="60" rx="6" stroke="#fff" strokeWidth="4" />
        <rect x="38" y="16" width="24" height="12" rx="3" stroke="#fff" strokeWidth="4" />
        <path d="M36 44 L42 50 L52 38" stroke="#fff" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />
        <line x1="58" y1="44" x2="66" y2="44" stroke="#fff" strokeWidth="3" strokeLinecap="round" />
        <path d="M36 62 L42 68 L52 56" stroke="#fff" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />
        <line x1="58" y1="62" x2="66" y2="62" stroke="#fff" strokeWidth="3" strokeLinecap="round" />
      </svg>
    );
  };

  // If a problem is selected for solving, render the Code Studio
  if (selectedProblem) {
    const qid = selectedProblem.id || selectedProblem.questionId;
    const isSolved = solvedIds.includes(qid);

    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
        {/* Studio Top Navigation */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '14px' }}>
          <button
            onClick={() => setSelectedProblem(null)}
            className="btn-secondary"
            style={{ padding: '8px 16px', fontSize: '0.86rem' }}
          >
            <ArrowLeft size={16} /> Back to Practice Challenges
          </button>

          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            {isSolved && (
              <span className="badge badge-emerald" style={{ fontSize: '0.82rem' }}>
                <CheckCircle2 size={14} /> Solved Challenge
              </span>
            )}
            <span className={selectedProblem.difficulty === 'Easy' ? 'badge badge-emerald' : selectedProblem.difficulty === 'Hard' ? 'badge badge-rose' : 'badge badge-amber'}>
              {selectedProblem.difficulty}
            </span>
            <span className="badge badge-indigo">
              {selectedProblem.topic || selectedProblem.track || 'DSA'}
            </span>
          </div>
        </div>

        {/* Studio Main Workspace Grid */}
        <div style={{ display: 'grid', gridTemplateColumns: '420px 1fr', gap: '22px' }}>
          {/* Left Column: Problem Statement & Test Cases */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <div className="glass-card" style={{ padding: '24px', display: 'flex', flexDirection: 'column', gap: '16px', maxHeight: '780px', overflowY: 'auto' }}>
              <div>
                <span style={{ fontSize: '0.74rem', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.06em', fontWeight: 700 }}>
                  PROBLEM STATEMENT
                </span>
                <h2 style={{ fontSize: '1.4rem', color: '#fff', marginTop: '4px' }}>
                  {selectedProblem.title}
                </h2>
              </div>

              <div style={{ display: 'flex', gap: '16px', padding: '10px 14px', background: 'rgba(15, 23, 42, 0.6)', borderRadius: '10px', border: '1px solid var(--border-glass)', fontSize: '0.82rem' }}>
                <div>
                  <span style={{ color: 'var(--text-muted)', display: 'block' }}>Attempted</span>
                  <strong style={{ color: '#fff' }}>{selectedProblem.attempted || '12k'}</strong>
                </div>
                <div style={{ borderLeft: '1px solid var(--border-glass)', paddingLeft: '16px' }}>
                  <span style={{ color: 'var(--text-muted)', display: 'block' }}>Acceptance</span>
                  <strong style={{ color: '#34d399' }}>{selectedProblem.acceptance || '65%'}</strong>
                </div>
                <div style={{ borderLeft: '1px solid var(--border-glass)', paddingLeft: '16px' }}>
                  <span style={{ color: 'var(--text-muted)', display: 'block' }}>Track</span>
                  <strong style={{ color: '#818cf8' }}>{selectedProblem.track || 'Practice'}</strong>
                </div>
              </div>

              <div>
                <h4 style={{ fontSize: '0.9rem', color: '#fff', marginBottom: '8px' }}>Description</h4>
                <p style={{ color: 'var(--text-muted)', fontSize: '0.88rem', lineHeight: '1.6', margin: 0, whiteSpace: 'pre-line' }}>
                  {selectedProblem.description}
                </p>
              </div>

              {selectedProblem.constraints && (
                <div style={{ background: 'rgba(15, 23, 42, 0.7)', padding: '12px 16px', borderRadius: '10px', border: '1px solid var(--border-glass)' }}>
                  <span style={{ fontSize: '0.78rem', color: '#f59e0b', fontWeight: 700, display: 'block', marginBottom: '4px' }}>
                    CONSTRAINTS
                  </span>
                  <code style={{ fontSize: '0.82rem', color: '#e2e8f0', fontFamily: 'monospace' }}>
                    {selectedProblem.constraints}
                  </code>
                </div>
              )}

              {selectedProblem.inputFormat && (
                <div style={{ background: 'rgba(15, 23, 42, 0.7)', padding: '12px 16px', borderRadius: '10px', border: '1px solid var(--border-glass)' }}>
                  <span style={{ fontSize: '0.78rem', color: '#818cf8', fontWeight: 700, display: 'block', marginBottom: '4px' }}>
                    INPUT FORMAT
                  </span>
                  <p style={{ fontSize: '0.82rem', color: '#cbd5e1', margin: 0 }}>
                    {selectedProblem.inputFormat}
                  </p>
                </div>
              )}

              {selectedProblem.outputFormat && (
                <div style={{ background: 'rgba(15, 23, 42, 0.7)', padding: '12px 16px', borderRadius: '10px', border: '1px solid var(--border-glass)' }}>
                  <span style={{ fontSize: '0.78rem', color: '#34d399', fontWeight: 700, display: 'block', marginBottom: '4px' }}>
                    OUTPUT FORMAT
                  </span>
                  <p style={{ fontSize: '0.82rem', color: '#cbd5e1', margin: 0 }}>
                    {selectedProblem.outputFormat}
                  </p>
                </div>
              )}

              {/* Sample Examples */}
              {selectedProblem.examples && selectedProblem.examples.length > 0 && (
                <div>
                  <h4 style={{ fontSize: '0.9rem', color: '#fff', marginBottom: '10px' }}>Sample Examples</h4>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                    {selectedProblem.examples.map((ex, idx) => (
                      <div key={idx} style={{ background: 'rgba(15, 23, 42, 0.8)', padding: '12px', borderRadius: '8px', border: '1px solid var(--border-glass)', fontSize: '0.82rem' }}>
                        <div style={{ marginBottom: '6px' }}>
                          <span style={{ color: 'var(--text-muted)', display: 'block', fontSize: '0.72rem' }}>INPUT:</span>
                          <code style={{ color: '#818cf8', fontFamily: 'monospace' }}>{ex.input}</code>
                        </div>
                        <div style={{ marginBottom: '6px' }}>
                          <span style={{ color: 'var(--text-muted)', display: 'block', fontSize: '0.72rem' }}>OUTPUT:</span>
                          <code style={{ color: '#34d399', fontFamily: 'monospace' }}>{ex.output}</code>
                        </div>
                        {ex.explanation && (
                          <div>
                            <span style={{ color: 'var(--text-muted)', display: 'block', fontSize: '0.72rem' }}>EXPLANATION:</span>
                            <span style={{ color: '#cbd5e1' }}>{ex.explanation}</span>
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Right Column: Code Editor, Execution Controls, Submission & AI Audit */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <CodeEditor
              code={userCode}
              setCode={setUserCode}
              language={codeLanguage}
              setLanguage={handleLanguageChange}
              onRunCode={handleRunCode}
              onEvaluateAi={handleEvaluateAi}
              loading={codeExecuting}
            />

            {/* Custom Input & Action Strip */}
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '12px', padding: '12px 18px', background: 'rgba(15, 23, 42, 0.7)', borderRadius: '12px', border: '1px solid var(--border-glass)' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <button
                  onClick={() => setShowCustomInput(!showCustomInput)}
                  className="btn-secondary"
                  style={{ padding: '6px 14px', fontSize: '0.8rem' }}
                >
                  {showCustomInput ? 'Hide Custom Input' : 'Use Custom Test Input'}
                </button>
                <button
                  onClick={() => updateCodeStub(selectedProblem, codeLanguage)}
                  className="btn-secondary"
                  title="Reset to starter code"
                  style={{ padding: '6px 12px', fontSize: '0.8rem' }}
                >
                  <RotateCcw size={14} /> Reset Code
                </button>
              </div>

              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <button
                  onClick={handleRunCode}
                  disabled={codeExecuting}
                  className="btn-primary"
                  style={{ padding: '8px 20px', fontSize: '0.86rem' }}
                >
                  <Play size={14} /> Run Code
                </button>
                <button
                  onClick={handleSubmitSolution}
                  disabled={codeExecuting}
                  className="btn-success"
                  style={{ padding: '8px 22px', fontSize: '0.86rem' }}
                >
                  <Check size={16} /> Submit Solution
                </button>
              </div>
            </div>

            {showCustomInput && (
              <div className="glass-card" style={{ padding: '14px' }}>
                <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)', display: 'block', marginBottom: '6px', fontWeight: 600 }}>
                  CUSTOM INPUT (STDIN)
                </span>
                <textarea
                  value={customInput}
                  onChange={(e) => setCustomInput(e.target.value)}
                  placeholder="Provide test input lines here..."
                  style={{
                    width: '100%',
                    minHeight: '80px',
                    padding: '10px',
                    fontFamily: 'monospace',
                    fontSize: '0.84rem'
                  }}
                />
              </div>
            )}

            {/* Run Code Execution Console */}
            {executionResult && (
              <div className="glass-card" style={{ padding: '20px', background: executionResult.status === 'Accepted' || executionResult.passed_test_cases > 0 ? 'rgba(16, 185, 129, 0.08)' : 'rgba(239, 68, 68, 0.08)', border: '1px solid var(--border-glass)' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
                  <span style={{ fontSize: '0.9rem', fontWeight: 700, color: executionResult.status === 'Accepted' ? '#34d399' : '#fca5a5', display: 'flex', alignItems: 'center', gap: '6px' }}>
                    {executionResult.status === 'Accepted' ? <Check size={16} /> : <X size={16} />}
                    Status: {executionResult.status} ({executionResult.execution_time_ms || executionResult.execution_time || 0} ms)
                  </span>

                  {executionResult.total_test_cases > 0 && (
                    <span className={executionResult.passed_test_cases === executionResult.total_test_cases ? 'badge badge-emerald' : 'badge badge-amber'}>
                      Public Cases Passed: {executionResult.passed_test_cases} / {executionResult.total_test_cases}
                    </span>
                  )}
                </div>

                {executionResult.test_case_results && executionResult.test_case_results.length > 0 && (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', marginTop: '10px' }}>
                    {executionResult.test_case_results.map((tc, idx) => (
                      <div key={idx} style={{ background: '#090d16', padding: '10px 14px', borderRadius: '8px', fontSize: '0.82rem', fontFamily: 'monospace' }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '4px' }}>
                          <span style={{ color: 'var(--text-muted)' }}>Case #{idx + 1}</span>
                          <span style={{ color: tc.passed ? '#34d399' : '#f87171', fontWeight: 700 }}>
                            {tc.passed ? 'PASSED' : 'FAILED'}
                          </span>
                        </div>
                        <div style={{ color: '#818cf8' }}>Input: {tc.input}</div>
                        <div style={{ color: '#34d399' }}>Expected: {tc.expected_output}</div>
                        <div style={{ color: '#e2e8f0' }}>Your Output: {tc.actual_output || '<none>'}</div>
                      </div>
                    ))}
                  </div>
                )}

                {executionResult.error_message && (
                  <div style={{ marginTop: '10px', background: '#2d0607', color: '#fca5a5', padding: '12px', borderRadius: '8px', fontFamily: 'monospace', fontSize: '0.82rem' }}>
                    {executionResult.error_message}
                  </div>
                )}
              </div>
            )}

            {/* Official Submission Results */}
            {submissionResult && (
              <div className="glass-card" style={{ padding: '22px', background: submissionResult.status === 'Accepted' ? 'rgba(16, 185, 129, 0.12)' : 'rgba(239, 68, 68, 0.12)', border: submissionResult.status === 'Accepted' ? '1px solid rgba(16, 185, 129, 0.4)' : '1px solid rgba(239, 68, 68, 0.4)' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                    <div style={{ width: '32px', height: '32px', borderRadius: '50%', background: submissionResult.status === 'Accepted' ? '#10b981' : '#ef4444', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                      {submissionResult.status === 'Accepted' ? <Check size={18} color="#fff" /> : <X size={18} color="#fff" />}
                    </div>
                    <div>
                      <h3 style={{ fontSize: '1.1rem', color: '#fff', margin: 0 }}>
                        {submissionResult.status === 'Accepted' ? 'Submission Accepted!' : `Submission Status: ${submissionResult.status}`}
                      </h3>
                      <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)' }}>
                        Validated against all public & secret test suites
                      </span>
                    </div>
                  </div>

                  <span className={submissionResult.status === 'Accepted' ? 'badge badge-emerald' : 'badge badge-rose'} style={{ fontSize: '0.88rem', padding: '6px 16px' }}>
                    {submissionResult.passed_test_cases} / {submissionResult.total_test_cases} Test Cases Passed
                  </span>
                </div>
              </div>
            )}

            {/* AI Big-O & Quality Audit */}
            {aiCodeAudit && (
              <div className="glass-card" style={{ padding: '22px', background: 'rgba(99, 102, 241, 0.08)', border: '1px solid rgba(99, 102, 241, 0.3)' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px' }}>
                  <h4 style={{ color: '#fff', fontSize: '1.05rem', margin: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <Sparkles size={18} color="var(--primary-light)" /> AI Code Quality & Big-O Complexity Audit
                  </h4>
                  <span className="badge badge-emerald" style={{ fontSize: '0.84rem' }}>
                    Overall Score: {aiCodeAudit.overall_code_score || aiCodeAudit.overall_score || 85}%
                  </span>
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '14px', marginBottom: '14px' }}>
                  <div style={{ background: 'rgba(15, 23, 42, 0.7)', padding: '12px', borderRadius: '8px', border: '1px solid var(--border-glass)', textAlign: 'center' }}>
                    <span style={{ fontSize: '0.74rem', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>TIME COMPLEXITY</span>
                    <strong style={{ fontSize: '1.25rem', color: '#818cf8' }}>{aiCodeAudit.time_complexity || 'O(N)'}</strong>
                  </div>
                  <div style={{ background: 'rgba(15, 23, 42, 0.7)', padding: '12px', borderRadius: '8px', border: '1px solid var(--border-glass)', textAlign: 'center' }}>
                    <span style={{ fontSize: '0.74rem', color: 'var(--text-muted)', display: 'block', fontWeight: 600 }}>SPACE COMPLEXITY</span>
                    <strong style={{ fontSize: '1.25rem', color: '#34d399' }}>{aiCodeAudit.space_complexity || 'O(1)'}</strong>
                  </div>
                </div>

                <p style={{ color: 'var(--text-muted)', fontSize: '0.86rem', lineHeight: '1.5', marginBottom: '10px' }}>
                  {aiCodeAudit.summary_feedback || aiCodeAudit.explanation || 'Clean algorithmic approach with solid variable conventions.'}
                </p>

                {aiCodeAudit.code_strengths && aiCodeAudit.code_strengths.length > 0 && (
                  <div style={{ fontSize: '0.82rem', color: '#6ee7b7', marginTop: '6px' }}>
                    ✓ Strength: {aiCodeAudit.code_strengths[0]}
                  </div>
                )}

                {aiCodeAudit.refactoring_tips && aiCodeAudit.refactoring_tips.length > 0 && (
                  <div style={{ fontSize: '0.82rem', color: '#fbcfe8', marginTop: '4px' }}>
                    💡 Optimization Tip: {aiCodeAudit.refactoring_tips[0]}
                  </div>
                )}
              </div>
            )}
          </div>
        </div>
      </div>
    );
  }

  // DEFAULT VIEW: Practice Catalog matching the Screenshot precisely!
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '26px' }}>
      {/* Top Heading */}
      <div style={{ display: 'flex', alignItems: 'baseline', gap: '16px', flexWrap: 'wrap' }}>
        <h1 style={{ fontSize: '2.1rem', fontWeight: 800, color: '#fff', letterSpacing: '-0.02em', margin: 0 }}>
          Practice
        </h1>
        <span style={{ color: '#64748b', fontSize: '1.4rem', fontWeight: 300 }}>|</span>
        <p style={{ color: 'var(--text-muted)', fontSize: '1rem', fontWeight: 500, margin: 0 }}>
          Sharpen your skills through hands-on coding practice
        </p>
      </div>

      {/* 6 Gradient Domain Track Cards */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))',
        gap: '18px'
      }}>
        {TRACK_CARDS.map((card) => {
          const isSelected = selectedTrack === card.id;
          return (
            <div
              key={card.id}
              onClick={() => setSelectedTrack(isSelected ? 'All' : card.id)}
              style={{
                position: 'relative',
                background: card.gradient,
                borderRadius: '16px',
                padding: '28px 24px',
                minHeight: '120px',
                display: 'flex',
                alignItems: 'center',
                cursor: 'pointer',
                overflow: 'hidden',
                boxShadow: isSelected ? `0 0 0 2px #fff, 0 8px 30px ${card.glow}` : '0 6px 20px rgba(0,0,0,0.35)',
                transition: 'all 0.25s cubic-bezier(0.4, 0, 0.2, 1)',
                transform: isSelected ? 'scale(1.02)' : 'scale(1)'
              }}
              onMouseEnter={(e) => {
                if (!isSelected) e.currentTarget.style.transform = 'translateY(-3px)';
              }}
              onMouseLeave={(e) => {
                if (!isSelected) e.currentTarget.style.transform = 'scale(1)';
              }}
            >
              <h2 style={{
                color: '#fff',
                fontSize: '1.45rem',
                fontWeight: 700,
                lineHeight: 1.2,
                whiteSpace: 'pre-line',
                zIndex: 2,
                margin: 0
              }}>
                {card.title}
              </h2>

              {/* Watermark SVG */}
              {renderCardWatermark(card.iconType)}
            </div>
          );
        })}
      </div>

      {/* Filter Tag Pills Bar */}
      <div style={{ display: 'flex', flexWrap: 'wrap', alignItems: 'center', gap: '8px' }}>
        <button
          onClick={() => setSelectedTag('All')}
          style={{
            padding: '6px 14px',
            borderRadius: '20px',
            fontSize: '0.82rem',
            fontWeight: 600,
            background: selectedTag === 'All' ? 'rgba(99, 102, 241, 0.3)' : 'rgba(255, 255, 255, 0.05)',
            color: selectedTag === 'All' ? '#818cf8' : 'var(--text-muted)',
            border: selectedTag === 'All' ? '1px solid var(--primary-light)' : '1px solid var(--border-glass)',
            cursor: 'pointer',
            transition: 'all 0.2s ease'
          }}
        >
          All Topics
        </button>

        {visibleTags.map((tag) => {
          const isSelected = selectedTag === tag;
          return (
            <button
              key={tag}
              onClick={() => setSelectedTag(isSelected ? 'All' : tag)}
              style={{
                padding: '6px 14px',
                borderRadius: '20px',
                fontSize: '0.82rem',
                fontWeight: 500,
                background: isSelected ? 'rgba(99, 102, 241, 0.3)' : 'rgba(255, 255, 255, 0.05)',
                color: isSelected ? '#818cf8' : 'var(--text-muted)',
                border: isSelected ? '1px solid var(--primary-light)' : '1px solid var(--border-glass)',
                cursor: 'pointer',
                transition: 'all 0.2s ease'
              }}
            >
              {tag}
            </button>
          );
        })}

        <button
          onClick={() => setIsTagsExpanded(!isTagsExpanded)}
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '4px',
            padding: '6px 12px',
            borderRadius: '20px',
            fontSize: '0.82rem',
            color: 'var(--text-muted)',
            background: 'transparent',
            border: 'none',
            cursor: 'pointer'
          }}
        >
          {isTagsExpanded ? 'Collapse' : 'Expand'} {isTagsExpanded ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
        </button>
      </div>

      {/* Secondary Filter Controls: Status, Difficulty & Search */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '14px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', flexWrap: 'wrap' }}>
          {/* Status Dropdown */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <select
              value={selectedStatus}
              onChange={(e) => setSelectedStatus(e.target.value)}
              style={{
                padding: '8px 14px',
                borderRadius: '10px',
                fontSize: '0.86rem',
                fontWeight: 600,
                background: 'rgba(15, 23, 42, 0.8)',
                border: '1px solid var(--border-glass)',
                color: '#fff',
                cursor: 'pointer'
              }}
            >
              <option value="All">Status: All</option>
              <option value="Solved">Solved</option>
              <option value="Unsolved">Unsolved</option>
            </select>
          </div>

          {/* Difficulty Dropdown */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <select
              value={selectedDifficulty}
              onChange={(e) => setSelectedDifficulty(e.target.value)}
              style={{
                padding: '8px 14px',
                borderRadius: '10px',
                fontSize: '0.86rem',
                fontWeight: 600,
                background: 'rgba(15, 23, 42, 0.8)',
                border: '1px solid var(--border-glass)',
                color: '#fff',
                cursor: 'pointer'
              }}
            >
              <option value="All">Difficulty: All</option>
              <option value="Easy">Easy</option>
              <option value="Med.">Medium</option>
              <option value="Hard">Hard</option>
            </select>
          </div>

          {(selectedTrack !== 'All' || selectedTag !== 'All' || selectedDifficulty !== 'All' || selectedStatus !== 'All' || searchQuery) && (
            <button
              onClick={() => {
                setSelectedTrack('All');
                setSelectedTag('All');
                setSelectedDifficulty('All');
                setSelectedStatus('All');
                setSearchQuery('');
              }}
              className="btn-secondary"
              style={{ padding: '6px 12px', fontSize: '0.78rem' }}
            >
              Reset Filters
            </button>
          )}
        </div>

        {/* Search Box */}
        <div style={{ position: 'relative', width: '280px' }}>
          <Search size={16} color="var(--text-muted)" style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)' }} />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search problems by name or tag..."
            style={{
              width: '100%',
              padding: '8px 14px 8px 36px',
              fontSize: '0.86rem',
              borderRadius: '10px',
              background: 'rgba(15, 23, 42, 0.7)'
            }}
          />
        </div>
      </div>

      {/* Problem Catalog Table */}
      <div className="glass-card" style={{ padding: '0', overflow: 'hidden' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
          <thead>
            <tr style={{ borderBottom: '1px solid var(--border-glass)', background: 'rgba(15, 23, 42, 0.8)' }}>
              <th style={{ padding: '16px 20px', fontSize: '0.76rem', color: 'var(--text-muted)', fontWeight: 700, letterSpacing: '0.05em', width: '60px' }}>
                #
              </th>
              <th style={{ padding: '16px 20px', fontSize: '0.76rem', color: 'var(--text-muted)', fontWeight: 700, letterSpacing: '0.05em' }}>
                TITLE
              </th>
              <th style={{ padding: '16px 20px', fontSize: '0.76rem', color: 'var(--text-muted)', fontWeight: 700, letterSpacing: '0.05em', width: '140px', textAlign: 'right' }}>
                ATTEMPTED
              </th>
              <th style={{ padding: '16px 20px', fontSize: '0.76rem', color: 'var(--text-muted)', fontWeight: 700, letterSpacing: '0.05em', width: '140px', textAlign: 'right' }}>
                ACCEPTANCE
              </th>
              <th style={{ padding: '16px 20px', fontSize: '0.76rem', color: 'var(--text-muted)', fontWeight: 700, letterSpacing: '0.05em', width: '120px', textAlign: 'right' }}>
                DIFFICULTY
              </th>
              <th style={{ padding: '16px 20px', fontSize: '0.76rem', color: 'var(--text-muted)', fontWeight: 700, letterSpacing: '0.05em', width: '130px', textAlign: 'center' }}>
                ACTION
              </th>
            </tr>
          </thead>
          <tbody>
            {loading ? (
              <tr>
                <td colSpan={6} style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>
                  Loading curated problems bank...
                </td>
              </tr>
            ) : filteredProblems.length === 0 ? (
              <tr>
                <td colSpan={6} style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>
                  No challenges match the active filters. Try adjusting your search or resetting filters.
                </td>
              </tr>
            ) : (
              filteredProblems.map((prob, index) => {
                const qid = prob.id || prob.questionId;
                const isSolved = solvedIds.includes(qid);
                const diffLabel = prob.difficulty === 'Medium' ? 'Med.' : prob.difficulty;
                const diffColor = prob.difficulty === 'Easy' ? '#10b981' : prob.difficulty === 'Hard' ? '#ef4444' : '#f59e0b';

                return (
                  <tr
                    key={qid}
                    onClick={() => handleOpenProblem(prob)}
                    style={{
                      borderBottom: '1px solid var(--border-glass)',
                      cursor: 'pointer',
                      transition: 'background 0.15s ease'
                    }}
                    onMouseEnter={(e) => e.currentTarget.style.background = 'rgba(255, 255, 255, 0.03)'}
                    onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
                  >
                    {/* Index / Solved Indicator */}
                    <td style={{ padding: '18px 20px', verticalAlign: 'middle' }}>
                      <div style={{
                        width: '26px',
                        height: '26px',
                        borderRadius: '50%',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontSize: '0.78rem',
                        fontWeight: 700,
                        color: isSolved ? '#10b981' : 'var(--text-muted)',
                        background: isSolved ? 'rgba(16, 185, 129, 0.15)' : 'rgba(255, 255, 255, 0.04)',
                        border: isSolved ? '1px solid #10b981' : '1px solid rgba(255, 255, 255, 0.1)'
                      }}>
                        {isSolved ? <Check size={14} /> : (index + 1)}
                      </div>
                    </td>

                    {/* Title & Topic */}
                    <td style={{ padding: '18px 20px', verticalAlign: 'middle' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                        <span style={{ fontSize: '0.98rem', fontWeight: 700, color: '#fff' }}>
                          {prob.title}
                        </span>
                        {prob.topic && (
                          <span className="badge badge-indigo" style={{ fontSize: '0.7rem', padding: '2px 8px' }}>
                            {prob.topic}
                          </span>
                        )}
                        {prob.track && prob.track !== prob.topic && (
                          <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>
                            • {prob.track}
                          </span>
                        )}
                      </div>
                    </td>

                    {/* Attempted */}
                    <td style={{ padding: '18px 20px', verticalAlign: 'middle', textAlign: 'right', color: 'var(--text-muted)', fontSize: '0.9rem', fontWeight: 500 }}>
                      {prob.attempted || '5.2k'}
                    </td>

                    {/* Acceptance */}
                    <td style={{ padding: '18px 20px', verticalAlign: 'middle', textAlign: 'right', color: 'var(--text-muted)', fontSize: '0.9rem', fontWeight: 500 }}>
                      {prob.acceptance || '60%'}
                    </td>

                    {/* Difficulty */}
                    <td style={{ padding: '18px 20px', verticalAlign: 'middle', textAlign: 'right' }}>
                      <span style={{ color: diffColor, fontWeight: 700, fontSize: '0.9rem' }}>
                        {diffLabel}
                      </span>
                    </td>

                    {/* Action */}
                    <td style={{ padding: '18px 20px', verticalAlign: 'middle', textAlign: 'center' }}>
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          handleOpenProblem(prob);
                        }}
                        className="btn-secondary"
                        style={{ padding: '6px 14px', fontSize: '0.78rem' }}
                      >
                        {isSolved ? 'Review' : 'Solve'}
                      </button>
                    </td>
                  </tr>
                );
              })
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
