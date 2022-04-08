import unittest
from classes.song import *

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Single Ladies", "Beyonce")
        self.song_2 = Song("Last Resort", "Papa Roach")
        self.song_3 = Song("Californication", "Red Hot Chilli Peppers")
        self.song_4 = Song("Scar Tissue", "Red Hot Chilli Peppers")
        self.song_5 = Song("The Message", "Grandmaster Flash")
    
    def test_song_has_name(self):
        self.assertEqual("Last Resort", self.song_2.song_name)
    
    
    def test_song_has_artist(self):
        self.assertEqual("Grandmaster Flash", self.song_5.artist_name)
    
    

  