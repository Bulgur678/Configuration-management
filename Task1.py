import os
import time


def act(command):
    command_split = command.split(" ")
    match command_split:
        case (): #Пробелы и ничего
            return
        case ("exit",*args):
            exit()
        case ("echo",*args):
            return command[5:]
        case ("date",*args):
            return time.asctime()
        case ("ls", *args) | ("cd",*args):
            return command.split(" ")

        case _ if command_split[0].startswith("$"):
            if (os.environ.get(command_split[0][1:]) != None):
                return os.environ.get(command_split[0][1:])
        case _:
            return f"{command_split[0]}: command not found"

if __name__ == "__main__":
    #Стартовый скрипт для проверки команд
    with open('start_script.txt') as f:
        for line in f:
            res = act(line.rstrip("\n"))
            print(f"{os.getcwd()} vfs@: {line}{res}")
            if ("command not found" in res):
                break

    while True:
        a = input(f"{os.getcwd()} vfs@: ")
        result = act(a)
        if result:  # Чтобы не выводить пустые строки
            print(result)