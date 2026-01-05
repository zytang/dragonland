"use client";

import React from 'react';
import Link from 'next/link';
import { useLanguage } from '@/context/LanguageContext';
import { getTranslation } from '@/utils/i18n';

export default function Home() {
  const { lang } = useLanguage();

  return (
    <div style={{ paddingTop: '50px' }}>
      {/* Hero Section */}
      <div style={{ textAlign: 'center', marginBottom: '50px' }}>
        <h1 style={{
          fontSize: '4rem',
          color: 'var(--color-primary)',
          textShadow: '3px 3px 0px white',
          marginBottom: '10px'
        }}>
          {getTranslation('home_title', lang)}
        </h1>
        <h3 style={{
          fontSize: '1.5rem',
          color: '#4A4A4A',
          fontWeight: 800
        }}>
          {getTranslation('home_subtitle', lang)}
        </h3>
      </div>

      {/* Story Card */}
      <div className="glass-card" style={{ maxWidth: '800px', margin: '0 auto' }}>
        <div style={{ textAlign: 'center' }}>
          <h2 style={{ color: 'var(--color-primary)', fontSize: '2.5rem', marginBottom: '20px' }}>
            {getTranslation('story_card_title', lang)}
          </h2>

          <div style={{ fontSize: '1.2rem', lineHeight: 1.8, color: '#333' }}>
            <p dangerouslySetInnerHTML={{ __html: getTranslation('story_p1', lang) }} />
            <br />
            <p dangerouslySetInnerHTML={{ __html: getTranslation('story_p2', lang) }} />
            <br />
            <p dangerouslySetInnerHTML={{ __html: getTranslation('story_p3', lang) }} />

            <div style={{
              display: 'flex',
              flexDirection: 'column',
              gap: '15px',
              background: 'rgba(255,255,255,0.6)',
              padding: '25px',
              borderRadius: '20px',
              textAlign: 'left',
              marginTop: '20px'
            }}>
              <div style={{ display: 'flex', alignItems: 'start', gap: '15px' }}>
                <span style={{ fontSize: '1.5rem' }}>🚀</span>
                <span dangerouslySetInnerHTML={{ __html: getTranslation('story_list_1', lang) }} />
              </div>
              <div style={{ display: 'flex', alignItems: 'start', gap: '15px' }}>
                <span style={{ fontSize: '1.5rem' }}>🌍</span>
                <span dangerouslySetInnerHTML={{ __html: getTranslation('story_list_2', lang) }} />
              </div>
              <div style={{ display: 'flex', alignItems: 'start', gap: '15px' }}>
                <span style={{ fontSize: '1.5rem' }}>🤝</span>
                <span dangerouslySetInnerHTML={{ __html: getTranslation('story_list_3', lang) }} />
              </div>
            </div>

            <p style={{ marginTop: '30px', fontSize: '1.3rem', fontWeight: 800, color: 'var(--color-primary)' }}>
              {getTranslation('join_quest', lang)}
            </p>
          </div>
        </div>
      </div>

      {/* Action Button */}
      <div style={{ textAlign: 'center', marginBottom: '60px' }}>
        <Link href="/gallery" className="btn-primary">
          {getTranslation('btn_start', lang)}
        </Link>
      </div>

      {/* Metrics */}
      <div className="glass-card" style={{ maxWidth: '800px', margin: '0 auto', textAlign: 'center' }}>
        <h3 style={{ marginBottom: '20px' }}>{getTranslation('metrics_title', lang)}</h3>
        <div style={{ display: 'flex', justifyContent: 'space-around', flexWrap: 'wrap', gap: '20px' }}>
          <div>
            <div style={{ fontSize: '2.5rem', color: '#FF6B6B', fontWeight: 'bold' }}>{getTranslation('metric_happiness_val', lang)}</div>
            <div style={{ color: '#666' }}>{getTranslation('metric_happiness_label', lang)}</div>
          </div>
          <div>
            <div style={{ fontSize: '2.5rem', color: '#4ECDC4', fontWeight: 'bold' }}>{getTranslation('metric_curiosity_val', lang)}</div>
            <div style={{ color: '#666' }}>{getTranslation('metric_curiosity_label', lang)}</div>
          </div>
          <div>
            <div style={{ fontSize: '2.5rem', color: '#FFC107', fontWeight: 'bold' }}>{getTranslation('metric_friends_val', lang)}</div>
            <div style={{ color: '#666' }}>{getTranslation('metric_friends_label', lang)}</div>
          </div>
        </div>
      </div>
    </div>
  );
}
