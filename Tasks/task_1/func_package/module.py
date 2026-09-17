#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def closure(line):
    def massage_line(surname, name):
        result = line.replace("%F%", surname)
        result = result.replace("%N%", name)
        return result

    return massage_line