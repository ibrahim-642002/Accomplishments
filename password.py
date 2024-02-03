import random
import string

ch = string.ascii_letters
let = string.digits
punc = string.punctuation


words = []

num = []

chars = []

for i in ch:
    words.append(i)

for i in let:
    num.append(i)

for i in punc:
    chars.append(i)


def create_password():
    password = []
    length = int(input(" Please Enter The Length Of Password: "))
    word_len = int(input(" Please Enter How Many Words Would You Like in Your Password: "))
    num_len = int(input(" Please Enter How Many Numbers Would You Like in Your Password: "))
    char_len = int(input(" Please Enter How Many Special Characters Would You Like in Your Password: "))

    while (word_len + num_len + char_len) > length:
        print(" Length Exceeded The Given Length ")
        word_len = int(input(" Please Enter How Many English Alphabets Would You Like in Your Password: "))
        num_len = int(input(" Please Enter How Many Numbers Would You Like in Your Password: "))
        char_len = int(input(" Please Enter How Many Special Characters Would You Like in Your Password: "))

    for j in range(word_len):
        password.append(random.choice(words))

    for j in range(num_len):
        password.append(str(random.choice(num)))

    for j in range(char_len):
        password.append(str(random.choice(chars)))

    passx = ''.join(password)
    # The join function expects strings therefore we are converting nums and
    # chars to string first and then applying join function

    print(f" Randomly Generated Password is {passx}")


create_password()
# print(random.choice(words))
# print(random.choice(num))
# print(randint(1, 5))
# print(random.choice(chars))
