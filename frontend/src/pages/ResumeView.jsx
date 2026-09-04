import React, { useState, useEffect } from 'react';
import { Upload, FileText, CheckCircle2, AlertTriangle, Cpu, Tag, ArrowRight, Sparkles, Key, TrendingUp, CheckSquare, Layers, FileQuestion } from 'lucide-react';

export default function ResumeView({ onResumeParsed, setParsedData, parsedData }) {
  const [activeResult, setActiveResult] = useState(parsedData || null);
  const [file, setFile] = useState(null);
  const [rawText, setRawText] = useState('');
  const [activeTab, setActiveTab] = useState('upload'); // 'upload' | 'text'
  const [selectedEngine, setSelectedEngine] = useState('local'); // 'local' | 'affinda' | 'rchilli' | 'textkernel'
  const [apiKey, setApiKey] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Sync activeResult when parsedData prop updates
  useEffect(() => {
    if (parsedData) {
      setActiveResult(parsedData);
    }
  }, [parsedData]);

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
      setError('');
    }
  };

  const handleParse = async () => {
    setLoading(true);
    setError('');

    try {
      let res;
      const token = localStorage.getItem('prepwise_session_token');
      const authHeader = token ? { 'Authorization': `Bearer ${token}` } : {};

      if (activeTab === 'upload') {
        if (!file) {
          throw new Error('Please select a PDF or DOCX file to upload.');
        }
        const formData = new FormData();
        formData.append('file', file);
        formData.append('engine', selectedEngine);
        if (apiKey) formData.append('api_key', apiKey);

        res = await fetch('/api/resume/parse', {
          method: 'POST',
          headers: authHeader,
          body: formData
        });
      } else {
        if (!rawText.trim() || rawText.length < 20) {
          throw new Error('Please paste your resume text (at least 20 characters).');
        }
        res = await fetch('/api/resume/parse', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', ...authHeader },
          body: JSON.stringify({
            text: rawText,
            filename: 'pasted_resume.txt',
            engine: selectedEngine,
            api_key: apiKey
          })
        });
      }

      const responseText = await res.text();
      let json;
      try {
        json = JSON.parse(responseText);
      } catch (e) {
        throw new Error(`Server returned unexpected response (${res.status}). Please check backend API server.`);
      }

      if (!res.ok) {
        throw new Error(json.error || 'Failed to parse resume.');
      }

      setActiveResult(json.data);
      if (setParsedData) {
        setParsedData(json.data);
      }
      if (onResumeParsed) {
        onResumeParsed(json.data);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      {/* Header Banner */}
      <div className="glass-card" style={{ padding: '24px 32px', background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.12) 0%, rgba(139, 92, 246, 0.08) 100%)' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px' }}>
          <div>
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', marginBottom: '8px' }}>
              <span className="badge badge-indigo">Module 1</span>
              <span className="badge badge-emerald">High-Precision ATS Resume Parser</span>
            </div>
            <h1 style={{ fontSize: '1.8rem', fontWeight: 700, color: '#fff' }}>Resume Analysis & ATS Scoring</h1>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.92rem', marginTop: '4px' }}>
              Upload your PDF/DOCX resume to receive a content-sensitive ATS score and personalized step-by-step improvement roadmap to reach 90%+.
            </p>
          </div>
          <div style={{ display: 'flex', gap: '12px' }}>
            <button
              onClick={() => setActiveTab('upload')}
              className={activeTab === 'upload' ? 'btn-primary' : 'btn-secondary'}
            >
              <Upload size={16} /> Upload File
            </button>
            <button
              onClick={() => setActiveTab('text')}
              className={activeTab === 'text' ? 'btn-primary' : 'btn-secondary'}
            >
              <FileText size={16} /> Paste Text
            </button>
          </div>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1.2fr', gap: '24px' }}>
        {/* Upload & Engine Selection Card */}
        <div className="glass-card" style={{ padding: '28px' }}>
          <h3 style={{ fontSize: '1.2rem', marginBottom: '16px', display: 'flex', alignItems: 'center', gap: '8px', color: '#fff' }}>
            <Cpu size={20} color="var(--primary-light)" />
            {activeTab === 'upload' ? 'Upload Resume File' : 'Paste Resume Content'}
          </h3>


          {error && (
            <div style={{
              background: 'rgba(239, 68, 68, 0.15)',
              border: '1px solid rgba(239, 68, 68, 0.3)',
              color: '#fca5a5',
              padding: '12px',
              borderRadius: '8px',
              marginBottom: '16px',
              fontSize: '0.88rem'
            }}>
              {error}
            </div>
          )}

          {activeTab === 'upload' ? (
            <div style={{
              border: '2px dashed var(--border-glow)',
              borderRadius: '12px',
              padding: '36px 20px',
              textAlign: 'center',
              background: 'rgba(15, 23, 42, 0.4)',
              cursor: 'pointer',
              marginBottom: '20px'
            }}>
              <Upload size={40} color="var(--primary-light)" style={{ marginBottom: '12px' }} />
              <h4 style={{ color: '#fff', fontSize: '1rem', marginBottom: '6px' }}>
                {file ? file.name : (activeResult ? `Currently Active: ${activeResult.filename || 'Uploaded Resume'}` : 'Drag & Drop or Click to Select File')}
              </h4>
              <p style={{ color: 'var(--text-dim)', fontSize: '0.82rem' }}>
                Supports PDF, DOCX, or DOC format (Max 10MB)
              </p>
              <input
                type="file"
                accept=".pdf,.docx,.doc"
                onChange={handleFileChange}
                style={{ display: 'none' }}
                id="resume-file-input"
              />
              <label htmlFor="resume-file-input" className="btn-secondary" style={{ marginTop: '16px', display: 'inline-flex' }}>
                {file ? 'Change Selected File' : 'Browse Files'}
              </label>
            </div>
          ) : (
            <textarea
              placeholder="Paste complete resume text here (including Skills, Work Experience, Education)..."
              value={rawText}
              onChange={(e) => setRawText(e.target.value)}
              rows={10}
              style={{
                width: '100%',
                padding: '14px',
                background: 'rgba(15, 23, 42, 0.6)',
                border: '1px solid var(--border-glass)',
                borderRadius: '10px',
                color: '#fff',
                fontFamily: 'inherit',
                marginBottom: '20px',
                resize: 'vertical'
              }}
            />
          )}

          <button
            onClick={handleParse}
            disabled={loading}
            className="btn-primary"
            style={{ width: '100%', justifyContent: 'center', padding: '14px', fontSize: '1rem' }}
          >
            {loading ? (
              <>Analyzing Resume with {selectedEngine.toUpperCase()}...</>
            ) : (
              <>
                <Sparkles size={18} /> {activeResult ? 'Re-Analyze / Update Resume' : 'Analyze Resume & Calculate ATS Score'}
              </>
            )}
          </button>
        </div>

        {/* Results Analysis Panel */}
        {activeResult ? (
          /* ATS Score Overview Card - PERSISTED ACROSS TABS */
          <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
            <div className="glass-card" style={{ padding: '24px', background: 'linear-gradient(135deg, rgba(18, 26, 43, 0.9) 0%, rgba(30, 41, 59, 0.9) 100%)' }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '16px' }}>
                <div>
                  <span className="badge badge-indigo" style={{ marginBottom: '6px' }}>
                    ENGINE: {activeResult.engine_used || 'Local High-Precision Engine'}
                  </span>
                  <h3 style={{ fontSize: '1.3rem', color: '#fff' }}>Candidate Profile Overview</h3>
                  <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>
                    {activeResult.candidate_name} • Industry Category: <span style={{ color: 'var(--primary-light)', fontWeight: 600 }}>{activeResult.predicted_category}</span>
                  </p>
                </div>
                <div style={{ textAlign: 'right' }}>
                  <div style={{ fontSize: '2.4rem', fontWeight: 800, color: activeResult.ats_score >= 80 ? '#10b981' : activeResult.ats_score >= 60 ? '#f59e0b' : '#ef4444' }}>
                    {activeResult.ats_score}%
                  </div>
                  <span className={activeResult.ats_score >= 80 ? 'badge badge-emerald' : activeResult.ats_score >= 60 ? 'badge badge-amber' : 'badge badge-rose'}>
                    ATS Score Rating
                  </span>
                </div>
              </div>

              {/* Section Breakdown Bars */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '16px' }}>
                {Object.entries(activeResult.section_breakdown || {}).map(([key, val]) => (
                  <div key={key}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.82rem', marginBottom: '4px', color: 'var(--text-muted)' }}>
                      <span>{key}</span>
                      <span style={{ color: '#fff', fontWeight: 600 }}>{val}</span>
                    </div>
                    <div style={{ height: '6px', background: 'rgba(255,255,255,0.1)', borderRadius: '3px', overflow: 'hidden' }}>
                      <div style={{
                        height: '100%',
                        width: `${(parseFloat(val.split('/')[0]) / parseFloat(val.split('/')[1])) * 100}%`,
                        background: 'linear-gradient(90deg, #6366f1, #10b981)',
                        borderRadius: '3px'
                      }} />
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* ACTIONABLE SCORE IMPROVEMENT ROADMAP */}
            {activeResult.actionable_improvements && activeResult.actionable_improvements.length > 0 && (
              <div className="glass-card" style={{ padding: '24px', border: '1px solid rgba(99, 102, 241, 0.4)', background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%)' }}>
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '16px', flexWrap: 'wrap', gap: '10px' }}>
                  <h4 style={{ fontSize: '1.15rem', color: '#fff', display: 'flex', alignItems: 'center', gap: '8px', margin: 0 }}>
                    <TrendingUp size={20} color="#10b981" />
                    How to Boost Your ATS Score from {activeResult.ats_score}% → 90%+
                  </h4>
                  <span className="badge badge-emerald" style={{ fontSize: '0.8rem', padding: '4px 10px' }}>
                    {activeResult.actionable_improvements.length} Action Steps Required
                  </span>
                </div>

                <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem', marginBottom: '16px' }}>
                  Make these specific changes to your resume file to pass recruiter screening and maximize your interview callbacks:
                </p>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                  {activeResult.actionable_improvements.map((item, idx) => (
                    <div
                      key={idx}
                      style={{
                        padding: '14px 16px',
                        borderRadius: '10px',
                        background: 'rgba(15, 23, 42, 0.7)',
                        border: '1px solid var(--border-glass)',
                        display: 'flex',
                        gap: '14px',
                        alignItems: 'flex-start'
                      }}
                    >
                      <div style={{
                        minWidth: '28px',
                        height: '28px',
                        borderRadius: '50%',
                        background: 'rgba(99, 102, 241, 0.2)',
                        color: 'var(--primary-light)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontWeight: 700,
                        fontSize: '0.85rem'
                      }}>
                        {idx + 1}
                      </div>

                      <div style={{ flex: 1 }}>
                        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '4px', flexWrap: 'wrap', gap: '6px' }}>
                          <span style={{ color: '#fff', fontWeight: 600, fontSize: '0.92rem' }}>
                            {item.title}
                          </span>
                          <div style={{ display: 'flex', gap: '6px', alignItems: 'center' }}>
                            <span className={item.priority === 'High' ? 'badge badge-rose' : item.priority === 'Medium' ? 'badge badge-amber' : 'badge badge-indigo'} style={{ fontSize: '0.72rem' }}>
                              {item.priority} Priority
                            </span>
                            <span className="badge badge-emerald" style={{ fontWeight: 700, fontSize: '0.75rem' }}>
                              Gain {item.potential_gain}
                            </span>
                          </div>
                        </div>
                        <p style={{ color: 'var(--text-muted)', fontSize: '0.84rem', margin: 0, lineHeight: 1.4 }}>
                          {item.description}
                        </p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Extracted Skills Tag Cloud */}
            <div className="glass-card" style={{ padding: '24px' }}>
              <h4 style={{ fontSize: '1.05rem', color: '#fff', marginBottom: '14px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                <Tag size={18} color="var(--primary-light)" />
                Extracted Skills & Competencies ({activeResult.skills ? activeResult.skills.length : 0})
              </h4>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
                {activeResult.skills && activeResult.skills.map((skill, idx) => (
                  <span key={idx} className="badge badge-indigo" style={{ padding: '6px 12px', fontSize: '0.85rem' }}>
                    <CheckCircle2 size={12} /> {skill}
                  </span>
                ))}
              </div>
            </div>
          </div>
        ) : (
          /* EMPTY PLACEHOLDER SHOWN STRICTLY BEFORE UPLOADING A RESUME FILE */
          <div className="glass-card" style={{
            padding: '40px 32px',
            textAlign: 'center',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            background: 'rgba(15, 23, 42, 0.45)',
            border: '2px dashed var(--border-glass)'
          }}>
            <div style={{
              width: '64px',
              height: '64px',
              borderRadius: '50%',
              background: 'rgba(99, 102, 241, 0.15)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              marginBottom: '16px'
            }}>
              <FileQuestion size={32} color="var(--primary-light)" />
            </div>

            <h3 style={{ fontSize: '1.3rem', color: '#fff', marginBottom: '8px' }}>
              Ready to Analyze Your Resume
            </h3>

            <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', maxWidth: '420px', lineHeight: 1.5, marginBottom: '20px' }}>
              Select a PDF or DOCX file on the left (or paste your resume text) and click <strong>"Analyze Resume & Calculate ATS Score"</strong> to calculate your ATS compatibility score and generate your candidate profile overview.
            </p>

            <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap', justifyContent: 'center' }}>
              <span className="badge badge-indigo">
                ⚡ 6-Factor Quantifiable ATS Scoring
              </span>
              <span className="badge badge-emerald">
                🎯 Actionable 90%+ Improvement Checklist
              </span>
              <span className="badge badge-amber">
                🎙️ Resume Skill Deep-Dive Questions
              </span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
