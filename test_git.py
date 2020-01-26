class People():
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def speak(self):
        print('my name is {}, I am {} years old, I am {}kg and \
I am {}m'.format(self.name, self.age, self.weight, self.height))
        return None

class Stu(People):
    def __init__(self, name, age, weight, height, grade):
        People.__init__(self, name, age, weight, height)
        self.grade = grade

    def intro(self):
        print('I am in grade{}'.format(self.grade))
        return None

s = Stu('chenpingan', 16, 66, 1.74, 9)
s.speak()
s.intro()
