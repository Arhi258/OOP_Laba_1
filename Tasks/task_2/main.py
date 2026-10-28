#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .find_flights import find_flights
from .input_flights import input_flights
from .print_flights import print_flights
from .sort_flights import sort_flights

if __name__ == "__main__":
    flights = input_flights()

    sort_flights(flights)
    print_flights(flights)

    plane_type = input("\nВведите тип самолета для поиска: ")
    find_flights(flights, plane_type)
