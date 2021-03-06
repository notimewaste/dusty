from ..testcases import DustyTestCase
from dusty.preflight import _assert_executable_exists, PreflightException

class PreflightTest(DustyTestCase):
    def test_assert_executable_exists(self):
        _assert_executable_exists('python')

    def test_assert_executable_exists_fails(self):
        with self.assertRaises(PreflightException):
            _assert_executable_exists('somecrazythingwhichforsuredoesnotexist')
