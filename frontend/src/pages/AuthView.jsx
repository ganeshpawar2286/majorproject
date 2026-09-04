import React, { useState } from 'react';
import { ShieldCheck, Mail, Lock, User, ArrowRight, Sparkles, KeyRound, CheckCircle2, ArrowLeft } from 'lucide-react';

export default function AuthView({ onLoginSuccess }) {
  // Modes: 'signin' | 'signup' | 'forgot' | 'reset'
  const [mode, setMode] = useState('signin');
  
  // Form fields
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [resetCode, setResetCode] = useState('');

  // UI state
  const [error, setError] = useState('');
  const [successMsg, setSuccessMsg] = useState('');
  const [loading, setLoading] = useState(false);

  const switchMode = (newMode) => {
    setError('');
    setSuccessMsg('');
    setMode(newMode);
  };

  // Sign In / Sign Up Handler
  const handleAuthSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccessMsg('');
    setLoading(true);

    const isSignup = mode === 'signup';
    const endpoint = isSignup ? '/api/auth/register' : '/api/auth/login';
    const inputVal = (email || username).trim();

    const payload = isSignup 
      ? { username: username || inputVal, email: inputVal, password } 
      : { email: inputVal, username: inputVal, password };

    try {
      const res = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      
      if (!res.ok) {
        throw new Error(data.error || 'Authentication failed');
      }

      if (isSignup) {
        setSuccessMsg(data.message || 'Account created! Please sign in with your new account.');
        switchMode('signin');
      } else {
        const loggedInUser = data.user || { username: inputVal || 'User', email: inputVal };
        if (data.token) {
          localStorage.setItem('prepwise_session_token', data.token);
          localStorage.setItem('prepwise_user_account', JSON.stringify(loggedInUser));
        }
        onLoginSuccess(loggedInUser);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Forgot Password Step 1: Request Verification Code
  const handleForgotPassword = async (e) => {
    e.preventDefault();
    setError('');
    setSuccessMsg('');

    const targetEmail = (email || username).trim();
    if (!targetEmail) {
      setError('Please enter your registered email address.');
      return;
    }

    setLoading(true);
    try {
      const res = await fetch('/api/auth/forgot-password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: targetEmail })
      });
      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.error || 'Failed to request reset code.');
      }

      setResetCode(data.reset_code || '');
      setSuccessMsg(`Verification code generated for ${targetEmail}! Please enter code and new password.`);
      setMode('reset');
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Reset Password Step 2: Update Password
  const handleResetPassword = async (e) => {
    e.preventDefault();
    setError('');
    setSuccessMsg('');

    if (!resetCode.trim()) {
      setError('Please enter the 6-digit verification code.');
      return;
    }
    if (newPassword.length < 6) {
      setError('New password must be at least 6 characters long.');
      return;
    }
    if (newPassword !== confirmPassword) {
      setError('New password and confirm password do not match.');
      return;
    }

    setLoading(true);
    try {
      const targetEmail = (email || username).trim();
      const res = await fetch('/api/auth/reset-password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: targetEmail,
          reset_code: resetCode,
          new_password: newPassword
        })
      });
      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.error || 'Failed to reset password.');
      }

      setSuccessMsg(data.message || 'Password reset successful! Please sign in.');
      switchMode('signin');
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Guest Demo User Bypass
  const handleGuestLogin = () => {
    const guestUser = { id: 1, username: 'Guest Candidate', email: 'guest@prepwise.ai' };
    localStorage.setItem('prepwise_session_token', 'guest_demo_token_123');
    localStorage.setItem('prepwise_user_account', JSON.stringify(guestUser));
    onLoginSuccess(guestUser);
  };

  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      minHeight: '80vh',
      padding: '20px'
    }}>
      <div className="glass-card" style={{ width: '100%', maxWidth: '440px', padding: '36px' }}>
        <div style={{ textAlign: 'center', marginBottom: '24px' }}>
          <div style={{
            width: '56px',
            height: '56px',
            borderRadius: '14px',
            background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)',
            display: 'inline-flex',
            alignItems: 'center',
            justifyContent: 'center',
            boxShadow: '0 8px 24px rgba(99, 102, 241, 0.4)',
            marginBottom: '16px'
          }}>
            {mode === 'forgot' || mode === 'reset' ? (
              <KeyRound size={28} color="#fff" />
            ) : (
              <Sparkles size={28} color="#fff" />
            )}
          </div>
          <h2 style={{ fontSize: '1.75rem', fontWeight: 700, color: '#fff' }}>
            {mode === 'signup' && 'Create PrepWise Account'}
            {mode === 'signin' && 'Welcome Back'}
            {mode === 'forgot' && 'Forgot Password'}
            {mode === 'reset' && 'Reset Your Password'}
          </h2>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.88rem', marginTop: '6px' }}>
            {mode === 'signup' && 'Creates a brand new candidate profile for your account'}
            {mode === 'signin' && 'Sign in to access your individual profile & ATS workspace'}
            {mode === 'forgot' && 'Enter your registered email to receive a reset code'}
            {mode === 'reset' && 'Enter the verification code and set your new password'}
          </p>
        </div>

        {error && (
          <div style={{
            background: 'rgba(239, 68, 68, 0.15)',
            border: '1px solid rgba(239, 68, 68, 0.3)',
            color: '#fca5a5',
            padding: '10px 14px',
            borderRadius: '8px',
            fontSize: '0.85rem',
            marginBottom: '18px'
          }}>
            {error}
          </div>
        )}

        {successMsg && (
          <div style={{
            background: 'rgba(16, 185, 129, 0.15)',
            border: '1px solid rgba(16, 185, 129, 0.3)',
            color: '#6ee7b7',
            padding: '10px 14px',
            borderRadius: '8px',
            fontSize: '0.85rem',
            marginBottom: '18px',
            display: 'flex',
            alignItems: 'center',
            gap: '8px'
          }}>
            <CheckCircle2 size={16} /> {successMsg}
          </div>
        )}

        {/* MODE 1 & 2: SIGN IN / SIGN UP */}
        {(mode === 'signin' || mode === 'signup') && (
          <form onSubmit={handleAuthSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {mode === 'signup' && (
              <div>
                <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>
                  FULL NAME / USERNAME
                </label>
                <div style={{ position: 'relative' }}>
                  <User size={18} style={{ position: 'absolute', left: '12px', top: '12px', color: 'var(--text-dim)' }} />
                  <input
                    type="text"
                    required
                    placeholder="e.g. Alex Johnson"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    style={{
                      width: '100%',
                      padding: '10px 12px 10px 40px',
                      background: 'rgba(15, 23, 42, 0.6)',
                      border: '1px solid var(--border-glass)',
                      borderRadius: '8px',
                      color: '#fff',
                      outline: 'none'
                    }}
                  />
                </div>
              </div>
            )}

            <div>
              <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>
                EMAIL ADDRESS / USERNAME
              </label>
              <div style={{ position: 'relative' }}>
                <Mail size={18} style={{ position: 'absolute', left: '12px', top: '12px', color: 'var(--text-dim)' }} />
                <input
                  type="text"
                  required
                  placeholder="pawarganesh5070@gmail.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '10px 12px 10px 40px',
                    background: 'rgba(15, 23, 42, 0.6)',
                    border: '1px solid var(--border-glass)',
                    borderRadius: '8px',
                    color: '#fff',
                    outline: 'none'
                  }}
                />
              </div>
            </div>

            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                <label style={{ fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)' }}>
                  PASSWORD
                </label>
                {mode === 'signin' && (
                  <span
                    onClick={() => switchMode('forgot')}
                    style={{ fontSize: '0.8rem', color: 'var(--primary-light)', cursor: 'pointer', fontWeight: 600 }}
                  >
                    Forgot password?
                  </span>
                )}
              </div>
              <div style={{ position: 'relative' }}>
                <Lock size={18} style={{ position: 'absolute', left: '12px', top: '12px', color: 'var(--text-dim)' }} />
                <input
                  type="password"
                  required
                  placeholder="••••••••"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '10px 12px 10px 40px',
                    background: 'rgba(15, 23, 42, 0.6)',
                    border: '1px solid var(--border-glass)',
                    borderRadius: '8px',
                    color: '#fff',
                    outline: 'none'
                  }}
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="btn-primary"
              style={{ width: '100%', justifyContent: 'center', padding: '12px', fontSize: '0.98rem', marginTop: '6px' }}
            >
              {loading ? (
                'Processing...'
              ) : (
                <>
                  {mode === 'signup' ? 'Create Account' : 'Sign In'} <ArrowRight size={18} />
                </>
              )}
            </button>

            <div style={{ textAlign: 'center', margin: '8px 0 0 0', position: 'relative' }}>
              <div style={{ borderBottom: '1px solid var(--border-glass)', margin: '14px 0' }} />
              <button
                type="button"
                onClick={handleGuestLogin}
                className="btn-secondary"
                style={{ width: '100%', justifyContent: 'center', fontSize: '0.88rem' }}
              >
                <ShieldCheck size={16} color="#10b981" /> Continue as Guest Demo User
              </button>
            </div>

            <div style={{ textAlign: 'center', fontSize: '0.86rem', color: 'var(--text-muted)', marginTop: '12px' }}>
              {mode === 'signin' ? (
                <>
                  Don't have an account yet?{' '}
                  <span
                    onClick={() => switchMode('signup')}
                    style={{ color: 'var(--primary-light)', cursor: 'pointer', fontWeight: 600 }}
                  >
                    Sign Up
                  </span>
                </>
              ) : (
                <>
                  Already have an account?{' '}
                  <span
                    onClick={() => switchMode('signin')}
                    style={{ color: 'var(--primary-light)', cursor: 'pointer', fontWeight: 600 }}
                  >
                    Sign In
                  </span>
                </>
              )}
            </div>
          </form>
        )}

        {/* MODE 3: FORGOT PASSWORD */}
        {mode === 'forgot' && (
          <form onSubmit={handleForgotPassword} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <div>
              <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>
                REGISTERED EMAIL ADDRESS
              </label>
              <div style={{ position: 'relative' }}>
                <Mail size={18} style={{ position: 'absolute', left: '12px', top: '12px', color: 'var(--text-dim)' }} />
                <input
                  type="email"
                  required
                  placeholder="pawarganesh5070@gmail.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '10px 12px 10px 40px',
                    background: 'rgba(15, 23, 42, 0.6)',
                    border: '1px solid var(--border-glass)',
                    borderRadius: '8px',
                    color: '#fff',
                    outline: 'none'
                  }}
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="btn-primary"
              style={{ width: '100%', justifyContent: 'center', padding: '12px', fontSize: '0.98rem' }}
            >
              {loading ? 'Sending Code...' : 'Get Verification Code'}
            </button>

            <button
              type="button"
              onClick={() => switchMode('signin')}
              className="btn-secondary"
              style={{ width: '100%', justifyContent: 'center', fontSize: '0.86rem' }}
            >
              <ArrowLeft size={16} /> Back to Sign In
            </button>
          </form>
        )}

        {/* MODE 4: RESET PASSWORD */}
        {mode === 'reset' && (
          <form onSubmit={handleResetPassword} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <div>
              <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>
                6-DIGIT VERIFICATION CODE
              </label>
              <input
                type="text"
                required
                placeholder="Enter 6-digit code..."
                value={resetCode}
                onChange={(e) => setResetCode(e.target.value)}
                style={{
                  width: '100%',
                  padding: '10px 12px',
                  background: 'rgba(15, 23, 42, 0.6)',
                  border: '1px solid var(--border-glow)',
                  borderRadius: '8px',
                  color: '#fff',
                  outline: 'none',
                  letterSpacing: '2px',
                  fontWeight: 700,
                  fontSize: '1rem'
                }}
              />
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>
                NEW PASSWORD
              </label>
              <input
                type="password"
                required
                placeholder="Minimum 6 characters"
                value={newPassword}
                onChange={(e) => setNewPassword(e.target.value)}
                style={{
                  width: '100%',
                  padding: '10px 12px',
                  background: 'rgba(15, 23, 42, 0.6)',
                  border: '1px solid var(--border-glass)',
                  borderRadius: '8px',
                  color: '#fff',
                  outline: 'none'
                }}
              />
            </div>

            <div>
              <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>
                CONFIRM NEW PASSWORD
              </label>
              <input
                type="password"
                required
                placeholder="Re-enter new password"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                style={{
                  width: '100%',
                  padding: '10px 12px',
                  background: 'rgba(15, 23, 42, 0.6)',
                  border: '1px solid var(--border-glass)',
                  borderRadius: '8px',
                  color: '#fff',
                  outline: 'none'
                }}
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className="btn-primary"
              style={{ width: '100%', justifyContent: 'center', padding: '12px', fontSize: '0.98rem' }}
            >
              {loading ? 'Updating Password...' : 'Update Password & Sign In'}
            </button>

            <button
              type="button"
              onClick={() => switchMode('signin')}
              className="btn-secondary"
              style={{ width: '100%', justifyContent: 'center', fontSize: '0.86rem' }}
            >
              <ArrowLeft size={16} /> Back to Sign In
            </button>
          </form>
        )}
      </div>
    </div>
  );
}
