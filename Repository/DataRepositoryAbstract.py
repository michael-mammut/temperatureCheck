#!/usr/bin/env python3
import logging
from abc import abstractmethod, ABC


class DataRepositoryAbstract(ABC):

    @abstractmethod
    def add(self, measureresult):
        pass

    @abstractmethod
    def read(self, numberOfDays = 10):
        pass