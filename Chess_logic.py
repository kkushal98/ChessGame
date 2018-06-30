class ChessBoard():
    def __init__(self):
        self.board=self.new_board()
    def new_board(self):
        board=[]
        for row in range(8):
            rows=[]
            for column in range(8):
                if row==1:
                    # Adding a white pawns
                    rows.append('WP')
                elif row==6:
                    # Adding Black pawns
                    rows.append('BP')
                elif (row==0 and column==1) or (row==0 and column==6):
                    # Adding White Horse
                    rows.append('WH')
                elif (row == 7 and column == 1) or (row == 7 and column == 6):
                    # Adding White Horse
                    rows.append('BH')
                elif (row==0 and column==0) or (row==0 and column==7):
                    # Adding White Rook
                    rows.append('WR')
                elif (row == 7 and column == 0) or (row == 7and column == 7):
                    # Adding White Horse
                    rows.append('BR')
                elif (row == 0 and column == 2) or (row == 0 and column == 5):
                    # Adding White Horse
                    rows.append('WB')
                elif (row == 7 and column == 2) or (row == 7 and column == 5):
                    # Adding White Horse
                    rows.append('BB')
                elif (row == 0 and column == 3):
                    # Adding White Horse
                    rows.append('WQ')
                elif (row == 7 and column == 3):
                    # Adding White Horse
                    rows.append('BQ')
                elif (row == 0 and column == 4):
                    # Adding White Horse
                    rows.append('WK')
                elif(row==7 and column==4):
                    rows.append('BK')

                else:
                    rows.append('.')
            board.append(rows)
        return board
    def print_board(self):
        print(self.board)/'.'

class Horse():
    def __init__(self,board):
        # ChessBoard.__init__(self)
        self.board=board
        self.x_coordinate=0
        self.y_coordinate=0
    def white_horse_coordinate(self):
        self.white_horse_coordinates=[]
        for row in range(8):
            for column in range(8):
                if self.board[row][column]=='WH':
                    self.white_horse_coordinates.append((row,column))
        return self.white_horse_coordinates
    def black_horse_coordinate(self):
        self.black_horse_coordinates=[]
        for row in range(8):
            for column in range(8):
                if self.board[row][column]=='BH':
                    self.black_horse_coordinates.append((row,column))
        return self.black_horse_coordinates

    def possible_moves_white(self):
        self.c=dict()
        for row,column in self.white_horse_coordinate():
            self.possible_white_coordinates = []
            try:
                if (row+2<=7 and column+1<=7) and self.board[row+2][column+1][0]!='W':
                    self.possible_white_coordinates.append((row+2,column+1))
                if (row+2<=7 and column-1>=0) and self.board[row+2][column-1][0]!='W':
                    self.possible_white_coordinates.append((row+2,column-1))
                if (row+1<=7 and column+2<=7) and self.board[row+1][column+2][0]!='W':
                    self.possible_white_coordinates.append((row+1,column+2))
                if (row+1<=7 and column-2>=0) and self.board[row+1][column-2][0]!='W':
                    self.possible_white_coordinates.append((row+1,column-2))
                if (row-2>=0 and column-1>=0) and self.board[row-2][column-1][0]!='W':
                    self.possible_white_coordinates.append((row-2,column-1))
                if (row-2>=0 and column+1<=7) and self.board[row-2][column+1][0]!='W':
                    self.possible_white_coordinates.append((row - 2, column + 1))
                if (row-1>=0 and column-2>=0) and self.board[row-1][column-2][0]!='W':
                    self.possible_white_coordinates.append((row-1,column-2))
                if (row - 1 >= 0 and column + 2<= 7) and self.board[row - 1][column - 2][0] != 'W':
                    self.possible_white_coordinates.append((row - 1, column + 2))
            except IndexError:
                pass

            self.c[(row, column)] = self.possible_white_coordinates
        return self.c

    def possible_moves_black(self):
        self.c=dict()
        for row,column in self.black_horse_coordinate():
            self.possible_black_coordinates = []
            if (row + 2 <= 7 and column + 1 <= 7) and self.board[row + 2][column + 1][0] != 'B':
                self.possible_black_coordinates.append((row + 2, column + 1))
            if (row + 2 <= 7 and column - 1 >= 0) and self.board[row + 2][column - 1][0] != 'B':
                self.possible_black_coordinates.append((row + 2, column - 1))
            if (row + 1 <= 7 and column + 2 <= 7) and self.board[row + 1][column + 2][0] != 'B':
                self.possible_black_coordinates.append((row + 1, column + 2))
            if (row + 1 <= 7 and column - 2 >= 0) and self.board[row + 1][column - 2][0] != 'B':
                self.possible_black_coordinates.append((row + 1, column - 2))
            if (row - 2 >= 0 and column - 1 >= 0) and self.board[row - 2][column - 1][0] != 'B':
                self.possible_black_coordinates.append((row - 2, column - 1))
            if (row - 2 >= 0 and column + 1 <= 7) and self.board[row - 2][column + 1][0] != 'B':
                self.possible_black_coordinates.append((row - 2, column + 1))
            if (row - 1 >= 0 and column - 2 >= 0) and self.board[row - 1][column - 2][0] != 'B':
                self.possible_black_coordinates.append((row - 1, column - 2))
            if (row - 1 >= 0 and column + 2 <= 7) and self.board[row - 1][column - 2][0] != 'B':
                self.possible_black_coordinates.append((row - 1, column + 2))
            self.c[(row,column)]=self.possible_black_coordinates

        return self.c
    def move_Knight(self,turn):

        while True:

                try:
                    print('Enter the x and y coordinate for Knight')
                    self.x_coordinate=int(input())
                    self.y_coordinate = int(input())
                    if turn=='W':
                        for key,values in self.possible_moves_white().items():
                            if (self.x_coordinate,self.y_coordinate) in values:
                                self.board[self.x_coordinate][self.y_coordinate]='WH'
                                self.board[key[0]][key[1]]='.'
                                print(values)
                                print(key)

                                break
                        else:
                            print('Not a valid move')
                        break
                    elif turn=='B':
                        for key, values in self.possible_moves_black().items():
                            if (self.x_coordinate, self.y_coordinate) in values:
                                self.board[self.x_coordinate][self.y_coordinate] = 'BH'
                                self.board[key[0]][key[1]] = '.'
                                print(values)
                                print(key)

                                break
                        else:
                            print('Not a valid move')
                        break
                except:
                    pass

