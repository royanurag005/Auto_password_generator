#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
total_length=nr_letters+nr_symbols+nr_numbers
password=[]
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# for l in range(nr_letters):
#   letter=random.randint(0,nr_letters)
#   password+=letters[letter]
# for s in range(nr_symbols):
#   symbol=random.randint(0,nr_symbols)
#   password+=symbols[symbol]  
# for n in range(nr_numbers):
#   number=random.randint(0,nr_numbers)
#   password+=numbers[number]

#'''We can also choose a random char by using random.choice(list) function'''
  

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# print(password)
# print(type(password))

#hard_complex



# mixed_bag_array=[letters,numbers,symbols]
# letter_count,num_count,symbol_count=0,0,0
# for char in range(0,total_length):
#   which_arr=random.randint(0,2)
#   if(which_arr==0):
#     which_letter=random.randint(0,len(letters)-1)
#     password+=letters[which_letter]
#   elif(which_arr==1):
#     which_number=random.randint(0,len(numbers)-1)
#     password+=numbers[which_number]
#   elif(which_arr==2):
#     which_symbol=random.randint(0,len(symbols)-1)
#     password+=symbols[which_symbol]  
# print(f"Your Password is : {password}")

#Angela's Solution
for l in range(0,nr_letters):
  password.append(random.choice(letters))
for n in range(0,nr_numbers):
  password.append(random.choice(numbers))
for s in range(0,nr_symbols):
  password.append(random.choice(symbols))
# print(password)
random.shuffle(password)
password_final=""
for char in password:
  password_final+=char
print(password_final)

# for s in range(nr_symbols):
#   symbol=random.randint(0,nr_symbols)
#   password+=symbols[symbol]  
# for n in range(nr_numbers):
#   number=random.randint(0,nr_numbers)
#   password+=numbers[number]
