print("Welcome to brain teasers: ")
play = input("Do you wish to play?(y/n) ")
if play.lower() != "y":
    print("k,bye.")
    quit()

print("Okay! Good Luck!")
score=0

answer = input("What is a three letter word that resembles the word mistake?").lower()
if answer == "err":
    print("Correct!")
    score += 1
else:
    print("Oops,incorect!")

answer = input("I’m tall when I’m young, and I’m short when I’m old, what am I?").lower()
if answer == "candle":
    print("yay, right!")
    score += 1
else:
    print("wrong!")

answer = input("What can run but not walk, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?").lower()
if answer == "river" or "a river":
    print("Kudos to you!")
    score += 1
else:
    print("wrong again!")

answer = input("Flat as a leaf, round as a ring; Has two eyes, can't see a thing. What is it?").lower()
if answer == "button" or "a button":
    print("right!")
    score += 1
else:
    print("Oops,incorect!")

answer = input("Are you dumb?").lower()
score+=1
print("no, you are dumb :)" )

print("\n you got " + str((score/5)*100) +"%.")





     
