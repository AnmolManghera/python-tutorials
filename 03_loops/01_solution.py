numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_num_cnt = 0

for num in numbers:
    if num > 0:
        positive_num_cnt += 1

print(positive_num_cnt)


n = 10
sum_even = 0
for i in range(1,n+1):
    if i%2 == 0:
        sum_even += 1


number = 3

for i in range(1,11):
    if i != 2:
        print(number*i)


input_str = "Python"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str

print(reversed_str)

input_str = "teeter"

for char in input_str:
    if input_str.count(char) == 2:
        print("Char is: ",char)
        break

fact = 1
number = 8

while number > 0:
    fact = fact*number
    number -= 1

print(fact)

# while True:
#     number = int(input("Enter value b/w 1 and 10"))
#     if 1 <= number <= 10:
#         print("Thanks")
#     else:
#         print("Invalid Number")


items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate Found")
        break
    else:
        unique_item.add(item)