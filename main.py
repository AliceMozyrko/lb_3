# class Device:
#     def __init__(self, name):
#         self.name = name
    
#     def process_message(self):
#         return f"Обробка повідомлення для {self.name}"

# class Radiomodule(Device):
#     def __init__(self):
#         super().__init__("Радіомодуль")

# class Buttons(Device):
#     def __init__(self):
#         super().__init__("Кнопки")

# class Battery(Device):
#     def __init__(self):
#         super().__init__("Батарея")

# class Screen(Device):
#     def __init__(self):
#         super().__init__("Екран")

# class Processor(Device):
#     def __init__(self):
#         super().__init__("Процесор")

# class Sensor(Device):
#     def __init__(self):
#         super().__init__("Сенсор")

# # Класи, які містять компоненти
# class Radio(Radiomodule, Buttons, Battery):
#     def __init__(self):
#         pass
    
#     def process_message(self):
#         return f"{self.radiomodule.process_message()} | {self.buttons.process_message()} | {self.battery.process_message()}"

# class Phone(Radiomodule, Buttons, Battery, Screen, Processor):
#     def __init__(self):
#         pass
#     def process_message(self):
#         return f"{self.radiomodule.process_message()} | {self.buttons.process_message()} | " \
#                f"{self.battery.process_message()} | {self.screen.process_message()} | {self.processor.process_message()}"

# class PC(Buttons, Screen, Processor):
#     def __init__(self):
#         pass
    
#     def process_message(self):
#         return f"{self.buttons.process_message()} | {self.screen.process_message()} | {self.processor.process_message()}"
    
# class Tablet(Battery, Processor, Screen, Sensor):
#     def __init__(self):
#         pass

#     def process_message(self):
#         return f"{self.processor.process_message()} | {self.screen.process_message()} | {self.sensor.process_message()} | {self.battery.process_message()}"

# # Створення об'єктів і перевірка роботи
# radio = Radio()
# phone = Phone()
# pc = PC()
# tablet = Tablet()

# print("Повідомлення для Радіо:")
# print(radio.process_message())
# print("\nПовідомлення для Телефона:")
# print(phone.process_message())
# print("\nПовідомлення для Компʼютера:")
# print(pc.process_message())
# print("\nПовідомлення для Планшета:")
# print(tablet.process_message())

class Device:
    def call (self): return 'Device '

class Radiomodule(Device):
        def call (self): return 'Радіомодуль '

class Buttons(Device):
    def call (self): return 'Кнопки '

class Battery(Device):
    def call (self): return 'Батарея '

class Screen(Device):
    def call (self): return 'Екран '

class Processor(Device):
    def call (self): return 'Процесор '

class Sensor(Device):
    def call (self): return 'Сенсор '

# Класи, що містять компоненти
class Radio(Radiomodule, Buttons, Battery):
    def __init__(self):
       self.type='Радіо'
       print(Device(). call ()+super(). call ()+'('+super(Radiomodule,self). call ()+ super(Buttons,self). call ()+') like '+self.type)

class Phone(Radiomodule, Buttons, Battery, Screen, Processor):
    def __init__(self):
        self.type='Телефон'
        print(Device(). call ()+super(). call ()
        +'('+super(Radiomodule,self). call ()
        + super(Buttons,self). call ()
        + super(Battery,self). call ()
        + super(Screen,self). call ()
        +')'+' like '+self.type)

class PC(Buttons, Screen, Processor):
    def __init__(self):
        self.type='Компʼютер'
        print(Device(). call ()+super(). call ()+'('+super(Buttons,self). call ()+ super(Screen,self). call ()+')'+' like '+self.type)

class Tablet(Battery, Processor, Screen, Sensor):
    def __init__(self):
        self.type='Планшет'
        print(Device(). call ()+super(). call ()
        +'('+super(Battery,self). call ()
        + super(Processor,self). call ()
        + super(Screen,self). call ()
        +')'+' like '+self.type)

# Створення об'єктів і перевірка роботи
radio = Radio()
phone = Phone()
pc = PC()
tablet = Tablet()

