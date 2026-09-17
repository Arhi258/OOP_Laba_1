#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from func_package import (
    input_flights,
    sort_flights,
    print_flights,
    find_flights
)


if __name__ == "__main__":
    flights = input_flights()

    sort_flights(flights)

    print_flights(flights)

    plane_type = input("\nВведите тип самолета для поиска: ")

    find_flights(flights, plane_type)