#Toni Tuunainen 1.2.5.4: Create a While Loop
while True:
    x=input("Enter a number to count to: ")
    if x == 'q' or x == 'quit':
        break

    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
