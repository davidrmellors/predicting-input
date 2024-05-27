string_input = input()
digits_list = [int(num) for num in string_input]

mean = sum(digits_list) / len(digits_list)
print(mean)
