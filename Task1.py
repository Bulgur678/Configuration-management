import os


def act(a):
    b = a.split()
    if a == "exit":
        exit()
    if len(b) == 0:
        return ""
    if  len(b) > 1:
        if b[0] == "echo":
            return a.replace("\n","")[5:]
        if (os.environ.get(b[1]) != None):
            b[1] = os.environ.get(b[1])
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
            print(f"{os.getcwd()} vfs@ {line}{res}")
            if ("command not found" in res):
                break

    while True:
        a = input(f"{os.getcwd()} vfs@: ")
        result = act(a)
        if result:  # Чтобы не выводить пустые строки
            print(result)

