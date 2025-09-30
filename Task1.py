import os
import time


def act(a):
    b = a.split()
    print(b)
    if a == "exit":
        exit()
    if len(b) == 0:
        return ""
    if b[0] == "date":
        return time.asctime()
    if b[0].startswith("$"):
        if (os.environ.get(b[0][1:]) != None):
            return os.environ.get(b[0][1:])
    if b[0] == "echo":
        if  len(b) > 1:
            return a.replace("\n","")[5:]
        else:
            return ""
    if b[0] == "ls":
        return b
    elif b[0] == "cd":
        return b
    else:
        return f"{b[0]}: command not found"

if __name__ == "__main__":
    # Стартовый скрипт для проверки команд
    with open('start_script.txt') as f:
        for line in f:
            res = act(line)
            print(f"{os.getcwd()} vfs@: {line}{res}")
            if ("command not found" in res):
                break

    while True:
        a = input(f"{os.getcwd()} vfs@: ")
        result = act(a)
        if result:  # Чтобы не выводить пустые строки
            print(result)

