print("-------Getting the square of each number in a list, tradational Way---------")

def square(list1):
    updated_list = []
    for num in list1:
        num =  num **2
        updated_list.append(num)
    return updated_list
        

list1  = [1 ,2, 3, 4, 5]

updated_list = square(list1)
print(updated_list)

print("-------Getting the square of each number in a list, \"\\map\\\"")

