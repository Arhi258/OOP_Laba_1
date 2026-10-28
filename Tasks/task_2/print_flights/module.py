#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_flights(flights):
    print("\nСписок рейсов:")

    for flight in flights:
        print(
            flight["destination"],
            flight["flight_number"],
            flight["plane_type"],
        )
