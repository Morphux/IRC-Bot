# Base Module
# By: Louis <louis@ne02ptzero>

import socket
import lxml.etree
import random
import re
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

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

    def wow(self, Morphux, infos):
        Morphux.sendMessage("https://www.youtube.com/embed/jUy9_0M3bVk?autoplay=1", infos['nick'])

    @staticmethod
    def youtube_url_validation(url):
        youtube_regex = (
            r'(https?://)?(www\.)?'
            '(youtube|youtu|youtube-nocookie)\.'
            '((com/((watch\?.v/|watch\?.*v=)|embed/))'
            '|(be/))([\w|\-]{11})'
            )
        youtube_regex_match = re.match(youtube_regex, url)
        if youtube_regex_match:
            return youtube_regex_match
        return youtube_regex_match

    def youtube(self, Morphux, line):
        infos = Morphux.getInfo(line, 1)
        if (infos == False):
            return 1

        if (infos['nick'] == "CL4P_TP"):
            return 1

        line = infos['command'];
        if ("args" in infos):
            line += " " + " ".join(infos['args'])

        if "youtu" in line:
            urls = [t for t in line.split() if self.youtube_url_validation(t)]
            for url in urls:
                if "http" not in url:
                    url = "https://" + url
                myparser = lxml.etree.HTMLParser(encoding='utf-8')
                req = Request(url)
                try:
                    response = urlopen(req)
                except HTTPError as e:
                    Morphux.sendMessage("No can do, page returned an error " + str(e.code))
                    return 1
                except URLError as e:
                    Morphux.sendMessage("Something bad happened, you don't want to know about it.")
                    return 1
                else:
                    youtube = lxml.etree.HTML(response.read(), parser=myparser)
                video_title = youtube.xpath("//span[@id='eow-title']/@title")
                if video_title:
                    Morphux.sendMessage("Video title: " + video_title[0])
                else:
                    Morphux.sendMessage("URL seems correct, but the video is probably unavailable")

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
                },
                "wow": {
                    "function": self.wow,
                    "usage": "wow",
                    "help": "Wooow !"
                }
            },
            "onJoin": {
                "join": self.join
            },
            "before": {
                "rms": self.rms,
                "yt": self.youtube
            }
        }
        return self.config
