import unittest
import logging
from runner3 import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='UTF-8',
    format='%(levelname)s: %(message)s'
)

def skip_if_frozen(cls_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if getattr(globals().get(cls_name), 'is_frozen', False):
                raise unittest.SkipTest("Тесты в этом кейсе заморожены")
            return func(*args, **kwargs)
        return wrapper
    return decorator

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen('RunnerTest')
    def test_walk(self):
        with self.assertRaises(ValueError) as cm:
            runner = Runner("TestWalk", -5)  # Передаем отрицательное значение в speed
        logging.warning('Неверная скорость для Runner')
        self.assertEqual(str(cm.exception), f'Скорость не может быть отрицательной, сейчас -5')

    @skip_if_frozen('RunnerTest')
    def test_run(self):
        with self.assertRaises(TypeError) as cm:
            runner = Runner(123, 10)  # Передаем что-то кроме строки в name
        logging.warning('Неверный тип данных для объекта Runner')
        self.assertEqual(str(cm.exception), f'Имя может быть только строкой, передано int')

    @skip_if_frozen('RunnerTest')
    def test_challenge(self):
        runner1 = Runner("TestChallenge1")
        runner2 = Runner("TestChallenge2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()