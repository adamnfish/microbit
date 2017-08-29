class TechnoTimer(Microbit):
    start_time = 0
    timing = False
    timer_length = 0

    def a_pressed(self, time):
        if self.timing:
            self.reset()
        else:
            self.start_timer(time, 30000)

    def b_pressed(self, time):
        if self.timing:
            self.reset()
        else:
            self.start_timer(time, 60000)

    def start_timer(self, time, timer_length):
        self.timing = True
        self.start_time = time
        self.timer_length = timer_length

    def reset(self):
        self.timing = False
        self.start_time = 0
        self.timer_length = 0
        microbit.display.show(microbit.Image())

    def tick(self, time, a_press, b_press, a_down, b_down):
        if self.timing:
            if time < self.start_time + self.timer_length:
                # show progress
                time_per_light = (self.timer_length) / 25
                lights_count = 25 - int((time - self.start_time) / time_per_light)
                microbit.display.show(microbit.Image(self.toDisplayString(lights_count)))
            elif time < self.start_time + self.timer_length + 2000:
                # show solid red for 1 second after timer finishes
                microbit.display.show(microbit.Image(self.SOLID))
            else:
                self.reset()

    def toDisplayString(self, n):
        ints = ("9" * n) + ("0" * (25 - n))
        coords = ""
        for (index, digit) in enumerate(ints):
            if (index) % 5 == 0 and index > 0:
                coords = coords + ":"
            coords = coords + digit
        return coords
