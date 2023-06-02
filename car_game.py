car = 'stopped'
while True:
    response = input("> ").lower()
    if response == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif response == 'start':
        if car == 'stopped':
            print('Car started...Ready to go!')
            car = 'started'
        else:
            print('Car is already started!')
    elif response == 'stop':
        if car == 'started':
            print('Car stopped.')
            car = 'stopped'
        else:
            print('Car is already stopped')
    elif response == 'quit':
        break
    else:
        print("Sorry I don't understand")