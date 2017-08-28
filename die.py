class XwingDice(Microbit):
    one = "00000:" \
          "00000:" \
          "00900:" \
          "00000:" \
          "00090"
    two = "00000:" \
          "09000:" \
          "00000:" \
          "00090:" \
          "00000"
    three = "90000:" \
            "00000:" \
            "00900:" \
            "00000:" \
            "00009"
    four = "00009:" \
           "09090:" \
           "00000:" \
           "09090:" \
           "00000"
    five = "90009:" \
           "00000:" \
           "00900:" \
           "00000:" \
           "90009"
    six = "00000:" \
          "90909:" \
          "00000:" \
          "90909:" \
          "00000"
    die_face = None
    roll_duration = 250
    show_duration = 1500
    roll_time = 0
    
    def a_pressed(self, time):
        """Attack die"""
        self.roll_time = time
        rnd = random.randint(1, 6)
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

    def b_pressed(self, time):
        """Defence die"""
        self.roll_time = time
        rnd = random.randint(1, 8)
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
                microbit.display.show(mirobit.Image(self.SOLID))
            elif time < self.roll_time + self.show_duration:
                microbit.display.show(mirobit.Image(self.die_face))
            else:
                microbit.display.show(mirobit.Image())
                self.die_face = None
    pass
