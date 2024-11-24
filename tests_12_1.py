import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("TestWalk")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 45)

    def test_run(self):
        runner = Runner("TestRun")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("TestChallenge1")
        runner2 = Runner("TestChallenge2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()