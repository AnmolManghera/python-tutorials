age_input = input("Provide me an age:\n")
age = int(age_input)

# age = 25

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")