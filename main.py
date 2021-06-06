import ResistorScreen
import CapacitorScreen

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty, DictProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.settings import SettingsWithSidebar
from kivy.config import Config
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget

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

    app_font_size = NumericProperty()
    app_header_size = NumericProperty()
    app_button_size = NumericProperty()


    def build(self):
        self.settings_cls = SettingsWithSidebar
        self.config.items("font")
        self.app_font_size = self.config.getint("font", "text_size")
        self.app_header_size = self.config.getint("font", "header_size")
        self.use_kivy_settings = False
        return RadioHelperScreenManager()

    def build_config(self, config):
        config.setdefaults("font", {
            "header_size": 30,
            "text_size": 30,
            "button_size": 30
        })

    def build_settings(self, settings):
        settings.add_json_panel("Размеры текста",
                                self.config,
                                data=settings_json)

    def on_config_change(self, config, section, key, value):
        config.set(section=section, option=key, value=value)
        config.write()
        self.app_font_size = self.config.getint("font", "text_size")
        self.app_header_size = self.config.getint("font", "header_size")


if __name__ == '__main__':
    RadioHelperApp().run()
