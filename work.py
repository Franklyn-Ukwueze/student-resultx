#x = 2+3

#y = 8

#z = x*
# 
# name = 'Franklyn'

#print(name)

#print(type(x))

#print(type(name))

#print(y/x)
#print(type(y/x))

#print(type([5,6]))
#print(type({'a':"John",'b':20}))

#def square(x):
 #   square = x ** 2
 #   print(square)
#square(10)

#def exponent(x,y):
#    print (x ** y)

#exponent(5,3)

#print(name[1:-1])

#print(len(name))
#scores = [1,2,3,4,5,6,7]
#even = scores[1: :2]
#odd = scores[ : :2]
#print(even)
# x=0
# while x < 10:
#     print(x,end = '-')
#     x = x + 1

# def my_sum(x,y):
#     return x+y
# my_sum(1024,1024)
# x = my_sum(1024,1024)
# print(x)

# def is_even(x):
#      if x % 2 == 0:  
#          return True
#      else:
#          return False

# print(is_even(12))

# def is_odd(x):
#     if x % 2 == 0:
#         return False
#     return True

# print(is_odd(45)) 

# def is_prime(x):
#     if x 
# with open('newfile', 'a') as newfile:
#     newfile.write('New file has been opened')
# file_name = input("Enter name for the file you want to create\n")
# if file_name: # means same thing as if the fie has characters in it.
#     new_text = input(f'Enter text to be saved in {file_name} and press enter when done:\n')

#     f = open(file_name, 'a')
#     f.write(new_text)

#     f.close()

#     with open(file_name) as new_file:
#         text = new_file.read

#         print(f"\nThe text in {file_name} has {len(text)} charracters in it.\nHere is the text itself:\n")
# else:
#     print("Please enter a valid file name")

# ls = [['a','z','d'],['b','c','d'],['e','f','g']]
# print(ls[0][0])
# print(ls[0][2])
# print(ls[1][1])
# print(ls[2][0])
# print(ls[2][2])

customer_info = {
    123456:{
        'name':'Frank',
        'age':20,
        'gender':'Male',
        'balance':500000,
'       dep':[100000,200000,300000],
        'withdrawals':[200000,50000]
        },
    654321:{
        'name':'John',
        'age':22,
        'gender':'Male',
        'balance':600000,
        'dep':[300000,400000],
        'withdrawals':[50000,200000] 
        }
}

#print(customer_info)
#print(sum(customer_info[654321]['withdrawals']))
total_deposit = sum(customer_info[123456]['dep'])
total_withdrawals = sum(customer_info[123456]['withdrawals'])
balance = total_deposit - total_withdrawals
print(f"Total deposit is:{total_deposit:,}")
print(f"Total withdrawals is: {total_withdrawals:,} ")
print(f"current balance is: {customer_info[123456]['balance']:,}")

customer_info[123456]['balance'] = balance
print(f"\nNew balance is: {customer_info[123456]['balance']:,} ")
