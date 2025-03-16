class Device:
    def __init__(self, name):
        self.name = name
    
    def process_message(self):
        return f"Обробка повідомлення для {self.name}"

class Radiomodule(Device):
    def __init__(self):
        super().__init__("Радіомодуль")

class Buttons(Device):
    def __init__(self):
        super().__init__("Кнопки")

class Battery(Device):
    def __init__(self):
        super().__init__("Батарея")

class Screen(Device):
    def __init__(self):
        super().__init__("Екран")

class Processor(Device):
    def __init__(self):
        super().__init__("Процесор")

class Sensor(Device):
    def __init__(self):
        super().__init__("Сенсор")

# Класи, які містять компоненти
class Radio:
    def __init__(self):
        self.radiomodule = Radiomodule()
        self.buttons = Buttons()
        self.battery = Battery()
    
    def process_message(self):
        return f"{self.radiomodule.process_message()} | {self.buttons.process_message()} | {self.battery.process_message()}"

class Phone:
    def __init__(self):
        self.radiomodule = Radiomodule()
        self.buttons = Buttons()
        self.battery = Battery()
        self.screen = Screen()
        self.processor = Processor()
    
    def process_message(self):
        return f"{self.radiomodule.process_message()} | {self.buttons.process_message()} | " \
               f"{self.battery.process_message()} | {self.screen.process_message()} | {self.processor.process_message()}"

class PC:
    def __init__(self):
        self.buttons = Buttons()
        self.screen = Screen()
        self.processor = Processor()
    
    def process_message(self):
        return f"{self.buttons.process_message()} | {self.screen.process_message()} | {self.processor.process_message()}"
    
class Tablet:
    def __init__(self):
        self.battery = Battery()
        self.processor = Processor()
        self.screen = Screen()
        self.sensor = Sensor()
    
    def process_message(self):
        return f"{self.processor.process_message()} | {self.screen.process_message()} | {self.sensor.process_message()} | {self.battery.process_message()}"

# Створення об'єктів і перевірка роботи
radio = Radio()
phone = Phone()
pc = PC()
tablet = Tablet()

print("Повідомлення для Радіо:")
print(radio.process_message())
print("\nПовідомлення для Телефона:")
print(phone.process_message())
print("\nПовідомлення для Компʼютера:")
print(pc.process_message())
print("\nПовідомлення для Планшета:")
print(tablet.process_message())