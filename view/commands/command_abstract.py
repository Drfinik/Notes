"""Модуль, реализующий абстрактный класс Command"""
from abc import ABC, abstractmethod


class Command(ABC):
    """Класс Command является абстрактным базовым классом для всех команд, которые могут быть
        выполнены в приложении.
        Каждая команда должна реализовывать методы "description" и "execute", которые определяют
        описание команды и ее выполнение соответственно.
        Атрибуты:
        ABC (класс): класс ABC из модуля abc, необходимый для создания абстрактных классов."""

    def __init__(self, console):
        self.console = console

    @abstractmethod
    def description(self):
        """Aбстрактный метод, который должен возвращать описание команды."""

    @abstractmethod
    def execute(self):
        """Aбстрактный метод, который должен выполнять действия, связанные с выполнением команды."""
