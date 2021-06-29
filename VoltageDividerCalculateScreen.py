from kivy.lang import Builder
from kivy.properties import DictProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class VoltageDividerCalculateScreen(Screen):

    dynamic_vars = DictProperty({})

    def build_divider(self, choose):
        """self.ids.divider_box.clear_widgets()
        if choose == "Расчёт выходного напряжения":
            self.ids.divider_box.add_widget(Label(text="TESTTESTTESTTEST"))
        elif choose == "Расчёт сопротивления":
            print("EGGS")"""

        if choose == "Расчёт выходного напряжения":
            Builder.load_file("kv/test.kv")
        else:
            self.ids.divider_box.clear_widgets()

class DividerBox(BoxLayout):
    pass