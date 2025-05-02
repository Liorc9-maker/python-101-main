# Always make sure there is a condition that terminates a while loop.
while True :
    prompt = input('say something: ')
    if prompt == 'quit':
       break
    print(prompt[::-1])
print("bye!! (it's tiuq, btw. ;)")

