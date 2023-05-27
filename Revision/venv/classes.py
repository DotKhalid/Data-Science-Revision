class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == "actor":
            print(self.name, "shoots a film")
        elif self.occupation == "crickter":
            print(self.name, "play cricket")

    def speak(self):
        print(self.name, "says Hello")


person1 = Human("ali zafar", "actor")
person1.do_work()
person1.speak()


person2 = Human("Babar Azam", "crickter")
person2.do_work()
person2.speak()