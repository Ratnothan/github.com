import random

# This section is just making the dice, the min and max determine what numbers we can roll between and include and the random import just pickes a number within those values.
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

# How many players will be playing

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid number of players.")

# Simulate each players turn
        
max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_index in range(players):
        print("\nPlayer number", player_index + 1, "turn!\n")
        print("Your total score is:", player_scores[player_index], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("\nYou rolled a 1! Your points for this turn are gone and your turn is over!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)


            print("Your score is:", current_score)
            potential_score = (current_score + player_scores[player_index])
            print("Your total would be:", potential_score, "\n")

        player_scores[player_index] += current_score
        print("Your total score is:", player_scores[player_index])

# Determine the winner!
max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print("Player number", winning_index + 1,
       "is the winner with a score of:", max_score)
