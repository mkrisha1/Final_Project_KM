import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def playTurn(self):
        input("Press Enter to roll dice.")
        one = random.randint(1, 6)
        two = random.randint(1, 6)
        three = random.randint(1, 6)
        print(f"{self.name} rolled: {one}, {two}, {three}")
        # Check for three of a kind
        if one == two == three:  # No points for three of a kind
            self.score += 0
            
        # Check for pairs
        elif one == two or one == three or two == three:
            self.score += self.reroll(one, two, three)

        # All dice are different
        else:
            self.score += one + two + three
        print(F"{self.name}'s score is: {self.score}")
        
# rerolling when a pair is rolled.
    def reroll(self, die1, die2, die3):
        if die1 == die2:
            initial_sum = die1 + die2
        elif die1 == die3:
            initial_sum = die1 + die3
        else:
            initial_sum = die2 + die3

        answer = input("Would you like to reroll? (yes/no): ").lower()

        # Initialize currDie to an invalid value
        currDie = -1
        # If the rerolled die is the same as the initial sum, return 0
        while answer == "yes":
            if initial_sum == currDie:
                return 0  # they tupled out
            currDie = random.randint(1, 6)
            print(f"Rerolled die: {currDie}")
            answer = input("Would you like to reroll? (yes/no): ").lower()
        return initial_sum + currDie

def playGame():
    players = []
    try:
        playerNum = int(input("Enter the number of players: "))
        rounds = int(input("Enter the number of rounds: "))
    except ValueError:
        print("Please enter valid integers for the number of players and rounds.")
        return
# number of players/names setup 
    for x in range(playerNum):
        name = input(f"Enter player {x + 1}'s name: ")
        players.append(Player(name))
        
# loop for the specified number of rounds
    for i in range(rounds):
        for player in players:
            print(f"It is now {player.name}'s turn")
            player.playTurn()

    # Calculate highscore/winners
    highScore = max(player.score for player in players)
    winners = [player.name for player in players if player.score == highScore]

    # Announce winner
    print("The winner(s):")
    for winner in winners:
        print(winner)

if __name__ == "__main__":
    playGame()

    ## game works great i just added notes that kind of seperates the code and explains which each section does. This helps other coders see what youre trying to do.
     
