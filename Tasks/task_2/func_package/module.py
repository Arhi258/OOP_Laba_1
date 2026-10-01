#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def input_flights():
    flights = []

    count = int(input("Введите количество рейсов: "))

    for i in range(count):
        destination = input("Введите пункт назначения: ")
        flight_number = input("Введите номер рейса: ")
        plane_type = input("Введите тип самолета: ")

        flight = {
            "destination": destination,
            "flight_number": flight_number,
            "plane_type": plane_type
        }

        flights.append(flight)

    return flights


def sort_flights(flights):
    flights.sort(key=lambda flight: flight["destination"])


def print_flights(flights):
    print("\nСписок рейсов:")

    for flight in flights:
        print(
            flight["destination"],
            flight["flight_number"],
            flight["plane_type"]
        )


def find_flights(flights, plane_type):
    found = False

    for flight in flights:
        if flight["plane_type"].lower() == plane_type.lower():
            print(
                f"Пункт назначения: {flight['destination']}, "
                f"номер рейса: {flight['flight_number']}"
            )
            found = True

    if not found:
        print("Рейсов с таким типом самолета нет.")
