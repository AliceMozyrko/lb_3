class Device:
    def call (self): return 'Device'

class Radiomodule(Device):
        def call (self): return 'Радіомодуль'

class Buttons(Device):
    def call (self): return 'Кнопки'

class Battery(Device):
    def call (self): return 'Батарея'

class Screen(Device):
    def call (self): return 'Екран'

class Processor(Device):
    def call (self): return 'Процесор'

class Sensor(Device):
    def call (self): return 'Сенсор'

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

