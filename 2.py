"""

Написати програму для реєстрації і авторизації користувача з наступним функціоналом:
-отримання в інтерактивному режимі логіну і пароля користувача;
-верифікація пароля і його шифрування за обраним алгоритмом шифрування;
-запис пари "логін-пароль" у словник з перевіркою на колізії;
-авторизація користувача за логіном і паролем.
"""

import math
import numpy as np
import pandas as pd
import hashlib
import os


class AccountTable:

    @classmethod
    def verify_length(self, length):                                 # Метод перевірки коректності задануого розміру хеш-таблиці
        if type(length) != int or length < 5 or length > 1000:
            raise TypeError("Довжина хеш-таблиці має бути цілим числом більше 5 та не більше 1000")

    def create_table_file(self, length):                            # Метод створення csv файлу заданої довжини
        self.verify_length(length)                                  # Перевірка на коректність заданого розміру хеш-таблиці
        table = [(None, None, None, None)] * length
        df = pd.DataFrame(table, columns=["account", "hash", "length", "count_acc"])
        df.loc[[0], ["length"] ] = length
        df.loc[[0], ["count_acc"]] = 0
        df.to_csv("login.csv", index=False)

    def delete_table_file(self):                                     # Метод видалення csv файлу
        os.remove("login.csv")




class Authorization:
    
    def __init__(self):
        self.__table = pd.read_csv("login.csv")              # Зчитування данних з файлу
        self.__length = self.__table.iat[0, 2]               # Довжина хеш таблиці
        self.__count_key = self.__table.iat[0, 3]            # Поточна кількість ключів в хеш-таблиці



    def sign_in_acc(self):                                  # Метод реалізує інтерактивний режим роботи з аккаунтом
        # Введення логіну
        acc = input("Input your account: ")
        mark, count_cell = self.__find_acc(acc)

        if mark:
            # Якщо логін знайдено - запит пароля
            pas = input("Input your password: ")
            hash_password = self.__pas_to_hash(pas)

            # Перевірка на правильність хешованого пароля
            if hash_password == self.__table.iat[count_cell, 1]:
                print("Congratulation! You've sign in!")
                flag_delete = input("Press  d  if you want delete your account (or anykey if no): ")
                if flag_delete.upper() == "D":
                    self.__table.iat[count_cell, 0] = "Delete"
                    self.__table.iat[count_cell, 1] = None
                    self.__count_key -= 1
                    self.__data_to_csv()
                    print("You've deleted your account (")
                else:
                    print("Sign out... Goodbuy!")
            else:
                print("Sorry! Password is incorrect..")

        # Якщо логін не знайдено - пропозиція створити новий аккаунт
        else:
            print("Your account hasn't been found! Do you want to create new account?")
            flag_create = input("Press  y  if yes (or anykey if no): ")
            if flag_create.upper() == "Y":
                mark, count_cell = self.__find_acc(acc)
                self.__table.iat[count_cell, 0] = acc
                pas = input("Input your password: ")
                hash_password = self.__pas_to_hash(pas)
                self.__table.iat[count_cell, 1] = hash_password
                self.__count_key += 1
                self.__data_to_csv()
                print("Congratulation! You've created new account!")
            else:
                print("Goodbuy!")


    def __data_to_csv(self):                                        # Метод запису зміненої таблиці у файл
        self.__table.to_csv("login.csv", index=False)

    def __pas_to_hash(self, pas):                                   # Метод отримання хешу з пароля
        hash_obj = hashlib.sha256(str(pas).encode())
        hex_dig = hash_obj.hexdigest()
        return hex_dig

    def __find_acc(self, acc):                                      # Метод пошуку аккаунту в таблиці
        # Отримання числового індексу ключа
        index = self.__get_index(str(acc))
        count_delete = None
        k_kolithion = 0
        while True:
            # Передача в хеш-функцію індексу ключа і коефіцієнта колізії, та отримання номеру комірки
            count_cell = self.__hash_function(index, k_kolithion)
            try:
                if np.isnan(self.__table.iat[count_cell, 0]):
                    # Якщо знайдена комірка None -> заданий ключ не знайдений
                    mark = False
                    break
            except TypeError:
                if self.__table.iat[count_cell, 0] == acc:
                    # Якщо знайдена комірка з ключем -> заданий ключ знайдений
                    mark = True
                    break
                elif self.__table.iat[count_cell, 0] == "Delete":
                    # Якщо знайдена комірка "Delete" -> заданий ключ не знайдений, продовжуємо пошук
                    count_delete = count_cell
                    k_kolithion += 1
                else:
                    # Якщо знайдена комірка з іншим ключем -> заданий ключ не знайдений, продовжуємо пошук
                    k_kolithion += 1
            if k_kolithion >= self.__length:
                print("Ahtung!")
        if (not mark) and count_delete:
            # Якщо ключ не знайдений і була присутня комірка "Delete" -> повертаємо її номер
            count_cell = count_delete
        return mark, int(count_cell)

    def __get_index(self, acc):                                             # Метод отримання числового індекса з логіну
        index = sum([ord(acc[i])*i for i in range(len(acc))])
        return index

    def __hash_function(self, index, i):                                   # Метод хешфункції
        A = (5 ** 0.5 - 1) / 2
        hash_1 = math.floor(self.__length * ((index * A) % 1))
        hash_2 = i * (1 + index % (self.__length - 1))
        hash = (hash_1 + hash_2) % self.__length
        return int(hash)


# c = AccountTable()
# c.create_table_file(10)
# c.delete_table_file()

n = Authorization()
n.sign_in_acc()


















