// Listen for messages from the background script.
chrome.runtime.onMessage.addListener((message) => {
    if (message.url) {
      // Create a new alert element.
      const alertElement = document.createElement("div");
      alertElement.style.position = "fixed";
      alertElement.style.top = "10px";
      alertElement.style.left = "10px";
      alertElement.style.padding = "10px";
      alertElement.style.backgroundColor = "#f0f0f0";
      alertElement.style.border = "1px solid #ccc";
      alertElement.style.zIndex = "9999";
      alertElement.textContent = `URL changed to: ${message.url}`;
  
      // Append the alert element to the document.
      document.body.appendChild(alertElement);
  
      // Remove the alert element after a few seconds (optional).
      setTimeout(() => {
        document.body.removeChild(alertElement);
      }, 5000); // Remove after 5 seconds (adjust as needed).
    }
  });
