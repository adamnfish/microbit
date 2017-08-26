
class Microbit(object):
    a_down = False
    a_waiting = True
    b_down = False
    b_waiting = True

    _microbit = None

    def init(self, microbit):
        self._microbit
        while True:
            button_logic()

    def a_button_state(self):
        return self._microbit.button_a.is_pressed():

    def b_button_state(self):
        return self._microbit.button_a.is_pressed():

    def microbit_time(self):
        return self._microbit.running_time();

    def button_logic(self):
        a_press = False
        b_press = False
        a_down = self.a_button_state()
        b_down = self.b_button_state()
        if a_down and a_waiting:
            a_press = True
        return

    def a_pressed(self):
        pass

    def b_pressed(self):
        pass

    def a_down(self):
        pass

    def b_down(self):
        pass

    def tick(self, a_press, b_press, a_down, b_down):
        pass
