import React, { useState, useEffect } from 'react';
import { User, Mail, Briefcase, Tag, FileText, Globe, Linkedin, Github, Phone, Save, Sparkles, CheckCircle2, ShieldCheck, Clock } from 'lucide-react';

export default function ProfileView({ user, onProfileUpdated }) {
  const [profile, setProfile] = useState({
    full_name: '',
    headline: '',
    target_role: 'Software Engineer',
    industry_category: 'INFORMATION-TECHNOLOGY',
    bio: '',
    skills: [],
    phone: '',
    linkedin_url: '',
    github_url: '',
    portfolio_url: ''
  });

  const [newSkillInput, setNewSkillInput] = useState('');
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    fetchProfile();
  }, [user]);

  const fetchProfile = async () => {
    setLoading(true);
    setError('');
    try {
      const token = localStorage.getItem('prepwise_session_token');
      const res = await fetch('/api/auth/profile', {
        headers: {
          'Authorization': token ? `Bearer ${token}` : ''
        }
      });
      const data = await res.json();
      if (res.ok && data.profile) {
        setProfile(data.profile);
      }
    } catch (err) {
      console.error('Fetch profile error:', err);
      setError('Failed to load candidate profile.');
    } finally {
      setLoading(false);
    }
  };

  const handleSaveProfile = async (e) => {
    e.preventDefault();
    setSaving(true);
    setMessage('');
    setError('');

    try {
      const token = localStorage.getItem('prepwise_session_token');
      const res = await fetch('/api/auth/profile', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': token ? `Bearer ${token}` : ''
        },
        body: JSON.stringify(profile)
      });
      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.error || 'Failed to update profile.');
      }

      setProfile(data.profile);
      setMessage('Your candidate profile has been updated successfully!');
      if (onProfileUpdated) {
        onProfileUpdated(data.profile);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setSaving(false);
    }
  };

  const handleAddSkill = () => {
    if (newSkillInput.trim() && !profile.skills.includes(newSkillInput.trim())) {
      setProfile(prev => ({
        ...prev,
        skills: [...prev.skills, newSkillInput.trim()]
      }));
      setNewSkillInput('');
    }
  };

  const handleRemoveSkill = (skillToRemove) => {
    setProfile(prev => ({
      ...prev,
      skills: prev.skills.filter(s => s !== skillToRemove)
    }));
  };

  if (loading) {
    return (
      <div style={{ textAlign: 'center', padding: '60px', color: 'var(--text-muted)' }}>
        Loading account profile...
      </div>
    );
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px', maxWidth: '1000px', margin: '0 auto' }}>
      {/* Header Banner */}
      <div className="glass-card" style={{ padding: '28px 36px', background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.14) 0%, rgba(139, 92, 246, 0.08) 100%)' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '18px' }}>
            <div style={{
              width: '64px',
              height: '64px',
              borderRadius: '50%',
              background: 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #ec4899 100%)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: '1.6rem',
              fontWeight: 800,
              color: '#fff',
              boxShadow: '0 6px 20px rgba(99, 102, 241, 0.4)'
            }}>
              {profile.full_name ? profile.full_name[0].toUpperCase() : 'U'}
            </div>

            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <h1 style={{ fontSize: '1.8rem', color: '#fff' }}>{profile.full_name || user.username}</h1>
                <span className="badge badge-emerald" style={{ display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
                  <ShieldCheck size={12} /> Account Verified
                </span>
              </div>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.92rem', marginTop: '4px' }}>
                {profile.headline || 'Job Candidate & Professional'} • {user.email}
              </p>
            </div>
          </div>

          <div style={{ textAlign: 'right' }}>
            <span style={{ fontSize: '0.78rem', color: 'var(--text-dim)', display: 'block' }}>Account ID: USER-{user.id || profile.user_id}</span>
            <span style={{ fontSize: '0.78rem', color: 'var(--text-dim)', display: 'block' }}>Created: {profile.created_at || '2026'}</span>
          </div>
        </div>
      </div>

      {message && (
        <div style={{ background: 'rgba(16, 185, 129, 0.18)', border: '1px solid rgba(16, 185, 129, 0.4)', color: '#6ee7b7', padding: '14px 20px', borderRadius: '12px', fontSize: '0.9rem' }}>
          ✓ {message}
        </div>
      )}

      {error && (
        <div style={{ background: 'rgba(239, 68, 68, 0.18)', border: '1px solid rgba(239, 68, 68, 0.4)', color: '#fca5a5', padding: '14px 20px', borderRadius: '12px', fontSize: '0.9rem' }}>
          ✕ {error}
        </div>
      )}

      {/* Main Profile Form */}
      <form onSubmit={handleSaveProfile} className="glass-card" style={{ padding: '32px', display: 'flex', flexDirection: 'column', gap: '24px' }}>
        <h3 style={{ fontSize: '1.25rem', color: '#fff', borderBottom: '1px solid var(--border-glass)', paddingBottom: '12px' }}>
          Personal Details & Career Preferences
        </h3>

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>
              FULL NAME
            </label>
            <input
              type="text"
              value={profile.full_name}
              onChange={(e) => setProfile({ ...profile, full_name: e.target.value })}
              placeholder="e.g. Alex Johnson"
              style={{ width: '100%', padding: '12px' }}
            />
          </div>

          <div>
            <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>
              PROFESSIONAL HEADLINE
            </label>
            <input
              type="text"
              value={profile.headline}
              onChange={(e) => setProfile({ ...profile, headline: e.target.value })}
              placeholder="e.g. Senior Software Engineer | Full-Stack & Cloud Architecture"
              style={{ width: '100%', padding: '12px' }}
            />
          </div>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>
              TARGET JOB ROLE
            </label>
            <input
              type="text"
              value={profile.target_role}
              onChange={(e) => setProfile({ ...profile, target_role: e.target.value })}
              placeholder="e.g. Lead Software Architect"
              style={{ width: '100%', padding: '12px' }}
            />
          </div>

          <div>
            <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>
              INDUSTRY CATEGORY
            </label>
            <select
              value={profile.industry_category}
              onChange={(e) => setProfile({ ...profile, industry_category: e.target.value })}
              style={{ width: '100%', padding: '12px' }}
            >
              <option value="INFORMATION-TECHNOLOGY">Information Technology & Software</option>
              <option value="ENGINEERING">Engineering & Hardware</option>
              <option value="FINANCE">Finance & Accounting</option>
              <option value="HR">Human Resources & Recruitment</option>
              <option value="BUSINESS-DEVELOPMENT">Business Development & Sales</option>
              <option value="HEALTHCARE">Healthcare & Medicine</option>
            </select>
          </div>
        </div>

        <div>
          <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>
            PROFESSIONAL BIO & SUMMARY
          </label>
          <textarea
            value={profile.bio}
            onChange={(e) => setProfile({ ...profile, bio: e.target.value })}
            rows={4}
            placeholder="Write a brief professional summary of your achievements and career goals..."
            style={{ width: '100%', padding: '12px', resize: 'vertical' }}
          />
        </div>

        {/* Technical Skills Manager */}
        <div>
          <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>
            CORE SKILLS & TECHNOLOGIES ({profile.skills ? profile.skills.length : 0})
          </label>
          
          <div style={{ display: 'flex', gap: '10px', marginBottom: '12px' }}>
            <input
              type="text"
              value={newSkillInput}
              onChange={(e) => setNewSkillInput(e.target.value)}
              onKeyDown={(e) => { if (e.key === 'Enter') { e.preventDefault(); handleAddSkill(); } }}
              placeholder="Add a new skill (e.g. Python, Docker, React, AWS)..."
              style={{ flex: 1, padding: '10px 14px' }}
            />
            <button type="button" onClick={handleAddSkill} className="btn-secondary">
              Add Skill
            </button>
          </div>

          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
            {profile.skills && profile.skills.map((skill, idx) => (
              <span key={idx} className="badge badge-indigo" style={{ padding: '6px 12px', fontSize: '0.85rem' }}>
                {skill}
                <button
                  type="button"
                  onClick={() => handleRemoveSkill(skill)}
                  style={{ background: 'none', border: 'none', color: '#fca5a5', marginLeft: '6px', cursor: 'pointer', fontWeight: 700 }}
                >
                  ×
                </button>
              </span>
            ))}
          </div>
        </div>

        {/* Contact & Social Links */}
        <h4 style={{ fontSize: '1.15rem', color: '#fff', borderBottom: '1px solid var(--border-glass)', paddingBottom: '10px', marginTop: '12px' }}>
          Contact Info & Portfolio Links
        </h4>

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>
              PHONE NUMBER
            </label>
            <input
              type="text"
              value={profile.phone}
              onChange={(e) => setProfile({ ...profile, phone: e.target.value })}
              placeholder="+91 9876543210"
              style={{ width: '100%', padding: '12px' }}
            />
          </div>

          <div>
            <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>
              LINKEDIN PROFILE URL
            </label>
            <input
              type="text"
              value={profile.linkedin_url}
              onChange={(e) => setProfile({ ...profile, linkedin_url: e.target.value })}
              placeholder="https://linkedin.com/in/username"
              style={{ width: '100%', padding: '12px' }}
            />
          </div>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>
              GITHUB REPOSITORY URL
            </label>
            <input
              type="text"
              value={profile.github_url}
              onChange={(e) => setProfile({ ...profile, github_url: e.target.value })}
              placeholder="https://github.com/username"
              style={{ width: '100%', padding: '12px' }}
            />
          </div>

          <div>
            <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: 'var(--text-muted)', marginBottom: '6px' }}>
              PORTFOLIO WEBSITE URL
            </label>
            <input
              type="text"
              value={profile.portfolio_url}
              onChange={(e) => setProfile({ ...profile, portfolio_url: e.target.value })}
              placeholder="https://myportfolio.dev"
              style={{ width: '100%', padding: '12px' }}
            />
          </div>
        </div>

        <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '12px' }}>
          <button type="submit" disabled={saving} className="btn-primary" style={{ padding: '12px 28px' }}>
            <Save size={18} /> {saving ? 'Saving Changes...' : 'Save Profile Changes'}
          </button>
        </div>
      </form>
    </div>
  );
}
