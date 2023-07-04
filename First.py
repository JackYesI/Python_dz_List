
# expression = input("Enter your expression --> ")

# list_1 = []

# list_1 = expression.split()

# if list_1[1] == '+':
#     print("{} + {} = {}".format(list_1[0], list_1[2], int(list_1[0]) + int(list_1[2])))
# elif list_1[1] == '-':
#     print("{} - {} = {}".format(list_1[0], list_1[2], int(list_1[0]) - int(list_1[2])))
# elif list_1[1] == '*':
#     print("{} * {} = {}".format(list_1[0], list_1[2], int(list_1[0]) * int(list_1[2])))
# elif list_1[1] == '/':
#     print("{} / {} = {}".format(list_1[0], list_1[2], int(list_1[0]) / int(list_1[2])))
# else:
#     print("Error")

expression = input("Enter your expression --> ")
list_1 = []

if '+' in expression:
    list_1 = expression.split('+')
    print("{} + {} = {}".format(list_1[0], list_1[1], int(list_1[0]) + int(list_1[1])))
elif '-' in expression:
    list_1 = expression.split('-')
    print("{} - {} = {}".format(list_1[0], list_1[1], int(list_1[0]) - int(list_1[1])))
elif '*' in expression:
    list_1 = expression.split('*')
    print("{} * {} = {}".format(list_1[0], list_1[1], int(list_1[0]) * int(list_1[1])))
elif '/' in expression:
    list_1 = expression.split('/')
    print("{} / {} = {}".format(list_1[0], list_1[1], int(list_1[0]) / int(list_1[1])))
