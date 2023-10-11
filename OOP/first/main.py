class Animal:

    def __init__(self, name):
        self.name = name

    def set_name(self, new_name):
        self.name = new_name
    
    def get_name(self):
        return self.name
    
    def speak(self):
        print('Don\'t know what to say')

if __name__ == "__main__":
    d = Animal("dog")
    print(d.get_name())

    d.set_name("Lucky")
    print(d.get_name())