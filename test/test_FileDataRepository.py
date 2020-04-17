#!/usr/bin/env python3
import csv
import os
from unittest import TestCase

from Entities.TemperatureMeasure import MeasureResult
from Repository.DataRepository import DataRepository


class test_FileDataRepository(TestCase):

    def setUp(self):
        self.TESTFILE = 'test_file.csv'
        self.removeTestFiles()

    def tearDown(self):
        self.removeTestFiles()

    def removeTestFiles(self):
        if os.path.exists(self.TESTFILE):
            os.remove(self.TESTFILE)
        pass

    def test_createEntry(self):
        repo = DataRepository(self.TESTFILE)
        repo.add(MeasureResult(25, 20))
        repo.add(MeasureResult(35, 30))

        f = open(self.TESTFILE, "r", newline="")
        lines = f.readlines()
        f.close()
        self.assertEqual(3, len(lines))


    def test_readEntriesWithOneLine(self):
        f = open(self.TESTFILE, "a", newline="")
        fields = ['value', 'ambient', 'created_at']
        dw = csv.DictWriter(f=f, fieldnames=fields, dialect="excel")
        dw.writerow({'value': 2, 'ambient': 4, 'created_at': '2020-04-14 21:17:56.047276'})
        f.close()

        repo = DataRepository(self.TESTFILE)
        lines = repo.read(1)
        self.assertEqual(1, len(lines))

    def test_readEntriesWithThreeLine(self):
        f = open(self.TESTFILE, mode='a', newline='')
        fields = ['value', 'ambient', 'created_at']
        dw = csv.DictWriter(f=f, fieldnames=fields, dialect="excel")
        dw.writerow({'value': 2, 'ambient': 4, 'created_at': '2020-04-14 21:17:56.047276'})
        dw.writerow({'value': 3, 'ambient': 5, 'created_at': '2020-04-14 21:17:56.047276'})
        dw.writerow({'value': 4, 'ambient': 6, 'created_at': '2020-04-14 21:17:56.047276'})
        f.close()

        repo = DataRepository(self.TESTFILE)
        lines = repo.read(2)
        self.assertEqual(2, len(lines))