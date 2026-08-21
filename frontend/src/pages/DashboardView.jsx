import React, { useState, useEffect } from 'react';
import { Award, TrendingUp, CheckCircle2, ShieldCheck, Target, Activity, FileText, Download, CheckSquare } from 'lucide-react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  RadialLinearScale
} from 'chart.js';
import { Line, Bar } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  RadialLinearScale,
  Title,
  Tooltip,
  Legend
);

export default function DashboardView({ user }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchDashboardAnalytics();
  }, [user]);

  const fetchDashboardAnalytics = async () => {
    setLoading(true);
    try {
      const token = localStorage.getItem('prepwise_session_token');
      const res = await fetch('/api/dashboard/analytics', {
        headers: {
          'Authorization': token ? `Bearer ${token}` : ''
        }
      });
      const json = await res.json();
      if (res.ok) {
        setData(json);
      }
    } catch (err) {
      console.error('Error fetching dashboard analytics:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div style={{ padding: '60px', textAlign: 'center', color: 'var(--text-muted)' }}>
        Loading Performance Dashboard analytics...
      </div>
    );
  }

  const metrics = data?.metrics || {
    ats_score: 0.0,
    avg_interview_score: 0.0,
    readiness_score: 0.0,
    readiness_status: 'Not Started (Upload Resume & Practice)',
    total_interviews: 0,
    total_questions_answered: 0
  };

  const trends = data?.session_trends || [
    { session_name: 'No Sessions', score: 0 }
  ];

  const skillBreakdown = data?.skill_breakdown || {
    keyword_relevance: 0,
    coherence: 0,
    fluency: 0,
    confidence: 0
  };

  const lineChartData = {
    labels: trends.map(t => t.session_name),
    datasets: [
      {
        label: 'Interview Performance Score (%)',
        data: trends.map(t => t.score),
        borderColor: '#6366f1',
        backgroundColor: 'rgba(99, 102, 241, 0.2)',
        tension: 0.35,
        fill: true,
        pointBackgroundColor: '#818cf8',
        pointRadius: 6
      }
    ]
  };

  const barChartData = {
    labels: ['Keyword Relevance', 'Coherence Index', 'Speech Fluency', 'Confidence Heuristic'],
    datasets: [
      {
        label: 'Sub-Competency Score (%)',
        data: [
          skillBreakdown.keyword_relevance,
          skillBreakdown.coherence,
          skillBreakdown.fluency,
          skillBreakdown.confidence
        ],
        backgroundColor: ['#6366f1', '#10b981', '#8b5cf6', '#ec4899'],
        borderRadius: 8
      }
    ]
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: { labels: { color: '#94a3b8' } }
    },
    scales: {
      x: { ticks: { color: '#94a3b8' }, grid: { color: 'rgba(255,255,255,0.05)' } },
      y: { min: 0, max: 100, ticks: { color: '#94a3b8' }, grid: { color: 'rgba(255,255,255,0.05)' } }
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      {/* Header Banner */}
      <div className="glass-card" style={{ padding: '24px 32px', background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(16, 185, 129, 0.1) 100%)' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px' }}>
          <div>
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', marginBottom: '8px' }}>
              <span className="badge badge-emerald">Module 4</span>
              <span className="badge badge-indigo">Progress & Analytics Engine</span>
            </div>
            <h1 style={{ fontSize: '1.8rem', fontWeight: 700, color: '#fff' }}>
              {user?.username ? `${user.username}'s Dashboard` : 'Performance & Readiness Dashboard'}
            </h1>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.92rem', marginTop: '4px' }}>
              Per-account career preparation tracking across ATS resume scores, mock interview sessions, and NLP skill dimensions.
            </p>
          </div>

          <div style={{ textAlign: 'right' }}>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', display: 'block', marginBottom: '4px' }}>OVERALL CAREER READINESS INDEX</span>
            <div style={{ fontSize: '2.5rem', fontWeight: 800, color: metrics.readiness_score >= 80 ? '#10b981' : metrics.readiness_score >= 50 ? '#f59e0b' : '#ef4444' }}>
              {metrics.readiness_score}%
            </div>
            <span className={metrics.readiness_score >= 80 ? 'badge badge-emerald' : 'badge badge-amber'}>
              {metrics.readiness_status}
            </span>
          </div>
        </div>
      </div>

      {/* Metric Cards Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '18px' }}>
        <div className="glass-card" style={{ padding: '20px' }}>
          <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontWeight: 600 }}>ATS RESUME COMPATIBILITY</span>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: '#818cf8', marginTop: '6px' }}>{metrics.ats_score}%</div>
          <span style={{ fontSize: '0.78rem', color: 'var(--text-dim)', marginTop: '4px', display: 'block' }}>Parsed Resume Benchmark</span>
        </div>

        <div className="glass-card" style={{ padding: '20px' }}>
          <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontWeight: 600 }}>AVG INTERVIEW SCORE</span>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: '#6ee7b7', marginTop: '6px' }}>{metrics.avg_interview_score}%</div>
          <span style={{ fontSize: '0.78rem', color: 'var(--text-dim)', marginTop: '4px', display: 'block' }}>NLP Mock Evaluations</span>
        </div>

        <div className="glass-card" style={{ padding: '20px' }}>
          <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontWeight: 600 }}>PRACTICE SESSIONS</span>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: '#fde047', marginTop: '6px' }}>{metrics.total_interviews}</div>
          <span style={{ fontSize: '0.78rem', color: 'var(--text-dim)', marginTop: '4px', display: 'block' }}>Completed Interview Runs</span>
        </div>

        <div className="glass-card" style={{ padding: '20px' }}>
          <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontWeight: 600 }}>QUESTIONS EVALUATED</span>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: '#fca5a5', marginTop: '6px' }}>{metrics.total_questions_answered}</div>
          <span style={{ fontSize: '0.78rem', color: 'var(--text-dim)', marginTop: '4px', display: 'block' }}>Total Speech/Text Responses</span>
        </div>
      </div>

      {/* Charts Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: '1.2fr 1fr', gap: '24px' }}>
        <div className="glass-card" style={{ padding: '24px' }}>
          <h3 style={{ fontSize: '1.1rem', color: '#fff', marginBottom: '16px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <TrendingUp size={18} color="var(--primary-light)" />
            Interview Score Progress Trajectory
          </h3>
          <div style={{ height: '260px' }}>
            <Line data={lineChartData} options={chartOptions} />
          </div>
        </div>

        <div className="glass-card" style={{ padding: '24px' }}>
          <h3 style={{ fontSize: '1.1rem', color: '#fff', marginBottom: '16px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Activity size={18} color="#10b981" />
            NLP Sub-Skills Competency Breakdown
          </h3>
          <div style={{ height: '260px' }}>
            <Bar data={barChartData} options={chartOptions} />
          </div>
        </div>
      </div>

      {/* Actionable Improvement Roadmap */}
      <div className="glass-card" style={{ padding: '24px' }}>
        <h3 style={{ fontSize: '1.15rem', color: '#fff', marginBottom: '14px', display: 'flex', alignItems: 'center', gap: '8px' }}>
          <CheckSquare size={20} color="var(--primary-light)" />
          Personalized Improvement Roadmap
        </h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          {(data?.recommendations || []).map((rec, idx) => (
            <div key={idx} style={{
              background: 'rgba(15, 23, 42, 0.5)',
              border: '1px solid var(--border-glass)',
              padding: '12px 16px',
              borderRadius: '8px',
              display: 'flex',
              alignItems: 'center',
              gap: '12px'
            }}>
              <CheckCircle2 size={18} color="#10b981" />
              <span style={{ fontSize: '0.9rem', color: 'var(--text-main)' }}>{rec}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
