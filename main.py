from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty, ObjectProperty
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
    nominal = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5,
               "blue": 6, "violet": 7, "grey": 8, "white": 9}
    multiplier = {"gold": 0.1, "silver": 0.01, "black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10000,
                  "green": 100000, "blue": 1000000, "violet": 10000000, "grey": 100000000}
    tolerance = {"gold": "±5%", "silver": "±10%", "black": "±0,005%", "brown": "±1%", "red": "±2%", "orange": "±0,01%",
                 "yellow": "±0,02%", "green": "±0,5%", "blue": "±0,25%", "violet": "±0,1%", "grey": "±0,05%"}

    def calculate_resistor(self, value):
        if value == "4":
            self.calculate_four_bands_resistor()
        elif value == "5":
            self.calculate_five_bands_resistor()

    def build_resistor(self, value):
        if value == "4":
            self.build_four_bands_resistor()
        elif value == "5":
            self.build_five_bands_resistor()

    def build_four_bands_resistor(self):
        self.ids.resistor_bands.clear_widgets()

        self.ids["resistor_bands"].add_widget(Spinner(
            text=list(self.nominal.keys())[1], values=list(self.nominal.keys())[1:],
        ))
        self.ids["resistor_bands"].add_widget(Widget(size_hint_x=0.2))

        self.ids["resistor_bands"].add_widget(Spinner(
            text=list(self.nominal.keys())[0], values=self.nominal.keys()))
        self.ids["resistor_bands"].add_widget(Widget(size_hint_x=0.2))

        self.ids["resistor_bands"].add_widget(Spinner(
            text=list(self.multiplier.keys())[0], values=self.multiplier.keys()))
        self.ids["resistor_bands"].add_widget(Widget(size_hint_x=0.2))

        self.ids["resistor_bands"].add_widget(Spinner(
            text=list(self.tolerance.keys())[0], values=self.tolerance.keys()))

    def build_five_bands_resistor(self):
        self.ids.resistor_bands.clear_widgets()

        self.ids["resistor_bands"].add_widget(Spinner(
            text=list(self.nominal.keys())[1], values=list(self.nominal.keys())[1:],
        ))
        self.ids["resistor_bands"].add_widget(Widget(size_hint_x=0.2))

        self.ids["resistor_bands"].add_widget(Spinner(
            text=list(self.nominal.keys())[0], values=self.nominal.keys()))
        self.ids["resistor_bands"].add_widget(Widget(size_hint_x=0.2))

        self.ids["resistor_bands"].add_widget(Spinner(
            text=list(self.nominal.keys())[0], values=self.nominal.keys()))
        self.ids["resistor_bands"].add_widget(Widget(size_hint_x=0.2))

        self.ids["resistor_bands"].add_widget(Spinner(
            text=list(self.multiplier.keys())[0], values=self.multiplier.keys()))
        self.ids["resistor_bands"].add_widget(Widget(size_hint_x=0.2))

        self.ids["resistor_bands"].add_widget(Spinner(
            text=list(self.tolerance.keys())[0], values=self.tolerance.keys()))

    def calculate_four_bands_resistor(self):
        resistance = (self.nominal[self.ids.resistor_bands.children[6].text] * 10 +
                      self.nominal[self.ids.resistor_bands.children[4].text]) * \
                      self.multiplier[self.ids.resistor_bands.children[2].text]

        tolerance = self.tolerance[self.ids.resistor_bands.children[0].text]
        if resistance < 1000:
            self.ids.resistance.text = "{} {}".format(resistance, tolerance)
        elif resistance < 1000000:
            self.ids.resistance.text = "{:.0f} кОм {}".format(resistance / 1000, tolerance)
        else:
            self.ids.resistance.text = "{:.0f} МОм {}".format(resistance / 1000000, tolerance)

    def calculate_five_bands_resistor(self):
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
