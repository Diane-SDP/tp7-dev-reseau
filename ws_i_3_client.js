const webSocket = new WebSocket("ws://localhost:8765");
msginput = document.getElementById("msg");
msginput.style.display = "none"
msgbtn = document.getElementById("sendmsg");
msgbtn.style.display = "none"
pseudoinput = document.getElementById("pseudo");
pseudobtn = document.getElementById("sendpseudo");
pseudo = ""

function sendmsg() {
    msg = msginput.value
    webSocket.send(msg)
}

function addpseudo() {
    pseudo = pseudoinput.value
    webSocket.send(pseudo)
    const welcometext = document.getElementById('welcome');
    welcometext.innerHTML += pseudo;
    pseudoinput.remove()
    pseudobtn.remove()
    msginput.style.display = "block"
    msgbtn.style.display = "block"
}


webSocket.onmessage = (event) => {
    console.log(event.data);
    const chatParagraph = document.getElementById('chat');
    chatParagraph.innerHTML += event.data + '<br>';
};

webSocket.onopen = () => {
    console.info("WebSocket oppened");
};


webSocket.onerror = (error) => {
    console.error("WebSocket error:", error);
};

webSocket.onclose = (event) => {
    console.log("WebSocket closed:", event);
};
