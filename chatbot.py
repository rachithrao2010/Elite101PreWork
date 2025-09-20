def CheckifInt(value):
    try:
        value = int(value)
        return True, value
    except ValueError:
        return False, value


# Welcome Message
print("Hello My name is Jarvis, a simple Scripted chatbot that can provide assistance for multiple programming languages.")

# User Input function
name = input("What is your name? This is so I can address you better. :   ")
age = input(f"{name}, what is your age?   ")
while True:
    try:
        age = int(age)
        break
    except ValueError:
        age = input("I'm Sorry, That wasn't a number. Please enter a valid Number :   ")

# Custom age appropriate message feature
if age < 15:
    print("Age Appropriate Message 1. This is a placeholder.")
elif age >= 15 and age < 18:
    print("Age Appropriate Message 2. This is a placeholder.")
elif age >= 18 and age < 55:
    print("Age Appropriate Message 3. This is a placeholder.")
elif age >= 55 and age < 120:
    print("Age Appropriate Message 4. This is a placeholder.")
else:
    print("Age Appropriate Message 5. This is a placeholder.")



languages = ["Python", "SQL", "Go", "HTML", "CSS", "JavaScript", "Java", "R"]
index = 1

print(f"Before I can Help You, {name}, I'd like to know which language you are interested in.")
print("Please select a language from these options \n")

for item in languages:
    
    print("Option " + str(index) + " - " + item + "\n")
    index += 1

language = input("Enter a number between 1 and 8.: ")

while True:
    isNumber = CheckifInt(language)[0]
    value = CheckifInt(language)[1]
    if isNumber== True and (value > 0 and value < 9):
        print(f"Thank you, {name}. I will help you with {languages[value - 1]}.")
        break

    elif isNumber == True and (value < 1 or value > 8):
        language = input(" Please enter a number between 1 and 8.   ")
    
    else:
        language = input(" Your answer was not a number. please enter a number between 1 and 8.")

options = ["View Docs", "See Uses", "See similar Languages", "Exit"]
index = 1
print("Now, choose from a menu option.")
for item in options:
    
    print("Option " + str(index) + " - " + item + "\n")
    index += 1

choice = input(" Choose a number from 1 to 4.   ")
        
while True:
    isNumber = CheckifInt(choice)[0]
    value = CheckifInt(choice)[1]
    if isNumber == True and (value > 0 and value < 5):
        break

    elif isNumber == True and (value < 1 or value > 4):
        language = input(" Please enter a number between 1 and 4.   ")

    else:
        language = input(" Your answer was not a number. please enter a number between 1 and 4.   ")

if value == 1:
    print("Placeholder 1")
if value == 2:
    print("Placeholder 2")
if value == 3:
    print("Placeholder 3")
if value == 4:
    print(f"Bye, {name}. ")
    