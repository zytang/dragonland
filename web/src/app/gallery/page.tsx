"use client";

import React, { useState } from 'react';
import Image from 'next/image';
import { useLanguage } from '@/context/LanguageContext';
import { getTranslation } from '@/utils/i18n';

// Dragon Data Keys
const dragons = [
    { key: "ignis", img: "/assets/dragon_fire.png" },
    { key: "aqua", img: "/assets/dragon_water.png" },
    { key: "terra", img: "/assets/dragon_nature.png" },
    { key: "frosty", img: "/assets/dragon_ice.png" },
    { key: "aurelius", img: "/assets/dragon_gold.png" }
];

export default function Gallery() {
    const { lang } = useLanguage();
    const [votedDragon, setVotedDragon] = useState<string | null>(null);

    return (
        <div style={{ paddingTop: '30px' }}>
            <h1 style={{ textAlign: 'center', color: 'var(--color-primary)', fontSize: '3rem', marginBottom: '10px' }}>
                {getTranslation('gallery_title', lang)}
            </h1>
            <p style={{ textAlign: 'center', fontSize: '1.2rem', marginBottom: '40px' }}>
                {getTranslation('gallery_subtitle', lang)}
            </p>

            {/* Grid Layout */}
            <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
                gap: '30px',
                marginBottom: '50px'
            }}>
                {dragons.map((dragon) => (
                    <DragonCard key={dragon.key} dragonKey={dragon.key} imgPath={dragon.img} lang={lang} />
                ))}
            </div>

            {/* Voting Section */}
            <div className="glass-card" style={{ textAlign: 'center' }}>
                <h3>{getTranslation('vote_label', lang)}</h3>
                <div style={{ display: 'flex', justifyContent: 'center', gap: '20px', flexWrap: 'wrap', marginTop: '20px' }}>
                    {dragons.map((d) => (
                        <button
                            key={d.key}
                            onClick={() => setVotedDragon(d.key)}
                            style={{
                                background: votedDragon === d.key ? 'var(--color-primary)' : '#fff',
                                color: votedDragon === d.key ? '#fff' : 'var(--color-primary)',
                                border: '2px solid var(--color-primary)',
                                padding: '10px 20px',
                                borderRadius: '20px',
                                cursor: 'pointer',
                                fontWeight: 'bold',
                                transition: 'all 0.2s'
                            }}
                        >
                            {getTranslation(`${d.key}_name` as any, lang).split(' ')[0]}
                        </button>
                    ))}
                </div>

                {votedDragon && (
                    <div style={{ marginTop: '20px', color: 'var(--color-primary)', fontSize: '1.2rem', fontWeight: 'bold', animation: 'fadeIn 0.5s' }}>
                        {getTranslation('vote_success', lang).replace('{name}', getTranslation(`${votedDragon}_name` as any, lang).split(' ')[0])}
                    </div>
                )}
            </div>
        </div>
    );
}

function DragonCard({ dragonKey, imgPath, lang }: { dragonKey: string, imgPath: string, lang: any }) {
    const [isExpanded, setIsExpanded] = useState(false);
    const name = getTranslation(`${dragonKey}_name` as any, lang);
    const title = getTranslation(`${dragonKey}_title` as any, lang);
    const food = getTranslation(`${dragonKey}_food` as any, lang);
    const power = getTranslation(`${dragonKey}_power` as any, lang);
    const story = getTranslation(`${dragonKey}_story` as any, lang);

    return (
        <div className="glass-card" style={{ padding: '2rem', display: 'flex', flexDirection: 'column', margin: 0 }}>
            {/* Header */}
            <div style={{ textAlign: 'center', marginBottom: '15px' }}>
                <h3 style={{ fontSize: '1.5rem', marginBottom: '5px' }}>{name}</h3>
                <p style={{ color: '#666', fontSize: '0.9rem' }}>{title}</p>
            </div>

            {/* Image */}
            <div style={{ position: 'relative', width: '100%', height: '200px', marginBottom: '20px' }}>
                <Image
                    src={imgPath}
                    alt={name}
                    fill
                    style={{ objectFit: 'contain' }}
                />
            </div>

            {/* Story Toggler */}
            <button
                onClick={() => setIsExpanded(!isExpanded)}
                style={{
                    background: 'none',
                    border: '2px solid var(--color-secondary)',
                    color: 'var(--color-secondary)',
                    padding: '10px',
                    borderRadius: '10px',
                    cursor: 'pointer',
                    fontWeight: 'bold',
                    marginBottom: '15px',
                    width: '100%'
                }}
            >
                {getTranslation('btn_read_story', lang).replace('{name}', name.split(' ')[0])}
                {isExpanded ? ' ▲' : ' ▼'}
            </button>

            {/* Expanded Story */}
            {isExpanded && (
                <div style={{
                    background: 'rgba(255,255,255,0.5)',
                    padding: '15px',
                    borderRadius: '10px',
                    marginBottom: '15px',
                    fontSize: '0.95rem',
                    fontStyle: 'italic',
                    lineHeight: '1.4'
                }}>
                    {story}
                </div>
            )}

            {/* Stats */}
            <div style={{ background: '#f0f2f6', padding: '15px', borderRadius: '10px', marginTop: 'auto' }}>
                <p style={{ marginBottom: '5px' }}><strong>{getTranslation('food_label', lang)}</strong> {food}</p>
                <p><strong>{getTranslation('power_label', lang)}</strong> {power}</p>
            </div>
        </div>
    );
}
