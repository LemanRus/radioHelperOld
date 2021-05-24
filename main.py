from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
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


class ResistorScreen(Screen):

    def calculate_resistor(self):
        band_list = ["first", "second"]
        resistance = 0
        tolerance = 0
        nominal = ("black", "brown", "red", "orange", "yellow", "green",
                   "blue", "violet", "grey", "white")
        for band in self.ids:
            if band in band_list:
                print(self.ids[band].text)
    def draw_bands(self):
        pass


class CapacitorScreen(Screen):
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
        self.settings_cls = SettingsWithSidebar
        self.config.items("font")
        self.use_kivy_settings = False
        return RadioHelperScreenManager()

    def build_config(self, config):
        config.setdefaults("font", {
            "Размер шрифта заголовков": 150,
            "Размер шрифта текста": 50,
        })

    def build_settings(self, settings):
        settings.add_json_panel("Panel Name",
                                self.config,
                                data=settings_json)

    def on_config_change(self, config, section, key, value):
        if key == "Размер шрифта заголовков":
            self.root.ids.one.ids.title1.font_size = value
        if key == "Размер шрифта текста":
            for up_id in self.root.ids:
                if up_id != 'title1':
                    for low_id in self.root.ids[up_id].ids:
                        self.root.ids[up_id].ids[low_id].font_size = value


if __name__ == '__main__':
    RadioHelperApp().run()
