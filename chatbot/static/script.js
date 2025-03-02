document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    input.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            const userMessage = input.value.trim();
            if (userMessage) {
                chatBox.innerHTML += `<p><strong>Tú:</strong> ${userMessage}</p>`;
                input.value = "";

                // Enviar mensaje al backend
                fetch("/chat", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ text: userMessage }),
                })
                .then(response => response.json())
                .then(data => {
                    chatBox.innerHTML += `<p>${data.response}</p>`;
                    chatBox.scrollTop = chatBox.scrollHeight;
                });
            }
        }
    });
});
