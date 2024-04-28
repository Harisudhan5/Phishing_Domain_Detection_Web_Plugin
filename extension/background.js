// event listner for getting URL from Webpage 
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.url) {
      // Send a message to the popup.js script when the URL changes.
      chrome.runtime.sendMessage({ url: changeInfo.url });
    }
  });
// Listen for messages from the extension popup.
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === 'sendURL') {
    const url = message.url;

    // Specify the Flask backend URL.
    const flaskBackendURL = 'http://localhost:5000/get_url'; // Replace with your Flask backend URL.

    // Send a POST request to the Flask backend with the URL.
    fetch(flaskBackendURL, {
      method: 'POST',
      body: JSON.stringify({ url }),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => response.json())
      .then((data) => {
        // Send the result back to the extension popup.
        sendResponse({ result: data.result });
      })
      .catch((error) => {
        console.error('Error sending data to Flask:', error);
        sendResponse('Backend is sleeping please wake it up');
      });
    // Return true to indicate that we want to use sendResponse asynchronously.
    return true;
  }
});
