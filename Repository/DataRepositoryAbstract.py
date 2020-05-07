#!/usr/bin/env python3
from abc import abstractmethod, ABC


class DataRepositoryAbstract(ABC):

    @abstractmethod
    def add(self, measureresult):
        pass

    @abstractmethod
    def read(self, number_of_days=10):
        pass
