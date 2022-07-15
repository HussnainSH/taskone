started = False
stopped = False

while True:
    car = input(f'Enter quit to exit >').lower()
    if car == 'start':
        if started:
            print(f'Car is already started!!')
        else:
            started = True
            stopped = False
            print(f'Car Started... Ready to go!')
    elif car == 'stop':
        if stopped:
            print(f'Car is already Stopped!!')
        else:
            stopped = True
            started = False
            print(f'Car Stopped.')
    elif car == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif car == 'quit':
        break
    else:
        print("I don't understand that...")
