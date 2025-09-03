#ITERATIVE: 
#iteratively building a list of numbers. Giving a range of 1:10 and randomly append each number ot the list 
from random import randint #random integer => randint(a, b): Returns a random integer between a and b (inclusive).

My_list = []
for num in range(0, 10):   #iteration 1: range 0, num is 2, my_list is empty >> add 2, 
    num = randint(1, 10)  #iteration 2: range 1, num became 2, 2 is already in the list
    while num in My_list:
        num = randint(1, 10)
    My_list.append(num)
print(My_list)

#RECURSIVE:             
#Recursively building a list of numbers. Giving a range of 1:10 and randomly append each number ot the list, #recursion call for keep updating the list till, the length of my list == the Target_length, then the func will stop

My_list = [] 
def Ten_numbers_in_alist(My_list, Target_length): #Target_length: how length I wany my list to be
        if len(My_list) == Target_length:
            return My_list
          
        num = randint(1, 10)
        if num not in My_list:
            My_list.append(num)
        return Ten_numbers_in_alist(My_list, Target_length)

Ten_numbers_in_alist(My_list, 10)
print(My_list)