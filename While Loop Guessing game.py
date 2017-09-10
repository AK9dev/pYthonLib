import random

guessesLeft = 15
userName = input("please enter your name:")
number = random.randint(1,1000)
print("hello",userName, "i'm thinking of a number between 0 and 100.")



while guessesLeft>0:
    print("your have",guessesLeft,"guesses left")
    guess = int(input("guess a number: "))
    guessesLeft=guessesLeft-1

    if guess<number:
        print("your number is too low,")
    elif guess>number:
        print("Your guess is too high.")
    elif guess==number:
        print("good job,",userName,"! You guessed my number is",(15-guessesLeft),"guesses!")
        break

    if guessesLeft == 0:
        print("Sorry. the number I was thinking was,",number)
        break

    
  
        
    



