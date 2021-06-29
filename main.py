import ResistorScreen, CapacitorScreen, VoltageDividerCalculateScreen

from kivy.app import App

from kivy.lang import Builder

from kivy.properties import NumericProperty

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.settings import SettingsWithSidebar
from kivy.config import Config
from kivy.uix.spinner import Spinner, SpinnerOption


from settingsjson import settings_json

Config.read("radiohelper.ini")

#TODO: обход всех файлов в папке в цикле для загрузки - экономия строк кода
Builder.load_file("kv/radiohelper.kv")
Builder.load_file("kv/inductor_screen.kv")
Builder.load_file("kv/resistor_LED_screen.kv")
Builder.load_file("kv/main_screen.kv")
Builder.load_file("kv/nominals.kv")
Builder.load_file("kv/parallel_res_screen.kv")
Builder.load_file("kv/serial_cap_screen.kv")
Builder.load_file("kv/components_screen.kv")
Builder.load_file("kv/divider.kv")


class RadioHelperScreenManager(ScreenManager):
    pass


class MainScreen(Screen):
    pass


class NominalsScreen(Screen):
    pass


class ComponentsScreen(Screen):
    pass


class ResistorLEDCalculateScreen(Screen):
    pass


class InductorCalculateScreen(Screen):
    pass


class ParallelResistorCalculateScreen(Screen):
    pass


class SerialCapacitorCalculateScreen(Screen):
    pass


class LM317CalculateScreen(Screen):
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


class MySpinnerOption(SpinnerOption):
    colors = {"gold": [1, 0.84, 0, 1], "silver": [0.75, 0.75, 0.75, 1], "black": [0, 0, 0, 1],
              "brown": [0.4, 0.22, 0, 1], "red": [1, 0, 0, 1], "orange": [0.98, 0.45, 0.02, 1],
              "yellow": [1, 1, 0, 1], "green": [0.05, 0.64, 0.05, 1], "blue": [0.05, 0.54, 0.95, 1],
              "violet": [0.54, 0.14, 0.59, 1], "grey": [0.5, 0.5, 0.5, 1], "white": [1, 1, 1, 1]}


class RadioHelperApp(App):

    app_font_size = NumericProperty()
    app_header_size = NumericProperty()
    app_button_size = NumericProperty()

    def build(self):
        self.settings_cls = SettingsWithSidebar
        self.config.items("font")
        self.app_font_size = self.config.getint("font", "text_size")
        self.app_header_size = self.config.getint("font", "header_size")
        self.app_button_size = self.config.getint("font", "button_size")
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
        self.app_button_size = self.config.getint("font", "button_size")
        self.root.ids.resistor.build_resistor( self.root.ids.resistor.ids.main_spinner.text)


if __name__ == '__main__':
    RadioHelperApp().run()
