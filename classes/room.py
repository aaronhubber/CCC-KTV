class Room:
    def __init__(self, input_room_name, input_room_capacity, input_fee, input_till):
        self.room_name = input_room_name
        self.room_capacity = input_room_capacity
        self.fee = input_fee
        self.till = input_till
        self.guest_list = []
        self.song_list = []
    
    def show_guests_name (self):
        return self.guest_list

    def add_guest (self, guest_1):
        self.guest_list.append(guest_1)
    
    def remove_guest (self, guest_1):
        self.guest_list.remove(guest_1)
    
    def show_song_list (self):
        for song in range(len(self.song_list)):
            return self.song_list[song]
    
    def add_song (self, song_1):
        self.song_list.append(song_1)

    def remove_song (self, song_1):
        self.song_list.remove(song_1)
    
    def capacity_checker (self):
        if len(self.guest_list) >= self.room_capacity:
            return "Not tonight, rooms full"
    
    def recieve_fee (self, room_1):
        self.till += room_1.fee
    

    
