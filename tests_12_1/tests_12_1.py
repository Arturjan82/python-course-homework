# -- coding: utf8 --
import unittest
import runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        Test_name = runner.Runner('Петя')
        for _ in range(10):
            Test_name.walk()
        self.assertEqual(50, Test_name.distance,'Дистанции не равны')

    def test_run(self):
        Test_name = runner.Runner('Петя')
        for _ in range(10):
            Test_name.run()
        self.assertEqual(100,Test_name.distance, ' Дистанция не равны')

    def test_challenge(self):
        Test_1 = runner.Runner('Петя')
        Test_2 = runner.Runner('Вася')
        for _ in range(10):
            Test_1.run()
            Test_2.walk()
        self.assertNotEqual(Test_1.distance,Test_2.distance, 'Дистанции одинаковы')

if __name__ == '__main__':
   unittest.main()