import unittest
from classes.guest import *
from classes.room import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Harry Pinkerton", 50)
        self.guest_2 = Guest("Alexa Chan", 30)
        self.guest_3 = Guest("Sally Marbels", 150)
    
    def test_guest_has_name(self):
        self.assertEqual("Sally Marbels", self.guest_3.name)
    
    
    def test_guest_has_money(self):
        self.assertEqual(30, self.guest_2.wallet)
    
    def test_guest_can_pay_fee(self):
        room_1 = Room("Green Room", 2, 10, 100,)
        self.guest_1.pay_to_sing(room_1)
        self.assertEqual(40, self.guest_1.wallet)