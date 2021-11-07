from dataclasses import dataclass
from math import ceil, floor


@dataclass
class Rect:
    length: float
    width: float


@dataclass
class Row:
    start: float
    full_b: int
    rst: float
    width: float


class Bepl():
    def __init__(self, surface, board, direction, dir_start):
        self.surface = surface
        self.board = board
        self.direction = direction
        self.rowcount: int
        self.lastrow: float
        self.rows = []
        self.RowCount()
        self.LastRow()
        self.dir_start = dir_start
        self.CalcRows()
        self.Print_Rows()

    def RowCount(self):
        if self.direction:
            raw = self.surface.width / self.board.width
            self.rowcount = ceil(raw)
        else:
            raw = self.surface.length / self.board.width
            self.rowcount = ceil(raw)

    def LastRow(self):
        if self.direction:
            raw = (self.rowcount * self.board.width) - self.surface.width
        else:
            raw = (self.rowcount * self.board.width) - self.surface.length
        self.lastrow = self.board.width - raw

    def CalcRows(self):
        if self.direction:
            self.Row_X()
        else:
            self.Row_Y()

    def Row_X(self):
        for i in range(self.rowcount):
            if len(self.rows) == 0:
                start = self.dir_start
            else:
                start = self.board.length - self.rows[i-1].rst
            length = self.surface.length - start
            b = length / self.board.length
            full_boards = floor(b)
            rest = length - (full_boards * self.board.length)
            if i == self.rowcount - 1:
                b_width = self.lastrow
                print(self.lastrow)
            else:
                b_width = self.board.width
            self.rows.append(Row(start=start,
                                 full_b=full_boards,
                                 rst=rest,
                                 width=b_width))

    def Row_Y(self):
        for i in range(self.rowcount):
            if len(self.rows) == 0:
                start = self.dir_start
            else:
                start = self.board.length - self.rows[i-1].rst
            length = self.surface.width - start
            b = length / self.board.length
            full_boards = floor(b)
            rest = length - (full_boards * self.board.length)
            if i == self.rowcount - 1:
                b_width = self.lastrow
                print(self.lastrow)
            else:
                b_width = self.board.width
            self.rows.append(Row(start=start,
                                 full_b=full_boards,
                                 rst=rest,
                                 width=b_width))

    def Print_Rows(self):
        for i in range(len(self.rows)):
            print(self.rows[i])


def Main():
    board = Rect(length=2.00, width=0.135)
    g_area = Rect(length=6.20, width=2.60)

    # If True == horizontal, If False == vertical
    _bepl = Bepl(surface=g_area, board=board, direction=False, dir_start=0.00)
    # print(_bepl.rows)
    # print(_bepl.lastrow)


Main()
