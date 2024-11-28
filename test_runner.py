import unittest
from runner2 import Runner

def skip_if_frozen(cls):
    def decorator(func):
        if cls.is_frozen:
            return unittest.skip("Тесты в этом кейсе заморожены")(func)
        return func
    return decorator

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen(RunnerTest)
    def test_walk(self):
        runner = Runner("TestWalk")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen(RunnerTest)
    def test_run(self):
        runner = Runner("TestRun")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen(RunnerTest)
    def test_challenge(self):
        runner1 = Runner("TestChallenge1")
        runner2 = Runner("TestChallenge2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()