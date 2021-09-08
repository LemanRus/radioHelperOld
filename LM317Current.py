from kivy.uix.screenmanager import Screen
from StandardRows import StandardRows


class LM317Current(Screen):
    def calculate_lm317_current(self, iout, vout):
        try:
            iout = float(iout)

            r1 = 1.25 / iout

            r1_corrected = StandardRows.calculate_standard_resistor(r1, False)

            iout_corrected = 1.25 / r1_corrected

            if iout > 3:
                recommend = "LM338"
            elif iout > 1.5:
                recommend = "LM350"
            else:
                recommend = "LM317"

            if r1_corrected == 0:
                result_corrected = "0 Ом (перемычка)"
            elif r1_corrected < 1000:
                result_corrected = "{:g} Ом".format(r1_corrected)
            elif r1_corrected < 1000000:
                result_corrected = "{:g} кОм".format(r1_corrected / 1000)
            else:
                result_corrected = "{:g} МОм".format(r1_corrected / 1000000)

            power_r1 = iout_corrected ** 2 * r1_corrected
            if vout:
                vout = float(vout)
                vin_corrected = vout + 3.7
                self.ids.lm317_vin_output_cur.text = "{:g} А".format(vin_corrected)
            else:
                self.ids.lm317_vin_output_cur.text = ""

            self.ids.lm317_r1_output_cur.text = result_corrected
            self.ids.lm317_r1_power_output_cur.text = "{:g} Вт".format(power_r1)
            self.ids.lm317_iout_output_cur.text = "{:g} А".format(iout_corrected)
            self.ids.lm317_recommend_output_cur.text = recommend



        except Exception:
            self.ids.lm317_r1_output_cur.text = "Неверный ввод!"
            self.ids.lm317_r1_power_output_cur.text = "Неверный ввод!"
            self.ids.lm317_iout_output_cur.text = "Неверный ввод!"
            self.ids.lm317_recommend_output_cur.text = "Неверный ввод!"
            self.ids.lm317_vin_output_cur.text = "Неверный ввод!"


