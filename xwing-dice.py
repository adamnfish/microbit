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

    def a_pressed(self, time):
        """Attack die"""
        rnd = random.randint(1, 8)
        if rnd <= 3:
            microbit.display.show(microbit.Image(self.blank))
        elif rnd == 4:
            microbit.display.show(microbit.Image(self.focus))
        elif rnd <= 7:
            microbit.display.show(microbit.Image(self.hit))
        elif rnd == 8:
            microbit.display.show(microbit.Image(self.crit))
    
    def b_pressed(self, time):
        """Defence die"""
        rnd = random.randint(1, 8)
        if rnd <= 4:
            microbit.display.show(microbit.Image(self.blank))
        elif rnd == 5:
            microbit.display.show(microbit.Image(self.focus))
        else:
            microbit.display.show(microbit.Image(self.evade))


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
