import microbit


class Microbit(object):
    _a_down = False
    _a_waiting = True
    _b_down = False
    _b_waiting = True

    _running = True

    _get_time = None
    _get_a_pressed = None
    _get_b_pressed = None

    def __init__(self, get_time, get_a_pressed, get_b_pressed):
        """
        Create instance and provide getters for microbit information.
        These functions should take no arguments and return an Int (time),
        or Booleans (button states).
        """
        self._get_time = get_time
        self._get_a_pressed = get_a_pressed
        self._get_b_pressed = get_b_pressed
        return

    def start(self):
        while self._running:
            self._logic()
        return

    def stop(self):
        self._running = False
        return

    def _logic(self):
        a_press = False
        b_press = False

        # ask device for state
        time = self._get_time()
        self._a_down = self._get_a_pressed()
        self._b_down = self._get_b_pressed()

        # detect button presses
        if self._a_down:
            if self._a_waiting:
                a_press = True
                self._a_waiting = False
        else:
            self._a_waiting = True
        if self._b_down:
            if self._b_waiting:
                b_press = True
                self._b_waiting = False
        else:
            self._b_waiting = True

        # run program according to calculated state
        if a_press:
            self.a_pressed(time)
        if b_press:
            self.b_pressed(time)
        self.tick(time, a_press, b_press, self._a_down, self._b_down)

        return

    # implement these to write microbit program
    def a_pressed(self, time):
        pass

    def b_pressed(self, time):
        pass

    def tick(self, time, a_press, b_press, a_down, b_down):
        pass

    pass

def get_time():
    return microbit.running_time()

def get_a_pressed():
    return microbit.button_a.is_pressed()

def get_b_pressed():
    return microbit.button_b.is_pressed()
