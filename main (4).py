# Define the base class Player
class Player:
    def play(self):
        print("The player is playing cricket.")

# Define the driver class Batsman
class Batsman(Player):
    def play(self):
        print("The bastman is batting.")

# Define the derived class Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Create object of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() mathod for each object
batsman.play()
bowler.play()