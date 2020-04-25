import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)  #**kwargs denotes that the constructor can accept multiple number of _____
        self.cols = 1

        self.inside = GridLayout()               # to create grid inside the main grid, so that the button could be placed at the middle in the GUI
        self.inside.cols = 2           

        self.inside.add_widget(Label(text="First Name:"))
        self.firstname = TextInput(multiline=False)
        self.inside.add_widget(self.firstname)

        self.inside.add_widget(Label(text="Last Name:"))
        self.lastname = TextInput(multiline=False)
        self.inside.add_widget(self.lastname)
        
        self.inside.add_widget(Label(text="Email:"))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit",font_size=40)
        self.submit.bind(on_press=self.pressed)               #Binds the function 'pressed' to the button - gets executed as the button is clicked
        self.add_widget(self.submit)

    def pressed(self, instance):
        firstname = self.firstname.text
        lastname = self.lastname.text
        email = self.email.text
        print(firstname, lastname, email)
        self.firstname.text = ""                              #Clears the fields in the GUI after the value is stored
        self.lastname.text = ""
        self.email.text = ""

class myapp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    myapp().run()
