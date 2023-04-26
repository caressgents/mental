const registerBtn = document.getElementById("register-btn");
const loginBtn = document.getElementById("login-btn");
const sendBtn = document.getElementById("send-btn");
const authentication = document.getElementById("authentication");
const chat = document.getElementById("chat");

registerBtn.addEventListener("click", async () => {
    const username = document.getElementById("register-username").value;
    const password = document.getElementById("register-password").value;
    const response = await fetch("/create_account", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    });
    const data = await response.json();

    if (data.success) {
        alert("Account created successfully!");
    } else {
        alert("Failed to create an account. Please try again.");
    }
});

loginBtn.addEventListener("click", async () => {
    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;
    const response = await fetch("/authenticate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    });
    const data = await response.json();

    if (data.success) {
        authentication.classList.add("hidden");
        chat.classList.remove("hidden");
    } else {
        alert("Invalid credentials. Please try again.");
    }
});

sendBtn.addEventListener("click", async () => {
    const messageInput = document.getElementById("message-input");
    const message = messageInput.value;
    const chatMessages = document.getElementById("chat-messages");

    if (message.trim() === "") return;

    const userMessage = document.createElement("div");
    userMessage.classList.add("message", "message-user");
    userMessage.textContent = message;
    chatMessages.appendChild(userMessage);
    messageInput.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message})
    });
    const data = await response.json();

    const botMessage = document.createElement("div");
    botMessage.classList.add("message", "message-bot");
    botMessage.textContent = data.response;
    chatMessages.appendChild(botMessage);

    chatMessages.scrollTop = chatMessages.scrollHeight;
});
