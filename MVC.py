class Model():
    def __init__(self):
        self.data = '1'

class View():
    pass

class Controller():
    def __init__(self):
        self.Model = Model()
        self.View = View()

con = Controller()
print(con.Model.data)