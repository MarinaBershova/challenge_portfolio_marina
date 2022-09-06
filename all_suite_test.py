import unittest

from unittest.loader import makeSuite

from test_cases.add_player_to_the_database import TestAddPlayer
from test_cases.framework import TestMediumPAge
from test_cases.change_language import TestChangeLanguage
from test_cases.clear_fields import TestClearFields
from test_cases.invalid_logging import TestInvalidLoginPage
from test_cases.login_to_the_system import TestLoginPage
from test_cases.sign_out import TestSignOut


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestAddPlayer))
   test_suite.addTest(makeSuite(TestMediumPAge))
   test_suite.addTest(makeSuite(TestChangeLanguage))
   test_suite.addTest(makeSuite(TestClearFields))
   test_suite.addTest(makeSuite(TestInvalidLoginPage))
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestSignOut))
   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())