class Rook():
    def __init__(self,board):
        self.board=board
        self.x_coordinate=0
        self.y_coordinate=0
        # ChessBoard.__init__(self)
    def white_rook_coordinate(self):
        self.white_rook_coordinates=[]
        for row in range(8):
            for column in range(8):
                if self.board[row][column]=='WR':
                    self.white_rook_coordinates.append((row,column))
        return self.white_rook_coordinates
    def black_rook_coordinate(self):
        self.black_rook_coordinates=[]
        for row in range(8):
            for column in range(8):
                if self.board[row][column]=='BR':
                    self.black_rook_coordinates.append((row,column))
        return self.black_rook_coordinates
    def possible_moves_white_rook(self):
        self.c=dict()
        for row, column in self.white_rook_coordinate():
            self.possible_white_coordinates=[]
            a = row + 1
            b = column
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == "."):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a + 1][b][0] == "B":
                        self.possible_white_coordinates.append((a + 1, b))
                except IndexError:
                    pass
                a += 1
            a = row
            b = column+1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == "."):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a][b+1][0] == "B":
                        self.possible_white_coordinates.append((a, b+1))
                except IndexError:
                    pass
                b+= 1
            a = row-1
            b = column
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == "."):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a-1][b][0] == "B":
                        self.possible_white_coordinates.append((a-1, b))
                except IndexError:
                    pass
                a -= 1
            a = row
            b = column-1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == "."):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a][b-1][0] == "B":
                        self.possible_white_coordinates.append((a, b-1))
                except IndexError:
                    pass
                b -= 1

            self.c[(row, column)] = self.possible_white_coordinates

        return self.c

    def possible_moves_black_rook(self):
        self.c=dict()
        for row, column in self.black_rook_coordinate():
            self.possible_black_coordinates = []
            a = row + 1
            b = column
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == "."):
                self.possible_black_coordinates.append((a, b))
                try:
                    if self.board[a + 1][b][0] == "W":
                        self.possible_black_coordinates.append((a + 1, b))
                except IndexError:
                    pass
                a += 1
            a = row
            b = column + 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == "."):
                self.possible_black_coordinates.append((a, b))
                try:
                    if self.board[a][b + 1][0] == "W":
                        self.possible_black_coordinates.append((a, b + 1))
                except IndexError:
                    pass
                b += 1
            a = row - 1
            b = column
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == "."):
                self.possible_black_coordinates.append((a, b))
                try:
                    if self.board[a - 1][b][0] == "W":
                        self.possible_black_coordinates.append((a - 1, b))
                except IndexError:
                    pass
                a -= 1
            a = row
            b = column - 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == "."):
                self.possible_black_coordinates.append((a, b))
                try:
                    if self.board[a][b - 1][0] == "W":
                        self.possible_black_coordinates.append((a, b - 1))
                except IndexError:
                    pass
                b -= 1
            self.c[(row, column)] = self.possible_black_coordinates

        return self.c
    def move_Rook(self,turn):
        while True:

                try:
                    # print('Enter the x and y coordinate for Knight')
                    self.x_coordinate=int(input('Enter x coordinate for Rook').strip())
                    self.y_coordinate = int(input('Enter y coordinate for Rook').strip())
                    if turn=='W':
                        for key,values in self.possible_moves_white_rook().items():
                            if (self.x_coordinate,self.y_coordinate) in values:
                                self.board[self.x_coordinate][self.y_coordinate]='WR'
                                self.board[key[0]][key[1]]='.'
                                print(values)
                                print(key)

                                break
                        else:
                            print('Not a valid move')
                        break
                    elif turn=='B':
                        for key, values in self.possible_moves_black_rook().items():
                            if (self.x_coordinate, self.y_coordinate) in values:
                                self.board[self.x_coordinate][self.y_coordinate] = 'BR'
                                self.board[key[0]][key[1]] = '.'
                                print(values)
                                print(key)

                                break
                        else:
                            print('Not a valid move')
                        break
                except:
                    pass
