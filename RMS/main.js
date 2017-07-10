var     irc = require('node-irc');
var     bot = new irc('irc.morphux.org', 6667, 'RMS', 'Richard Stallman');
var     net = require('net');
var     quotes = [
            "TRIGERRED",
            "What you mean by saying ‘Linux’, is in fact, GNU slash Linux, or as I’ve recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU core libs, shell utilities and vital system components comprising a full OS.",
            "IT'S FUCKING GNU/Linux",
            "..."
        ]

var server = net.createServer(function(socket) {
    socket.setEncoding('utf8');
    socket.on('data', function(data) {
        var args = data.split(" ");
        var rand = Math.floor((Math.random() * quotes.length))
        console.log(args);
        bot.join('#' + args[0]);
        setTimeout(function () {
            bot.say('#' + args[0], args[1] + ": " + quotes[rand])
            setTimeout(function() {
                bot.part('#' + args[0], 'EMACS4vr');
            }, 2000);
        }, 2000);
    })
});
server.listen(1337, '127.0.0.1');

bot.connect()
