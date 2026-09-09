import random

# 1 = Snake
# -1 = Water
# 0 = Gun

# Computer randomly chooses Snake, Water, or Gun
computer = random.choice([1, -1, 0])

# Take user's choice
youstr = input("Enter your choice (s/w/g): ")

# Convert user's letter into a number
youDict = {
    "s": 1,
    "w": -1,
    "g": 0
}

# Convert number back into a word for displaying
reverseDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

you = youDict[youstr]

# Show choices
print(f"You chose: {reverseDict[you]}")
print(f"Computer chose: {reverseDict[computer]}")

# Check for draw
if computer == you:
    print("It's a draw!")

# Computer has Water, You have Snake
elif computer == -1 and you == 1:
    print("You win!")

# Computer has Water, You have Gun
elif computer == -1 and you == 0:
    print("You lose!")

# Computer has Snake, You have Water
elif computer == 1 and you == -1:
    print("You lose!")

# Computer has Snake, You have Gun
elif computer == 1 and you == 0:
    print("You win!")

# Computer has Gun, You have Snake
elif computer == 0 and you == 1:
    print("You lose!")

# Computer has Gun, You have Water
elif computer == 0 and you == -1:
    print("You win!")