import sys
import os




def print_usage(list_of_arguments):
    if len(sys.argv) ==1:
        print("$ todo" "\n"
          "\n"
          "Command Line Todo application" "\n"
          "=============================" "\n"
          "\n"
          "Command line arguments:""\n"
          "-l   Lists all the tasks""\n"
          "-a   Adds a new task""\n"
          "-r   Removes an task""\n"
          "-c   Completes an task)")




def read_todos(file_path):
    file=open(file_path, 'r')
    index=1
    for i in file:
        content=file.read()
        print(str(index) + "-" + content + "\n")
        index +=1
    return content
    file.close()


def no_todos(file_path):
    file=open(file_path, 'r')
    file.close()
    return ("No todos for today! :)")

def append_todo(file_path):
    file=open(file_path, 'a')
    file.write('\n''Feed the monkey')
    file.close()
    return ("Feed the monkey")

def no_todo_provided(file_path):
    file=open(file_path, 'a')
    file.write()
    file.close()
    return ("Unable to add: no task provided")

def remove_todo(file_path):
    file=open(file_path, 'r')
    if len(sys.argv) < 3:
        print("Unable to remove: no index provided")
    elif len(sys.argv) == 3:
        if sys.argv[2].isnumeric():
            index = int(sys.argv[2]) - 1
            del [index]
        else:
            return "Unable to remove: index out of bound"

def check_todo(file_path):
    file=open(file_path, 'r+')
    if len(sys.argv) < 3:
        print("Unable to check: no index provided")
    elif len(sys.argv) == 3:
        if sys.argv[2].isnumeric():
            index = str(int(sys.argv[2]) - 1)
            for i in file:
                content=file.read()
            check=index +'[x]'+content
            return check
        else:
            return "Unable to check: index out of bound"
    else:
        return "Unable to check: index is not a number"


def main(todo_application):
    if len(sys.argv)==1:
         print(print_usage('list_of_arguments'))
    # elif len(sys.argv) > 2:
    #     print("How can I help you?")
    elif len(sys.argv) > 2:            #when you start giving values after the first argument
        if sys.argv[1] == '-l':
            print(read_todos('list_todo.txt'))
        elif sys.argv[1] == '-l' and len(sys.argv)<3:
            print(no_todos('list_todo.txt'))
        elif sys.argv[1] == '-a':
           print(append_todo('list_todo.txt'))
        if sys.argv[1] == '-a' and len(sys.argv)<3:
                 print(no_todo_provided('list_todo.txt'))
        elif sys.argv[1] == '-r':
            print(remove_todo('list_todo.txt'))
        elif sys.argv[1] == '-c':
            print(check_todo('list_todo.txt'))
    elif len(sys.argv)==1:
            print(print_usage('list_of_arguments'))
#         return main(todo_application)
print(main('todo_application'))


