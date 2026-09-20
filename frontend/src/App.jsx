import { BrowserRouter, Routes, Route } from 'react-router-dom';
import TopNav from './components/TopNav';
import AnalyzePage from './pages/AnalyzePage';
import HistoryPage from './pages/HistoryPage';
import SecurityGuidePage from './pages/SecurityGuidePage';
import AboutPage from './pages/AboutPage';

export default function App() {
  return (
    <BrowserRouter>
      <div className="page-wrapper">
        <TopNav />
        <Routes>
          <Route path="/" element={<AnalyzePage />} />
          <Route path="/history" element={<HistoryPage />} />
          <Route path="/guide" element={<SecurityGuidePage />} />
          <Route path="/about" element={<AboutPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}
