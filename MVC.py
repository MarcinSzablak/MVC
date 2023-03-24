class Model():
    def __init__(self, id = None, danie = None):
        self.id = id
        self.danie = danie
    def pokaz_danie(self):
        print(f"numer {self.id} przygotowujemy twoje {self.danie}")

class View():
    def podaj(self, danieId, danie):
        self.id = danieId
        self.danie = danie
        print(f'numer {self.id} proszę odebrać danie {self.danie}')

class Controller():
    def zrub_danie(self, id = None, danie = None):
        self.model = Model(id,danie)
        self.danie = self.model.danie
        self.danieId = self.model.id
        self.model.pokaz_danie()
    def pokaz_danie(self):
        self.view = View()
        self.view.podaj(self.danieId, self.danie)


con = Controller()
con.zrub_danie(1,'schabowe')
con.pokaz_danie()