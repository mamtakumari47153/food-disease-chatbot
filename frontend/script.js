async function sendImage() {
  const fileInput = document.getElementById("fileInput");
  const file = fileInput.files[0];

  if (!file) {
    alert("Please select an image");
    return;
  }

  const chatbox = document.getElementById("chatbox");

  // 👤 User message
  chatbox.innerHTML += `
    <div class="msg user">📤 ${file.name}</div>
  `;

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch("http://localhost:8000/chat/", {
      method: "POST",
      body: formData
    });

    if (!response.ok) {
      throw new Error("Server response not OK");
    }

    const data = await response.json();

    // 🤖 Bot message
    chatbox.innerHTML += `
      <div class="msg bot">🤖 ${data.bot}</div>
    `;

    chatbox.scrollTop = chatbox.scrollHeight;

  } catch (error) {
    console.error("Error:", error);

    chatbox.innerHTML += `
      <div class="msg bot">❌ Server not connected</div>
    `;
  }
}