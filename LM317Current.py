from kivy.uix.screenmanager import Screen
from StandardRows import StandardRows


class LM317Current(Screen):
    def calculate_lm317_current(self, iout, vout):
        try:
            iout = float(iout)
            if iout <= 5:
                r1 = 1.25 / iout
                
                r1_corrected = StandardRows.calculate_standard_resistor(r1, True)
                
                if iout > 3:
                    recommend = "LM338"
                elif iout > 1.5:
                    recommend = "LM350"
                else:
                    recommend = "LM317"
                result = StandardRows.format_output_resistor(r1)
                result_corrected = StandardRows.format_output_resistor(r1_corrected)

                iout_corrected = 1.25 / r1_corrected

                power_r1 = iout ** 2 * r1
                power_corrected = iout_corrected ** 2 * r1_corrected

                if vout:
                    vout = float(vout)
                    if not (3 <= vout <= 38):
                        self.ids.lm317_vin_output_cur.text = "Падение напряжения должно быть больше 2В и меньше 38В!"
                    else:
                        vin_corrected = vout + 3.7
                        self.ids.lm317_vin_output_cur.text = "{:g} А".format(vin_corrected)
                else:
                    self.ids.lm317_vin_output_cur.text = ""
    
                self.ids.lm317_r1_output_cur.text = result
                self.ids.lm317_r1_corrected_output_cur.text = result_corrected
                self.ids.lm317_r1_power_output_cur.text = "{:g} Вт".format(power_r1)
                self.ids.lm317_r1_power_corrected_output_cur.text = "{:g} Вт".format(power_corrected)
                self.ids.lm317_iout_corrected_output_cur.text = "{:g} А".format(iout_corrected)
                self.ids.lm317_recommend_output_cur.text = recommend
            else:
                self.ids.lm317_r1_output_cur.text = "Ток должен быть менее 5А!"
                self.ids.lm317_r1_corrected_output_cur.text = ""
                self.ids.lm317_r1_power_output_cur.text = ""
                self.ids.lm317_r1_power_corrected_output_cur.text = ""
                self.ids.lm317_iout_corrected_output_cur.text = ""
                self.ids.lm317_recommend_output_cur.text = ""
                self.ids.lm317_vin_output_cur.text = ""

        except Exception:
            self.ids.lm317_r1_output_cur.text = "Неверный ввод!"
            self.ids.lm317_r1_corrected_output_cur.text = "Неверный ввод!"
            self.ids.lm317_r1_power_output_cur.text = "Неверный ввод!"
            self.ids.lm317_r1_power_corrected_output_cur.text = "Неверный ввод!"
            self.ids.lm317_iout_corrected_output_cur.text = "Неверный ввод!"
            self.ids.lm317_recommend_output_cur.text = "Неверный ввод!"
            self.ids.lm317_vin_output_cur.text = "Неверный ввод!"
