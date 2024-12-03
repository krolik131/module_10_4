from queue import Queue
import time
import random
from threading import Thread

class Table:
    def __init__(self,number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        wait_time = random.randint(3,10)
        time.sleep(wait_time)

class Cafe:
    def __init__(self,*tables):
        self.queue = Queue()
        self.tables = tables
    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} заняла стол № {table.number}')
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} находится в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал и ушёл')
                        print(f'стол номер {table.number} свободен')
                        table.guest = None
                    if table.guest is None and not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f'{next_guest.name} вышел из очереди и занял стол {table.number}')

# # Создание пяти экземпляров столов класса Table
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman','Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
#Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()