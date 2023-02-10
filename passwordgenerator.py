# py password GeneratorExit
import random
import string
print("Welcome to the PyPassword Generator")
abc = int(input("How many letters would you like in your password?"))
num = int(input("How many numbers would you like in your password?"))
sym = int(input("How many symbols would you like in your password?"))
symbols = ["!", "@", ".", "%", "$"]
char_list = []
for letter in range (abc):
    char_list.append(random.choice(string.ascii_letters))
for number in range (num):
    string_num = str(random.randint(0,9))
    char_list.append(string_num)
for symbol in range (sym):
    char_list.append(random.choice(string.punctuation))

random.shuffle(char_list)
print(''.join(map(str, char_list)))

