class Athlete:
    athlete_count = 0
    medal_list = [ ]
    def __init__(self, name_p = None, dob_p = None, origin_p = None , medals_p = [ ]):
        self.name = name_p 
        self.dob = dob_p
        self.origin = origin_p
        self.medals = medals_p
        Athlete.athlete_count += 1
    def get_name (self):
        return self.name
    def get_dob(self):
        return self.dob
    def get_origin(self):
        return self.origin
    def get_medals(self):
        return self.medals
    def add_medal(medals_p):
        medal_list.append(medal_p)