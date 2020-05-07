#!/usr/bin/env python3

import csv
import logging
import os

from Repository.DataRepositoryAbstract import DataRepositoryAbstract
from Settings.datastore import LOGFILE_WITH_PATH


class DataRepository(DataRepositoryAbstract):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename
        self._fields = ['value', 'ambient', 'created_at']

        logging.basicConfig(format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s',
                            level=logging.ERROR, filename=LOGFILE_WITH_PATH)

    def add(self, result):
        try:
            if not os.path.isfile(self._filename):
                f = open(self._filename, "a", newline='')
                dw = csv.DictWriter(f=f, fieldnames=self._fields, dialect="excel")
                dw.writeheader()
            else:
                f = open(self._filename, "a", newline='')
                dw = csv.DictWriter(f=f, fieldnames=self._fields, dialect="excel")

            dw.writerow(result.__dict__)
            f.close()
        except OSError:
            logging.error("Writing into the CSV " + self._filename)

    def read(self, number_of_measurements=10):
        return self.__file_read_from_tail(self._filename, number_of_measurements)

    # Source code copied and partitial modified
    # src: https://www.w3resource.com/python-exercises/file/python-io-exercise-4.php
    def __file_read_from_tail(self, fname, lines):
        try:
            line_list = []
            bufsize = 8192
            fsize = os.stat(fname).st_size
            item = 0
            with open(fname) as f:
                if bufsize > fsize:
                    bufsize = fsize - 1
                    data = []
                    while True:
                        item += 1
                        f.seek(fsize - bufsize * item)
                        data.extend(f.readlines())
                        if len(data) >= lines or f.tell() == 0:
                            line_list.extend(data[-lines:])
                            break

            return line_list
        except OSError:
            logging.error("Reading from CSV " + self._filename)
