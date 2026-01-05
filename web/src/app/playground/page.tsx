"use client";

import React, { useState, useEffect } from 'react';
import { useLanguage } from '@/context/LanguageContext';
import { getTranslation } from '@/utils/i18n';

export default function Playground() {
    const { lang } = useLanguage();
    const [activeTab, setActiveTab] = useState('math');

    const tabs = [
        { id: 'math', label: 'tab_math' },
        { id: 'friendship', label: 'tab_friend' },
        { id: 'name', label: 'tab_name' },
        { id: 'color', label: 'tab_color' }
    ];

    return (
        <div style={{ paddingTop: '30px', paddingBottom: '50px' }}>
            <h1 style={{ textAlign: 'center', color: 'var(--color-primary)', fontSize: '3rem', marginBottom: '10px' }}>
                {getTranslation('playground_title', lang)}
            </h1>
            <p style={{ textAlign: 'center', fontSize: '1.2rem', marginBottom: '40px' }}>
                {getTranslation('playground_subtitle', lang)}
            </p>

            {/* Tabs */}
            <div style={{
                display: 'flex',
                justifyContent: 'center',
                gap: '10px',
                flexWrap: 'wrap',
                marginBottom: '30px'
            }}>
                {tabs.map((tab) => (
                    <button
                        key={tab.id}
                        onClick={() => setActiveTab(tab.id)}
                        style={{
                            padding: '10px 20px',
                            borderRadius: '20px',
                            border: 'none',
                            background: activeTab === tab.id ? 'var(--color-primary)' : 'rgba(255,255,255,0.8)',
                            color: activeTab === tab.id ? '#fff' : 'var(--color-text)',
                            fontWeight: 'bold',
                            cursor: 'pointer',
                            boxShadow: activeTab === tab.id ? 'var(--shadow-button)' : 'none',
                            transition: 'all 0.2s',
                            fontSize: '1.1rem'
                        }}
                    >
                        {getTranslation(tab.label as any, lang)}
                    </button>
                ))}
            </div>

            {/* Content Area */}
            <div className="glass-card">
                {activeTab === 'math' && <MathGame lang={lang} />}
                {activeTab === 'friendship' && <FriendshipGame lang={lang} />}
                {activeTab === 'name' && <NameCreator lang={lang} />}
                {activeTab === 'color' && <ColorMatch lang={lang} />}
            </div>
        </div>
    );
}

// --- Game 1: Math ---
function MathGame({ lang }: { lang: any }) {
    const [target, setTarget] = useState(3);
    const [input, setInput] = useState('');
    const [feedback, setFeedback] = useState<string | null>(null);

    // Initialize random number
    useEffect(() => {
        setTarget(Math.floor(Math.random() * 10) + 1);
    }, []);

    const checkAnswer = () => {
        const val = parseInt(input);
        if (val === target) {
            setFeedback(getTranslation('math_correct', lang));
            // Reset after a moment
            setTimeout(() => {
                setTarget(Math.floor(Math.random() * 10) + 1);
                setInput('');
                setFeedback(null);
            }, 2000);
        } else {
            setFeedback(getTranslation('math_wrong', lang));
        }
    };

    return (
        <div style={{ textAlign: 'center' }}>
            <h2>{getTranslation('math_q', lang)}</h2>
            <div style={{ fontSize: '3rem', margin: '20px 0' }}>
                {Array(target).fill('🐉').join('')}
            </div>

            <div style={{ display: 'flex', justifyContent: 'center', gap: '10px', alignItems: 'center', marginBottom: '20px' }}>
                <label>{getTranslation('math_input_label', lang)}</label>
                <input
                    type="number"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    style={{ padding: '10px', fontSize: '1.2rem', width: '80px', borderRadius: '10px', border: '1px solid #ccc' }}
                />
            </div>

            <button onClick={checkAnswer} className="btn-primary" style={{ fontSize: '1rem', padding: '10px 30px' }}>
                {getTranslation('math_check', lang)}
            </button>

            {feedback && (
                <div style={{ marginTop: '20px', fontSize: '1.5rem', fontWeight: 'bold', color: feedback.includes('Oops') ? 'red' : 'green' }}>
                    {feedback}
                </div>
            )}
        </div>
    );
}

// --- Game 2: Friendship ---
function FriendshipGame({ lang }: { lang: any }) {
    const [feedback, setFeedback] = useState<{ msg: string, type: 'success' | 'warn' } | null>(null);

    const handleChoice = (opt: 1 | 2) => {
        if (opt === 1) {
            setFeedback({ msg: getTranslation('friend_fb1', lang), type: 'success' });
        } else {
            setFeedback({ msg: getTranslation('friend_fb2', lang), type: 'warn' });
        }
    };

    return (
        <div style={{ textAlign: 'center' }}>
            <h2>{getTranslation('friend_q', lang)}</h2>

            <div style={{ display: 'flex', justifyContent: 'center', gap: '20px', margin: '30px 0' }}>
                <button
                    onClick={() => handleChoice(1)}
                    style={{ padding: '15px 25px', borderRadius: '15px', border: '2px solid #4ECDC4', background: '#fff', fontSize: '1.1rem', cursor: 'pointer' }}
                >
                    {getTranslation('friend_opt1', lang)}
                </button>
                <button
                    onClick={() => handleChoice(2)}
                    style={{ padding: '15px 25px', borderRadius: '15px', border: '2px solid #FF6B6B', background: '#fff', fontSize: '1.1rem', cursor: 'pointer' }}
                >
                    {getTranslation('friend_opt2', lang)}
                </button>
            </div>

            {feedback && (
                <div style={{
                    padding: '15px',
                    borderRadius: '10px',
                    background: feedback.type === 'success' ? '#d4edda' : '#fff3cd',
                    color: feedback.type === 'success' ? '#155724' : '#856404',
                    marginBottom: '30px'
                }}>
                    {feedback.msg}
                </div>
            )}

            <hr style={{ margin: '30px 0', opacity: 0.3 }} />
            <h3>{getTranslation('friend_magic', lang)}</h3>
            <div style={{ display: 'flex', justifyContent: 'center', gap: '15px', marginTop: '15px' }}>
                {['magic_please', 'magic_thank_you', 'magic_sorry'].map(key => (
                    <div key={key} style={{ background: '#f8f9fa', padding: '10px 20px', borderRadius: '20px', fontWeight: 'bold' }}>
                        {getTranslation(key as any, lang)}
                    </div>
                ))}
            </div>
        </div>
    );
}

