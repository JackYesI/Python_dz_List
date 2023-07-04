j = int(input("Enter len --> "))

list_1 = list()
count_1 = 0
count_2 = 0

for i in range(0,j):
    list_1.append(int(input("Enter your int --> ")))
    if list_1[i] < 0:
        count_1 += 1
    if list_1[i] > 0:
        count_2 += 1
    
print("MAX = {}".format(max(list_1)))
print("MIN = {}".format(min(list_1)))
print("< 0 = {}".format(count_1))
print("> 0 = {}".format(count_2))
print("0 = {}".format(len(list_1) - count_2 - count_1))