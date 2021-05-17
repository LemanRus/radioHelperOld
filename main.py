from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class RadioHelperScreenManager(ScreenManager):
    pass


class MainScreen(Screen):
    pass


class NominalsScreen(Screen):
    pass


class ComponentsScreen(Screen):
    pass


class PinsScreen(Screen):
    pass


class SchemesScreen(Screen):
    pass


class SymbolsScreen(Screen):
    pass


class StatesScreen(Screen):
    pass


class HelpScreen(Screen):
    pass


class AboutScreen(Screen):
    pass


class RadioHelperApp(App):
    def build(self):
        return RadioHelperScreenManager()


if __name__ == '__main__':
    RadioHelperApp().run()
