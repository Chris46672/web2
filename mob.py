from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
import sys


class Mywork(Widget):
    btn = ObjectProperty(None)
    btn1 = ObjectProperty(None)
    def clear(self):
        self.ent.text = ""

    def add1(self):
        self.ent.text = self.ent.text+str(1)

    def add2(self):
        self.ent.text = self.ent.text + str(2)

    def add3(self):
        self.ent.text = self.ent.text + str(3)

    def add4(self):
        self.ent.text = self.ent.text + str(4)

    def add5(self):
        self.ent.text = self.ent.text + str(5)
    def add6(self):
        self.ent.text = self.ent.text + str(6)

    def add7(self):
        self.ent.text = self.ent.text + str(7)

    def add8(self):
        self.ent.text = self.ent.text + str(8)

    def add9(self):
        self.ent.text = self.ent.text + str(9)

    def add0(self):
        self.ent.text = self.ent.text + str(0)

    def add(self):
        self.ent.text = self.ent.text + "+"

    def sub(self):
        self.ent.text = self.ent.text + "-"

    def div(self):
        self.ent.text = self.ent.text + "/"

    def mul(self):
        self.ent.text = self.ent.text + "*"

    def Answer(self):
        try:
            self.ent.text = str(float(eval(self.ent.text)))
        except:
            self.ent.text="An Error"
    def exit(self):
        sys;exit()


class MyApp(App):

    def build(self):
        return Mywork()


if __name__ == '__main__':
    MyApp().run()