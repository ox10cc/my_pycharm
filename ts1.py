class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('my name is cc')

if __name__ == '__main__':
    p = People
    p.say(p)