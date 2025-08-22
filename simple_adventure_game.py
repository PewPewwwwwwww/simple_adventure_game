# simple_adventure_game
name = input("Enter your name: ")
print(f"Welcome {name} tp this Adventure game!")

answer = input("You are in a dark forest. Do you want to go left or right? (left/right): ").lower()

if answer == "left":
    answer = input("You see a river. Do you want to swim across or walk around? type swim or walk: ").lower()
    if answer == "swim":
        print("You swam across the river and found a treasure!")
    elif answer == "walk":
        print("You walked around the road and found a village!")
    else:
        print("Not valid option. game over!")

elif answer == "right":
    answer = input("You see a mountain. Do you want to climb it or go around it? type climb or go: ").lower()
    if answer == "climb":
        print("You climbed the mountain and found a beautiful view!")
    elif answer == "go":
        answer = input("You went around the mountain and found a hidden cave you want to hide and you find some villagers! (yes/no): ").lower()
    
    if answer == "yes":
        print("You talked to the villagers and they gave you food and shelter.")
    elif answer == "no":
        print("You decided to leave the mountain and continue your adventure.")

    else:
        print("Not valid option. game over!")

else:
    print("Not valid option. game over!")

print(f"Thank you for playing, {name}!")
