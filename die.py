import random
import microbit

class D6(Microbit):
    one = "00000:" \
          "00000:" \
          "00900:" \
          "00000:" \
          "00000"
    two = "90000:" \
          "00000:" \
          "00000:" \
          "00000:" \
          "00009"
    three = "90000:" \
            "00000:" \
            "00900:" \
            "00000:" \
            "00009"
    four = "90009:" \
           "00000:" \
           "00000:" \
           "00000:" \
           "90009"
    five = "90009:" \
           "00000:" \
           "00900:" \
           "00000:" \
           "90009"
    six = "90909:" \
          "00000:" \
          "00000:" \
          "00000:" \
          "90909"
    die_face = None
    roll_duration = 250
    show_duration = 2000
    roll_time = 0
    
    def a_pressed(self, time):
        """Attack die"""
        self.roll_time = time
        rnd = random.randint(1, 6)
        self.face(rnd)

    def b_pressed(self, time):
        """Defence die"""
        self.roll_time = time
        rnd = random.randint(1, 8)
        self.face(rnd)

    def face(self, rnd):
        if rnd == 1:
            self.die_face = self.one
        elif rnd == 2:
            self.die_face = self.two
        elif rnd == 3:
            self.die_face = self.three
        elif rnd == 4:
            self.die_face = self.four
        elif rnd == 5:
            self.die_face = self.five
        elif rnd == 6:
            self.die_face = self.six
            
    def tick(self, time, a_pressed, b_pressed, a_down, b_down):
        if self.die_face:
            if time < self.roll_time + self.roll_duration:
                # rolling
                microbit.display.show(microbit.Image(self.SOLID))
            elif time < self.roll_time + self.show_duration:
                # show result
                microbit.display.show(microbit.Image(self.die_face))
            else:
                # reset
                microbit.display.show(microbit.Image())
                self.die_face = None
