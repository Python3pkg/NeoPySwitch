"""Quick test script"""

__author__ = 'Thomas Li Fredriksen'
__license__ = 'MIT'

from NeoPySwitch import SwitchCase as case, PySwitch as switch

import unittest



class Test_PySwitch(unittest.TestCase):

    def SetUp(self):
        pass

    def test_switch(self):
        """Test to see if things work as intended"""
        @case
        def case_1(arg1):
            print(('Case 1: ', arg1))

        @case
        def case_2(arg1, arg2):
            print(('Case 2: ', arg2))

        @case
        def default_case(arg1, arg2, arg3):
            print(('Default case: ', arg1, arg2, arg3))

        switch(2, {
            1: case_1('a'),
            2: case_2('abc', 42),
            }, default_case(13, 'somestring', 3.14))


print('ok')
