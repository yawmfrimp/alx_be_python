size = int(input("Enter the size of the patttern: "))
count = 0

while size in range(1,size+1):
    for i in range(size):
        print("*", end="")
    print("/n")
    count += 1
    if count == size:
        break
