# Base Module
# By: Louis <louis@ne02ptzero>

import random
import socket

class Base:

    def ping(self, Morphux, infos):
        Morphux.sendMessage("Pong !", infos['nick'])

    def join(self, Morphux, user):
        if (user != "RMS"):
            Morphux.sendMessage("Hi there !", user)

    def nyan(self, Morphux, infos):
        Morphux.sendMessage(str("telnet nyancat.dakko.us"), infos['nick'])

    def ah(self, Morphux, infos):
        Morphux.sendMessage("https://youtu.be/XE6YaLtctcI", infos['nick'])

    def rms(self, Morphux, line):
        infos = Morphux.getInfo(line, 1)
        if (infos == False):
            return 1;
        if (infos['nick'] == "RMS"):
            return 1
        if (("Linux" in line or "linux" in line) and "GNU" not in line):
            clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientsocket.connect(('localhost', 1337))
            cmd = 'main ' + infos['nick']
            clientsocket.send(cmd.encode())


    def command(self):
        self.config = {
            "command": {
                "ping": {
                    "function": self.ping,
                    "usage": "ping",
                    "help": "Make a ping to the bot"
                },
                "nyan": {
                    "function": self.nyan,
                    "usage": "nyan",
                    "help": "nyannyannyannyannyan"
                },
                "ah": {
                    "function": self.ah,
                    "usage": "ah",
                    "help": "AH !"
                }
            },
            "onJoin": {
                "join": self.join
            },
            "before": {
                "rms": self.rms
            }
        }
        return self.config
