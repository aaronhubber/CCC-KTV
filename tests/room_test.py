import unittest
from classes.room import *
from classes.guest import *
from classes.song import *


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Green Room", 8, 10, 100,)
        self.room_2 = Room("Sky Room", 20, 5, 100,)
        self.guest_1 = Guest("Harry Pinkerton", 30)
        self.guest_2 = Guest("Alexa Chan", 30)
        self.guest_3 = Guest("Sally Marbels", 150)
        self.song_1 = Song("Single Ladies", "Beyonce")
        self.song_2 = Song("Last Resort", "Papa Roach")
        self.song_3 = Song("Californication", "Red Hot Chilli Peppers")
        self.song_4 = Song("Scar Tissue", "Red Hot Chilli Peppers")
        self.song_5 = Song("The Message", "Grandmaster Flash")

    def test_room_has_name(self):
        self.assertEqual("Green Room", self.room_1.room_name)
    
    
    def test_room_has_till(self):
        self.assertEqual(100.00, self.room_1.till)

    def test_room_has_capacaity(self):
        self.assertEqual(8, self.room_1.room_capacity)
    
    def test_amount_charged_for_room(self):
        self.assertEqual(10, self.room_1.fee)
    
    def test_can_add_guest_to_room(self):
        self.room_1.add_guest(self.guest_1)
        self.assertEqual(1, len(self.room_1.guest_list))

    def test_show_guest_list(self):
        self.room_1.add_guest(self.guest_1.name)
        self.assertEqual("Harry Pinkerton", self.room_1.show_guests())
    
    def test_remove_guest_from_room(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.remove_guest(self.guest_1)
        self.assertEqual(0, len(self.room_1.guest_list))
    
    def test_show_guest_list_after_remove(self):
        self.room_1.add_guest(self.guest_1.name)
        self.room_1.add_guest(self.guest_2.name)
        self.room_1.remove_guest(self.guest_1.name)
        self.assertEqual("Alexa Chan", self.room_1.show_guests())
    
    def test_add_song_to_list(self):
        self.room_1.add_song(self.song_2)
        self.assertEqual(1, len(self.room_1.song_list))
    
    def test_song_list(self):
        self.room_1.add_song(self.song_2.song_name)
        self.assertEqual ("Last Resort", self.room_1.show_song_list())
    
    def test_remove_song_from_list(self):
        self.room_1.add_song(self.song_1)
        self.room_1.remove_song(self.song_1)
        self.assertEqual(0, len(self.room_1.song_list))
    
    def test__song_list_after_remove_song_from_list(self):
       self.room_1.add_song(self.song_2.song_name)
       self.room_1.add_song(self.song_4.song_name)
       self.room_1.remove_song(self.song_2.song_name)
       self.assertEqual("Scar Tissue", self.room_1.show_song_list())

        
    
