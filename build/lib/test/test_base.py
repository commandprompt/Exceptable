import unittest
import exceptable

class TestBase(unittest.TestCase):
    
    def testGeneric(self):
        pass
        """Will test catching the a generic exception through Exceptable"""
        
    def testExpanded(self):
        
        """Will test catching a new exception after adding it to the exception
        map through the .add interface."""