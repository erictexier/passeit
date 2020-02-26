#!/usr/local/bin/python3


if __name__ == '__main__':
    f = open("./numbers.txt","r")
    line = f.readline()
    f.close()
    b = line.strip()
    b = b.split(",")
    for i in b:
        print(i)