class Bishop():
    def __init__(self,board):
        self.board=board
        self.x_coordinate=0
        self.y_coordinate=0
        # ChessBoard.__init__(self)
    def white_bishop_coordinate(self):
        self.white_bishop_coordinates=[]
        for row in range(8):
            for column in range(8):
                if self.board[row][column]=='WB':
                    self.white_bishop_coordinates.append((row,column))
        return self.white_bishop_coordinates
    def black_bishop_coordinate(self):
        self.black_bishop_coordinates=[]
        for row in range(8):
            for column in range(8):
                if self.board[row][column]=='BB':
                    self.black_bishop_coordinates.append((row,column))
        return self.black_bishop_coordinates

    def possible_moves_white_bishop(self):
        self.c=dict()
        for row, column in self.white_bishop_coordinate():
            self.possible_white_coordinates = []
            a=row+1
            b=column+1
            while (7>=a>=0 and 7>=b>=0) and (self.board[a][b]=='.'):
                self.possible_white_coordinates.append((a,b))
                try:
                    if self.board[a+1][b+1][0]=='B':
                        self.possible_white_coordinates.append((a+1,b+1))
                except IndexError:
                    pass

                a+=1
                b+=1
            a = row + 1
            b = column - 1
            while (7>=a>=0 and 7>=b>=0) and (self.board[a][b]=='.'):
                self.possible_white_coordinates.append((a,b))
                try:
                    if self.board[a+1][b-1][0]=='B':
                        self.possible_white_coordinates.append((a+1,b-1))
                except IndexError:
                    pass

                a+=1
                b-=1
            a = row - 1
            b = column + 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == '.'):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a -1][b + 1][0] == 'B':
                        self.possible_white_coordinates.append((a - 1, b + 1))
                except IndexError:
                    pass

                a -= 1
                b += 1
            a = row - 1
            b = column- 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == '.'):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a - 1][b - 1][0] == 'B':
                        self.possible_white_coordinates.append((a - 1, b - 1))
                except IndexError:
                    pass

                a -= 1
                b -= 1

            self.c[(row, column)] = self.possible_white_coordinates
        return self.c

    def possible_moves_black_bishop(self):
        self.c = dict()
        for row, column in self.black_bishop_coordinate():
            self.possible_black_coordinates = []
            a = row + 1
            b = column + 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == '.'):
                self.possible_black_coordinates.append((a, b))
                try:
                    if self.board[a + 1][b + 1][0] == 'W':
                        self.possible_black_coordinates.append((a + 1, b + 1))
                except IndexError:
                    pass

                a += 1
                b += 1
            a = row + 1
            b = column - 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == '.'):
                self.possible_black_coordinates.append((a, b))
                try:
                    if self.board[a + 1][b - 1][0] == 'W':
                        self.possible_black_coordinates.append((a + 1, b - 1))
                except IndexError:
                    pass

                a += 1
                b -= 1
            a = row - 1
            b = column + 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == '.'):
                self.possible_black_coordinates.append((a, b))
                try:
                    if self.board[a - 1][b + 1][0] == 'W':
                        self.possible_black_coordinates.append((a - 1, b + 1))
                except IndexError:
                    pass

                a -= 1
                b += 1
            a = row - 1
            b = column - 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == '.'):
                self.possible_black_coordinates.append((a, b))
                try:
                    if self.board[a - 1][b - 1][0] == 'W':
                        self.possible_black_coordinates.append((a - 1, b - 1))
                except IndexError:
                    pass

                a -= 1
                b -= 1

            self.c[(row, column)] = self.possible_black_coordinates
        return self.c
    def move_Bishop(self,turn):
        while True:

                try:
                    # print('Enter the x and y coordinate for Knight')
                    self.x_coordinate=int(input('Enter x coordinate for Bishop').strip())
                    self.y_coordinate = int(input('Enter y coordinate for Bishop').strip())
                    if turn=='W':
                        for key,values in self.possible_moves_white_bishop().items():
                            if (self.x_coordinate,self.y_coordinate) in values:
                                self.board[self.x_coordinate][self.y_coordinate]='WB'
                                self.board[key[0]][key[1]]='.'
                                print(values)
                                print(key)

                                break
                        else:
                            print('Not a valid move')
                        break
                    elif turn=='B':
                        for key, values in self.possible_moves_black_bishop().items():
                            if (self.x_coordinate, self.y_coordinate) in values:
                                self.board[self.x_coordinate][self.y_coordinate] = 'BB'
                                self.board[key[0]][key[1]] = '.'
                                print(values)
                                print(key)

                                break
                        else:
                            print('Not a valid move')
                        break
                except:
                    pass

