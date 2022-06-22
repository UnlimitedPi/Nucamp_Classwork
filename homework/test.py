def function(name):
    return f'First test function in GitHub by {name}!\n'

hello = function('UnlimitedPi')

print(hello)

class User:
    def __init__(self, f_name, l_name, age, job):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.job =job
    
    def list_user(self):
        return f'Your user info: {self.l_name}, {self.f_name} - Age: {self.age}, Job: {self.job}.'

user_1 = User('Ryan', 'Castillo', '24', 'Software Dev')

print(user_1.list_user())
