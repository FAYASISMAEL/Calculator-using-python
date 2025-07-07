def add (n1, n2):
    return n1 + n2

def sub (n1, n2):
    return n1 - n2

def mul (n1, n2):
    return n1 * n2

def div (n1, n2):
    return n1 / n2

# options to select the operators.

print("Select the options: -\n"
      "1. Add\n"
      "2. Substract\n"
      "3. Multiply\n"
      "4. Divide\n"
      )

select = int(input("Select any option: "))

# number inputs.

n1 = int(input("Enter your First number: "))
n2 = int(input("Enter your Second number: "))

# calculation conditions.

if select == 1:
    print(n1, "+", n2, "=", add(n1, n2))
elif select == 2:
    print(n1, "-", n2, "=", sub(n1, n2))
elif select == 3:
    print(n1, "*", n2, "=", mul(n1, n2))
elif select == 4:
    print(n1, "/", n2, "=", div(n1, n2))
else:
    print("Error 404")
