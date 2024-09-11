from random import *

def randlist(rang):
    liste = [randint(0,100) for i in range(rang)]
    return liste

def your_name():
    yourname = input("What is your name?: ")
    return f"Bonjour, {yourname}"

def add():
    num1 = int(input("Entrez votre premier nobre: "))
    num2 = int(input("Entrez votre second nobre: "))
    res = num1 + num2
    return res


def main():
    print(randlist(10))
    print(your_name())
    
    print("Votre resultat est: ", add())

if __name__ == '__main__':
    main()