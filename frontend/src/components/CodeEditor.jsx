import React from 'react';
import { Code, Play, RotateCcw, Copy, Check } from 'lucide-react';

export default function CodeEditor({
  code,
  setCode,
  language,
  setLanguage,
  onRunCode,
  onEvaluateAi,
  loading
}) {
  const [copied, setCopied] = React.useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const lineNumbers = code.split('\n').map((_, i) => i + 1);

  return (
    <div style={{
      background: '#0d1117',
      border: '1px solid var(--border-glass)',
      borderRadius: '12px',
      overflow: 'hidden',
      display: 'flex',
      flexDirection: 'column'
    }}>
      {/* Editor Top Bar */}
      <div style={{
        padding: '12px 18px',
        background: '#161b22',
        borderBottom: '1px solid var(--border-glass)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        flexWrap: 'wrap',
        gap: '12px'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <span style={{ fontSize: '0.86rem', color: 'var(--text-muted)', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Code size={16} color="var(--primary-light)" /> Language:
          </span>
          <select
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
            style={{
              padding: '6px 12px',
              background: '#0d1117',
              border: '1px solid var(--border-glass)',
              borderRadius: '6px',
              color: '#6366f1',
              fontWeight: 700,
              fontSize: '0.85rem',
              outline: 'none'
            }}
          >
            <option value="python">Python 3.10</option>
            <option value="java">Java 17</option>
            <option value="cpp">C++ 20 (GCC)</option>
            <option value="c">C (GCC 11)</option>
            <option value="sql">SQL (SQLite / PostgreSQL)</option>
          </select>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <button
            onClick={handleCopy}
            className="btn-secondary"
            style={{ padding: '6px 12px', fontSize: '0.78rem' }}
          >
            {copied ? <Check size={14} color="#10b981" /> : <Copy size={14} />}
            {copied ? 'Copied' : 'Copy'}
          </button>

          <button
            onClick={onRunCode}
            disabled={loading}
            className="btn-primary"
            style={{ padding: '6px 16px', fontSize: '0.84rem' }}
          >
            <Play size={14} /> Run Code
          </button>

          <button
            onClick={onEvaluateAi}
            disabled={loading}
            className="btn-success"
            style={{ padding: '6px 16px', fontSize: '0.84rem' }}
          >
            ✨ AI Big-O & Quality Audit
          </button>
        </div>
      </div>

      {/* Editor Body */}
      <div style={{ display: 'flex', position: 'relative', minHeight: '280px', maxHeight: '420px', overflowY: 'auto' }}>
        {/* Line Numbers Gutter */}
        <div style={{
          padding: '16px 12px',
          background: '#090d16',
          borderRight: '1px solid rgba(255,255,255,0.06)',
          color: '#475569',
          fontFamily: 'Consolas, Monaco, "Andale Mono", monospace',
          fontSize: '0.86rem',
          lineHeight: '1.5',
          textAlign: 'right',
          userSelect: 'none'
        }}>
          {lineNumbers.map(n => (
            <div key={n}>{n}</div>
          ))}
        </div>

        {/* Textarea Code Entry */}
        <textarea
          value={code}
          onChange={(e) => setCode(e.target.value)}
          placeholder="// Type or paste your code here..."
          spellCheck="false"
          style={{
            flex: 1,
            padding: '16px',
            background: '#0d1117',
            color: '#e2e8f0',
            border: 'none',
            outline: 'none',
            fontFamily: 'Consolas, Monaco, "Andale Mono", monospace',
            fontSize: '0.88rem',
            lineHeight: '1.5',
            resize: 'none',
            minHeight: '280px'
          }}
        />
      </div>
    </div>
  );
}
