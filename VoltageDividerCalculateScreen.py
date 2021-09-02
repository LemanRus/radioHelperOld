from ResistorLEDCalculateScreen import ResistorLEDCalculateScreen
from kivy.uix.screenmanager import Screen


class VoltageDividerCalculateScreen(Screen):
    def divider_calculate_vout(self, vin, r1, r2):
        try:
            vin = float(vin)
            r1 = float(r1)
            r2 = float(r2)

            vout = r2 * vin / (r1 + r2)
            rate = vin / vout

            self.ids.v_out.text = "{:g}".format(vout)
            self.ids.divider_rate.text = "{:g}".format(rate)
        except Exception:
            self.ids.v_out.text = "Неверный ввод!"
            self.ids.divider_rate.text = ""

    def divider_calculate_r(self, vin, vout, r1):
        try:
            vin = float(vin)
            vout = float(vout)
            r1 = float(r1)

            if vin <= vout:
                self.ids.r2_calculated.text = "Проверьте напряжения!"
                self.ids.divider_rate_r.text = ""
            else:
                r2 = r1 * vout / (vin - vout)
                rate = vin / vout

                self.ids.r2_calculated.text = "{:g}".format(r2)
                if r2 == 0:
                    self.ids.r2_calculated.text = "0 Ом (перемычка)"
                elif r2 < 1000:
                    self.ids.r2_calculated.text = "{:g} Ом".format(r2)
                elif r2 < 1000000:
                    self.ids.r2_calculated.text = "{:g} кОм".format(r2 / 1000)
                else:
                    self.ids.r2_calculated.text = "{:g} МОм".format(r2 / 1000000)

                self.ids.divider_rate_r.text = "{:g}".format(rate)

                E6 = ResistorLEDCalculateScreen.E6
                # TODO сделать поиск стандартного резистора функцией класса приложения
                e6_test = r2
                while e6_test >= 10:
                    e6_test /= 10
                list_of_difs = [abs(e6_test - x) for x in E6]
                result_index = list_of_difs.index(min(list_of_difs))
                e6 = E6[result_index]
                interact = r2 / e6
                counter = 0
                while True:
                    if interact < 10:
                        break
                    counter += 1
                    interact /= 10
                e6_result = e6 * 10 ** counter
                if e6_result < r2:
                    e6_result = E6[result_index + 1] * 10 ** counter
                if e6_result == 0:
                    self.ids.r2_e24.text = "0 Ом (перемычка)"
                elif e6_result < 1000:
                    self.ids.r2_e24.text = "{:g} Ом".format(e6_result)
                elif e6_result < 1000000:
                    self.ids.r2_e24.text = "{:g} кОм".format(e6_result / 1000)
                else:
                    self.ids.r2_e24.text = "{:g} МОм".format(e6_result / 1000000)

                vout_corrected = e6_result * vin / (r1 + e6_result)
                self.ids.vout_e24.text = "{:g} В".format(vout_corrected)
        except (ZeroDivisionError, ValueError):
            self.ids.r2_calculated.text = "Неверный ввод!"
            self.ids.divider_rate_r.text = ""
