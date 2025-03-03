setTimeout(function() {
    let messages = document.querySelectorAll('.flash-message');
    messages.forEach(msg => {
        msg.style.opacity = '0';  // Start fading out
        
        // Wait for the CSS transition (500ms) before removing the message
        setTimeout(() => {
            msg.remove(); // Remove the message from the DOM
        }, 500); // Match the transition duration
    });
}, 3000); // Start after 5 seconds
