import Athlete
class Boxer:
    boxer_count = 0  
    def __init__(self, name_p = None, dob_p = None, origin_p = None , medals_p = [ ], weight_class_p = None):
        Athlete.__init__(self, name_p = None, dob_p = None, origin_p = None , medals_p = [ ])
        self.weight_class = weight_class_p 
        self.record = [0,0]
        Boxer.boxer_count += 1
    def __self__(self):
        return (f"Boxer: {self.name}\n Date of Birth (DOB): {self.dob}\n Weight Class: {self.weight_class}\n Origin: {self.origin}\n Medals: {self.medals} ")
    def get_weight_class(self):
        return self.weight_class
    def get_record(self):
        return self.record
    def set_weight_class(self, weight_class_p):
        self.weight_class = weight_class_p
    def win_fight(self):
        self.record[0] +=1
    def lose_fight(self):
        self.record[1] += 1