class Queen():
    def __init__(self,board):
        # ChessBoard.__init__(self)
        self.board=board
        self.x_coordinate=0
        self.y_coordinate=0

    def white_queen_coordinate(self):
        self.white_queen_coordinates = []
        for row in range(8):
            for column in range(8):
                if self.board[row][column] == 'WQ':
                    self.white_queen_coordinates.append((row, column))
        return self.white_queen_coordinates

    def black_queen_coordinate(self):
        self.black_queen_coordinates = []
        for row in range(8):
            for column in range(8):
                if self.board[row][column] == 'BQ':
                    self.black_queen_coordinates.append((row, column))
        return self.black_queen_coordinates
    def possible_moves_queen_white(self):
        self.c=dict()
        for row,column in self.white_queen_coordinate():
            self.possible_white_coordinates=[]
            a = row + 1
            b = column + 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == '.'):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a + 1][b + 1][0] == 'B':
                        self.possible_white_coordinates.append((a + 1, b + 1))
                except IndexError:
                    pass

                a += 1
                b += 1
            a = row + 1
            b = column - 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == '.'):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a + 1][b - 1][0] == 'B':
                        self.possible_white_coordinates.append((a + 1, b - 1))
                except IndexError:
                    pass

                a += 1
                b -= 1
            a = row - 1
            b = column + 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == '.'):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a - 1][b + 1][0] == 'B':
                        self.possible_white_coordinates.append((a - 1, b + 1))
                except IndexError:
                    pass

                a -= 1
                b += 1
            a = row - 1
            b = column - 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == '.'):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a - 1][b - 1][0] == 'B':
                        self.possible_white_coordinates.append((a - 1, b - 1))
                except IndexError:
                    pass

                a -= 1
                b -= 1
            a = row + 1
            b = column
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == "."):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a + 1][b][0] == "B":
                        self.possible_white_coordinates.append((a + 1, b))
                except IndexError:
                    pass
                a += 1
            a = row
            b = column + 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == "."):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a][b + 1][0] == "B":
                        self.possible_white_coordinates.append((a, b + 1))
                except IndexError:
                    pass
                b += 1
            a = row - 1
            b = column
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == "."):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a - 1][b][0] == "B":
                        self.possible_white_coordinates.append((a - 1, b))
                except IndexError:
                    pass
                a -= 1
            a = row
            b = column - 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == "."):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a][b - 1][0] == "B":
                        self.possible_white_coordinates.append((a, b - 1))
                except IndexError:
                    pass
                b -= 1

            self.c[(row, column)] = self.possible_white_coordinates
        return self.c

    def possible_moves_queen_black(self):

        self.c = dict()
        for row, column in self.black_queen_coordinate():
            self.possible_black_coordinates = []
            a = row + 1
            b = column + 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == '.'):
                self.possible_black_coordinates.append((a, b))
                try:
                    if self.board[a + 1][b + 1][0] == 'B':
                        self.possible_black_coordinates.append((a + 1, b + 1))
                except IndexError:
                    pass

                a += 1
                b += 1
            a = row + 1
            b = column - 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == '.'):
                self.possible_black_coordinates.append((a, b))
                try:
                    if self.board[a + 1][b - 1][0] == 'B':
                        self.possible_black_coordinates.append((a + 1, b - 1))
                except IndexError:
                    pass

                a += 1
                b -= 1
            a = row - 1
            b = column + 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == '.'):
                self.possible_black_coordinates.append((a, b))
                try:
                    if self.board[a - 1][b + 1][0] == 'B':
                        self.possible_black_coordinates.append((a - 1, b + 1))
                except IndexError:
                    pass

                a -= 1
                b += 1
            a = row - 1
            b = column - 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == '.'):
                self.possible_black_coordinates.append((a, b))
                try:
                    if self.board[a - 1][b - 1][0] == 'B':
                        self.possible_black_coordinates.append((a - 1, b - 1))
                except IndexError:
                    pass

                a -= 1
                b -= 1
            a = row + 1
            b = column
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == "."):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a + 1][b][0] == "B":
                        self.possible_black_coordinates.append((a + 1, b))
                except IndexError:
                    pass
                a += 1
            a = row
            b = column + 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == "."):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a][b + 1][0] == "B":
                        self.possible_black_coordinates.append((a, b + 1))
                except IndexError:
                    pass
                b += 1
            a = row - 1
            b = column
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == "."):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a - 1][b][0] == "B":
                        self.possible_black_coordinates.append((a - 1, b))
                except IndexError:
                    pass
                a -= 1
            a = row
            b = column - 1
            while (7 >= a >= 0 and 7 >= b >= 0) and (self.board[a][b] == "."):
                self.possible_white_coordinates.append((a, b))
                try:
                    if self.board[a][b - 1][0] == "B":
                        self.possible_black_coordinates.append((a, b - 1))
                except IndexError:
                    pass
                b -= 1

            self.c[(row, column)] = self.possible_black_coordinates
        return self.c
    def move_Queen(self,turn):
        while True:

                try:
                    # print('Enter the x and y coordinate for Knight')
                    self.x_coordinate=int(input('Enter x coordinate for Queen').strip())
                    self.y_coordinate = int(input('Enter y coordinate for Queen').strip())
                    if turn=='W':
                        for key,values in self.possible_moves_queen_white().items():
                            if (self.x_coordinate,self.y_coordinate) in values:
                                self.board[self.x_coordinate][self.y_coordinate]='WQ'
                                self.board[key[0]][key[1]]='.'
                                print(values)
                                print(key)

                                break
                        else:
                            print('Not a valid move')
                        break
                    elif turn=='B':
                        for key, values in self.possible_moves_queen_black().items():
                            if (self.x_coordinate, self.y_coordinate) in values:
                                self.board[self.x_coordinate][self.y_coordinate] = 'BQ'
                                self.board[key[0]][key[1]] = '.'
                                print(values)
                                print(key)

                                break
                        else:
                            print('Not a valid move')
                        break
                except:
                    pass



