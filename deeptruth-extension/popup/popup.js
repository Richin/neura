const API_URL = 'http://localhost:8000/analyze';

document.addEventListener('DOMContentLoaded', function() {
  // Get current tab URL
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    document.getElementById('url').textContent = tabs[0].url;
  });

  document.getElementById('analyze').addEventListener('click', async function() {
    const results = document.getElementById('results');
    const loading = document.getElementById('loading');
    const error = document.getElementById('error');
    const analyzeBtn = document.getElementById('analyze');

    // Show loading state
    results.classList.add('hidden');
    error.classList.add('hidden');
    loading.classList.remove('hidden');
    analyzeBtn.disabled = true;

    try {
      // Get current tab content
      const [tab] = await chrome.tabs.query({active: true, currentWindow: true});
      
      // Get page content
      const [{ result: pageContent }] = await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        function: () => document.body.innerText,
      });

      console.log('Sending request to:', API_URL);
      console.log('Request data:', {
        url: tab.url,
        content: pageContent.substring(0, 8000)
      });

      // Send to API
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
        body: JSON.stringify({
          url: tab.url,
          content: pageContent.substring(0, 8000)
        })
      });

      console.log('Response status:', response.status);

      if (!response.ok) {
        const errorText = await response.text();
        console.error('Error response:', errorText);
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log('Response data:', data);

      // Update UI with results
      document.getElementById('score').textContent = data.trust_score;
      document.getElementById('analysis-text').textContent = data.analysis;
      
      // Show results
      loading.classList.add('hidden');
      results.classList.remove('hidden');

    } catch (err) {
      console.error('Error:', err);
      loading.classList.add('hidden');
      error.classList.remove('hidden');
      error.textContent = `Error: ${err.message}`;
    } finally {
      analyzeBtn.disabled = false;
    }
  });
}); 