// --- Game 3: Name Creator ---
function NameCreator({ lang }: { lang: any }) {
    const prefixes = lang === 'zh'
        ? ["闪闪", "雷霆", "星光", "月亮", "彩虹", "小小", "勇敢"]
        : ["Glitter", "Thunder", "Star", "Moon", "Rainbow", "Little", "Brave"];

    const suffixes = lang === 'zh'
        ? ["之翼", "鳞片", "利爪", "之心", "吐息", "尾巴", "脚趾"]
        : ["Wing", "Scale", "Claw", "Heart", "Breath", "Tail", "Toe"];

    const [p, setP] = useState(prefixes[0]);
    const [s, setS] = useState(suffixes[0]);

    // Reset selection when language changes
    useEffect(() => {
        setP(prefixes[0]);
        setS(suffixes[0]);
    }, [lang]);

    const fullName = lang === 'zh' ? p + s : `${p} ${s}`;

    return (
        <div style={{ textAlign: 'center' }}>
            <h2>{getTranslation('tab_name', lang)}</h2>

            <div style={{ display: 'flex', justifyContent: 'center', gap: '20px', margin: '30px 0', alignItems: 'center', flexWrap: 'wrap' }}>
                <div>
                    <label style={{ display: 'block', marginBottom: '5px' }}>{getTranslation('name_prefix', lang)}</label>
                    <select
                        value={p} onChange={e => setP(e.target.value)}
                        style={{ padding: '10px', fontSize: '1.1rem', borderRadius: '10px', border: '1px solid #ccc' }}
                    >
                        {prefixes.map(val => <option key={val} value={val}>{val}</option>)}
                    </select>
                </div>
                <div style={{ fontSize: '2rem' }}>+</div>
                <div>
                    <label style={{ display: 'block', marginBottom: '5px' }}>{getTranslation('name_suffix', lang)}</label>
                    <select
                        value={s} onChange={e => setS(e.target.value)}
                        style={{ padding: '10px', fontSize: '1.1rem', borderRadius: '10px', border: '1px solid #ccc' }}
                    >
                        {suffixes.map(val => <option key={val} value={val}>{val}</option>)}
                    </select>
                </div>
            </div>

            <div style={{ fontSize: '2rem', color: 'var(--color-primary)', fontWeight: 'bold' }}>
                {getTranslation('name_result', lang).replace('{name}', fullName).replace(/\*\*/g, '')}
            </div>
        </div>
    );
}

// --- Game 4: Color Match ---
function ColorMatch({ lang }: { lang: any }) {
    const elements = [
        { key: "fire", nameKey: "color_fire", emoji: "🟥", colorKey: "color_red" },
        { key: "water", nameKey: "color_water", emoji: "🟦", colorKey: "color_blue" },
        { key: "nature", nameKey: "color_nature", emoji: "🟩", colorKey: "color_green" }
    ];

    const [target, setTarget] = useState(elements[0]);
    const [feedback, setFeedback] = useState<string | null>(null);

    const checkColor = (selectedKey: string) => {
        if (selectedKey === target.key) {
            setFeedback(getTranslation('color_correct', lang));
            setTimeout(() => {
                setTarget(elements[Math.floor(Math.random() * elements.length)]);
                setFeedback(null);
            }, 1500);
        } else {
            setFeedback(getTranslation('color_wrong', lang));
        }
    };

    return (
        <div style={{ textAlign: 'center' }}>
            <h2>
                {getTranslation('color_q', lang).replace('{element}', getTranslation(target.nameKey as any, lang)).replace(/\*\*/g, '')}
            </h2>
            <p style={{ margin: '15px 0' }}>{getTranslation('color_instruction', lang)}</p>

            <div style={{ display: 'flex', justifyContent: 'center', gap: '20px', marginTop: '20px' }}>
                {elements.map((el) => (
                    <button
                        key={el.key}
                        onClick={() => checkColor(el.key)}
                        style={{
                            padding: '20px',
                            fontSize: '1.2rem',
                            borderRadius: '15px',
                            border: '2px solid #eee',
                            background: '#fff',
                            cursor: 'pointer',
                            minWidth: '120px'
                        }}
                    >
                        <div style={{ fontSize: '2rem', marginBottom: '5px' }}>{el.emoji}</div>
                        <div>{getTranslation(el.colorKey as any, lang)}</div>
                    </button>
                ))}
            </div>

            {feedback && (
                <div style={{ marginTop: '30px', fontSize: '1.5rem', fontWeight: 'bold', color: feedback.includes('match') ? 'green' : 'orange' }}>
                    {feedback}
                </div>
            )}
        </div>
    );
}