class Pawn():
    def __init__(self,board):
        self.board=board
        self.x_coordinate = 0
        self.y_coordinate = 0
    def white_pawn_coordinate(self):
        self.white_pawn_coordinates=[]
        for row in range(8):
            for column in range(8):
                if self.board[row][column]=='WP':
                    self.white_pawn_coordinates.append((row,column))
        return self.white_pawn_coordinates
    def black_pawn_coordinate(self):
        self.black_pawn_coordinates=[]
        for row in range(8):
            for column in range(8):
                if self.board[row][column]=='BP':
                    self.black_pawn_coordinates.append((row,column))
        return self.black_pawn_coordinates
    def possible_moves_white(self):
        self.c=dict()
        for row,column in self.white_pawn_coordinate():
            self.possible_white_coordinate=[]
            if (row+1<=7) and self.board[row+1][column]=='.':
                self.possible_white_coordinate.append((row+1,column))
            elif (row+1<=7 and column+1<=7) and self.board[row+1][column+1]=='BP':
                self.possible_white_coordinate.append((row+1,column+1))
            elif (row==1) and self.board[row+2][column]=='.':
                self.possible_white_coordinate.append((row+2,column))
            self.c[(row, column)] = self.possible_white_coordinate
        return self.c
    def possible_moves_black(self):
        self.c=dict()
        for row,column in self.black_pawn_coordinate():
            self.possible_black_coordinate=[]
            if (row+1<=7) and self.board[row+1][column]=='.':
                self.possible_black_coordinate.append((row+1,column))
            elif (row+1<=7 and column+1<=7) and self.board[row+1][column+1]=='BP':
                self.possible_black_coordinate.append((row+1,column+1))
            elif (row==6) and self.board[row+2][column]=='.':
                self.possible_black_coordinate.append((row+2,column))
            self.c[(row, column)] = self.possible_black_coordinate
        return self.c
    def move_Pawn(self,turn):
        while True:

                try:
                    # print('Enter the x and y coordinate for Knight')
                    self.x_coordinate=int(input('Enter x coordinate for Pawn').strip())
                    self.y_coordinate = int(input('Enter y coordinate for Pawn').strip())
                    if turn=='W':
                        for key,values in self.possible_moves_white().items():
                            if (self.x_coordinate,self.y_coordinate) in values:
                                self.board[self.x_coordinate][self.y_coordinate]='WP'
                                self.board[key[0]][key[1]]='.'
                                print(values)
                                print(key)

                                break
                        else:
                            print('Not a valid move')
                        break
                    elif turn=='B':
                        for key, values in self.possible_moves_white().items():
                            if (self.x_coordinate, self.y_coordinate) in values:
                                self.board[self.x_coordinate][self.y_coordinate] = 'BP'
                                self.board[key[0]][key[1]] = '.'
                                print(values)
                                print(key)

                                break
                        else:
                            print('Not a valid move')
                        break
                except:
                    pass
