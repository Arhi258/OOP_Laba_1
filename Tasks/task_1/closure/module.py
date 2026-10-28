#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def closure(template):
    def make_message(surname, name):
        result = template.replace("%F%", surname)
        result = result.replace("%N%", name)
        return result

    return make_message
