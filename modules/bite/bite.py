# -*- coding: utf-8 -*-

# Bite Module
# By: Enerdhil <hezardj@gmail.com>

class Bite:

    def command(self):
        self.config = {
                "command": {
                        "bite": {
                                "function": self.bite,
                                "usage": "bite",
                                "help": "C'est ma bite !"
                        },
                        "mabite": {
                                "function": self.mabite,
                                "usage": "bite",
                                "help": "C'est ma bite !"
                        },
                }
        }
        return self.config

    def bite(self, Morphux, infos):
        Morphux.sendMessage("c∷∷∷∷∷3", infos['nick'])

    def mabite(self, Morphux, infos):
            Morphux.sendMessage("∷∷∷∷∷Э")
            Morphux.sendMessage("OO")
