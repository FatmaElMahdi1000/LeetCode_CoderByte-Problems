def mx(x, y):
    if x > y:
        return x
    else:
        return y 

result = mx(2, 4)
print(result)

print("***Another way with Lambda*****")

mx = lambda x, y: x if x > y else y
print(mx(8, 5))

