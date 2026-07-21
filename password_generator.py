import random
print("Welcome to generating your password!")
name = input("Username : ")
input_letters= int(input("How many letters? "))
input_nums = int(input("How many numbers? "))
input_symbol = int(input("How many symbols? "))
ans = input("Do you want to randomize the order?(Y/N) ").upper()
letters = "abcdefghiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
symbol = "+-_+/\[]<>,."
total = input_letters+input_nums+input_symbol
password = []
while input_letters>0:
    password.append(random.choice(letters))
    input_letters-=1
while input_nums>0:
    password.append(random.choice(nums))
    input_nums-=1
while input_symbol>0:
    password.append(random.choice(symbol))
    input_symbol-=1
print(password)
if ans=='Y':
    random.shuffle(password)
f_password ="".join(password)
print(f"Your password is {f_password}")
print("Thankyou for using our program!")
