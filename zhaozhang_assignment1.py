print('welcome to lotto')
unique = []
for i in range(6):
    user_input = input("please enter a number between 1 and 50\n")
    value = int(user_input)
    while value <= 0 or value >= 50:
        print('the number you entered is not between 1 and 50')
        value = int(input('please enter a new number\n'))        
    unique.append(value)
    
total = 100
import random
computer = []
for i in range(6):
    num = random.randint(1,50)
    computer.append(num)
count = 0
for j in range(len(computer)):
    for k in range(len(unique)):
        if computer[j] == unique[k]:
            count += 0
            break
percentage = float(count) / 6
win = percentage * total
print("you have won %d" % win)
print("the correct numbers are: ", computer) 
        


      
