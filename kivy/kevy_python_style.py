import kivy
from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    ##**kwargs == unlimited amount of things as list
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        
        #main grid has one colomn, inside has two. 
        self.cols = 1
        ##this if for button
        self.inside = GridLayout()
        self.inside.cols = 2
        
        
        self.inside.add_widget(Label(text="First Name: "))
        self.name= TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.last_name= TextInput(multiline=False)
        self.inside.add_widget(self.last_name)


        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)
        
        
        self.add_widget(self.inside)

        ##to get it to fill bottom put grid layout in gridlayout
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
        
    def pressed(self, instance):
        ##check
        print("Pressed")
        ##how to get the input from the text fields
        name=self.name.text
        last=self.last_name.text
        email=self.email.text
        
        print("First Name: ", name, "\nLast Name:", last, "\nEmail:", email)
        ##clear the text from the fields
        self.name.text = ""
        self.last_name.text = ""
        self.email.text = ""
        
class MyApp(App):    
    def build(self):
        return MyGrid()
    

if __name__ == "__main__":
    MyApp().run()