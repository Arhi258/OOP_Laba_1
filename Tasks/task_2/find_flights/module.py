#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
