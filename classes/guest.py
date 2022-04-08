class Guest:
    def __init__(self, input_name, input_wallet, input_favourite_song):
        self.name = input_name
        self.wallet = input_wallet
        self.fav_song = input_favourite_song
    
    def pay_to_sing (self, room_1):
        self.wallet -= room_1.fee
    
    def favourite_song (self, song_1):
        if self.fav_song == song_1:
            return "This song is all about me!"