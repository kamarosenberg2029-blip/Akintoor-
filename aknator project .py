guesses = [
    "Jennifer lawrence", "Jenna Ortega", "Scarlett Johansson",
    "Jeniffer Aniston", "Millie Bobby Brown", "Emma Waston",
    "Fiona Shaw", "Helena Bonham Carter", "Brittany Murphy",
    "Marilyn Monroe", "Catherine O'Hara", "Betty White",
    "Divya Bhart", "Lucy Gordon", "Ofra Haza", "Greta Garbo",
    "Patrick Schwarzenegger", "Timothée Chalamet", "Tom Hanks",
    "Tom Cruise", "Tom Holland", "Daniel Radcliffe",
    "David Bradley", "Ralph Fiennes", "John Belushi",
    "River Phoenix", "Christopher Plummer", "Paul Walker",
    "Bruce Lee", "Heath Ledger", "Simon Fisher-Becker",
    "Michael Gambon"
]

name = input("hi, what is your name?")
print("hi " + name)
print("I can guess one of these names")
for guess in guesses:
    print(guess)
is_female = input("is it a female?")
is_alive  = input("are they alive?")
is_American= input ("are they American?")
is_younger_than_40=input ("are they younger than 40?")
is_married=input("are they married?")

guess = ""
if is_female=="yes":
    if is_alive=="yes":
        if is_American=="yes":
            if is_younger_than_40 == "yes":
                if is_married=="yes":
                    guess = input("is it jennifer lawrence?")
                else:
                    guess = input("is it jenna ortega?")
            elif is_married == "yes":
                guess = input("is it scarlett johansson?")
            else:
                guess = input("is is jeniffer aniston?")
        elif is_younger_than_40 == "yes":
            if is_married == "yes":
                guess = input("is it millie bobby brown?")
            else:
                guess = input("is it emma watson?")
        elif is_married == "yes":
            guess = input("is it Fiona Shaw?")
        else:
            guess = input("is it Helena Bonham Carter?")
    elif is_American == "yes":
        if is_younger_than_40 == "yes":
            if is_married=="yes":
                guess=input("is it Brittany Murphy?")
            else:
                guess = input("is it Marilyn Monroe?")
        elif is_married=="yes":
            guess= input ("is it Catherine O'Hara?")
        else:
            guess = input("is is Betty White?")
    elif is_younger_than_40=="yes":
        if is_married == "yes":
            guess = input("is it Divya Bhart?")
        else:
            guess=input("is it Lucy Gordon?")
    elif is_married == "yes":
        guess = input("is it Ofra Haza?")
    else:
        guess = input("is it Greta Garbo?")
elif is_alive=="yes":
    if is_American=="yes":
        if is_younger_than_40 == "yes":
            if is_married=="yes":
                guess = input("is it Patrick Schwarzenegger?")
            else:
                guess = input("is it Timothée Chalamet?")
        elif is_married == "yes":
            guess = input("is it Tom Hanks?")
        else:
            guess = input("is is Tom Cruise?")
    elif is_younger_than_40 == "yes":
        if is_married == "yes":
            guess = input("is it Tom Holland?")
        else:
            guess = input("is it Daniel Radcliffe?")
    elif is_married == "yes":
        guess = input("is it David Bradley?")
    else:
        guess = input("is it Ralph Fiennes?")
elif is_American == "yes":
    if is_younger_than_40 == "yes":
        if is_married=="yes":
            guess=input("is it John Belushi?")
        else:
            guess = input("is it River Phoenix?")
    elif is_married=="yes":
        guess= input ("is it Cristopher Plummer?")
    else:
        guess = input("is is Paul Walker?")
elif is_younger_than_40=="yes":
    if is_married == "yes":
        guess = input("is it Bruce Lee?")
    else:
        guess=input("is it Heath Ledger?")
elif is_married == "yes":
    guess = input("is it Simon Fisher-Becker?")
else:
    guess = input("is it Michael Gambon?")

          
# check if we guessed it right
if guess == "yes":
    if is_alive == "yes" and not is_American == "yes" and is_younger_than_40 == "yes" and is_married == "yes" and is_female =="yes":
        # easter egg
        print("good job you're in the upside down!")
    else:
        print("yay good job!")
else:
    print("I give up")