class King():
    def __init__(self,board):
        self.board=board
        self.x_coordinate = 0
        self.y_coordinate = 0
    def white_King_coordinate(self):
        self.white_King_coordinates=[]
        for row in range(8):
            for column in range(8):
                if self.board[row][column]=='WK':
                    self.white_King_coordinates.append((row,column))
        return self.white_King_coordinates
    def black_King_coordinate(self):
        self.black_King_coordinates=[]
        for row in range(8):
            for column in range(8):
                if self.board[row][column]=='BK':
                    self.black_King_coordinates.append((row,column))
        return self.black_King_coordinates
    def possible_moves_white(self):
        self.c=dict()
        for row,column in self.white_King_coordinate():
            self.possible_white_coordinate=[]
            if (row+1<=7) and self.board[row+1][column][0]!='W':
                self.possible_white_coordinate.append((row+1,column))
            if (row+1<=7 and column<=7) and self.board[row+1][column+1][0]!='W':
                self.possible_white_coordinate.append((row+1,column+1))
            if (row + 1 <= 7 and column-1 >= 0) and self.board[row + 1][column - 1][0] != 'W':
                self.possible_white_coordinate.append((row + 1, column -1))
            if (row<=7 and column+1<=7) and self.board[row][column+1][0]!='W':
                self.possible_white_coordinate.append((row,column+1))
            if (row-1>=0) and  self.board[row-1][column][0]!='W':
                self.possible_white_coordinate.append((row-1,column))
            if (column-1>=0) and self.board[row][column-1][0]!='W':
                self.possible_white_coordinate.append((row,column-1))
            if (row-1>=0 and column-1 >=0) and self.board[row-1][column-1][0]!='W':
                self.possible_white_coordinate.append((row-1,column-1))
            if (row - 1 >= 0 and column + 1<= 7) and self.board[row - 1][column + 1][0] != 'W':
                self.possible_white_coordinate.append((row - 1, column +1))

        self.c[(row, column)] = self.possible_white_coordinate
        return self.c
    def possible_moves_black(self):
        self.c=dict()
        for row,column in self.black_King_coordinate():
            self.possible_black_coordinate=[]
            if (row+1<=7) and self.board[row+1][column][0]!='W':
                self.possible_black_coordinate.append((row+1,column))
            if (row+1<=7 and column<=7) and self.board[row+1][column+1][0]!='B':
                self.possible_black_coordinate.append((row+1,column+1))
            if (row + 1 <= 7 and column-1 >= 0) and self.board[row + 1][column - 1][0] != 'W':
                self.possible_black_coordinate.append((row + 1, column -1))
            if (row<=7 and column+1<=7) and self.board[row][column+1][0]!='B':
                self.possible_black_coordinate.append((row,column+1))
            if (row-1>=0) and  self.board[row-1][column][0]!='B':
                self.possible_black_coordinate.append((row-1,column))
            if (column-1>=0) and self.board[row][column-1][0]!='W':
                self.possible_black_coordinate.append((row,column-1))
            if (row-1>=0 and column-1 >=0) and self.board[row-1][column-1][0]!='B':
                self.possible_black_coordinate.append((row-1,column-1))
            if (row - 1 >= 0 and column + 1<= 7) and self.board[row - 1][column + 1][0] != 'B':
                self.possible_black_coordinate.append((row - 1, column +1))

        self.c[(row, column)] = self.possible_black_coordinate
        return self.c
    def move_King(self,turn):
        while True:

                try:
                    # print('Enter the x and y coordinate for Knight')
                    self.x_coordinate=int(input('Enter x coordinate for King').strip())
                    self.y_coordinate = int(input('Enter y coordinate for King').strip())
                    if turn=='W':
                        for key,values in self.possible_moves_white().items():
                            if (self.x_coordinate,self.y_coordinate) in values:
                                self.board[self.x_coordinate][self.y_coordinate]='WK'
                                self.board[key[0]][key[1]]='.'
                                print(values)
                                print(key)

                                break
                        else:
                            print('Not a valid move')
                        break
                    elif turn=='B':
                        for key, values in self.possible_moves_white().items():
                            if (self.x_coordinate, self.y_coordinate) in values:
                                self.board[self.x_coordinate][self.y_coordinate] = 'BP'
                                self.board[key[0]][key[1]] = '.'
                                print(values)
                                print(key)

                                break
                        else:
                            print('Not a valid move')
                        break
                except:
                    pass
