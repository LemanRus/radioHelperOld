from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.settings import SettingsWithSidebar
from kivy.config import Config

from settingsjson import settings_json

Config.read("radiohelper.ini")


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
    data = ObjectProperty(None)
    data.headers_font_size = NumericProperty(Config.getint("font", "размер шрифта заголовков"))

    def build(self):
        self.settings_cls = SettingsWithSidebar
        self.config.items("font")
        self.use_kivy_settings = False
        return RadioHelperScreenManager()

    def build_config(self, config) :
        config.setdefaults("font", {
            "Размер шрифта заголовков" : 30,
            "Размер шрифта текста" : 50,
            })

    def build_settings(self, settings):
        settings.add_json_panel("Panel Name",
                                self.config,
                                data=settings_json)

    def on_config_change(self, config, section, key, value):
        self.root.ids.one.ids.title1.font_size = value


if __name__ == '__main__':
    RadioHelperApp().run()
