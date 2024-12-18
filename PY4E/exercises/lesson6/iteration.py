numbers = [1,2,3,4,5]

for i in range(len(numbers)): 
        numbers[i] = numbers[i] * 2
sum_total = 0 
i = 0 
while i< len(numbers):
    if numbers[i] % 4 == 0: 
        i += 1
        continue 
    sum_total += numbers[i]
