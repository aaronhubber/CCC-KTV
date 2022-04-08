class Guest:
    def __init__(self, input_name, input_wallet):
        self.name = input_name
        self.wallet = input_wallet
    

    def pay_to_sing (self, room_1):
        self.wallet -= room_1.fee