import React, { useState, useEffect } from 'react';
import { FileText, Briefcase, Mic, LayoutDashboard, User, LogOut, Sparkles, ShieldCheck } from 'lucide-react';
import ResumeView from './pages/ResumeView';
import JobMatchView from './pages/JobMatchView';
import InterviewView from './pages/InterviewView';
import DashboardView from './pages/DashboardView';
import ProfileView from './pages/ProfileView';
import AuthView from './pages/AuthView';

export default function App() {
  const [user, setUser] = useState(() => {
    try {
      const savedUser = localStorage.getItem('prepwise_user_account');
      return savedUser ? JSON.parse(savedUser) : null;
    } catch (e) {
      return null;
    }
  });

  const [activeTab, setActiveTabState] = useState(() => {
    try {
      const savedTab = localStorage.getItem('prepwise_active_tab');
      return savedTab || 'resume';
    } catch (e) {
      return 'resume';
    }
  });

  const setActiveTab = (tab) => {
    setActiveTabState(tab);
    try {
      localStorage.setItem('prepwise_active_tab', tab);
    } catch (e) {
      console.warn("Could not save activeTab to localStorage:", e);
    }
  };
  
  // Parsed resume data state - ALWAYS STARTS NULL FOR EVERY LOGIN SESSION
  const [parsedData, setParsedDataState] = useState(null);

  const setParsedData = (data) => {
    // Keep parsed resume strictly in component memory for active session only
    setParsedDataState(data);
  };

  useEffect(() => {
    const token = localStorage.getItem('prepwise_session_token');
    if (token) {
      // Verify session token on page load/refresh
      fetch('/api/auth/verify-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ token })
      })
      .then(res => res.json())
      .then(data => {
        if (data.valid && data.user) {
          setUser(data.user);
          localStorage.setItem('prepwise_user_account', JSON.stringify(data.user));
          // Always keep parsedData null on initial login/load so application stays clear
        } else {
          handleLogout();
        }
      })
      .catch(() => {
        // Handled gracefully
      });
    } else {
      setUser(null);
      setParsedDataState(null);
    }
  }, []);

  const handleLogout = () => {
    // Wipes all transient state so every login session starts 100% fresh and blank!
    localStorage.removeItem('prepwise_session_token');
    localStorage.removeItem('prepwise_user_account');
    localStorage.removeItem('prepwise_active_tab');
    localStorage.removeItem('prepwise_current_parsed_resume');
    setParsedDataState(null);
    setUser(null);
  };

  if (!user) {
    return <AuthView onLoginSuccess={(u) => {
      setUser(u);
      localStorage.setItem('prepwise_user_account', JSON.stringify(u));
      
      // CLEAR RESUME STATE ON EVERY NEW LOGIN SO APPLICATION STARTS 100% FRESH & BLANK!
      setParsedDataState(null);
      setActiveTabState('resume');
    }} />;
  }

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Top Floating Glassmorphic Navigation Header */}
      <header style={{
          background: 'rgba(11, 15, 23, 0.85)',
          backdropFilter: 'blur(20px)',
          WebkitBackdropFilter: 'blur(20px)',
          borderBottom: '1px solid var(--border-glass)',
          position: 'sticky',
          top: 0,
          zIndex: 100
        }}>
        <div style={{
          maxWidth: '1360px',
          margin: '0 auto',
          padding: '12px 28px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          flexWrap: 'wrap',
          gap: '16px'
        }}>
          {/* Brand Logo */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px', cursor: 'pointer' }} onClick={() => setActiveTab('resume')}>
            <div style={{
              width: '42px',
              height: '42px',
              borderRadius: '12px',
              background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #ec4899 100%)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              boxShadow: '0 4px 20px rgba(99, 102, 241, 0.5)'
            }}>
              <Sparkles size={24} color="#fff" />
            </div>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '1.35rem', fontWeight: 800, color: '#fff', letterSpacing: '-0.02em' }}>
                  PrepWise <span style={{ background: 'linear-gradient(135deg, #818cf8, #c084fc)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>AI</span>
                </span>
                <span className="badge badge-emerald" style={{ fontSize: '0.68rem', padding: '2px 8px' }}>v2.0 Pro</span>
              </div>
              <span style={{ fontSize: '0.74rem', color: 'var(--text-muted)', display: 'block', fontWeight: 500 }}>
                Unified Career Intelligence Platform
              </span>
            </div>
          </div>

          {/* Navigation Pill Tabs */}
          <nav style={{
            display: 'flex',
            gap: '6px',
            background: 'rgba(15, 23, 42, 0.7)',
            padding: '5px',
            borderRadius: '14px',
            border: '1px solid var(--border-glass)',
            flexWrap: 'wrap'
          }}>
            <button
              onClick={() => setActiveTab('resume')}
              className={activeTab === 'resume' ? 'btn-primary' : 'btn-secondary'}
              style={{
                fontSize: '0.86rem',
                padding: '8px 16px',
                borderRadius: '10px',
                border: activeTab === 'resume' ? 'none' : '1px solid transparent'
              }}
            >
              <FileText size={16} /> Resume Analysis
            </button>
            
            <button
              onClick={() => setActiveTab('jobs')}
              className={activeTab === 'jobs' ? 'btn-primary' : 'btn-secondary'}
              style={{
                fontSize: '0.86rem',
                padding: '8px 16px',
                borderRadius: '10px',
                border: activeTab === 'jobs' ? 'none' : '1px solid transparent'
              }}
            >
              <Briefcase size={16} /> Job Matcher
            </button>
            
            <button
              onClick={() => setActiveTab('interview')}
              className={activeTab === 'interview' ? 'btn-primary' : 'btn-secondary'}
              style={{
                fontSize: '0.86rem',
                padding: '8px 16px',
                borderRadius: '10px',
                border: activeTab === 'interview' ? 'none' : '1px solid transparent'
              }}
            >
              <Mic size={16} /> Interview & Practice
            </button>
            
            <button
              onClick={() => setActiveTab('dashboard')}
              className={activeTab === 'dashboard' ? 'btn-primary' : 'btn-secondary'}
              style={{
                fontSize: '0.86rem',
                padding: '8px 16px',
                borderRadius: '10px',
                border: activeTab === 'dashboard' ? 'none' : '1px solid transparent'
              }}
            >
              <LayoutDashboard size={16} /> Performance Dashboard
            </button>

            <button
              onClick={() => setActiveTab('profile')}
              className={activeTab === 'profile' ? 'btn-primary' : 'btn-secondary'}
              style={{
                fontSize: '0.86rem',
                padding: '8px 16px',
                borderRadius: '10px',
                border: activeTab === 'profile' ? 'none' : '1px solid transparent'
              }}
            >
              <User size={16} /> Candidate Profile
            </button>
          </nav>

          {/* User Profile Badge & Logout */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
            <div
              onClick={() => setActiveTab('profile')}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '10px',
                padding: '6px 14px',
                borderRadius: '12px',
                background: 'rgba(255,255,255,0.04)',
                border: '1px solid var(--border-glass)',
                cursor: 'pointer'
              }}
            >
              <div style={{
                width: '32px',
                height: '32px',
                borderRadius: '50%',
                background: 'linear-gradient(135deg, #6366f1, #8b5cf6)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontWeight: 700,
                color: '#fff',
                fontSize: '0.85rem'
              }}>
                {user.username ? user.username[0].toUpperCase() : 'U'}
              </div>
              <div style={{ textAlign: 'left' }}>
                <span style={{ fontSize: '0.84rem', fontWeight: 700, color: '#fff', display: 'block', lineHeight: 1.2 }}>
                  {user.username}
                </span>
                <span style={{ fontSize: '0.72rem', color: 'var(--text-muted)' }}>
                  {user.email}
                </span>
              </div>
            </div>

            <button
              onClick={handleLogout}
              className="btn-secondary"
              title="Sign Out"
              style={{ padding: '9px 14px', borderRadius: '10px' }}
            >
              <LogOut size={16} />
            </button>
          </div>
        </div>
      </header>

      {/* Main Workspace Canvas */}
      <main style={{
        maxWidth: '1360px',
        width: '100%',
        margin: '0 auto',
        padding: '32px 28px',
        flex: 1
      }}>
        {activeTab === 'resume' && (
          <ResumeView
            parsedData={parsedData}
            setParsedData={setParsedData}
            onResumeParsed={(data) => {
              setParsedData(data);
            }}
          />
        )}

        {activeTab === 'jobs' && (
          <JobMatchView
            parsedData={parsedData}
            onNavigateToResume={() => setActiveTab('resume')}
          />
        )}

        {activeTab === 'interview' && (
          <InterviewView 
            parsedData={parsedData} 
          />
        )}

        {activeTab === 'dashboard' && (
          <DashboardView user={user} />
        )}

        {activeTab === 'profile' && (
          <ProfileView user={user} />
        )}
      </main>

      {/* Footer Banner */}
      <footer style={{
        borderTop: '1px solid var(--border-glass)',
        padding: '24px',
        textAlign: 'center',
        fontSize: '0.84rem',
        color: 'var(--text-muted)',
        background: 'rgba(11, 15, 23, 0.7)',
        backdropFilter: 'blur(10px)'
      }}>
        PrepWise AI Platform • Integrated NLP Resume Screening, TF-IDF Job Matching & Proctored Voice AI Mock Interviewing
      </footer>
    </div>
  );
}
