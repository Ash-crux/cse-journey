numbers =[4,2,7,9,1]
def find_max(numbers):
    max_num=numbers[0]
    for num in numbers:
        if num>max_num:
         max_num=num

    return max_num

result =find_max(numbers)
print(result)




