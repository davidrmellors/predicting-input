# the list "meals" is already defined
# your code here
total_kcal = 0
for meal in meals:
    total_kcal += meal["kcal"]

print(total_kcal)