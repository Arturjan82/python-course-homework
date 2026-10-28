# -- coding: utf8 --
import logging
from rt_with_exceptions import Runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            peshehod = Runner('Пешеход', -3)
            for i in range(10):
                peshehod.walk()
            self.assertEqual(peshehod.distance, 50)
            logging.info(f'test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner')

    def test_run(self):
        try:
            begun = Runner(1234)
            for i in range(10):
                begun.run()
            self.assertEqual(begun.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename="runner.log", filemode="w", encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    unittest.main()
