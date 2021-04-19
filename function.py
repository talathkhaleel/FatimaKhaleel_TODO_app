import sys
import os

#
# def text_file(list_todo.txt, mode):
#     index=1

def read_todos(file_path):
    file=open(file_path, 'r')
    index=1
    for i in file:
        content=file.read()
        print(str(index) + "-" + content + "\n")
        index +=1
    return content
    file.close()

print(read_todos('list_todo.txt'))

# def no_todos(file_path):
#     file=open(file_path, 'r')
#     return ("No todos for today! :)")
#
# print(no_todos('list_todo.txt'))


# def append_todo(file_path):
#     file=open(file_path, 'a')
#     file.write('\n''Feed the monkey')
#     return ("Feed the monkey")
#
# print(append_todo('list_todo.txt'))

# def no_todo_provided(file_path):
#     file=open(file_path, 'a')
#     file.write()                                  need to check
#     return ("Unable to add: no task provided")
#
# print(no_todo_provided('list_todo.txt'))

# def remove_todo(file_path):
#     file=open(file_path, 'r')
#     if len(sys.argv) < 3:
#         print("Unable to remove: no index provided")
#     elif len(sys.argv) == 3:
#         if sys.argv[2].isnumeric():
#             index = int(sys.argv[2]) - 1
#             del [index]
#         else:
#             return "Unable to remove: index out of bound"
# print(remove_todo('list_todo.txt'))

# def check_todo(file_path):
#     file=open(file_path, 'r+')
#     if len(sys.argv) < 3:
#         print("Unable to check: no index provided")
#     elif len(sys.argv) == 3:
#         if sys.argv[2].isnumeric():
#             index = str(int(sys.argv[2]) - 1)
#             for i in file:
#                 content=file.read()
#             check=index +'[x]'+content
#             return check
#         else:
#             return "Unable to check: index out of bound"
#     else:
#         return "Unable to check: index is not a number"
#
# print(check_todo('list_todo.txt'))


# def addToList():
#     value = str(sys.argv[2])
#     contents = open('list_todo.txt', 'r').readlines()
#     filesize = os.path.getsize("list_todo.txt")
#     if filesize == 0:
#         contents.append(value)
#     else:
#         contents.append("\n" + value)
#         AddTask = open("list_todo.txt", "w")
#         contents = "".join(contents)
#         AddTask.write(contents)
#         AddTask.close()