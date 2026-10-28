#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Tasks.task_1 import closure


def test_name_substitution():
    message = closure("Уважаемый %F% %N%!")
    assert message("Иванов", "Иван") == "Уважаемый Иванов Иван!"


def test_repeated_placeholders():
    message = closure("%F% / %F% / %N%")
    assert message("Петров", "Петр") == "Петров / Петров / Петр"


def test_template_without_placeholders():
    message = closure("Привет!")
    assert message("Иванов", "Иван") == "Привет!"


def test_different_names():
    message = closure("%N% %F%")
    assert message("Сидоров", "Сергей") == "Сергей Сидоров"
    assert message("Морозова", "Анна") == "Анна Морозова"
