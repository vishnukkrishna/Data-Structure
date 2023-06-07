# Stack
# stack = []
# print(len(stack)==0)
# Adding the element to the stack
# stack.append(10)
# stack.append(20)
# stack.append(30)

# Deleting the element from the stack
# stack.pop(2) # Stack index number
# print(stack)


# import collections
# stack = collections.deque()
# print(stack)
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack)
# stack.pop()
# print(stack)

# import queue
# stack = queue.LifoQueue()
# # stack = queue.LifoQueue(3)
# # Adding the element 
# stack.put(10)
# stack.put(20)
# stack.put(30)

# # Deleting the element 
# print(stack.get())
# print(stack.get())
# print(stack.get())

# Stack Middle Point deletion
# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)
# midd = len(stack)//2

# print(midd)
# stack.pop(midd)
# print(stack)

# Stack string reverse
# s = 'vishnuk'
# arr = list(s)
# reversed_arr = []

# for i in range(len(arr)):
#     reversed_arr.append(arr.pop())

# print(reversed_arr)

# stack = []

# def push():
#    print('-------------------------------------------')
#    value = int(input('Enter the number to push: '))
#    stack.append(value)
#    print('Stack is:',stack)
#    print('-------------------------------------------')



# def pop():
#    print('-------------------------------------------')
#    s =  stack.pop()
#    print('Deleted element is:', s)
#    print('Stack is:',stack)
#    print('-------------------------------------------')

# def find_mid():
#     mid = len(stack) // 2
#     mid_value = stack[mid]
#     print('-------------------------------------------')
#     print('Middle element is : ', mid_value)
#     print('-------------------------------------------')

# while True:
#     choice = int(input('Enter your choice:\n1.Push\n2.Pop\n3.Find mid\n4.Quit\n'))
#     if choice == 1:
#         push()
#     elif choice == 2:
#         pop()
#     elif choice == 3:
#         find_mid()
#     elif choice == 4:
#         break
#     else:
#         print('Enter correct choice')




stack = []

def push():
   value = int(input('Enter the number to push: '))
   stack.append(value)
   print('Stack is:',stack)

def pop():
   s =  stack.pop()
   print('Deleted element is:', s)
   print('Stack is:',stack)

def find_mid():
    mid = len(stack) // 2
    mid_value = stack[mid]
    print('Middle element is : ', mid_value)

def delete_middle():
    midd = len(stack) // 2
    if not stack:
        return -1
    else:
        temp_stack = []
        while len(stack) - 1 > midd:
            temp_stack.append(stack.pop())
        stack.pop()
        while True:
            if not temp_stack:
                break
            else:
                stack.append(temp_stack.pop())
        print(stack)


while True:
    choice = int(input('Enter your choice:\n1.Push\n2.Pop\n3.Find mid\n4.Quit\n5.middle_delete\n'))
    if choice == 1:
        push()
    # elif choice == 2:
    #     pop()
    # elif choice == 3:
    #     find_mid()
    elif choice == 4:
        break
    elif choice == 5:
        delete_middle()
    else:
        print('Enter correct choice')