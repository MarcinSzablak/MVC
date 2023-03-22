class Model():
    def __init__(self, id = None, danie = None):
        self.id = id
        self.danie = danie
    def pokaz_danie(self):
        print(f"numer {self.id} przygotowujemy twoje {self.danie}")

class View():
    def __init__(self, controller):
        self.controller = controller
        self.model = controller.model
        
    def podaj(self):
        self.id = self.model.id
        self.danie = self.model.danie
        print(f'numer {self.id} proszę odebrać danie {self.danie}')

class Controller():
    def zrub_danie(self, id = None, danie = None):
        self.model = Model(id,danie)
        self.model.pokaz_danie()
    def pokaz_danie(self):
        self.view = View(self)
        self.view.podaj()


con = Controller()
con.zrub_danie(1,'schabowe')
con.pokaz_danie()