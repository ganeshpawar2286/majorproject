import React, { useState, useEffect } from 'react';
import {
  Brain, Calculator, Lightbulb, BookOpen, Clock, CheckCircle2, XCircle,
  HelpCircle, ChevronRight, ChevronLeft, RotateCcw, Award, Play, AlertCircle, Check, Flag,
  Shuffle, Grid, Sparkles, Filter, RefreshCw
} from 'lucide-react';

export default function AptitudeSection() {
  const [activeTabMode, setActiveTabMode] = useState('practice'); // 'practice' | 'test'
  const [activeCategory, setActiveCategory] = useState('Quantitative');
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [currentPracticeIndex, setCurrentPracticeIndex] = useState(0);

  // Practice state
  const [practiceCount, setPracticeCount] = useState(50); // Options: 15, 30, 45, 50 questions
  const [selectedTopic, setSelectedTopic] = useState('All');
  const [selectedDifficulty, setSelectedDifficulty] = useState('All');
  const [categoriesData, setCategoriesData] = useState([]);
  const [showPracticePalette, setShowPracticePalette] = useState(false);
  const [shuffleToast, setShuffleToast] = useState('');
  const [practiceAnswers, setPracticeAnswers] = useState({}); // { [qId]: selectedOptionIndex }
  const [showExplanation, setShowExplanation] = useState({}); // { [qId]: boolean }

  // Timed Test state
  const [testActive, setTestActive] = useState(false);
  const [testConfig, setTestConfig] = useState({ questionCount: 20, durationMinutes: 20 });
  const [testQuestions, setTestQuestions] = useState([]);
  const [currentTestIndex, setCurrentTestIndex] = useState(0);
  const [testAnswers, setTestAnswers] = useState({}); // { [qId]: selectedOptionIndex }
  const [flaggedForReview, setFlaggedForReview] = useState({}); // { [qId]: boolean }
  const [secondsRemaining, setSecondsRemaining] = useState(1200);
  const [testResult, setTestResult] = useState(null);
  const [testSubmitting, setTestSubmitting] = useState(false);

  const CATEGORIES = [
    { id: 'Quantitative', label: 'Quantitative Aptitude', icon: Calculator, desc: 'Percentages, Work, Speed, Profit & Loss, Probability' },
    { id: 'Logical', label: 'Logical Reasoning', icon: Lightbulb, desc: 'Series, Syllogisms, Blood Relations, Seating, Coding' },
    { id: 'Verbal', label: 'Verbal Ability', icon: BookOpen, desc: 'Grammar, Synonyms, Antonyms, Idioms, Comprehension' },
    { id: 'Technical', label: 'Technical Aptitude', icon: Brain, desc: 'OS, DBMS, SQL, Computer Networks, OOP Concepts' }
  ];

  // Fetch category & topic metadata on mount
  useEffect(() => {
    fetch('/api/aptitude/categories')
      .then(res => res.json())
      .then(data => {
        if (data.categories) setCategoriesData(data.categories);
      })
      .catch(err => console.warn('Categories fetch error:', err));
  }, []);

  // Fetch practice questions when category changes
  useEffect(() => {
    if (activeTabMode === 'practice') {
      setSelectedTopic('All');
      fetchPracticeQuestions(practiceCount, 'All', selectedDifficulty, true);
    }
  }, [activeCategory, activeTabMode]);

  const fetchPracticeQuestions = async (count = practiceCount, topic = selectedTopic, difficulty = selectedDifficulty, forceShuffle = true) => {
    try {
      setLoading(true);
      const topicParam = encodeURIComponent(topic || 'All');
      const diffParam = encodeURIComponent(difficulty || 'All');
      const res = await fetch(`/api/aptitude/questions?category=${encodeURIComponent(activeCategory)}&mode=practice&limit=${count}&topic=${topicParam}&difficulty=${diffParam}&shuffle=${forceShuffle}&_t=${Date.now()}`);
      const data = await res.json();
      if (res.ok && data.questions) {
        setQuestions(data.questions);
        setCurrentPracticeIndex(0);
        setPracticeAnswers({});
        setShowExplanation({});
        if (forceShuffle) {
          setShuffleToast(`Loaded ${data.questions.length} fresh randomized questions!`);
          setTimeout(() => setShuffleToast(''), 3500);
        }
      }
    } catch (err) {
      console.error('Fetch aptitude questions error:', err);
    } finally {
      setLoading(false);
    }
  };

  // Countdown timer for active timed assessment test
  useEffect(() => {
    if (!testActive || secondsRemaining <= 0) return;

    const timer = setInterval(() => {
      setSecondsRemaining((prev) => {
        if (prev <= 1) {
          clearInterval(timer);
          handleFinishTest();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [testActive, secondsRemaining]);

  const handleStartTest = async () => {
    try {
      setTestSubmitting(true);
      const res = await fetch('/api/aptitude/test/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question_count: testConfig.questionCount })
      });
      const data = await res.json();
      if (res.ok && data.questions) {
        setTestQuestions(data.questions);
        setSecondsRemaining((data.duration_minutes || testConfig.durationMinutes) * 60);
        setTestAnswers({});
        setFlaggedForReview({});
        setCurrentTestIndex(0);
        setTestResult(null);
        setTestActive(true);
      }
    } catch (err) {
      console.error('Start aptitude test error:', err);
    } finally {
      setTestSubmitting(false);
    }
  };

  const handleFinishTest = async () => {
    try {
      setTestSubmitting(true);
      const res = await fetch('/api/aptitude/test/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ answers: testAnswers })
      });
      const data = await res.json();
      if (res.ok) {
        setTestResult(data);
        setTestActive(false);
      }
    } catch (err) {
      console.error('Submit aptitude test error:', err);
    } finally {
      setTestSubmitting(false);
    }
  };

  const formatTime = (secs) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  // -------------------------------------------------------------
  // VIEW: TIMED TEST ACTIVE HUD
  // -------------------------------------------------------------
  if (testActive && testQuestions.length > 0) {
    const curQ = testQuestions[currentTestIndex];
    const isAnswered = testAnswers[curQ.id] !== undefined;
    const isFlagged = flaggedForReview[curQ.id];

    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
        {/* Test HUD Top Bar */}
        <div className="glass-card" style={{ padding: '16px 24px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '14px' }}>
          <div>
            <span style={{ fontSize: '0.74rem', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 700, letterSpacing: '0.05em' }}>
              OFFICIAL TIMED APTITUDE TEST
            </span>
            <h2 style={{ fontSize: '1.2rem', color: '#fff', margin: '2px 0 0 0' }}>
              Question {currentTestIndex + 1} of {testQuestions.length}
            </h2>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
            {/* Countdown Timer */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              padding: '8px 18px',
              borderRadius: '12px',
              background: secondsRemaining < 120 ? 'rgba(239, 68, 68, 0.2)' : 'rgba(99, 102, 241, 0.15)',
              border: secondsRemaining < 120 ? '1px solid #ef4444' : '1px solid var(--border-glass)',
              color: secondsRemaining < 120 ? '#f87171' : '#818cf8',
              fontWeight: 800,
              fontSize: '1.1rem'
            }}>
              <Clock size={18} />
              {formatTime(secondsRemaining)}
            </div>

            <button
              onClick={() => {
                if (window.confirm('Are you sure you want to submit your test?')) {
                  handleFinishTest();
                }
              }}
              disabled={testSubmitting}
              className="btn-success"
              style={{ padding: '8px 20px', fontSize: '0.86rem' }}
            >
              Finish & Submit Test
            </button>
          </div>
        </div>

        {/* Test Main Layout: Question + Question Palette */}
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 320px', gap: '22px' }}>
          {/* Left Column: Current Question */}
          <div className="glass-card" style={{ padding: '30px', display: 'flex', flexDirection: 'column', gap: '22px' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <span className="badge badge-indigo">{curQ.category} • {curQ.topic}</span>
              <span className={curQ.difficulty === 'Easy' ? 'badge badge-emerald' : curQ.difficulty === 'Hard' ? 'badge badge-rose' : 'badge badge-amber'}>
                {curQ.difficulty}
              </span>
            </div>

            <p style={{ fontSize: '1.12rem', color: '#fff', lineHeight: 1.6, margin: 0, fontWeight: 500, whiteSpace: 'pre-line' }}>
              {curQ.question}
            </p>

            {/* Options */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              {curQ.options.map((opt, optIdx) => {
                const isSelected = testAnswers[curQ.id] === optIdx;
                return (
                  <div
                    key={optIdx}
                    onClick={() => setTestAnswers({ ...testAnswers, [curQ.id]: optIdx })}
                    style={{
                      padding: '14px 18px',
                      borderRadius: '12px',
                      background: isSelected ? 'rgba(99, 102, 241, 0.2)' : 'rgba(15, 23, 42, 0.6)',
                      border: isSelected ? '2px solid var(--primary-light)' : '1px solid var(--border-glass)',
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '14px',
                      transition: 'all 0.15s ease'
                    }}
                  >
                    <div style={{
                      width: '24px',
                      height: '24px',
                      borderRadius: '50%',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontSize: '0.82rem',
                      fontWeight: 700,
                      background: isSelected ? '#6366f1' : 'rgba(255,255,255,0.06)',
                      color: isSelected ? '#fff' : 'var(--text-muted)',
                      border: isSelected ? 'none' : '1px solid rgba(255,255,255,0.1)'
                    }}>
                      {String.fromCharCode(65 + optIdx)}
                    </div>
                    <span style={{ fontSize: '0.96rem', color: isSelected ? '#fff' : '#cbd5e1' }}>
                      {opt}
                    </span>
                  </div>
                );
              })}
            </div>

            {/* Question Actions */}
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: '10px', paddingTop: '16px', borderTop: '1px solid var(--border-glass)' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <button
                  onClick={() => setFlaggedForReview({ ...flaggedForReview, [curQ.id]: !isFlagged })}
                  className="btn-secondary"
                  style={{ padding: '8px 14px', fontSize: '0.82rem', color: isFlagged ? '#c084fc' : 'var(--text-muted)' }}
                >
                  <Flag size={14} color={isFlagged ? '#c084fc' : 'currentColor'} /> {isFlagged ? 'Marked for Review' : 'Mark for Review'}
                </button>

                {isAnswered && (
                  <button
                    onClick={() => {
                      const updated = { ...testAnswers };
                      delete updated[curQ.id];
                      setTestAnswers(updated);
                    }}
                    className="btn-secondary"
                    style={{ padding: '8px 14px', fontSize: '0.82rem' }}
                  >
                    Clear Choice
                  </button>
                )}
              </div>

              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <button
                  onClick={() => setCurrentTestIndex(Math.max(0, currentTestIndex - 1))}
                  disabled={currentTestIndex === 0}
                  className="btn-secondary"
                  style={{ padding: '8px 16px', fontSize: '0.86rem' }}
                >
                  <ChevronLeft size={16} /> Previous
                </button>
                <button
                  onClick={() => setCurrentTestIndex(Math.min(testQuestions.length - 1, currentTestIndex + 1))}
                  disabled={currentTestIndex === testQuestions.length - 1}
                  className="btn-primary"
                  style={{ padding: '8px 18px', fontSize: '0.86rem' }}
                >
                  Next <ChevronRight size={16} />
                </button>
              </div>
            </div>
          </div>

          {/* Right Column: Question Palette Matrix */}
          <div className="glass-card" style={{ padding: '22px', display: 'flex', flexDirection: 'column', gap: '18px' }}>
            <h4 style={{ color: '#fff', fontSize: '0.94rem', margin: 0, fontWeight: 700 }}>
              Question Palette ({Object.keys(testAnswers).length} / {testQuestions.length} Answered)
            </h4>

            {/* Status Legend */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '8px', fontSize: '0.74rem' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <div style={{ width: '10px', height: '10px', borderRadius: '3px', background: '#10b981' }} />
                <span style={{ color: 'var(--text-muted)' }}>Answered</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <div style={{ width: '10px', height: '10px', borderRadius: '3px', background: '#c084fc' }} />
                <span style={{ color: 'var(--text-muted)' }}>Review</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <div style={{ width: '10px', height: '10px', borderRadius: '3px', background: '#475569' }} />
                <span style={{ color: 'var(--text-muted)' }}>Unanswered</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <div style={{ width: '10px', height: '10px', borderRadius: '3px', border: '2px solid #818cf8' }} />
                <span style={{ color: 'var(--text-muted)' }}>Current</span>
              </div>
            </div>

            {/* Grid Palette */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: '8px' }}>
              {testQuestions.map((q, idx) => {
                const ans = testAnswers[q.id] !== undefined;
                const flg = flaggedForReview[q.id];
                const isCur = idx === currentTestIndex;

                let bg = '#1e293b';
                let color = '#94a3b8';
                if (ans) {
                  bg = '#059669';
                  color = '#fff';
                }
                if (flg) {
                  bg = '#7c3aed';
                  color = '#fff';
                }

                return (
                  <button
                    key={q.id}
                    onClick={() => setCurrentTestIndex(idx)}
                    style={{
                      aspectRatio: '1',
                      borderRadius: '8px',
                      background: bg,
                      color: color,
                      fontWeight: 700,
                      fontSize: '0.84rem',
                      border: isCur ? '2px solid #fff' : '1px solid transparent',
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      boxShadow: isCur ? '0 0 10px rgba(99, 102, 241, 0.6)' : 'none'
                    }}
                  >
                    {idx + 1}
                  </button>
                );
              })}
            </div>
          </div>
        </div>
      </div>
    );
  }

  // -------------------------------------------------------------
  // VIEW: TEST RESULTS SCORECARD
  // -------------------------------------------------------------
  if (testResult) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
        {/* Scorecard Hero Banner */}
        <div className="glass-card" style={{ padding: '36px', textAlign: 'center', background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(139, 92, 246, 0.1) 100%)', border: '1px solid rgba(99, 102, 241, 0.3)' }}>
          <div style={{ display: 'inline-flex', padding: '14px', borderRadius: '50%', background: 'rgba(99, 102, 241, 0.2)', marginBottom: '14px' }}>
            <Award size={42} color="var(--primary-light)" />
          </div>

          <h2 style={{ fontSize: '2rem', color: '#fff', margin: 0 }}>Aptitude Assessment Report</h2>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.94rem', marginTop: '6px' }}>
            Comprehensive evaluation across Quantitative, Logical, Verbal, and Technical domains
          </p>

          <div style={{ display: 'flex', justifyContent: 'center', gap: '30px', margin: '28px 0 10px 0', flexWrap: 'wrap' }}>
            <div style={{ padding: '16px 24px', background: 'rgba(15, 23, 42, 0.7)', borderRadius: '12px', border: '1px solid var(--border-glass)' }}>
              <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)', display: 'block' }}>OVERALL SCORE</span>
              <strong style={{ fontSize: '2.2rem', color: testResult.overall_score >= 70 ? '#34d399' : '#f59e0b' }}>
                {testResult.overall_score}%
              </strong>
            </div>

            <div style={{ padding: '16px 24px', background: 'rgba(15, 23, 42, 0.7)', borderRadius: '12px', border: '1px solid var(--border-glass)' }}>
              <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)', display: 'block' }}>CORRECT ANSWERS</span>
              <strong style={{ fontSize: '2.2rem', color: '#34d399' }}>
                {testResult.correct_count} / {testResult.total_questions}
              </strong>
            </div>

            <div style={{ padding: '16px 24px', background: 'rgba(15, 23, 42, 0.7)', borderRadius: '12px', border: '1px solid var(--border-glass)' }}>
              <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)', display: 'block' }}>ACCURACY</span>
              <strong style={{ fontSize: '2.2rem', color: '#818cf8' }}>
                {testResult.answered_count > 0 ? Math.round((testResult.correct_count / testResult.answered_count) * 100) : 0}%
              </strong>
            </div>
          </div>

          {/* Section-Wise Breakdown Bars */}
          <div style={{ maxWidth: '680px', margin: '24px auto 0 auto', display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {Object.entries(testResult.section_breakdown || {}).map(([sec, stats]) => (
              <div key={sec} style={{ display: 'flex', flexDirection: 'column', gap: '4px', textAlign: 'left' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.84rem' }}>
                  <span style={{ color: '#fff', fontWeight: 600 }}>{sec}</span>
                  <span style={{ color: 'var(--text-muted)' }}>{stats.correct} / {stats.total} ({stats.score}%)</span>
                </div>
                <div style={{ height: '8px', borderRadius: '4px', background: 'rgba(255,255,255,0.06)', overflow: 'hidden' }}>
                  <div style={{ width: `${stats.score}%`, height: '100%', background: 'linear-gradient(90deg, #6366f1, #10b981)', borderRadius: '4px' }} />
                </div>
              </div>
            ))}
          </div>

          <div style={{ marginTop: '28px' }}>
            <button
              onClick={() => {
                setTestResult(null);
                setActiveTabMode('practice');
              }}
              className="btn-primary"
              style={{ padding: '10px 24px' }}
            >
              <RotateCcw size={16} /> Return to Aptitude Hub
            </button>
          </div>
        </div>

        {/* Question Solutions Review */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          <h3 style={{ fontSize: '1.25rem', color: '#fff', margin: '8px 0' }}>
            Detailed Solutions & Step-by-Step Explanations ({testResult.detailed_results?.length || 0})
          </h3>

          {(testResult.detailed_results || []).map((res, idx) => (
            <div
              key={idx}
              className="glass-card"
              style={{
                padding: '24px',
                borderLeft: res.is_correct ? '4px solid #10b981' : '4px solid #ef4444'
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '12px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span style={{ fontWeight: 700, color: '#fff' }}>Question {idx + 1}</span>
                  <span className="badge badge-indigo">{res.category} • {res.topic}</span>
                </div>
                <span className={res.is_correct ? 'badge badge-emerald' : 'badge badge-rose'}>
                  {res.is_correct ? 'Correct' : 'Incorrect'}
                </span>
              </div>

              <p style={{ color: '#fff', fontSize: '0.96rem', lineHeight: 1.6, margin: '0 0 16px 0', whiteSpace: 'pre-line' }}>
                {res.question}
              </p>

              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '10px', marginBottom: '14px' }}>
                {res.options.map((opt, oIdx) => {
                  const isUserAns = res.user_answer === oIdx;
                  const isCorrectAns = res.correct_answer === oIdx;
                  let optBg = 'rgba(15, 23, 42, 0.6)';
                  let border = '1px solid var(--border-glass)';
                  if (isCorrectAns) {
                    optBg = 'rgba(16, 185, 129, 0.15)';
                    border = '1px solid #10b981';
                  } else if (isUserAns && !isCorrectAns) {
                    optBg = 'rgba(239, 68, 68, 0.15)';
                    border = '1px solid #ef4444';
                  }

                  return (
                    <div key={oIdx} style={{ padding: '10px 14px', borderRadius: '8px', background: optBg, border, fontSize: '0.86rem', color: isCorrectAns ? '#6ee7b7' : isUserAns ? '#fca5a5' : '#cbd5e1' }}>
                      <strong>{String.fromCharCode(65 + oIdx)}.</strong> {opt} {isCorrectAns && '✓ (Correct)'} {isUserAns && !isCorrectAns && '✗ (Your Choice)'}
                    </div>
                  );
                })}
              </div>

              {res.formula && (
                <div style={{ background: 'rgba(99, 102, 241, 0.1)', padding: '10px 14px', borderRadius: '8px', border: '1px solid rgba(99, 102, 241, 0.2)', marginBottom: '10px', fontSize: '0.82rem', color: '#c7d2fe' }}>
                  <strong>Key Formula / Principle:</strong> {res.formula}
                </div>
              )}

              {res.explanation && (
                <div style={{ background: 'rgba(15, 23, 42, 0.7)', padding: '12px 16px', borderRadius: '8px', border: '1px solid var(--border-glass)', fontSize: '0.84rem', color: '#94a3b8', lineHeight: 1.5, whiteSpace: 'pre-line' }}>
                  <strong style={{ color: '#fff', display: 'block', marginBottom: '4px' }}>Step-by-Step Explanation:</strong>
                  {res.explanation}
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    );
  }

  // -------------------------------------------------------------
  // DEFAULT VIEW: PRACTICE & TEST SETUP
  // -------------------------------------------------------------
  const curPracticeQ = questions[currentPracticeIndex];
  const userChoice = curPracticeQ ? practiceAnswers[curPracticeQ.id] : undefined;
  const isExpVisible = curPracticeQ ? showExplanation[curPracticeQ.id] : false;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      {/* Top Banner & Mode Switcher */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px' }}>
        <div>
          <h2 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#fff', margin: 0 }}>
            Aptitude & Technical Reasoning
          </h2>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.92rem', marginTop: '4px' }}>
            Sharpen quantitative, logical, verbal, and technical aptitude with instant step-by-step solutions or full timed tests.
          </p>
        </div>

        <div style={{ display: 'flex', gap: '8px', background: 'rgba(15, 23, 42, 0.8)', padding: '6px', borderRadius: '12px', border: '1px solid var(--border-glass)' }}>
          <button
            onClick={() => setActiveTabMode('practice')}
            className={activeTabMode === 'practice' ? 'btn-primary' : 'btn-secondary'}
            style={{ padding: '8px 18px', fontSize: '0.86rem' }}
          >
            <Lightbulb size={16} /> Interactive Practice
          </button>
          <button
            onClick={() => setActiveTabMode('test')}
            className={activeTabMode === 'test' ? 'btn-primary' : 'btn-secondary'}
            style={{ padding: '8px 18px', fontSize: '0.86rem' }}
          >
            <Clock size={16} /> Timed Assessment Test
          </button>
        </div>
      </div>

      {/* MODE 1: INTERACTIVE PRACTICE */}
      {activeTabMode === 'practice' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          {/* Domain Category Selector Tabs */}
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '14px' }}>
            {CATEGORIES.map((cat) => {
              const Icon = cat.icon;
              const isSelected = activeCategory === cat.id;
              return (
                <div
                  key={cat.id}
                  onClick={() => setActiveCategory(cat.id)}
                  style={{
                    padding: '16px 20px',
                    borderRadius: '14px',
                    background: isSelected ? 'rgba(99, 102, 241, 0.2)' : 'rgba(15, 23, 42, 0.7)',
                    border: isSelected ? '1px solid var(--primary-light)' : '1px solid var(--border-glass)',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '14px',
                    transition: 'all 0.2s ease'
                  }}
                >
                  <div style={{
                    width: '42px',
                    height: '42px',
                    borderRadius: '10px',
                    background: isSelected ? '#6366f1' : 'rgba(255,255,255,0.06)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center'
                  }}>
                    <Icon size={20} color={isSelected ? '#fff' : 'var(--primary-light)'} />
                  </div>
                  <div>
                    <h4 style={{ color: '#fff', fontSize: '0.94rem', margin: 0 }}>{cat.label}</h4>
                    <span style={{ color: 'var(--text-muted)', fontSize: '0.72rem', display: 'block', marginTop: '2px' }}>
                      {cat.desc}
                    </span>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Practice Toolbar Controls (Question Count, Topic, Difficulty, Shuffle, Palette) */}
          <div className="glass-card" style={{ padding: '16px 22px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px' }}>
            {/* Left: Question Set Size Selector */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
              <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                Practice Size:
              </span>
              <div style={{ display: 'inline-flex', gap: '4px', background: 'rgba(15, 23, 42, 0.6)', padding: '4px', borderRadius: '10px', border: '1px solid var(--border-glass)' }}>
                {[15, 30, 45, 50].map((cnt) => (
                  <button
                    key={cnt}
                    onClick={() => {
                      setPracticeCount(cnt);
                      fetchPracticeQuestions(cnt, selectedTopic, selectedDifficulty, true);
                    }}
                    style={{
                      padding: '5px 12px',
                      borderRadius: '7px',
                      fontSize: '0.82rem',
                      fontWeight: 700,
                      cursor: 'pointer',
                      background: practiceCount === cnt ? '#6366f1' : 'transparent',
                      color: practiceCount === cnt ? '#fff' : 'var(--text-muted)',
                      border: 'none',
                      transition: 'all 0.15s ease'
                    }}
                  >
                    {cnt} Qs
                  </button>
                ))}
              </div>
            </div>

            {/* Middle: Topic & Difficulty Filters */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px', flexWrap: 'wrap' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <Filter size={14} color="var(--primary-light)" />
                <select
                  value={selectedTopic}
                  onChange={(e) => {
                    const val = e.target.value;
                    setSelectedTopic(val);
                    fetchPracticeQuestions(practiceCount, val, selectedDifficulty, true);
                  }}
                  style={{
                    padding: '6px 12px',
                    borderRadius: '8px',
                    background: 'rgba(15, 23, 42, 0.8)',
                    border: '1px solid var(--border-glass)',
                    color: '#fff',
                    fontSize: '0.82rem'
                  }}
                >
                  <option value="All">All Topics ({categoriesData.find(c => c.category === activeCategory)?.topics?.length || 0})</option>
                  {(categoriesData.find(c => c.category === activeCategory)?.topics || []).map((t) => (
                    <option key={t} value={t}>{t}</option>
                  ))}
                </select>
              </div>

              <select
                value={selectedDifficulty}
                onChange={(e) => {
                  const val = e.target.value;
                  setSelectedDifficulty(val);
                  fetchPracticeQuestions(practiceCount, selectedTopic, val, true);
                }}
                style={{
                  padding: '6px 12px',
                  borderRadius: '8px',
                  background: 'rgba(15, 23, 42, 0.8)',
                  border: '1px solid var(--border-glass)',
                  color: '#fff',
                  fontSize: '0.82rem'
                }}
              >
                <option value="All">All Difficulties</option>
                <option value="Easy">Easy</option>
                <option value="Medium">Medium</option>
                <option value="Hard">Hard</option>
              </select>
            </div>

            {/* Right: Shuffle / New Questions + Palette Toggle */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <button
                onClick={() => fetchPracticeQuestions(practiceCount, selectedTopic, selectedDifficulty, true)}
                className="btn-primary"
                style={{ padding: '8px 16px', fontSize: '0.84rem', gap: '7px' }}
                title="Shuffle and generate new questions"
              >
                <Shuffle size={15} /> New Questions / Shuffle
              </button>

              <button
                onClick={() => setShowPracticePalette(!showPracticePalette)}
                className={showPracticePalette ? 'btn-primary' : 'btn-secondary'}
                style={{ padding: '8px 14px', fontSize: '0.84rem', gap: '6px' }}
              >
                <Grid size={15} /> Palette ({Object.keys(practiceAnswers).length}/{questions.length})
              </button>
            </div>
          </div>

          {/* Shuffle Toast Banner */}
          {shuffleToast && (
            <div style={{
              padding: '12px 20px',
              borderRadius: '12px',
              background: 'linear-gradient(90deg, rgba(16, 185, 129, 0.2) 0%, rgba(99, 102, 241, 0.2) 100%)',
              border: '1px solid rgba(16, 185, 129, 0.4)',
              color: '#6ee7b7',
              fontSize: '0.88rem',
              fontWeight: 600,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              gap: '12px',
              boxShadow: '0 4px 14px rgba(16, 185, 129, 0.15)'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <Sparkles size={18} color="#34d399" />
                <span>{shuffleToast}</span>
              </div>
              <button onClick={() => setShuffleToast('')} style={{ background: 'none', border: 'none', color: '#6ee7b7', cursor: 'pointer', fontSize: '1rem', fontWeight: 700 }}>✕</button>
            </div>
          )}

          {/* Interactive Question Palette Matrix (1..50) */}
          {showPracticePalette && questions.length > 0 && (
            <div className="glass-card" style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '14px', background: 'rgba(15, 23, 42, 0.95)', border: '1px solid rgba(99, 102, 241, 0.3)' }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '10px' }}>
                <div>
                  <h4 style={{ margin: 0, fontSize: '0.94rem', color: '#fff', fontWeight: 700 }}>
                    Question Matrix ({Object.keys(practiceAnswers).length} / {questions.length} Solved)
                  </h4>
                  <span style={{ fontSize: '0.76rem', color: 'var(--text-muted)' }}>
                    Click any question number to jump directly to it.
                  </span>
                </div>

                {/* Status Legend */}
                <div style={{ display: 'flex', alignItems: 'center', gap: '14px', fontSize: '0.74rem' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
                    <div style={{ width: '10px', height: '10px', borderRadius: '3px', background: '#059669' }} />
                    <span style={{ color: '#6ee7b7' }}>Correct</span>
                  </div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
                    <div style={{ width: '10px', height: '10px', borderRadius: '3px', background: '#dc2626' }} />
                    <span style={{ color: '#fca5a5' }}>Incorrect</span>
                  </div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
                    <div style={{ width: '10px', height: '10px', borderRadius: '3px', border: '2px solid #fff' }} />
                    <span style={{ color: '#fff' }}>Current</span>
                  </div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
                    <div style={{ width: '10px', height: '10px', borderRadius: '3px', background: '#1e293b' }} />
                    <span style={{ color: 'var(--text-muted)' }}>Unanswered</span>
                  </div>
                </div>
              </div>

              {/* 50-Question Palette Grid */}
              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fill, minmax(36px, 1fr))',
                gap: '6px',
                maxHeight: '220px',
                overflowY: 'auto',
                paddingRight: '4px'
              }}>
                {questions.map((q, idx) => {
                  const userAns = practiceAnswers[q.id];
                  const isAnswered = userAns !== undefined;
                  const isCorrect = userAns === q.correct_answer;
                  const isCur = idx === currentPracticeIndex;

                  let bg = '#1e293b';
                  let color = '#94a3b8';
                  if (isAnswered) {
                    bg = isCorrect ? '#059669' : '#dc2626';
                    color = '#fff';
                  }

                  return (
                    <button
                      key={q.id || idx}
                      onClick={() => setCurrentPracticeIndex(idx)}
                      style={{
                        aspectRatio: '1',
                        borderRadius: '7px',
                        background: bg,
                        color: color,
                        fontWeight: 700,
                        fontSize: '0.78rem',
                        border: isCur ? '2px solid #fff' : '1px solid rgba(255,255,255,0.06)',
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        boxShadow: isCur ? '0 0 10px rgba(99, 102, 241, 0.7)' : 'none',
                        transition: 'all 0.1s ease'
                      }}
                    >
                      {idx + 1}
                    </button>
                  );
                })}
              </div>
            </div>
          )}

          {/* Current Practice Question Card */}
          {loading ? (
            <div className="glass-card" style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>
              Loading practice questions...
            </div>
          ) : curPracticeQ ? (
            <div className="glass-card" style={{ padding: '32px', display: 'flex', flexDirection: 'column', gap: '22px' }}>
              {/* Overall Progress Bar Across Questions */}
              <div style={{ width: '100%', height: '5px', background: 'rgba(255,255,255,0.06)', borderRadius: '3px', overflow: 'hidden' }}>
                <div style={{
                  width: `${((currentPracticeIndex + 1) / questions.length) * 100}%`,
                  height: '100%',
                  background: 'linear-gradient(90deg, #6366f1, #10b981)',
                  borderRadius: '3px',
                  transition: 'width 0.25s ease'
                }} />
              </div>

              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '10px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <span className="badge badge-indigo">{curPracticeQ.category}</span>
                  <span className="badge badge-purple">{curPracticeQ.topic}</span>
                  <span className={curPracticeQ.difficulty === 'Easy' ? 'badge badge-emerald' : curPracticeQ.difficulty === 'Hard' ? 'badge badge-rose' : 'badge badge-amber'}>
                    {curPracticeQ.difficulty}
                  </span>
                </div>

                <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                  <span style={{ fontSize: '0.84rem', color: 'var(--text-muted)', fontWeight: 600 }}>
                    Question {currentPracticeIndex + 1} of {questions.length}
                  </span>
                  <span className="badge badge-indigo" style={{ fontSize: '0.72rem' }}>
                    {Object.keys(practiceAnswers).length} / {questions.length} Answered
                  </span>
                </div>
              </div>

              <h3 style={{ fontSize: '1.15rem', color: '#fff', lineHeight: 1.6, margin: 0, fontWeight: 500, whiteSpace: 'pre-line' }}>
                {curPracticeQ.question}
              </h3>

              {/* Options */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                {curPracticeQ.options.map((opt, optIdx) => {
                  const isSelected = userChoice === optIdx;
                  const isCorrect = curPracticeQ.correct_answer === optIdx;
                  const hasAnswered = userChoice !== undefined;

                  let optBg = 'rgba(15, 23, 42, 0.6)';
                  let borderColor = 'var(--border-glass)';
                  let textColor = '#cbd5e1';

                  if (hasAnswered) {
                    if (isCorrect) {
                      optBg = 'rgba(16, 185, 129, 0.15)';
                      borderColor = '#10b981';
                      textColor = '#6ee7b7';
                    } else if (isSelected && !isCorrect) {
                      optBg = 'rgba(239, 68, 68, 0.15)';
                      borderColor = '#ef4444';
                      textColor = '#fca5a5';
                    }
                  } else if (isSelected) {
                    optBg = 'rgba(99, 102, 241, 0.2)';
                    borderColor = 'var(--primary-light)';
                    textColor = '#fff';
                  }

                  return (
                    <div
                      key={optIdx}
                      onClick={() => {
                        if (!hasAnswered) {
                          setPracticeAnswers({ ...practiceAnswers, [curPracticeQ.id]: optIdx });
                          setShowExplanation({ ...showExplanation, [curPracticeQ.id]: true });
                        }
                      }}
                      style={{
                        padding: '14px 18px',
                        borderRadius: '12px',
                        background: optBg,
                        border: `1px solid ${borderColor}`,
                        cursor: hasAnswered ? 'default' : 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'space-between',
                        gap: '14px',
                        transition: 'all 0.15s ease'
                      }}
                    >
                      <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
                        <div style={{
                          width: '24px',
                          height: '24px',
                          borderRadius: '50%',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          fontSize: '0.82rem',
                          fontWeight: 700,
                          background: isSelected ? (isCorrect ? '#10b981' : '#ef4444') : 'rgba(255,255,255,0.06)',
                          color: isSelected ? '#fff' : 'var(--text-muted)'
                        }}>
                          {String.fromCharCode(65 + optIdx)}
                        </div>
                        <span style={{ fontSize: '0.96rem', color: textColor }}>
                          {opt}
                        </span>
                      </div>

                      {hasAnswered && isCorrect && <Check size={18} color="#10b981" />}
                      {hasAnswered && isSelected && !isCorrect && <XCircle size={18} color="#ef4444" />}
                    </div>
                  );
                })}
              </div>

              {/* Step-by-Step Explanation Drawer */}
              {isExpVisible && (
                <div style={{ background: 'rgba(99, 102, 241, 0.08)', borderRadius: '12px', border: '1px solid rgba(99, 102, 241, 0.25)', padding: '20px', display: 'flex', flexDirection: 'column', gap: '10px' }}>
                  {curPracticeQ.formula && (
                    <div style={{ fontSize: '0.84rem', color: '#c7d2fe' }}>
                      <strong style={{ color: '#818cf8' }}>Key Formula / Core Rule:</strong> {curPracticeQ.formula}
                    </div>
                  )}

                  <div style={{ fontSize: '0.86rem', color: '#cbd5e1', lineHeight: 1.6, whiteSpace: 'pre-line' }}>
                    <strong style={{ color: '#34d399', display: 'block', marginBottom: '4px' }}>Step-by-Step Solution:</strong>
                    {curPracticeQ.explanation}
                  </div>
                </div>
              )}

              {/* Navigation Controls */}
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', paddingTop: '16px', borderTop: '1px solid var(--border-glass)', flexWrap: 'wrap', gap: '10px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <button
                    onClick={() => setShowExplanation({ ...showExplanation, [curPracticeQ.id]: !isExpVisible })}
                    className="btn-secondary"
                    style={{ padding: '8px 16px', fontSize: '0.82rem' }}
                  >
                    <Lightbulb size={14} /> {isExpVisible ? 'Hide Solution Steps' : 'View Solution Steps'}
                  </button>

                  {userChoice !== undefined && (
                    <button
                      onClick={() => {
                        const updatedAns = { ...practiceAnswers };
                        delete updatedAns[curPracticeQ.id];
                        setPracticeAnswers(updatedAns);
                      }}
                      className="btn-secondary"
                      style={{ padding: '8px 12px', fontSize: '0.82rem' }}
                      title="Re-attempt question"
                    >
                      Clear Answer
                    </button>
                  )}
                </div>

                <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <button
                    onClick={() => setCurrentPracticeIndex(Math.max(0, currentPracticeIndex - 1))}
                    disabled={currentPracticeIndex === 0}
                    className="btn-secondary"
                    style={{ padding: '8px 16px', fontSize: '0.86rem' }}
                  >
                    <ChevronLeft size={16} /> Previous
                  </button>
                  <button
                    onClick={() => setCurrentPracticeIndex(Math.min(questions.length - 1, currentPracticeIndex + 1))}
                    disabled={currentPracticeIndex === questions.length - 1}
                    className="btn-primary"
                    style={{ padding: '8px 18px', fontSize: '0.86rem' }}
                  >
                    Next <ChevronRight size={16} />
                  </button>
                  {currentPracticeIndex === questions.length - 1 && (
                    <button
                      onClick={() => fetchPracticeQuestions(practiceCount, selectedTopic, selectedDifficulty, true)}
                      className="btn-secondary"
                      style={{ padding: '8px 14px', fontSize: '0.84rem', borderColor: 'var(--primary-light)' }}
                    >
                      <RotateCcw size={14} /> Load Next 50 Set
                    </button>
                  )}
                </div>
              </div>
            </div>
          ) : (
            <div className="glass-card" style={{ padding: '40px', textAlign: 'center', color: 'var(--text-muted)' }}>
              No practice questions available for this category yet.
            </div>
          )}
        </div>
      )}

      {/* MODE 2: TIMED ASSESSMENT SETUP */}
      {activeTabMode === 'test' && (
        <div className="glass-card" style={{ padding: '36px', maxWidth: '720px', margin: '0 auto', width: '100%' }}>
          <div style={{ textAlign: 'center', marginBottom: '24px' }}>
            <div style={{ display: 'inline-flex', padding: '14px', borderRadius: '50%', background: 'rgba(99, 102, 241, 0.2)', marginBottom: '14px' }}>
              <Clock size={36} color="var(--primary-light)" />
            </div>
            <h2 style={{ fontSize: '1.6rem', color: '#fff', margin: 0 }}>Configure Timed Aptitude Assessment</h2>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.88rem', marginTop: '6px' }}>
              Simulate actual placement and company recruitment tests with real-time countdown, question palettes, and post-test analytics.
            </p>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
            <div>
              <label style={{ fontSize: '0.84rem', color: 'var(--text-muted)', fontWeight: 600, display: 'block', marginBottom: '8px' }}>
                TOTAL QUESTIONS COUNT
              </label>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '12px' }}>
                {[15, 30, 45, 50].map((count) => (
                  <button
                    key={count}
                    onClick={() => setTestConfig({ ...testConfig, questionCount: count, durationMinutes: count })}
                    style={{
                      padding: '12px',
                      borderRadius: '10px',
                      background: testConfig.questionCount === count ? 'rgba(99, 102, 241, 0.25)' : 'rgba(15, 23, 42, 0.7)',
                      border: testConfig.questionCount === count ? '2px solid var(--primary-light)' : '1px solid var(--border-glass)',
                      color: '#fff',
                      fontWeight: 700,
                      cursor: 'pointer'
                    }}
                  >
                    {count} Questions
                  </button>
                ))}
              </div>
            </div>

            <div style={{ padding: '16px', background: 'rgba(15, 23, 42, 0.6)', borderRadius: '12px', border: '1px solid var(--border-glass)', fontSize: '0.86rem', color: 'var(--text-muted)', lineHeight: 1.6 }}>
              <strong style={{ color: '#fff', display: 'block', marginBottom: '4px' }}>Assessment Structure:</strong>
              • Balanced blend of Quantitative, Logical, Verbal, and Technical Aptitude.<br />
              • Exactly {testConfig.durationMinutes} minutes countdown timer with auto-submit.<br />
              • Interactive question palette allowing you to flag and review answers before final submission.<br />
              • Detailed scorecard and step-by-step solution breakdowns upon test completion.
            </div>

            <button
              onClick={handleStartTest}
              disabled={testSubmitting}
              className="btn-primary"
              style={{ width: '100%', padding: '14px', justifyContent: 'center', fontSize: '1rem', marginTop: '10px' }}
            >
              <Play size={18} /> Start Timed Assessment Now
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
