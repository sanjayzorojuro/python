import random
system=random.choice([1,2,])

enter=input("Enter rock or paper or sizor::")
youDict={"r":1,"p":2,"s":3}
revdict={"r":'rock',"p":"paper","s":"sizor"}

you=youDict[enter]

dict2={1:'rock',2:"paper",3:"sizor"}
print("the computer choose:",dict2[system])
print("And you choose:",revdict[enter])

if system == enter:
    print("DRAW!!")

else:
    if system == 1 and you == 2:
        print("YOU WIN!!!")
    elif system == 1 and you == 3:
        print("YOU LOSE!!!")
    elif system == 2 and you == 3:
        print("YOU WIN!!!")
    elif system == 2 and you == 1:
        print("YOU LOSE!!!")
    elif system == 3 and you == 1:
        print("YOU WIN!!!")
    elif system == 3 and you == 2:
        print("YOU LOSE!!!")
    else:
        print("something is not good ")
    