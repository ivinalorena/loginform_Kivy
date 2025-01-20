import database.database
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import database

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != '' and self.email.text != '' and self.email.text.count('@') == 1 and self.email.text.count('.') > 0:
            if self.password.text != '':  # Corrigido para acessar text corretamente
                db.add_user(self.email.text, self.password.text, self.namee.text)
                self.reset()
                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"  # Corrigido aspas

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = 'login'

    def on_enter(self, *args):
        user_data = db.get_user(self.current)
        if user_data:  # Garantir que os dados do usuário existem antes de atribuir
            password, name, created = user_data
            self.n.text = 'Account Name: ' + name
            self.email.text = 'Email: ' + self.current
            self.created.text = 'Created On: ' + created

class WindowManager(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title='Invalid Login', content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()

def invalidForm():
    pop = Popup(title='Invalid Form',
                content=Label(text='Please fill in all inputs with valid information'),
                size_hint=(None, None), size=(400, 400))
    pop.open()

kv = Builder.load_file('my.kv')
sm = WindowManager()
import database  
#db = database("users.txt") # Se Database for uma classe dentro do módulo
class DataBase:
        def __init__(self, filename):
            self.filename = filename
screens = [LoginWindow(name='login'), CreateAccountWindow(name='create'), MainWindow(name='main')]
db = DataBase("users.txt")  # Corrigido a chamada da classe
for screen in screens:
    sm.add_widget(screen)  # Corrigido erro ao adicionar as telas

sm.current = 'login'  # Agora está no local correto

class MyMainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":  # Corrigido aspas
    MyMainApp().run()
