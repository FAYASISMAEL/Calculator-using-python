# print varialbles

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 60:
    print("Hello ", name, ". You are ", age, "years old, you cannot apply for lisence because youo are over aged.")
elif age >= 18:
    print("Hello ", name, ". You are ", age, "years old, you can applying for lisence.")
else:
    print("Hello ", name, ". You are ", age, "years old, you cannot apply for lisence.")