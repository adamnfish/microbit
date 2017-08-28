import random
import microbit

class Dodge(Microbit):
    """
    random obstacles in every row, moving down one by one.
    Use a/b tomove light left and right to avoid them.
    """

    obstacle_row = False
    field = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    move_count = 0
    move_interval = 900
    difficulty = 21
    next_advance_time = 0
    player_column = 2
    alive = True

    def tick(self, time, a_press, b_press, a_down, b_down):
        if self.alive:
            if a_press:
                self.player_column = max(0, self.player_column - 1)
                self.check_death()
                self.display()
            if b_press:
                self.player_column = min(4, self.player_column + 1)
                self.check_death()
                self.display()
            if self.next_advance_time < time:
                self.difficulty = min(self.difficulty + 1, 99)
                self.move_interval = max(self.move_interval - 5, 400)
                self.advance()
                self.display()
                self.check_death()
                self.next_advance_time = time + self.move_interval
#        elif self.next_advance_time + 1500 < time:
#            microbit.display.show(microbit.Image.SKULL)
                
    def advance(self):
        if self.obstacle_row:
            next_row = self.generate_row()
        else:
            next_row = [False] * 5

        self.field[4] = self.field[3]
        self.field[3] = self.field[2]
        self.field[2] = self.field[1]
        self.field[1] = self.field[0]
        self.field[0] = next_row

        self.obstacle_row = not self.obstacle_row
        return

    def check_death(self):
        if self.field[4][self.player_column]:
            self.alive = False
        return

    def display(self):
        display_str = ""
        for row_index, row in enumerate(self.field):
            display_str += ":"
            for cell_index, cell in enumerate(row):
                if row_index == 4 and cell_index == self.player_column:
                    display_str += "9"
                elif cell:
                    display_str += "6"
                else:
                    display_str += "0"
        microbit.display.show(microbit.Image(display_str[1:]))
        return

    def generate_row(self):
        """
        Difficulty 1-99, randomnly produces 0 - 4 obstacles.
        """
        obstacle_count = int(random.randint(10, self.difficulty) / 20)
        row = []
        for i in range(0, 5):
            if i < obstacle_count:
                row.append(True)
            else:
                row.append(False)
        shuffled = []
        while len(row) > 0:
            shuffled.append(row.pop(random.randint(0, len(row) - 1)))
        return shuffled
