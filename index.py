class human:
    def __init__(self, name, age, height, color):
        self.name, self.age, self.height, self.color = name, age, height, color
        
    def speak(self, sentence1):
        print(f"{self.name} is going to talk about {sentence1}")

    # def __str__(self, name, age, height, color) -> str:
    #     print(f"{name}, {age}, {height}, {color}")
    

human1=human("raj", 24, 1.8, "brown")
human2=human("meena", 17, 1.4, "lightish brown")

print(human1.speak("this is a good life"))
