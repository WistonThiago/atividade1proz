print("Usando o loop FOR: ")
#Using FOR
for i in range (20, 13, -1):
    print("ANDAR: ", i)
for i in range (12, 0, -1):
    print("ANDAR: ", i)
print("===================")
print("Usando o loop WHILE: ")
#Using WHILE
counter = 20
while (counter >= 1):
    if (counter == 13):
        counter -= 1
        continue
    else:
        print ("ANDAR: ", counter)
        counter -= 1