class ProgramingLanguage:
    def __init__(self,field,typing,reflection,year):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year= year

    def is_dynamic(self):
        if self.typing =="Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} Typing, Reflection = {}, first appeared in {}".format(self.field,self.typing, self.reflection, self.year)