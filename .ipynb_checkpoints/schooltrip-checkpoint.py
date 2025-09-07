def schoolTrip(tripcost, Y_percentages, N):
    
    Y_list = Y_percentages.split()
    updated_Y_list = []
    for num1 in Y_list:
        updated_Y_list.append(float(num1))
    
    student_total_num = sum(updated_Y_list)       
    if student_total_num < 1:
        diff = 1 - student_total_num
        max_value = max(updated_Y_list)
        max_idx = updated_Y_list.index(max_value)
        updated_Y_list[max_idx] = max_value + diff
        
    elif student_total_num > 1:
        diff = student_total_num - 1 
        max_value = max(updated_Y_list)
        max_idx = updated_Y_list.index(max_value)
        updated_Y_list[max_idx] = max_value - diff
        
    students = []
    payments = [12, 10, 7, 5]
    for num2 in updated_Y_list:
        num2 = num2 * N
        students.append(int(num2))
    
    i = 0
    j = 0
    Proceeds = []
    while j < len(payments):
        Y_cost = payments[j] * students[i]
        Proceeds.append(Y_cost)
        j += 1
        i += 1
    Proceeds = sum(Proceeds)
    if (Proceeds/2) >= tripcost:
        return "NO"
    else:
        return "YES"
    
# driver for multiple trips

for dataset in range(10):
    tripcost = int(input())
    Y_percentages = input().strip()
    N = int(input())
    print(schoolTrip(tripcost, Y_percentages, N))
    