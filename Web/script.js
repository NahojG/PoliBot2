document.addEventListener('DOMContentLoaded', function () {

    var sendButton = document.getElementById('send-btn');
    var messageInput = document.getElementById('input-msg');
    var chatContent = document.getElementById('chat-content');

    sendButton.addEventListener('click', function () {
        var userMessage = messageInput.value.trim();
        if (userMessage) {
            // Disable the send button to prevent multiple clicks
            sendButton.disabled = true;

            // Create and append the user message to the chat content
            var userDiv = document.createElement('div');
            userDiv.textContent = 'Tú: ' + userMessage;
            userDiv.className = 'message user-message';
            chatContent.appendChild(userDiv);

            // Clear the input field
            messageInput.value = '';

            // Send the user message to the Flask backend using AJAX
            fetch('http://159.203.99.44:5000/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ 'question': userMessage })
            })
                .then(response => response.json())
                .then(data => {
                    // Create and append the bot response to the chat content
                    var botDiv = document.createElement('div');
                    //botDiv.textContent = 'PoliBot: ' + data.response;
                    botDiv.className = 'message bot-message';

                    // Split the reponse into paragraphs
                    var paragraphs = data.response.split('\n')

                    // Create a <p> element for each paragraph
                    paragraphs.forEach(paragraph => {
                        var p = document.createElement('p');
                        if (p !== '\n') {
                            p.textContent = paragraph;
                            botDiv.appendChild(p);
                        }
                    });


                    chatContent.appendChild(botDiv);

                    // Scroll to the last message
                    chatContent.scrollTop = chatContent.scrollHeight;
                })
                .catch(error => {
                    console.error('Error:', error);
                })
                .finally(() => {
                    // Re-enable the send button once the fetch is complete
                    sendButton.disabled = false;
                });
        }
    });

    function changeBackgroundImage() {
        // Generating a random number between 1 and 10
        var randomNumber = Math.floor(Math.random() * 10) + 1;
        var imagePath = 'backgrounds/' + randomNumber + '.png'; // Building the image path with folder

        // Assuming you want to change the background of the body
        document.body.style.backgroundImage = 'url(' + imagePath + ')';
        document.body.style.backgroundSize = 'cover';
        document.body.style.backgroundRepeat = 'no-repeat';
    }

    // Change the background image every 30 seconds
    setInterval(changeBackgroundImage, 30000);

    // Also change the image immediately when the page loads
    changeBackgroundImage();

    // Allow pressing "Enter" to send the message
    messageInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter' && !sendButton.disabled) {
            sendButton.click();
        }
    });
});