class ChessGame(Horse,Rook,Bishop,Queen,Pawn,King):
    def __init__(self,board):
        self.turn='W'
        self.board=board
        self.piece_move='.'
        Horse.__init__(self,board)
        Rook.__init__(self,board)
        Bishop.__init__(self,board)
        Queen.__init__(self,board)
        Pawn.__init__(self,board)
        King.__init__(self,board)
    def play(self):
        # self.piece_move=input('Choose a piece you want to move').strip()
        if self.piece_move=='king':
            King.move_King(self,self.turn)
        elif self.piece_move == 'queen':
            Queen.move_Queen(self,self.turn)
        elif self.piece_move == 'bishop':
            Bishop.move_Bishop(self,self.turn)
            
        elif self.piece_move == 'knight':
            Horse.move_Knight(self,self.turn)
            
        elif self.piece_move == 'rook':
            Rook.move_Rook(self,self.turn)
            
        else:
            print('please choose again')
        self.turn_change()

    def turn_change(self):
        if self.turn=='W':
            self.turn='B'
        elif self.turn=='B':
            self.turn='W'
        return self.turn
    # def check(self):


if __name__=='__main__':
    board=[['.', '.', '.', 'WQ', '', 'WB', 'WH', 'WR'],
           ['.', 'WP', 'WP', '.', 'WP', 'WP', 'WP', '.'],
           ['', '.', '.', '.', '.', '.', '.', '.'],
           ['WR', '.', 'WH', 'WB', '.', 'BP', 'BP', '.'],
           ['.', '.', '.', '.', '.', '.', '.', '.'],
           ['.', '.', '.', '.', 'WK', '.', '.', 'BR'],
           ['BP', '.', '.', '.', '.', '.', '.', '.'],
           ['BR', 'BH', '.', 'BQ', 'BK', 'BB', 'BH', '.']]
    # Test for Horse
    # o=Horse(board)
    # print("The White knights coordinates are", o.white_horse_coordinate())
    # print("The Black knight coordinates are", o.black_horse_coordinate())
    # print("The possible moves for white rook", o.possible_moves_white())
    # print("The possible moves for black rook", o.possible_moves_black())
    # o.move_Knight('B')
    print(board)
    # Test for Rook
    # R=Rook(board)
    # print("The White rook coordinates are", R.white_rook_coordinate())
    # print("The Black rook coordinates are", R.black_rook_coordinate())
    # print("The possible moves for white rook", R.possible_moves_white_rook())
    # print("The possible moves for black rook", R.possible_moves_black_rook())
    # R.move('W')
    # print(board)

    # Test for Bishop
    # B=Bishop(board)
    # print("The White bishop coordinates are", B.white_bishop_coordinate())
    # print("The Black bishop coordinates are", B.black_bishop_coordinate())
    # print("The possible moves for white bishop", B.possible_moves_white_bishop())
    # print("The possible moves for black bishop", B.possible_moves_black_bishop())
    # B.move('W')
    # print(board)
    # Test for Queen
    # Q=Queen(board)
    # print("The White Queen coordinates are", Q.white_queen_coordinate())
    # print("The Black Queen coordinates are", Q.black_queen_coordinate())
    #
    # print("The possible moves for white queen", Q.possible_moves_queen_white())
    # print("The possible moves for black queen", Q.possible_moves_queen_black())
    # Q.move('W')
    # print(board)

    # Test for Pawn
    # p=Pawn(board)
    # print("The White pawn coordinates are", p.white_pawn_coordinate())
    # print("The Black pawn coordinates are", p.black_pawn_coordinate())
    # print("The possible moves for white pawn", p.possible_moves_white())
    # print("The possible moves for black pawn", p.possible_moves_black())
    # p.move('B')
    # print(board)
    # Test for King
    # K=King(board)
    # print("The White King coordinates are", K.white_King_coordinate())
    # print("The White pawn coordinates are", K.black_King_coordinate())
    # print("The possible moves for white King", K.possible_moves_white())
    # print("The possible moves for black King", K.possible_moves_black())
    # K.move('B')
    # print(board)
    # Test Play
    c=ChessGame(board)
    print(c.board)
    c.play()
    print(c.board)






