class Person:
    def __init__(self,name) -> None:
        self.name = name
    

    def talk(self,message):
        print(f'{self.name} says {message}')

Jerry = Person('Jerry')

Jerry.talk('Yo what is up')