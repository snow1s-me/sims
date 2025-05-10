class Osoba:
    def __init__(self, name, vik):
        self.name = name
        self.vik = vik


class Vodiy(Osoba):
    def __init__(self, name, vik, poc):
        super().__init__(name, vik)
        self.poc = poc

    def dia(self):
        return f"Номер посвідчення: {self.poc}"


# Приклад використання:
v = Vodiy("Іван", 36, "AB123456")
print(f"Ім'я: {v.name}")
print(f"Вік: {v.vik}")
print(v.dia())
