class calculator(object):
    def __init__(self,a,b,o):
        self.first_number = a
        self.second_number = b
        self.operator = o
    def calc(self):
        if self.operator == '+':
            return self.first_number + self.second_number
        elif self.operator == '-':
            return self.first_number - self.second_number
        elif self.operator == '*':
            return self.first_number * self.second_number
        elif self.operator == '/':
            return self.first_number/self.second_number
        return "Wrong Input"

