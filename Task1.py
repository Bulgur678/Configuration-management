import os

def act(a):
    b = a.split()
    if a == "exit":
        exit()
    if len(b) == 0:
        return ""
    if  b[0].startswith("$"):
        if (os.environ.get(b[0][1:]) != None):
             return os.environ.get(b[0][1:])
    if b[0] == "ls":
        return b
    elif b[0] == "cd":
        return b
    else:
        return f"{b[0]}: command not found"

if __name__ == "__main__":
    while True:
        a = input("vfs@ ")
        result = act(a)
        if result:  # Чтобы не выводить пустые строки
            print(result)