# upper triangle
num = input("Enter number of rows you need: ")
num = int(num)

print("What do you wish to do?")
print("1. upper triangle.")
print("2. down triangle.")
print("3. pyramid.")
choice = input("Enter choice: ")

if choice=='1':
    for i in range(0, num):
        for j in range (0, i+1):
            print ("*", end=" ")
        print()

# lower triangle
elif choice=='2':
    for i in range(0, num):
        for j in range (0, num-i):
            print ("*", end=" ")
        print()

# pyramid
else:
    for i in range(0, num):
        for j in range(0, num - 1 - i):
            print(" ", end=" ")
        for k in range(0, 2 * i + 1):
            print("*", end=" ")
        print()
