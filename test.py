def printOddEven(a):
    if a%2==0:
        print("Even")
    else:
        print("Odd")

#printOddEven(1)


def print_element_pos(x):
    for pos, temp in enumerate(x):
        print(temp, pos)

def print_element(x):
    for temp in x:
        print(temp)

def print_odd_element(x):
    for temp in x:
        if temp%2==1:
            print(temp)

def print_even_element(x):
    for temp in x:
        if temp%2==0:
            print(temp)

def print_oddth_element(x):
    for pos, value in enumerate(x):
        if pos%2==1:
            print(value)    

def elem_in_list(x, y):
    for value in x:
        if value==y:
            return True
    return False

# [0,1,2,3,4,5,6,...,size-1]

def get_num_from_user(prompt, can_be_negative):
    value = None if can_be_negative else -1
    while (not isinstance(value, int)) if can_be_negative else value < 0:
        try:
            value = int(input(prompt))
            if not can_be_negative and value < 0:
                print("Please only specify positive integers.")
        except ValueError:
            print("Please enter only a postive integer value.")
    return value


#size = -1
#while size < 0 :
#    try:
#        size = int(input("Enter size of list: "))
#    except ValueError as e:
#        print("Please enter only a number value.")

size = get_num_from_user("Enter size of list: ", False)

new_list=[]
for idx in range(0, size):
    enter_element = get_num_from_user("Enter element: ", True)
    new_list.append(enter_element)


#check_list = input("Enter elements of the list: ")  # user to enter 1,3,4,5

check_num = get_num_from_user("Enter a number: ", True)

if elem_in_list(new_list, check_num):
    print("Exists")
else:
    print("Does Not Exist")


def is_dup(x):
    cache = {}
    for value in x:
        if value in cache:
            return True
        else:
            cache[value] = "exists"
    return False

#print("Has Duplicates" if is_dup ([1,0,2,3]) else "No Duplicates")

#print_even_element([1,2,3,4,666666,6,6,6,6,6])
#print_element_pos([3,4])
#print_oddth_element([1,4,6,7,3,2,9])


#hashtable / map
# a = {"foo":1, "bar":2, "bbq": [2,3,4]}
# print(a["foo"])  ----> prints 1
# print(a["bar"])  ---- prints 2
# print(a["bbq"])  ---- prints [2,3,4]
# for num in a["bbq"]:
#     print(num)  ---- prints 2 then 3 then 4
# for k, v in a.items():
#     print(toupper(k))
#     print(v)
# a.keys() returns a list of keys -----> ["foo", "bar", "bbq"]
# a.values() returns a list of values ------> [1,2,[2,3,4]]

