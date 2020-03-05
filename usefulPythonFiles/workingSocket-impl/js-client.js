document.addEventListener("DOMContentLoaded", () => {
    console.log("trying to connect... ")
    var socket = io("http://localhost:5000");

    socket.on('connect', () => {
        socket.send("I am connected");
    });

    socket.on('message', data => {
        console.log("Message recieved: " + data);
    })
})