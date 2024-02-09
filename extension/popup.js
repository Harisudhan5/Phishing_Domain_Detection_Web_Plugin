// Initialize the URL display element.
const urlDisplay = document.getElementById('url-display');

// Get the currently active tab's URL and display it.
chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
  const currentTab = tabs[0];
  if (currentTab) {
    urlDisplay.textContent = currentTab.url;
  }
});

// Add an event listener to the tabs for URL changes.
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.url) {
    urlDisplay.textContent = changeInfo.url;
  }
});

// Add a click event listener to the "Load Webpage" button.
const loadWebpageButton = document.getElementById('load-webpage-button');
loadWebpageButton.addEventListener('click', () => {
  // Get the URL of the currently active tab.
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const currentTab = tabs[0];
    if (currentTab) {
      const currentUrl = currentTab.url;

      // Send a message to the background script to send the URL to Flask.
      chrome.runtime.sendMessage({ action: 'sendURL', url: currentUrl }, (response) => {
        // Handle the response from the background script.
        if (response && response.result) {
          // Update the popup UI or take further actions here.
          // For example, display the result on the popup.
          const resultElement = document.getElementById('result-display');
          resultElement.textContent = response.result;
          console.log(response.result)

        } else {
          // Handle errors if needed.
          console.error('Error in response:', response);
        }
      });
    }
  });
});
