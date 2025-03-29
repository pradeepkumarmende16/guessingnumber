import random
lowerbound=1
higherbound=100
target_number=random.randint(lowerbound,higherbound)
max_attempts=10

for i in range(max_attempts):
    guess=input(f"enter a number between {lowerbound} to {higherbound}: ")
    
    if not guess.isdigit():
        print("Your number is invalid")
        continue
    guess=int(guess)
    if guess>100 or guess<0:
        print("Your number is invalid")
        continue
    if guess<target_number:
        print("Your Guess number is too low")
    elif guess>target_number:
        print("Your Guess number is high")
    else:
        print("Congratulations,You are right!!!")
        break
else:
    print("You reached your limits")
