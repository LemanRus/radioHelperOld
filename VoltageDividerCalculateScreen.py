from kivy.lang import Builder
from kivy.properties import DictProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class VoltageDividerCalculateScreen(Screen):

    dynamic_vars = DictProperty({})


class DividerVoltageScreen(Screen):
    pass


class DividerResistanceScreen(Screen):
    pass
