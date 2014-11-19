import	random

class Matches:
		def command(self):
			self.config = {
				"command": {
					"matches": {
						"function": self.matchesCommand,
						"usage": "matches [user]",
						"help": "Duel another user in a matches game"
					},
					"game": {
						"function": self.gameCommand,
						"usage": "game",
						"help": "Starts the matches fight"
					},
					"decline": {
						"function": self.declineCommand,
						"usage": "decline",
						"help": "Refuses the matches fight"
					},
					"remove": {
						"function": self.removeMatches,
						"usage": "remove [1-2-3]",
						"help": "Removes a number of matches"
					}
				}
			}
			self.matchStarted = 0
			self.firstPlayer = 0
			self.secondPlayer = 0
			self.currentPlayer = 0
			self.matchesNumber = 0
			return self.config
		def matchesCommand(self, Morphux, infos):
			if (self.matchStarted == 0):
				if (len(infos['args']) == 0):
					Morphux.sendMessage("No AI ready yet, choose an opponent", infos['nick'])
				elif (infos['args'][0] == infos['nick']):
					Morphux.sendMessage("Choose ANOTHER player", infos['nick'])
				elif (Morphux.userExists(infos['args'][0])):
					Morphux.sendMessage("Hey " + infos['args'][0] + ", " + infos['nick'] + " wants to play a game of matches with you! !game or !decline", infos['nick'])
					self.firstPlayer = infos['nick']
					self.secondPlayer = infos['args'][0]
					self.matchStarted = 1;
				else:
					Morphux.sendMessage("No such user " + infos['args'][0] + " :(", infos['nick'])
			else:
				Morphux.sendMessage("A match is already started")
		def gameCommand(self, Morphux, infos):
			if (self.secondPlayer != infos['nick']):
				Morphux.sendMessage("Not you!")
			else:
				self.matchesNumber = random.randint(15, 25)
				Morphux.sendMessage("There are " + str(self.matchesNumber) + " matches on the board.")
				Morphux.sendMessage("Its " + str(self.firstPlayer) + " time to play.")
				self.currentPlayer = self.firstPlayer
		def declineCommand(self, Morphux, infos):
			if (self.secondPlayer == infos['nick']):
				Morphux.sendMessage("No time to play, I see...", infos['nick'])
				self.matchStarted = 0
		def removeMatches(self, Morphux, infos):
			if (self.matchStarted == 1):
				if (self.currentPlayer != infos['nick']):
					Morphux.sendMessage("Not you!")
				else:
					if (int(infos['args'][0]) >= 1 and int(infos['args'][0]) <= 3):
						self.matchesNumber -= int(infos['args'][0])
						if (self.matchesNumber <= 0):
							Morphux.sendMessage(infos['nick'] + " just lost the game!")
							goKick(infos['nick'], "No noobs in my chan")
						else:
							if (int(infos['args'][0]) > 1):
								Morphux.sendMessage(infos['nick'] + " removed " + str(infos['args'][0]) + " matches, " + str(self.matchesNumber) + " remaining")
							else:
								Morphux.sendMessage(infos['nick'] + " removed " + str(infos['args'][0]) + " match, " + str(self.matchesNumber) + " remaining")
							if (self.currentPlayer == self.firstPlayer):
								self.currentPlayer = self.secondPlayer
							else:
								self.currentPlayer = self.firstPlayer
			else:
				Morphux.sendMessage("Not in playmode!")

