# -- coding: utf8 --
import unittest
import run_tour
import inspect
from pprint import pprint

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        print('Начинаем тестировать')

    def setUp(self):
        self.usein = run_tour.Runner('Усэйн', 10)
        self.andrey = run_tour.Runner('Андрей', 9)
        self.nik = run_tour.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print()
        for test in cls.all_results:
            print()
            print(f'{test}:')
            print({k: str(v) for k, v in cls.all_results[test].items()})

    def test_usein_nik(self):
        tour = run_tour.Tournament(90, self.usein, self.nik)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    def test_andrey_nik(self):
        tour = run_tour.Tournament(90, self.andrey, self.nik)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    def test_usein_andrey_nik(self):
        tour = run_tour.Tournament(90, self.usein, self.andrey, self.nik)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

if __name__ == '__main__':
    unittest.main()