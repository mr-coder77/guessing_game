import random

name = input("what's your name? ")
print("Best of luck " + name + " ;)")

words = ['python', 'javascript' , "swift" , "rust" , "kotlin" , "dart" , "ruby" , "c++", "flutter" , "react" , "pascal" , "basic"]
word = random.choice(words)

print("guess the game XD ","  pls keep in mind all the words in lower case")

guesses = ''
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)

        else:
            print("_")
            failed += 1
    if failed == 0:
        print("you won !!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("the word is: ", word) 
        break

    print()
    guess = input("guess a charctar: ")
    guesses += guess
    if guess not in word:
        turns -=1
        print("wrong :( ")
        print("you have", + turns ,"more guesses")

        if turns == 0:
            print("you loose :(((  ")
