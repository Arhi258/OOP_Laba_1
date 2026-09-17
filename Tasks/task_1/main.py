#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from func_package import closure


if __name__ == '__main__':
    line = ("Уважаемый %F% %N%! "
            "Вы делаете работу по замыканию функций.")

    message = closure(line)

    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")

    print(message(surname, name))