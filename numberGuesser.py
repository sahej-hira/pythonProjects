import random
answer = input("Guess the number")
#the input that the user types in returns to us as a "string". 
# Therefore, we have to convert this str to int to proceed with the program
if answer.isdigit():#need to check if the input is infact a digit, else might throw an error.
    answer = int(answer)
    if answer <=0:
        print("Take better guess next time.")
else:
    print("Please Type a number next time.")
    quit()

randnum= random.randint(0,13)
guesses = 0

while True:
    guesses +=1
    answer = input("Guess the number: ")
    #the input that the user types in returns to us as a "string". 
    # Therefore, we have to convert this str to int to proceed with the program
    if answer.isdigit():#need to check if the input is infact a digit, else might throw an error.
        answer = int(answer)
        '''
        if answer <=0:
            print("Take better guess next time.")
            '''
    else:
        print("Type a number next time ")
        continue

    if answer== randnum:
        print("You got it!")
        break
    elif answer > randnum:
        print("try a lower number. ")
    else:
        print("try a higher number. ")
print("You got it in ",guesses,"guesses.")
# the 'guesses' variable automatically gets converted to a string.
# when used with commas and strings.