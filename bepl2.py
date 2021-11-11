from dataclasses import dataclass
from math import ceil, floor

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
        print("rowcount:", self.rowcount)

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
            while k < self.ground.length:

                if self.startval > 0:
                    #print("startval", self.startval)
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
                else:
                    if self.ground.length - k > self.full_board.length:
                        #print("Addboard")
                        if self.lrow:
                            r.append(Board(pos=0,
                                           length=self.full_board.length,
                                           width=self.lastrow,
                                           thick=self.full_board.thick
                                           ))
                            k = k + self.full_board.length
                        else:
                            r.append(self.full_board)
                            k = k + self.full_board.length

                    else:
                        rst = self.ground.length - k
                        if self.lrow:
                            r.append(Board(length=rst,
                                           pos=1,
                                           width=self.lastrow,
                                           thick=self.full_board.thick
                                           ))
                        else:
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

                        self.startval = self.full_board.length -rst
                        k = k + rst
                        break
            return r

    def Rows(self):
        if self.ground.direction:
            for i in range(self.rowcount):
                if i == self.rowcount-1:
                    self.lrow = True
                row = self.FillRow()
                print("row", i)
                print(row)


def Main():
    g = Ground(length=2.00, width=2.40, direction=True)
    b = Board(pos=0, length=2.50, width=0.675, thick=0.015)
    c = Bepl(g, b)



Main()
