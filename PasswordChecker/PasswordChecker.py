import math

def passwordChecker(password, Combinations, Count):
    LowerFlag = bool(False)
    UpperFlag = bool(False)
    SymbolFlag = bool(False)
    NumberFlag = bool(False)

    for letter in password:  # Itterates through every letter in the password
        ASCIILetter = ord(letter)
        Count = Count + 1
        if ASCIILetter >= 97 and ASCIILetter <= 122:  # letter between a and z
            LowerFlag = True
        elif ASCIILetter >= 65 and ASCIILetter <= 90:  # letter between A and Z
            UpperFlag = True
        elif ASCIILetter >= 48 and ASCIILetter <= 57:  # number between 0 and 9
            NumberFlag = True
        elif ASCIILetter >= 33 and ASCIILetter <= 47:  # symbol between ! and /
            SymbolFlag = True
        elif ASCIILetter >= 58 and ASCIILetter <= 64:  # symbol between : and @
            SymbolFlag = True
    if LowerFlag == True:  # total number of combinations checked
        Combinations = Combinations + 26
    elif UpperFlag == True:
        Combinations = Combinations + 26
    elif NumberFlag == True:
        Combinations = Combinations + 10
    elif SymbolFlag == True:
        Combinations = Combinations + 22

    return Combinations, Count

def EntropyCalculator(Combinations, Count):
    EntropyScore = math.pow(Combinations, Count)
    EntropyScore = math.log2(EntropyScore)
    StringEntropy = str(EntropyScore)
    return EntropyScore, StringEntropy

def ScorePrint(EntropyScore, StringEntropy):
    if EntropyScore < 28:
        print("Your Score is " + StringEntropy + ". Your password is very weak")
    elif EntropyScore >= 28 and EntropyScore < 35:
        print("Your Score is " + StringEntropy + ". Your password is weak")
    elif EntropyScore >= 36 and EntropyScore < 59:
        print("Your Score is " + StringEntropy + ". Your password is reasonable")
    elif EntropyScore >= 60 and EntropyScore < 127:
        print("Your Score is " + StringEntropy + ". Your password is strong")
    else:
        print("Password is very strong")

Combinations = int(0)
Count = int(0)
print("Starting...")
print("Importing...")
print("Password checker started")
print("Please enter your password to be checked")
password = str(input())
Combinations,Count = passwordChecker(password, Combinations, Count)
EntropyScore, StringEntropy = EntropyCalculator(Combinations,Count)
ScorePrint(EntropyScore, StringEntropy)






