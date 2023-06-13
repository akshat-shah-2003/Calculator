from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window

class MyWidget(Widget):
    input1 = TextInput(multiline=False, size_hint=(None,None), size=(400,50), pos=(450,600), font_size=30, disabled=True)
    button1 = Button(text='+', size_hint=(None,None), size=(100,100), pos=(750,500), font_size=30)
    button2 = Button(text='-', size_hint=(None,None), size=(100,100), pos=(750,400), font_size=30)
    button3 = Button(text='*', size_hint=(None,None), size=(100,100), pos=(750,300), font_size=30)
    button4 = Button(text='/', size_hint=(None,None), size=(100,100), pos=(750,200), font_size=30)
    button5 = Button(text='C', size_hint=(None,None), size=(200,100), pos=(650,100), font_size=30)
    button6 = Button(text='<--', size_hint=(None,None), size=(200,100), pos=(450,100), font_size=30)
    button7 = Button(text='=', size_hint=(None,None), size=(100,100), pos=(650,200), font_size=30)
    button8 = Button(text='1', size_hint=(None,None), size=(100,100), pos=(450,500), font_size=30)
    button9 = Button(text='2', size_hint=(None,None), size=(100,100), pos=(550,500), font_size=30)
    button10 = Button(text='3', size_hint=(None,None), size=(100,100), pos=(650,500), font_size=30)
    button11 = Button(text='4', size_hint=(None,None), size=(100,100), pos=(450,400), font_size=30)
    button12 = Button(text='5', size_hint=(None,None), size=(100,100), pos=(550,400), font_size=30)
    button13 = Button(text='6', size_hint=(None,None), size=(100,100), pos=(650,400), font_size=30)
    button14 = Button(text='7', size_hint=(None,None), size=(100,100), pos=(450,300), font_size=30)
    button15 = Button(text='8', size_hint=(None,None), size=(100,100), pos=(550,300), font_size=30)
    button16 = Button(text='9', size_hint=(None,None), size=(100,100), pos=(650,300), font_size=30)
    button17 = Button(text='0', size_hint=(None,None), size=(100,100), pos=(450,200), font_size=30)
    button18 = Button(text='.', size_hint=(None,None), size=(100,100), pos=(550,200), font_size=30)

    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.add_widget(self.input1)
        self.add_widget(self.button1)
        self.button1.bind(on_press=lambda x: self.appen("+",x))
        self.add_widget(self.button2)
        self.button2.bind(on_press=lambda x: self.appen("-",x))
        self.add_widget(self.button3)
        self.button3.bind(on_press=lambda x: self.appen("*",x))
        self.add_widget(self.button4)
        self.button4.bind(on_press=lambda x: self.appen("/",x))
        self.add_widget(self.button5)
        self.button5.bind(on_press=self.clr)
        self.add_widget(self.button6)
        self.button6.bind(on_press=self.clr_pop)
        self.add_widget(self.button7)
        self.button7.bind(on_press=self.calc)
        self.add_widget(self.button8)
        self.button8.bind(on_press=lambda x: self.appen("1",x))
        self.add_widget(self.button9)
        self.button9.bind(on_press=lambda x: self.appen("2",x))
        self.add_widget(self.button10)
        self.button10.bind(on_press=lambda x: self.appen("3",x))
        self.add_widget(self.button11)
        self.button11.bind(on_press=lambda x: self.appen("4",x))
        self.add_widget(self.button12)
        self.button12.bind(on_press=lambda x: self.appen("5",x))
        self.add_widget(self.button13)
        self.button13.bind(on_press=lambda x: self.appen("6",x))
        self.add_widget(self.button14)
        self.button14.bind(on_press=lambda x: self.appen("7",x))
        self.add_widget(self.button15)
        self.button15.bind(on_press=lambda x: self.appen("8",x))
        self.add_widget(self.button16)
        self.button16.bind(on_press=lambda x: self.appen("9",x))
        self.add_widget(self.button17)
        self.button17.bind(on_press=lambda x: self.appen("0",x))
        self.add_widget(self.button18)
        self.button18.bind(on_press=lambda x: self.appen(".",x))
     
    def appen(self,sign,instance):
        self.input1.insert_text(sign)
    
    def clr(self, instance):
        self.input1.text=""

    def clr_pop(self, instance):
        self.input1.text=self.input1.text[:len(self.input1.text)-1]
    
    def calc(self, instance):
        self.input1.text=str(eval(self.input1.text))

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Window.fullscreen = 'auto'
    MyApp().run()
