from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class myApp(App):
    def build(self):

        s=Scatter()
        fl=FloatLayout(size=(600, 200))
        s.add_widget(fl)
        fl.add_widget(Button(
            text="Это кнопка",
            font_size=20,
            on_press=self.btn_press,
            background_color='#008EB0',
            background_normal='#008EB0',
            size_hint=(.5, .25),
            pos=(200, 200)));
        fl.add_widget(Button(
            text="Это другая кнопка",
            font_size=20,
            on_press=self.btn_press,
            background_color='#FF3030',
            background_normal='',
            size_hint=(.5, .25),
            pos=(100, 100)));
        return s
    def btn_press(self, instance):        
        instance.text='Я нажата'
        
if __name__=="__main__":
    myApp().run()
