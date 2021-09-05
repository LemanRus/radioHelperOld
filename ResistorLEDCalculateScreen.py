from kivy.uix.screenmanager import Screen
from StandardRows import StandardRows


class ResistorLEDCalculateScreen(Screen):
    diodes = {'3 мм зелёный': (2.3, 20), '3 мм красный': (1.9, 20), '3 мм жёлтый': (2.1, 20), '3 мм синий': (2.9, 20),
              '5 мм зелёный': (2.3, 20), '5 мм красный': (1.9, 20), '5 мм жёлтый': (2.1, 20), '5 мм синий': (3.6, 75),
              '5 мм белый': (3.6, 75), '10 мм синий': (3.2, 20), '10 мм белый': (3.2, 20), 'Cree MX-3': (3.7, 350)}

    E6 = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8,
          7.5, 8.2, 9.1]  #todo e24!!!!!!!!!!

    def led_calculate(self, vol, led_vol, led_cur, led_quant):
        try:
            led_resistance = (float(vol) - (float(led_vol) * float(led_quant))) / (float(led_cur) / 1000)
            if led_resistance < 0:
                self.ids.led_result.text = "Слишком малое напряжение источника питания!"
                self.ids.led_res_power.text = ''
                self.ids.led_cur.text = ''
                self.ids.led_e24.text = ''
            else:
                if led_resistance == 0:
                    result = "0 Ом (перемычка)"
                elif led_resistance < 1000:
                    result = "{:g} Ом".format(led_resistance)
                elif led_resistance < 1000000:
                    result = "{:g} кОм".format(led_resistance / 1000)
                else:
                    result = "{:g} МОм".format(led_resistance / 1000000)
                self.ids.led_result.text = result
                e6_result = StandardRows.calculate_standard_resistor(led_resistance, True)
                if e6_result == 0:
                    self.ids.led_e24.text = "0 Ом (перемычка)"
                elif e6_result < 1000:
                    self.ids.led_e24.text = "{:g} Ом".format(e6_result)
                elif e6_result < 1000000:
                    self.ids.led_e24.text = "{:g} кОм".format(e6_result / 1000)
                else:
                    self.ids.led_e24.text = "{:g} МОм".format(e6_result / 1000000)
                self.ids.led_res_power.text = "{:g} мВт".format((float(vol) - float(led_vol)) * float(led_cur) * float(led_quant))
                self.ids.led_cur.text = "{:g} мА".format(float(led_cur) * float(led_quant))
        except ValueError:
            self.ids.led_e24.text = "Неверный ввод!"
