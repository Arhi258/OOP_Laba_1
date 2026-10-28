#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sort_flights(flights):
    flights.sort(key=lambda flight: flight["destination"].lower())
