import { useState, useCallback } from 'react';
import { analyzeMessage } from '../services/api';
import { addHistoryEntry } from '../services/history';

const STEPS = [
  'Processing text',
  'Detecting intent',
  'Extracting entities',
  'Assessing indicators',
  'Preparing assessment',
];

export function useAnalysis() {
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [loadingStep, setLoadingStep] = useState(0);
  const [error, setError] = useState(null);
  const [currentMessage, setCurrentMessage] = useState('');

  const run = useCallback(async (message, demoMode = false) => {
    setLoading(true);
    setError(null);
    setAnalysis(null);
    setLoadingStep(0);
    setCurrentMessage(message);

    // Simulate step progression during API call
    const stepInterval = setInterval(() => {
      setLoadingStep((s) => Math.min(s + 1, STEPS.length - 1));
    }, 400);

    try {
      const result = await analyzeMessage(message, demoMode);
      clearInterval(stepInterval);
      setLoadingStep(STEPS.length);
      setAnalysis(result);
      addHistoryEntry(message, result);
    } catch (err) {
      clearInterval(stepInterval);
      setError(err.message || 'Analysis could not be completed.');
    } finally {
      setLoading(false);
    }
  }, []);

  const reset = useCallback(() => {
    setAnalysis(null);
    setError(null);
    setLoadingStep(0);
    setCurrentMessage('');
  }, []);

  const restoreFromHistory = useCallback((entry) => {
    setCurrentMessage(entry.message);
    setAnalysis(entry.analysis);
    setError(null);
  }, []);

  return {
    analysis,
    loading,
    loadingStep,
    loadingSteps: STEPS,
    error,
    currentMessage,
    run,
    reset,
    restoreFromHistory,
  };
}
