
import numpy as np

# number of guesses
guesses = 10

# generating random number
no = np.random.randint(100)


while guesses >= 0:

    #if guesses are zero the game ends
    if (guesses == 0):
        print("you loose, number was =", no)
        break

    else :
        choice = int(input("guess number[1-100] :"))

        if choice == no:
            print("you won")
            break

        elif choice < no:

            guesses -= 1        #decrementing guesses value by - 1
            print("guesses remain =", guesses)

            if (no - 5 < choice):   #if number were near by - 5
                print("u r too close..increment the number")

            elif (no - 10 < choice):    #if number were near by - 10
                print("u r a bit closer to number..u need to increment the number")

            else:
                print("u r far away..u need increment the number")

        elif choice > no:

            guesses -= 1        #decrementing guesses value by - 1
            print("guesses remain =", guesses)

            if (no + 5 > choice):      #if number were near by + 5
                print("u r too close..decrement the number")

            elif (no + 10 > choice):        #if number were near by + 10
                print("u r a bit closer to number..u need to decrement the number")
                
            else:
                print("u r far away..u need to decrement the number")






