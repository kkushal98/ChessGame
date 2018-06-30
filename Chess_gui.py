import pygame
from ChessLogic import *
import pygame
import time
class Game(ChessGame):
    def __init__(self,board):
        self.board=board
        self.row=0
        self.column=0
        ChessGame.__init__(self, board)



    def draw_board(self):
        """ Draw a chess board with queens, as determined by the the_board. """
        # h=Horse(self.board)
        # r=Rook(board)
        # b=Bishop(board)
        # q=Queen(board)
        # k=King(board)
        # p=Pawn(board)

        # objects=[h,r,b,q,k,p]
        pygame.init()
        colors = [(139,69,19), (205,133,63)]    # Set up colors [red, black]

        n = len(self.board)
        # This is an NxN chess board.
        self.surface_sz = 480           # Proposed physical surface size.
        self.sq_sz = self.surface_sz // n    # sq_sz is length of a square.
        self.surface_sz = n * self.sq_sz     # Adjust to exactly fit n squares.
        self.surface = pygame.display.set_mode((480, 480), pygame.RESIZABLE)

        # Look for an event from keyboard, mouse, etc.


        # Look for an event from keyboard, mouse, etc.
        # Create the surface of (width, height), and its window.
        for row in range(n):  # Draw each row of the board.
            c_indx = row % 2  # Alternate starting color
            for col in range(n):  # Run through cols drawing squares
                the_square = (col * self.sq_sz, row * self.sq_sz, self.sq_sz, self.sq_sz)
                self.surface.fill(colors[c_indx], the_square)
                # Now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        # for i in range(0, 480, 60):
        #     self.surface.blit(whitepawn, (i + 5, 360))

        pygame.display.flip()

    def eventhandler(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                return False


            if ev.type == pygame.MOUSEBUTTONDOWN:

                if self.valid_mouse_click_piece():



                    #the model must be updated to display the available moves

                    #ChessGame.updateAvailableMovesForDisplay()
                    #redraw board
                    for ev in pygame.event.get():
                        if ev.type==pygame.MOUSEBUTTONDOWN:
                          self.valid_mouse_click_piece()




                    ChessGame.play(self) 



                    print(self.board[self.row][self.column])
            return True


    def valid_mouse_click_piece(self):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        print(mouse)
        # know what the square

        self.column = int(mouse[0] / (self.surface_sz / 8))
        self.row = 7 - int(mouse[1] / (self.surface_sz / 8))

        ChessGame.piece_move = getPiece(self.row, self.column)  # name of the piece

        if not ((self.board[self.row][self.column][0]=='W' and self.turn=='W') or (self.board[self.row][self.column][0]=='B' and self.turn=='B' )):
            return False
        if self.board[self.row][self.column][1]=='H':
            Horse.update_coordinates(self.row,self.column)
        elif self.board[self.row][self.column][1]=='R':
            Rook.update_coordinates(self.row, self.column)
        elif self.board[self.row][self.column][1]=='B':
            Bishop.update_coordinates(self.row, self.column)
        elif self.board[self.row][self.column][1]=='Q':
            Queen.update_coordinates(self.row, self.column)
        elif self.board[self.row][self.column][1]=='K':
            King.update_coordinates(self.row, self.column)
        elif self.board[self.row][self.column][1] == 'P':
            Pawn.update_coordinates(self.row, self.column)

        return True





    def placepieces(self):
        whitepawn = pygame.image.load("white_pawn.png").convert_alpha()
        whitepawn = pygame.transform.scale(whitepawn, (50, 50))
        for i in range(0, 480, 60):
            self.surface.blit(whitepawn, (i + 5, 360))
        blackpawn=pygame.image.load("black_pawn.png").convert_alpha()
        blackpawn=pygame.transform.scale(blackpawn,(50,50))
        for i in range(0,480,60):
            self.surface.blit(blackpawn,(i+5,60))
        whitehorse=pygame.image.load("white_horse.png").convert_alpha()
        whitehorse=pygame.transform.scale(whitehorse,(50,50))
        self.surface.blit(whitehorse,(62,420))
        whitehorse1=pygame.image.load("white_horse.png").convert_alpha()
        whitehorse1=pygame.transform.scale(whitehorse,(50,50))
        self.surface.blit(whitehorse1,(362,420))
        blackhorse = pygame.image.load("black_horse.png").convert_alpha()
        blackhorse = pygame.transform.scale(blackhorse, (50, 50))
        self.surface.blit(blackhorse, (62, 0))
        blackhorse1 = pygame.image.load("black_horse.png").convert_alpha()
        blackhorse1 = pygame.transform.scale(blackhorse1, (50, 50))
        self.surface.blit(blackhorse1, (362, 0))
        whiterook = pygame.image.load("white_rook.png").convert_alpha()
        whiterook = pygame.transform.scale(whiterook, (50, 50))
        self.surface.blit(whiterook, (0, 420))
        whiterook1 = pygame.image.load("white_rook.png").convert_alpha()
        whiterook1 = pygame.transform.scale(whiterook1, (50, 50))
        self.surface.blit(whiterook1, (420, 420))
        blackrook = pygame.image.load("black_rook.png").convert_alpha()
        blackrook = pygame.transform.scale(blackrook, (50, 50))
        self.surface.blit(blackrook, (0, 0))
        blackrook1 = pygame.image.load("black_rook.png").convert_alpha()
        blackrook1 = pygame.transform.scale(blackrook1, (50, 50))
        self.surface.blit(blackrook1, (420, 0))
        whitebishop = pygame.image.load("white_bishop.png").convert_alpha()
        whitebishop = pygame.transform.scale(whitebishop, (50, 50))
        self.surface.blit(whitebishop, (125, 420))
        whitebishop1 = pygame.image.load("white_bishop.png").convert_alpha()
        whitebishop1 = pygame.transform.scale(whitebishop1, (50, 50))
        self.surface.blit(whitebishop1, (305, 420))
        blackbishop = pygame.image.load("black_bishop.png").convert_alpha()
        blackbishop = pygame.transform.scale(blackbishop, (50, 50))
        self.surface.blit(blackbishop, (120, 0))
        blackbishop1 = pygame.image.load("black_bishop.png").convert_alpha()
        blackbishop1 = pygame.transform.scale(blackbishop1, (50, 50))
        self.surface.blit(blackbishop1, (300, 0))
        whitequeen = pygame.image.load("white_queen.png").convert_alpha()
        whitequeen = pygame.transform.scale(whitequeen, (50, 50))
        self.surface.blit(whitequeen, (185, 420))
        blackqueen = pygame.image.load("black_queen.png").convert_alpha()
        blackqueen = pygame.transform.scale(blackqueen, (50, 50))
        self.surface.blit(blackqueen, (185, 0))
        whiteking = pygame.image.load("white_king.png").convert_alpha()
        whiteking = pygame.transform.scale(whiteking, (50, 50))
        self.surface.blit(whiteking, (245, 420))
        blackking = pygame.image.load("black_king.png").convert_alpha()
        blackking = pygame.transform.scale(blackking, (50, 50))
        self.surface.blit(blackking, (245, 0))

        pygame.display.flip()


            # blackpawn=pygame.image.load

        # return self.surface
    # def move(self):




    # def resized(self):
    #     pygame.init()
    #     self.surface=self.draw_board(self.width,self.height)
    #
    #     while True:
    #
    #         # Look for an event from keyboard, mouse, etc.
    #        for ev in pygame.event.get():
    #         if ev.type == pygame.QUIT:
    #             break
    #         if ev.type==pygame.MOUSEBUTTONDOWN:
    #             mouse=pygame.mouse.get_pos()
    #             click=pygame.mouse.get_pressed()
    #             print(mouse)
    #         if ev.type == pygame.VIDEORESIZE:
    #             screensize = ev.size
    #             print(screensize[0], screensize[1])
    #             new_surface = pygame.display.set_mode(ev.size)
    #     # new_surface.blit(surface,(0,0))
    #     # del surface
    #
    #
    #
    #
    #
    #                 # rect=pygame.Rect(whitepawn.get_rect())
    #             # print(rect)
    #
    #             # column=(int(mouse[0]))
    #             # print(column)
    #             # row=(int((mouse[1]/60)))
    #             #
    #             # print((row,column))
    #
    #
    #         # Draw a fresh background (a blank chess board)
    #         # for row in range(n):           # Draw each row of the board.
    #         #     c_indx = row % 2           # Alternate starting color
    #         #     for col in range(n):       # Run through cols drawing squares
    #         #         the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
    #         #         surface.fill(colors[c_indx], the_square)
    #         #         # Now flip the color index for the next square
    #         #         c_indx = (c_indx + 1) % 2
    #         #
    #         # for i in range(0, 480, 60):
    #         #     surface.blit(whitepawn, (i + 5, 360))
    #         #
    #         # pygame.display.flip()
    #
    #
    #     pygame.quit()
    # def available_moves(self):


if __name__ == "__main__":
    i=ChessBoard()
    o=Game(i.board)
    o.draw_board()
    o.placepieces()
    while o.eventhandler():
        time.sleep(1)






