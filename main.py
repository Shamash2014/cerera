import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label


class Cerera(App):
    def build(self):
        return Label(text='Hello world')

if __name__ == '__main__':
    Cerera().run()
