#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Tasks.task_2 import (
    find_flights,
    input_flights,
    print_flights,
    sort_flights,
)


def sample_flights():
    return [
        {
            "destination": "Сызрань",
            "flight_number": "3",
            "plane_type": "ЛП-02",
        },
        {
            "destination": "Москва",
            "flight_number": "12",
            "plane_type": "ТУ-13",
        },
        {
            "destination": "Город",
            "flight_number": "1",
            "plane_type": "ТУ-1",
        },
    ]


def test_sort_flights():
    flights = sample_flights()
    sort_flights(flights)

    assert [flight["destination"] for flight in flights] == [
        "Город",
        "Москва",
        "Сызрань",
    ]


def test_sort_empty_list():
    flights = []
    sort_flights(flights)
    assert flights == []


def test_input_flights(monkeypatch):
    responses = iter(["1", "Москва", "12", "ТУ-13"])
    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(responses),
    )

    assert input_flights() == [
        {
            "destination": "Москва",
            "flight_number": "12",
            "plane_type": "ТУ-13",
        }
    ]


def test_print_flights(capsys):
    print_flights(sample_flights())
    output = capsys.readouterr().out

    assert "Список рейсов:" in output
    assert "Москва 12 ТУ-13" in output


def test_find_flights(capsys):
    find_flights(sample_flights(), "лп-02")
    output = capsys.readouterr().out

    assert "Пункт назначения: Сызрань, номер рейса: 3" in output


def test_find_flights_not_found(capsys):
    find_flights(sample_flights(), "Боинг")
    output = capsys.readouterr().out

    assert "Рейсов с таким типом самолета нет." in output
