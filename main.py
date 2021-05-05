import sys
import os

def print_usage():
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
    content = file.readlines() # readlines reads content line by line but read reads the entire content of the file.
    if len(content)<1:
        print("No todos for today! :)")
    else:
        for i in range(len(content)):
            print(str(index) + "-" + content[i] + "\n")
            index +=1
        file.close()
        return content


def append_todo(file_path):
    file=open(file_path, 'a')
    if len(sys.argv)<2:
        print("Unable to add: no task provided")
    else:
        file.write("\n" + sys.argv[2])
        file.close()


def remove_todo(file_path):
    if len(sys.argv) == 2:
        print("Unable to remove: no index provided")
    elif len(sys.argv) > 2:
        if sys.argv[2].isnumeric():
            file = open(file_path, 'r')# reading and closing
            content = file.readlines()
            file.close()
            index = int(sys.argv[2])-1
            content.remove(content[index])
            file=open(file_path, 'w')
            file.write("".join(content))# we are overwriting existing file
            file.close()
        elif sys.argv[2] == str(sys.argv[2]):# if second argument given is a string
            print("Unable to remove: index is not a number")

def unsupported_argument(): # is this correct?
    any_other_phrase =["-l", "-a", "-r", "-c"]
    if len(sys.argv)<=2 and not any_other_phrase.__contains__(sys.argv[1]):
        print("Unsupported argument")
        print_usage()


def check_todo(file_path): #follow the logic of remove_todo() but instead of remove use append
    # file=open(file_path, 'r+')#read and write / edit
    if len(sys.argv) < 3:
        print("Unable to check: no index provided")# running
    elif len(sys.argv) == 3:
        if sys.argv[2].isnumeric():
            file = open(file_path, 'r')  # reading and closing
            content = file.readlines()
            file.close()
            index = int(sys.argv[2]) - 1
            content[index]= "[x]" + "".join(content[index])
            file = open(file_path, 'w')
            for line in content:
                file.write(line)  # we are overwriting existing file
            file.close()
        elif sys.argv[2].isnumeric():
            index = int(sys.argv[2]) - 1
            if sys.argv[2]< index:
                print("Unable to check: index out of bound")# if index out of range is given, the index number is raised but this imessage is not displayed.
        elif sys.argv[2] == str(sys.argv[2]):
            print("Unable to check: index is not a number")


def main(todo_application):
    if len(sys.argv)==1:
         print_usage()
    elif len(sys.argv) >= 2:            #when you start giving values after the first argument
        if sys.argv[1] == '-l':
            read_todos('list_todo.txt')
        elif sys.argv[1] == '-a' and len(sys.argv)>= 3:
            append_todo('list_todo.txt')
        elif sys.argv[1] == '-r':
            remove_todo('list_todo.txt')
        elif sys.argv[1] == '-c':
            check_todo('list_todo.txt')
        else:
            unsupported_argument()

main('todo_application')


