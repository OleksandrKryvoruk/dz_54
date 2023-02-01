"""

Написати клас для створення і роботи з хеш-таблицями. Клас повинен мати наступні функції:
- створення хеш-таблиці заданої довжини;
- пошук, додавання і видалення елементів;
- друкування хеш-таблиці;
- виправлення колізій

"""
import math


class HashTable:
    
    def __init__(self, length):
        self.verify_length(length)                      # Перевірка на коректність заданого розміру хеш-таблиці

        self.__length = length                          # Довжина хеш таблиці
        self.__start_length = length                    # Початкова довжина, менше якої таблиця не зменшиться у випадку видалення ключів
        self.__table = [(None, None)] * self.__length   # Безпосередньо хеш-таблиця у вигляді списку кортежів вигляду (key, data)
        self.__count_key = 0                            # Поточна кількість ключів в хеш-таблиці


    @classmethod
    def verify_length(self, length):                    # Метод перевірки коректності задануого розміру хеш-таблиці
        if type(length) != int or length < 5:
            raise TypeError("Довжина хеш-таблиці має бути цілим числом більше 5")

    @property
    def table(self):                                # Метод отримання хеш-таблиці
        return self.__table


    def get_data(self, data_key):                       # Метод отримання данних із хеш-таблиці
        # Виконання пошуку даного ключа у таблиці
        mark, count_cell = self.__find_data(data_key)
        if not mark:
            return "Current key hasn't been found!"
        else:
            return self.__table[count_cell]


    def set_data(self, data_key, data_value):           # Метод додавання данних до хеш-таблиці
        # Виконання пошуку даного ключа у таблиці
        mark, count_cell =  self.__find_data(data_key)
        if not mark:
            # Якщо ключ не було знайдено, данні додаються до таблиці
            self.__table[count_cell] = (data_key, data_value)
            # Інкремент лічильника ключів
            self.__count_key += 1
            if self.__count_key / self.__length > 0.9:
                # Якщо коефіціент  відношення кількості ключів до величини таблиці більше 0,9 -> подвоєння розміру таблиці
                self.__multiply_table()
        else:
            print("Current key is already in hash table!")



    def del_data(self, data_key):                       # Метод видалення данних із хеш-таблиці
        # Виконання пошуку даного ключа у таблиці
        mark, count_cell = self.__find_data(data_key)
        if mark:
            # Якщо ключ знайдений, то данні замінюються на ("Delete", None)
            self.__table[count_cell] = ("Delete", None)
            # Декремент лічильника ключів
            self.__count_key -= 1
            if (self.__count_key / self.__length < 0.3) and (self.__length / 2 >= self.__start_length):
                # Якщо коефіціент  відношення кількості ключів до величини таблиці менше 0,3  -> зменшення таблиці в два рази
                self.__division_table()


    def __get_index(self, data):                          # Метод отримання індексу із ключа даних, що додються
        # Сумма значень юнікоду кожного символу ключа помноженного на порядковий номер символу
        index = sum([ord(data[i])*i for i in range(len(data))])
        return index


    def __hash_function(self, index, i):                  # Метод алгоритму подвійного хешування
        A = (5 ** 0.5 - 1) / 2
        hash_1 = math.floor(self.__length * ((index * A) % 1))
        hash_2 = i * (1 + index % (self.__length - 1))
        hash = (hash_1 + hash_2) % self.__length
        return hash


    def __find_data(self, data_key):                    # Метод пошуку ключа у таблиці
        # Отримання числового індексу ключа
        index = self.__get_index(str(data_key))
        count_delete = None
        k_kolithion = 0
        while True:
            # Передача в хеш-функцію індексу ключа і коефіцієнта колізії, та отримання номеру комірки
            count_cell = self.__hash_function(index, k_kolithion)
            if self.__table[count_cell][0] == None:
                # Якщо знайдена комірка None -> заданий ключ не знайдений
                mark = False
                break
            elif self.__table[count_cell][0] == data_key:
                # Якщо знайдена комірка з ключем -> заданий ключ знайдений
                mark = True
                break
            elif self.__table[count_cell][0] == "Delete":
                # Якщо знайдена комірка "Delete" -> заданий ключ не знайдений, продовжуємо пошук
                count_delete = count_cell
                k_kolithion += 1
            else:
                # Якщо знайдена комірка з іншим ключем -> заданий ключ не знайдений, продовжуємо пошук
                k_kolithion += 1
            if k_kolithion >= self.__length:
                print("Atation!")
        if (not mark) and count_delete:
            # Якщо ключ не знайдений і була присутня комірка "Delete" -> повертаємо її номер
            count_cell = count_delete
        return mark, count_cell


    def __multiply_table(self):                                 # Метод динамічного збільшення таблиці
        self.__count_key = 0
        old_table = self.__table
        self.__table = [(None, None)] * self.__length * 2
        self.__length = self.__length * 2
        for i in old_table:
            if not i[0] in ("Delete", None):
                self.set_data(i[0], i[1])


    def __division_table(self):                                 # Метод динамічного зменшення таблиці
        self.__count_key = 0
        old_table = self.__table
        self.__table = [(None, None)] * (int(self.__length / 2))
        self.__length = int(self.__length / 2)
        for i in old_table:
            if not i[0] in ("Delete", None):
                self.set_data(i[0], i[1])








n = HashTable(10)

n.set_data("1", "Hai")
n.set_data("2", "Hova")
n.set_data("1.5", "Hai")
n.set_data("122", "Harov")
n.set_data("Svetlana", "Hova")
n.set_data("Людмила", "Hai")
print("Первісний розмір хеш-таблиці:")
print(n.table)
print(f"Отримання даних по ключу 'Svetlana' : {n.get_data('Svetlana')}")
print(f"Отримання даних по ключу 'Boris' : {n.get_data('Boris')}\n")

n.set_data("Bred", "Pitt")
n.set_data("Angelina", "Jolly")
n.set_data("Met", "Daimon")
n.set_data("Evgen", "Hai")
n.set_data("Price", 1000)
n.set_data(1000, "Blume")
print("Збільшена таблиця:")
print(n.table)
print(f"Отримання даних по ключу 1000 : {n.get_data(1000)}\n")

n.del_data("Met")
n.del_data("1")
n.del_data("2")
n.del_data("1.5")
n.del_data("Svetlana")
n.del_data("122")
n.del_data("Evgen")
n.del_data("Bred")
print("Зменшена таблиця:")
print(n.table)
print(f"Отримання даних по ключу 'Людмила' : {n.get_data('Людмила')}")
print(f"Отримання даних по ключу 'Svetlana' : {n.get_data('Svetlana')}\n")

