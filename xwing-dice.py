import microbit
import random

class XwingDice(Microbit):
    blank = "00000:00000:00000:00000:00000"
    hit = "09990:" \
          "90009:" \
          "90009:" \
          "90009:" \
          "09990"
    crit = "09990:" \
           "97079:" \
           "90909:" \
           "97079:" \
           "09990"
    focus = "00000:" \
            "09990:" \
            "90709:" \
            "09990:" \
            "00000"
    evade = "00799:" \
            "90089:" \
            "00907:" \
            "09000:" \
            "90000"
    die_face = None
    roll_duration = 250
    show_duration = 2000
    roll_time = 0

    def a_pressed(self, time):
        """Attack die"""
        self.roll_time = time
        rnd = random.randint(1, 8)
        if rnd <= 2:
            self.die_face = self.blank
        elif rnd <= 4:
            self.die_face = self.focus
        elif rnd <= 7:
            self.die_face = self.hit
        elif rnd == 8:
            self.die_face = self.crit

    def b_pressed(self, time):
        """Defence die"""
        self.roll_time = time
        rnd = random.randint(1, 8)
        if rnd <= 3:
            self.die_face = self.blank
        elif rnd <= 5:
            self.die_face = self.focus
        elif rnd <= 8:
            self.die_face = self.evade

    def tick(self, time, a_pressed, b_pressed, a_down, b_down):
        if self.die_face:
            if time < self.roll_time + self.roll_duration:
                # rolling
                microbit.display.show(microbit.Image().fill(9))
            elif time < self.roll_time + self.show_duration:
                # show result
                microbit.display.show(microbit.Image(self.die_face))
            else:
                # reset
                microbit.display.show(microbit.Image())
                self.die_face = None
