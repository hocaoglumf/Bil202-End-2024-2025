#import DrawBoard as db
import tkinter as tk

from fontTools.svgLib.path.parser import UPPERCASE

import Pieces as pieces
class Cell:
    def __init__(self,name):
        self.piece=None
        self.name=name
        self.x1=0
        self.x2=0
        self.y1=0
        self.y2=0


    def RemovePiece(self):
        del self.piece
        self.piece=None

class Board:
    def __init__(self):
        self.turn=True
        self.root = tk.Tk()
        self.root.title("Chess Board with Pieces")
        self.root.geometry("550x550")
        self.cell_size = 60
        self.canvas = tk.Canvas(self.root, width=self.cell_size * 8, height=self.cell_size * 8)
        self.canvas.pack()
        self.entry_from=None
        self.entry_to=None


        self.board={}
        self.pieces = {
            'R':[pieces.Kale, '♖'], 'N': [pieces.At,'♘'], 'B':[pieces.Fil, '⚜️'], 'Q':[pieces.Vezir, '♕'], 'K':[pieces.Sah, '♔'], 'P':[pieces.Piyon, '♙'],
            'r':[pieces.Kale, '♜'], 'n':  [pieces.At,'♞'], 'b': [pieces.Fil,'⚜️'], 'q':[pieces.Vezir,  '♛'], 'k':[pieces.Sah,  '♚'], 'p':[pieces.Piyon, '♟'],
            ' ': [pieces.Piece,' ']
        }
        self.initial_board = [
                   ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                    ['p'] * 8,
                    [' '] * 8,
                    [' '] * 8,
                    [' '] * 8,
                    [' '] * 8,
                    ['P'] * 8,
                    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
                ]


    def Draw(self):
        colors = ["#f0d9b5", "#b58863"]
        size=self.cell_size
        for i in list(self.board.keys()):
            c=self.board[i].piece
            cell=self.board[i]
            color=colors[self.board[i].piece.color]
            txt=c.figure
            self.canvas.create_text(
                cell.x1 + size // 2,
                cell.y1 + size // 2,
                text=txt,
                font=("Arial", int(size / 1.5)),
                fill="black" if c.ts.isupper() else "white"
            )

    def CreatePieces(self):
        for i in range(8):
            for j in range(8):
                ts=self.initial_board[i][j]
                piece=self.pieces[ts][0]
                color = int(ts.isupper())
                cell=self.board[chr(65+j)+str(i+1)]
                if cell.piece==None or cell.piece.name=='Tas':
                    p = piece()
                    p.board=self
                    p.ts = ts
                    p.figure = self.pieces[ts][1]
                    p.color = color
                    cell.piece=p
                else:
                    print("x")


    def Create(self):
        letters=['A','B', 'C', 'D', 'E', 'F', 'G', 'H']
        size=self.cell_size
        colors = ["#f0d9b5", "#b58863"]
        for i in range(8):
            for j in range(8):
                if letters[i]+str(j+1) in list(self.board.keys()):
                    c = self.board[letters[i] + str(j + 1)]
                else:
                    c = Cell(letters[i] + str(j + 1))
                    self.board[letters[i] + str(j + 1)] = c
                    c.x1 = i * size
                    c.y1 = j * size
                    c.x2 = c.x1 + size
                    c.y2 = c.y1 + size
                    color = colors[(i + j) % 2]
                    c.color=color
                self.canvas.create_rectangle(c.x1, c.y1, c.x2, c.y2, fill=c.color, outline="black")

        y=503
        # From Label
        label_from = tk.Label(self.root, text="From:")
        label_from.place(x=30, y=y)

        # From Entry
        self.entry_from = tk.Entry(self.root, width=20,bg=colors[0] )
        self.entry_from.place(x=70, y=y)

        # To Label
        label_to = tk.Label(self.root, text="To:")
        label_to.place(x=230, y=y)

        # To Entry
        self.entry_to = tk.Entry(self.root, width=20,bg=colors[0])
        self.entry_to.place(x=255, y=y)

        # Play  Butonu
        button_play = tk.Button(self.root, text="  Play  ", bg=colors[0], command=self.Play)
        button_play.place(x=420, y=y-3)
        self.ColRowLabels()

    def ColRowLabels(self):
        x =52
        for i in ['A','B', 'C', 'D', 'E', 'F', 'G', 'H']:
            label=tk.Label(self.root,text=i)
            label.place(x=x,y=481)
            x +=self.cell_size

        for p in range(1,9):
            label=tk.Label(text=str(p))
            label.place(x=10,y=497-p*59,)
            label=tk.Label(text=str(p))
            label.place(x=520,y=25+(p-1)*59,)

    def Play(self):
        frm=self.entry_from.get()
        to=self.entry_to.get()
        if not(self.turn):
            frmList=list(frm)
            toList=list(to)
            frmadr=str(9-int(frmList[1]))
            toadr=str(9-int(toList[1]))
            frm=frmList[0]+frmadr
            to=toList[0]+toadr
        frm=frm.upper()
        to=to.upper()
        pfrm=self.board[frm].piece
        frmCell=self.board[frm]
        tofrm=self.board[to].piece
        toCell=self.board[to]
        res = pfrm.Play(frmCell,toCell)
        print(pfrm.name, tofrm.name)
        self.Create()
        self.Draw()
        if res:
            self.turn=not(self.turn)

board=Board()
board.Create()
board.CreatePieces()
board.Draw()

board.root.mainloop()
print("")
