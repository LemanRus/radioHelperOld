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


class ResistorScreen(Screen):
    dynamic_vars = DictProperty({})

    nominal = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5,
               "blue": 6, "violet": 7, "grey": 8, "white": 9}
    multiplier = {"gold": 0.1, "silver": 0.01, "black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10000,
                  "green": 100000, "blue": 1000000, "violet": 10000000, "grey": 100000000}
    tolerance = {"gold": "±5%", "silver": "±10%", "black": "±0,005%", "brown": "±1%", "red": "±2%", "orange": "±0,01%",
                 "yellow": "±0,02%", "green": "±0,5%", "blue": "±0,25%", "violet": "±0,1%", "grey": "±0,05%"}
    thermal = {"gold": "±500 ppm/°С", "silver": "±1000 ppm/°С", "brown": "±100 ppm/°С", "red": "±50 ppm/°С",
               "orange": "±15 ppm/°С", "yellow": "±25 ppm/°С", "blue": "±10 ppm/°С", "violet": "±5 ppm/°С",
               "white": "±1 ppm/°С"}
    colors = {"gold": [1, 0.84, 0, 1], "silver": [0.75, 0.75, 0.75, 1], "black": [0, 0, 0, 1],
              "brown": [0.4, 0.22, 0, 1], "red": [1, 0, 0, 1], "orange": [0.98, 0.45, 0.02, 1],
              "yellow": [1, 1, 0, 1], "green": [0.05, 0.64, 0.05, 1], "blue": [0.05, 0.54, 0.95, 1],
              "violet": [0.54, 0.14, 0.59, 1], "grey": [0.5, 0.5, 0.5, 1], "white": [1, 1, 1, 1]}

    def select_color(self):
        pass

    def calculate_resistor(self, value):

        thermal = False

        if "band5" in self.dynamic_vars.keys():
            thermal = self.thermal[self.dynamic_vars["band5"].text]
        if "band4" in self.dynamic_vars.keys():
            tolerance = self.tolerance[self.dynamic_vars["band4"].text]
        if len(self.ids["resistor_bands"].children) == 5 or len(self.ids["resistor_bands"].children) == 7:
            multiplier = self.multiplier[self.dynamic_vars["band2"].text]
            resistance = (self.nominal[self.dynamic_vars["band0"].text] * 10 + \
                         self.nominal[self.dynamic_vars["band1"].text]) * multiplier

            if "band3" in self.dynamic_vars.keys():
                tolerance = self.tolerance[self.dynamic_vars["band3"].text]
            else:
                tolerance = "±20%"
        else:
            multiplier = self.multiplier[self.dynamic_vars["band3"].text]
            resistance = (self.nominal[self.dynamic_vars["band0"].text] * 100 + \
                         self.nominal[self.dynamic_vars["band1"].text] * 10 + \
                          self.nominal[self.dynamic_vars["band1"].text]) * multiplier

        if resistance < 1000:
            self.ids.resistance.text = "{:g} Ом {}{}".format(resistance, tolerance, (", ТКС: " + thermal) if thermal else "")
        elif resistance < 1000000:
            self.ids.resistance.text = "{:g} кОм {}{}".format(resistance / 1000, tolerance, (", ТКС: " + thermal) if thermal else "")
        else:
            self.ids.resistance.text = "{:g} МОм {}{}".format(resistance / 1000000, tolerance, (", ТКС: " + thermal) if thermal else "")

    def build_resistor(self, value):
        bands = {3: {0: list(self.nominal.keys())[1:], 1: list(self.nominal.keys()), 2: list(self.multiplier.keys())},
                 4: {0: list(self.nominal.keys())[1:], 1: list(self.nominal.keys()), 2: list(self.multiplier.keys()),
                     3: list(self.tolerance.keys())},
                 5: {0: list(self.nominal.keys())[1:], 1: list(self.nominal.keys()), 2: list(self.nominal.keys()),
                     3: list(self.multiplier.keys()), 4: list(self.tolerance.keys())},
                 6: {0: list(self.nominal.keys())[1:], 1: list(self.nominal.keys()), 2: list(self.nominal.keys()),
                     3: list(self.multiplier.keys()), 4: list(self.tolerance.keys()), 5: list(self.thermal.keys())},
                 }

        self.ids.resistor_bands.clear_widgets()
        self.dynamic_vars.clear()

        for bands_qty in range(0, int(value)):
            try:
                self.dynamic_vars["band{}".format(bands_qty)] = Spinner(text=bands[int(value)][bands_qty][0],
                                                                        values=list(bands[int(value)][bands_qty]),
                                                                        background_color=self.colors[bands[int(value)][bands_qty][0]])
                self.ids["resistor_bands"].add_widget(self.dynamic_vars["band{}".format(bands_qty)])
                for key, band in self.dynamic_vars.items():
                    if key.startswith("band"):
                        band.bind(text=self.colourize)
                if bands_qty < int(value) - 1:
                    self.dynamic_vars["gap{}".format(bands_qty)] = Widget(size_hint_x=0.2)
                    self.ids["resistor_bands"].add_widget(self.dynamic_vars["gap{}".format(bands_qty)])
            except KeyError:
                continue

    def colourize(self, *args):
        for key, band in self.dynamic_vars.items():
            if key.startswith("band"):
                band.background_color = self.colors[band.text]


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
            "header_size": 150,
            "text_size": 50,
        })

    def build_settings(self, settings):
        settings.add_json_panel("Panel Name",
                                self.config,
                                data=settings_json)

    def on_config_change(self, config, section, key, value):
        if key == "header_size":
            self.root.ids.one.ids.title1.font_size = value
        if key == "text_size":
            for up_id in self.root.ids:
                if up_id != 'title1':
                    for low_id in self.root.ids[up_id].ids:
                        self.root.ids[up_id].ids[low_id].font_size = value


if __name__ == '__main__':
    RadioHelperApp().run()
