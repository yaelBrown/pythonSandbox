document.addEventListener("DOMContentLoaded", () => {
    console.log("trying to connect")
    var socket = io("http://localhost:5000");
    socket.on('connect', () => {
        socket.send("I am connected");
    });
    socket.on('message', data => {
        console.log("Message recieved: " + data);
    })

    // socket.on('my response', function(msg) {
    //     $('#log').append('<p>Received: ' + msg.data + '</p>');
    // });
    // $('form#emit').submit(function(event) {
    //     socket.emit('my event', {data: $('#emit_data').val()});
    //     return false;
    // });
    // $('form#broadcast').submit(function(event) {
    //     socket.emit('my broadcast event', {data: $('#broadcast_data').val()});
    //     return false;
    // });
})