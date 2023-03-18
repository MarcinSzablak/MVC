class Model():
    def __init__(self):
        self.data = '1'

class View():
    def __init__(self, controller):
        self.controller = controller
        self.model = controller.Model
        
    def display_data(self):
        data = self.model.data
        print(f"Data from the model: {data}")

class Controller():
    def __init__(self):
        self.Model = Model()
        self.View = View(self)

con = Controller()
con.View.display_data()