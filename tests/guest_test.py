import unittest
from classes.guest import *


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Harry Pinkerton", 50)
        self.guest_2 = Guest("Alexa Chan", 30)
        self.guest_3 = Guest("Sally Marbels", 150)
    
    def test_guest_has_name(self):
        self.assertEqual("Sally Marbels", self.guest_3.name)
    
    
    def test_guest_has_money(self):
        self.assertEqual(30, self.guest_2.wallet)