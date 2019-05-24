import sys 

print("input number")
input()

lines = [i.strip() for i in sys.stdin.readlines()]

for i in range(len(lines)):
    print("{0}:{1}".format(i+1,lines[i]))