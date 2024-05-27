# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
group_students = {name: None for name in groups}
num_groups = int(input())

for i in range(num_groups):
    group_students[groups[i]] = int(input())

print(group_students)
