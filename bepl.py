from dataclasses import dataclass
from math import ceil
import argparse

@dataclass
class Board:
    pos: int
    length: float
    width: float
    thick: float


@dataclass
class Ground:
    length: float
    width: float
    direction: bool


class Bepl():
    def __init__(self, ground, board):
        self.ground = ground
        self.full_board = board
        self.startval = 0.00
        self.rows = []
        self.lrow = False
        self.RowCount()
        self.LastRow()
        self.RowCount()
        self.Rows()


    def RowCount(self):
        if self.ground.direction:
            self.rowcount = ceil(self.ground.width / self.full_board.width)
        else:
            self.rowcount = ceil(self.ground.length / self.full_board.width)

    def LastRow(self):
        if self.ground.direction:
            brds = (self.rowcount * self.full_board.width) - self.ground.width
        else:
            brds = (self.rowcount * self.full_board.width) - self.ground.length

        self.lastrow = self.full_board.width - brds

    def FillRow(self):
        if self.ground.direction:
            k = 0.00
            r = []
            length = self.ground.length
        else:
            k = 0.00
            r = []
            length = self.ground.width
        while k < length:
            if self.startval > 0:
                if self.lrow:
                    r.append(Board(length=self.startval,
                                   pos=1,
                                   width=self.lastrow,
                                   thick=self.full_board.thick
                                   ))
                else:
                    r.append(Board(length=self.startval,
                                   pos=1,
                                   width=self.full_board.width,
                                   thick=self.full_board.thick
                                   ))
                k = k + self.startval
                self.startval = 0.00
                continue
            else:
                if length - k > self.full_board.length:
                    if self.lrow:
                        r.append(Board(pos=0,
                                       length=self.full_board.length,
                                       width=self.lastrow,
                                       thick=self.full_board.thick
                                       ))
                        k = k + self.full_board.length
                        continue
                    else:
                        r.append(self.full_board)
                        k = k + self.full_board.length
                        continue
                else:
                    rst = length - k

                    if self.lrow:
                        r.append(Board(length=rst,
                                       pos=1,
                                       width=self.full_board.width,
                                       thick=self.full_board.thick
                                       ))
                    else:
                        r.append(Board(length=rst,
                                       pos=1,
                                       width=self.full_board.width,
                                       thick=self.full_board.thick
                                       ))

                    self.startval = self.full_board.length - rst
                    k = k + rst
                    
            return r

    def Rows(self):
        for i in range(self.rowcount):
            if i == self.rowcount-1:
                self.lrow = True
            self.rows.append(self.FillRow())

    def PrinBoards(self):
        for i in range(len(self.rows)):
            print("Reihe:", i+1)
            for j in range(len(self.rows[i])):
                print("%.3f" % self.rows[i][j].width, end="x")
                print("%.3f" % self.rows[i][j].length, end=" ")
            print()


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("Ground Size", metavar="n", type=float, nargs=2)

    args = parser.parse_args()
    print(args)

    g = Ground(length=6.20, width=2.40, direction=False)
    b = Board(pos=0, length=2.00, width=1.25, thick=0.015)
    c = Bepl(g, b)
    c.PrinBoards()




Main()
