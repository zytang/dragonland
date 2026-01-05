"use client";

import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useLanguage } from '@/context/LanguageContext';

export default function Navbar() {
    const pathname = usePathname();
    const { lang, setLang } = useLanguage();

    const toggleLang = () => {
        setLang(lang === 'en' ? 'zh' : 'en');
    };

    const isActive = (path: string) => pathname === path;

    return (
        <nav style={{
            background: 'rgba(255, 255, 255, 0.95)',
            backdropFilter: 'blur(10px)',
            padding: '15px 0',
            boxShadow: '0 2px 10px rgba(0,0,0,0.1)',
            position: 'sticky',
            top: 0,
            zIndex: 1000
        }}>
            <div className="container" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <Link href="/" style={{ fontSize: '1.8rem', fontWeight: 800, color: 'var(--color-primary)' }}>
                    🐉
                </Link>

                <div style={{ display: 'flex', gap: '20px', alignItems: 'center' }}>
                    <Link href="/" style={{
                        fontWeight: isActive('/') ? 800 : 400,
                        color: isActive('/') ? 'var(--color-primary)' : 'var(--color-text)'
                    }}>Home</Link>
                    <Link href="/gallery" style={{
                        fontWeight: isActive('/gallery') ? 800 : 400,
                        color: isActive('/gallery') ? 'var(--color-primary)' : 'var(--color-text)'
                    }}>Gallery</Link>
                    <Link href="/playground" style={{
                        fontWeight: isActive('/playground') ? 800 : 400,
                        color: isActive('/playground') ? 'var(--color-primary)' : 'var(--color-text)'
                    }}>Playground</Link>

                    <button onClick={toggleLang} style={{
                        background: 'var(--color-background)',
                        border: '2px solid var(--color-primary)',
                        borderRadius: '20px',
                        padding: '5px 15px',
                        cursor: 'pointer',
                        fontWeight: 700,
                        color: 'var(--color-primary)'
                    }}>
                        {lang === 'en' ? '🇨🇳 中文' : '🇺🇸 English'}
                    </button>
                </div>
            </div>
        </nav>
    );
}
