import random
def Guess_the_number():
    print("Hello! What is your name?")
    name=input()
    
    print("Well,{name},I am thinking of a number between 1 and 20.")
    secret_number=random.randint(1,20)
    sum_taken=0
    
    while True:
        print("Take a quess")
        guess=int(input())
        sum_taken+=1
        if secret_number>guess:
            print("Your guess is too low.")
        elif guess>secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job,{name}! You guessed mu number in {sum_taken}, guesses!")
            
Guess_the_number()  
        