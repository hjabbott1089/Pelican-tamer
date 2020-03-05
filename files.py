name_file = open("name.txt", "w")
name = input("What is your name? ")
name_file.write(name)
name_file.close()


read_file = open("name.txt", "r")
name = read_file.read().strip()
read_file.close()
print("Your name is", name)


with open("name.txt", "r") as read_file:
    name = read_file.read().strip()
print("Your name is", name)


number_file = open("numbers.txt", "r")
number1 = int(number_file.readline())
number2 = int(number_file.readline())
number_file.close()
print(number1 + number2)


number_file = open("numbers.txt", "r")
total = 0
for line in number_file:
    number = int(line)
    total += number
number_file.close()
print(total)
