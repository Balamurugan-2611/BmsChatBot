function toggleChatbot() {
    const chatbotContainer = document.getElementById("chatbot");
    chatbotContainer.scrollIntoView({ behavior: 'smooth' });
}

function sendMessage() {
    const userInput = document.getElementById("user-input");
    const message = userInput.value;
    if (message.trim() === "") return;

    appendMessage("You", message, "user");
    userInput.value = "";

    fetch("/get_response", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        appendMessageWithTypingEffect("InfiPsy", data.response, "bot");
    });
}

function appendMessage(sender, message, type) {
    const chatLog = document.getElementById("chat-log");
    const messageElement = document.createElement("div");
    messageElement.className = `chat-message ${type}`;
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatLog.appendChild(messageElement);
    chatLog.scrollTop = chatLog.scrollHeight;
}

function appendMessageWithTypingEffect(sender, message, type) {
    const chatLog = document.getElementById("chat-log");
    const messageElement = document.createElement("div");
    messageElement.className = `chat-message ${type}`;
    messageElement.innerHTML = `<strong>${sender}:</strong> <span id="typing"></span>`;
    chatLog.appendChild(messageElement);
    chatLog.scrollTop = chatLog.scrollHeight;

    const typingElement = messageElement.querySelector("#typing");
    let index = 0;

    function type() {
        if (index < message.length) {
            typingElement.innerHTML += message.charAt(index);
            index++;
            setTimeout(type, 50); 
        }
    }

    type();
}
