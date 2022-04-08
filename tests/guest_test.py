import unittest
from classes.guest import *
from classes.room import *
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Harry Pinkerton", 30, "Single Ladies")
        self.guest_2 = Guest("Alexa Chan", 30, "Californication")
        self.guest_3 = Guest("Sally Marbels", 150, "Last Resort")
    
    def test_guest_has_name(self):
        self.assertEqual("Sally Marbels", self.guest_3.name)
    
    
    def test_guest_has_money(self):
        self.assertEqual(30, self.guest_2.wallet)
    
    def test_guest_can_pay_fee(self):
        room_1 = Room("Green Room", 2, 10, 100,)
        self.guest_1.pay_to_sing(room_1)
        self.assertEqual(20, self.guest_1.wallet)
    
    def test_favourite_song (self):
        fav_song_1 = Song("Last Resort", "Papa Roach")
        self.guest_3.favourite_song(fav_song_1)
        self.assertEqual("This song is all about me!", self.guest_3.favourite_song("Last Resort"))