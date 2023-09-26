import Athlete
class Swimmer:
    swimmer_count = 0 
    def __init__(self, name_p = None, dob_p = None, origin_p = None , medals_p = [ ], strokes_p = [ ]):
        Athlete.__init__(self, name_p = None, dob_p = None, origin_p = None , medals_p = [ ])
        self.strokes = strokes_p 
        Swimmer.swimmer_count += 1
    def __str__(self):
        return print(f"Swimmer: {self.name}\n Date of Birth (DOB): {self.dob}\n Weight Class: {self.weight_class}\n Origin: {self.origin}\n Medals: {self.medals}\n Strokes: {self.strokes}")
    def get_strokes(self):
        return self.strokes
    def add_stroke(self, stroke):
        if stroke not in self.strokes:
            self.strokes.append(stroke)
