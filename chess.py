board = [[0 for j in range(0, 8)] for i in range(0, 8)]

class Pieces:
    def __init__(self, typ, color, cur_pos):
        self.typ = typ
        self.color = color
        self.cur_pos = cur_pos
        board[cur_pos[0]][cur_pos[1]] = self
    def validate_movement(self, next_pos):
        if self.typ == 'pawn':
            if not self.cur_pos[1] - next_pos[1] in [1, 2]:
                return False
            elif not self.cur_pos[0] - next_pos[0] !=0:
                if not self.check_kill():
                    return False
    def is_block(self, next_pos):
        if self.typ == 'pawn':
            if board[next_pos[0]][next_pos[1]] != 0:
                return True
            else:
                return False
    def is_kill(self, next_pos):
        if self.typ == 'pawn':
            l = abs(next_pos[0] - self.cur_pos[0])
            if l == 0:
                return False
            b = abs(next_pos[1] - self.cur_pos[1])
            if b != 1:
                return False
            if not self.is_block(next_pos):
                return False
            return True
    def is_check(self, next_pos):
        p = board[next_pos[0]][next_pos[1]]
        if (p.typ == 'king') and (p.color != self.color):
            return True
        return True
                

p1 = Pieces("pawn", "black", [6, 1])

p1.is_block([6, 1])

p1.is_kill([7,2])