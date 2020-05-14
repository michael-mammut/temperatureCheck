#!/usr/bin/env python3
import csv
import os
from unittest import TestCase

from Entities.MeasureResult import MeasureResult
from Repository.CsvDataRepository import CsvDataRepository


class test_FileDataRepository(TestCase):

    def setUp(self):
        self.TESTFILE = 'test_file.csv'
        self.TESTFILECOLUMNS=['value', 'ambient', 'created_at']
        self.removeTestFiles()

    def tearDown(self):
        self.removeTestFiles()

    def removeTestFiles(self):
        if os.path.exists(self.TESTFILE):
            os.remove(self.TESTFILE)
        pass

    def test_createEntry(self):
        repo = CsvDataRepository(self.TESTFILE, self.TESTFILECOLUMNS)
        repo.add(MeasureResult(25, 20))
        repo.add(MeasureResult(35, 30))

        f = open(self.TESTFILE, "r", newline="")
        lines = f.readlines()
        f.close()
        self.assertEqual(3, len(lines))


    def test_readEntriesWithOneLine(self):
        f = open(self.TESTFILE, "a", newline="")
        dw = csv.DictWriter(f=f, fieldnames=self.TESTFILECOLUMNS, dialect="excel")
        dw.writerow({'value': 2, 'ambient': 4, 'created_at': '2020-04-14 21:17:56.047276'})
        f.close()

        repo = CsvDataRepository(self.TESTFILE, self.TESTFILECOLUMNS)
        lines = repo.read(1)
        self.assertEqual(1, len(lines))

    def test_readEntriesWithThreeLine(self):
        f = open(self.TESTFILE, mode='a', newline='')
        dw = csv.DictWriter(f=f, fieldnames=self.TESTFILECOLUMNS, dialect="excel")
        dw.writerow({'value': 2, 'ambient': 4, 'created_at': '2020-04-14 21:17:56.047276'})
        dw.writerow({'value': 3, 'ambient': 5, 'created_at': '2020-04-14 21:17:56.047276'})
        dw.writerow({'value': 4, 'ambient': 6, 'created_at': '2020-04-14 21:17:56.047276'})
        f.close()

        repo = CsvDataRepository(self.TESTFILE, self.TESTFILECOLUMNS)
        lines = repo.read(2)
        self.assertEqual(2, len(lines))