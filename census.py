class Census:
    def __init__(self):
        self.year = 0
        self.pop = 0
    def __init__(self, year, pop):
        self.year = year
        self.pop = pop
    ## to_string method
    def __str__(self):
        return "{0} {1}".format(self.year,self.pop)
    ##-------------------meths--------------------------
    def get_yr(self):
        return self.year
    def get_pop(self):
        return self.pop
    def find_change_in_pop(self, new_pop):
        """Find change in population from self's current year info and a different year."""
        change_in_pop = new_pop - self.pop
        return change_in_pop

