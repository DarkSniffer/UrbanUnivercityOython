import unittest
from test_runner1 import RunnerTest
from test_tournament1 import TournamentTest

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(RunnerTest))
    test_suite.addTest(unittest.makeSuite(TournamentTest))
    return test_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())