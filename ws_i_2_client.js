const webSocket = new WebSocket("ws://localhost:8765");


function sendmsg() {
    msg = document.getElementById("msg").value
    webSocket.send(msg)
}

webSocket.onopen = () => {
};

webSocket.onmessage = (event) => {
    alert(event.data);
};

webSocket.onerror = (error) => {
    console.error("WebSocket error:", error);
};

webSocket.onclose = (event) => {
    console.log("WebSocket closed:", event);
};
