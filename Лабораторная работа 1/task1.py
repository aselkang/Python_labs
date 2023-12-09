numbers = [1, -10, 0.8, 3, None, 3, -4, 0, 12]
for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = 0
        numbers[i] = sum(numbers)/len(numbers)
print(numbers)