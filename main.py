from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):

    def build(self):
        self.title = 'KivyMD File Manager'
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"


MainApp().run()
