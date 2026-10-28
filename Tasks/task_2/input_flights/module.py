#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def input_flights():
    flights = []
    count = int(input("Введите количество рейсов: "))

    for _ in range(count):
        destination = input("Введите пункт назначения: ")
        flight_number = input("Введите номер рейса: ")
        plane_type = input("Введите тип самолета: ")

        flight = {
            "destination": destination,
            "flight_number": flight_number,
            "plane_type": plane_type,
        }

        flights.append(flight)

    return flights
