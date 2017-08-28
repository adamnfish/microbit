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
            "00499:" \
            "00907:" \
            "49400:" \
            "90000"
    die_face = None
    roll_duration = 250
    show_duration = 1500
    roll_time = 0
    
    def a_pressed(self, time):
        """Attack die"""
        self.roll_time = time
        rnd = random.randint(1, 8)
        if rnd <= 3:
            self.die_face = self.blank
        elif rnd == 4:
            self.die_face = self.focus
        elif rnd <= 7:
            self.die_face = self.hit
        elif rnd == 8:
            self.die_face = self.crit
    
    def b_pressed(self, time):
        """Defence die"""
        self.roll_time = time
        rnd = random.randint(1, 8)
        if rnd <= 4:
            self.die_face = self.blank
        elif rnd == 5:
            self.die_face = self.focus
        else:
            self.die_face = self.evade

    def tick(self, time, a_pressed, b_pressed, a_down, b_down):
        if self.die_face:
            if time < self.roll_time + self.roll_duration:
                # rolling
                microbit.display.show(mirobit.Image(self.SOLID))
            elif time < self.roll_time + self.show_duration:
                microbit.display.show(mirobit.Image(self.die_face))
            else:
                microbit.display.show(mirobit.Image())
                self.die_face = None
    pass



"""
HIT
09990
90009
90009
90009
09990

CRIT
09990
95059
90509
95059
09990

HiIT (ALT)
02020
24742
07070
24742
02020

CRIT (ALT)
02020
24742
07970
24742
02020

EVADE
00099
00159
00500
15100
50000

FOCUS
00000
09990
90509
09990
00000
"""
