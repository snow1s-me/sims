class Human:
    def __init__(self, name, vik, stat, game, isha , happy=0, golod=0):
        self.name = name
        self.vik = vik
        self.happy = happy
        self.golod = golod
        self.stat = stat
        self.game = game
        self.isha = isha
    def eating(self):
        self.golod = self.golod - 10
    def playing(self):
        self.golod = self.golod + 10
    def speaking(self):
        self.happy = self.happy + 10
    def sora(self):
        self.happy = self.happy - 10
    def procebe1(self):
        print(f"1 людина- {self.stat}, Звати- {self.name}, {self.vik} років, Улюблена гра- {self.game}")
    def procebe2(self):
        print(f"2 людина- {self.stat}, Звати- {self.name}, {self.vik} років, Улюблена гра- {self.game}")

print("-----Перша людина-----")
s1 = input("Стать(Чоловік/Жінка):")
im1 = input("Ім'я:")
v1 = int(input("Вік:"))
g1 = input("Улюблена гра:")
is1 = input("Улюблена їжа:")

print("-----Друга людина-----")
s2 = input("Стать(Чоловік/Жінка):")
im2 = input("Ім'я:")
v2 = int(input("Вік:"))
g2 = input("Улюблена гра:")
is2 = input("Улюблена їжа:")

r = 0
g = 0

l1 = Human(name = im1, vik = v1, stat = s1, game = g1, isha = is1, happy = r, golod = g)
l2 = Human(name = im2, vik = v2, stat = s2, game = g2, isha = is2, happy = r, golod = g)
print("-----Ітог-----")
l1.procebe1()
l2.procebe2()
print("------------------")
while True:
    x = int(input("Що вони будуть робити?(1-Грати, 2-Говорити, 3-Ругатись, 4-Їсти):"))
    if x == 1:
        print(f"{im1} грає в {g1}")
        l1.playing()
        print(f"{im2} грає в {g2}")
        l2.playing()
        g = g + 10
    if x == 2:
        print(f"{im1} і {im2} спілкуються між собою")
        l1.speaking()
        l2.speaking()
        r = r + 10
    if x == 3:
        print(f"{im1} і {im2} ругаються між собою між собою")
        l1.sora()
        l2.sora()
        r = r - 10
    if x == 4:
        print(f"{im1} їсть {is1}")
        l1.eating()
        print(f"{im2} їсть {is2}")
        l2.eating()
        g = g - 10
    print(f"Радість- {r}, Голод- {g}")
    if g == 100:
        print(f"УПС!{im1} і {im2} померли від голоду")
    if r == 100:
        if s1 == "Чоловік" and s2 == "Жінка":
            print(f"УРА!{im1} і {im2} подружилися")
        if s1 == "Жінка" and s2 == "Чоловік":
            print(f"УРА!{im1} і {im2} подружилися")
        if s1 == "Жінка" and s2 == "Жінка":
            print(f"УРА!{im1} і {im2} тепер друзі")
        if s1 == "Чоловік" and s2 == "Чоловік":
            print(f"УРА!{im1} і {im2} тепер друзі")
