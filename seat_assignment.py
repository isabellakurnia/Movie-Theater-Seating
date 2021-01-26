class Solution:
    def __init__(self):
        self.outputStr = ''
        self.rows = 'ACEGI'
        self.seats = [[i + str(j + 1) for j in range(20)] for i in self.rows]
        self.last = [0, 0]
        self.answers = []
        self.leftovers = []

    def read_write(self):
        filename_in = 'input.txt'
        filename_out = 'output.txt'
        with open(filename_in, 'r') as input:
            with open(filename_out, 'w') as output:
                line = input.readline()
                while line:
                    self.algo(line)
                    line = input.readline()
                output.write(self.outputStr)

    def algo(self, reservation):
        group = reservation.split(' ')
        group[1] = [int(i) for i in group[1].split() if i.isdigit()][0]

        # When there is enough seats for the group
        if self.last[1] <= 20 - group[1]:
            for i in range(group[1]):
                self.answers.append(self.seats[self.last[0]][self.last[1] + i])
            self.last[1] += group[1] + 3
            # When row can no longer be filled and there exist more rows
            if self.last[1] >= 20 and self.last[0] < 5:
                self.outputStr += group[0] + " " + ", ".join(self.answers) + "\n"
                self.last = [self.last[0] + 1, 0]
                self.leftovers.append(0)
            # When there does not exist more rows
            elif self.last[0] >= 5:
                self.leftovers.append(20 - self.last[1])

        # When there is not enough seats for the group and there exist more rows
        elif self.last[0] + 1 < 5:
            self.leftovers.append(20 - self.last[1])
            self.last = [self.last[0] + 1, 0]
            self.algo(reservation)
            return

        # When max capacity of theatre is filled and group cannot book tickets
        elif sum(self.leftovers) < group[1]:
            self.outputStr += group[0] + " Cinema is filled and cannot accept this group.\n"
            return

        # When all rows are filled but there exist leftover seats
        else:
            self.last = [20, 20]
            absolute_difference_function = lambda list_value : abs(list_value - group[1])
            closest_value = min(self.leftovers, key=absolute_difference_function)
            idx = self.leftovers.index(closest_value)
            self.leftovers[idx] -= closest_value - 3
            for i in range(closest_value):
                self.answers = [self.rows[idx] + str(20 - i)] + self.answers
            if group[1] - closest_value > 0:
                self.algo(group[0] + ' ' + str(group[1] - closest_value))
        if self.answers:
            self.outputStr += group[0] + " " + ", ".join(self.answers) + "\n"
        self.answers = []

object = Solution()
object.read_write()
