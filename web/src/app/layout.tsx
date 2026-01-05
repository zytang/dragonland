import type { Metadata } from 'next';
import './globals.css';
import { LanguageProvider } from '@/context/LanguageContext';
import Navbar from '@/components/Navbar';

export const metadata: Metadata = {
  title: 'Dragonland 🐉',
  description: 'A magical place for friendship and imagination.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <LanguageProvider>
          <Navbar />
          <main className="container" style={{ paddingBottom: '50px' }}>
            {children}
          </main>
        </LanguageProvider>
      </body>
    </html>
  );
}
