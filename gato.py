import tkinter as tk
from tkinter import messagebox
import random as rd

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Gato")
        self.jugadas_rival:list = []

        self.current_player = tk.StringVar(value="X")
        self.board = [""] * 9

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.window, text="Elija quién empieza:")
        self.label.grid(row=0, column=0, columnspan=2)

        self.player_x_button = tk.Radiobutton(self.window, text="Jugador X", variable=self.current_player, value="X")
        self.player_x_button.grid(row=1, column=0)

        self.player_o_button = tk.Radiobutton(self.window, text="Jugador O", variable=self.current_player, value="O", command= self.inicia_ia)
        self.player_o_button.grid(row=1, column=1)

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text="", font=('normal', 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i + 3, column=j)
                self.buttons.append(button)

    def colocar_simbolo(self, row, col): #Colocar simbolo en la ventana
        index = 3 * row + col
        self.board[index] = self.current_player.get()
        self.buttons[index].config(text=self.current_player.get(), state="disabled")
        return index
    def inicia_ia(self): #Si la ia comienza tirando escoje alguna casilla de las esquinas o el centro
        posiciones_iniciales = [[0,0],[0,2],[2,0],[2,2],[1,1]]
        casilla = posiciones_iniciales[rd.randint(0,4)]
        self.colocar_simbolo(casilla[0],casilla[1])
        self.current_player = tk.StringVar(value="X")
    def elegir_tiro(self): #LA IA ESCOGE DONDE TIRAR
        
        if len(self.jugadas_rival) == 1: #Si el rival hizo la primera jugada
            eleccion_inicial = rd.randint(0,1) #Un poco de diversidad
            print(eleccion_inicial)
            if self.jugadas_rival[0] == 0: #Esquina superior izquierda
                if eleccion_inicial == 1:
                    self.colocar_simbolo(0,1)
                else:
                    self.colocar_simbolo(1,0)
            elif self.jugadas_rival[0] == 2: #Esquina superior derecha
                if eleccion_inicial == 1:
                    self.colocar_simbolo(1,2)
                else:
                    self.colocar_simbolo(0,1)
            elif self.jugadas_rival[0] == 6: #Esquina inferior izquierda
                if eleccion_inicial == 1:
                    self.colocar_simbolo(2,1)
                else:
                    self.colocar_simbolo(1,0)
            elif self.jugadas_rival[0] == 8: #Esquina inferior derecha
                if eleccion_inicial == 1:
                    self.colocar_simbolo(1,2)
                else:
                    self.colocar_simbolo(2,1)

    def on_button_click(self, row, col):
        index = 3 * row + col #indice de la casilla

        if self.board[index] == "": #Cuando el rival humano elige la casilla
            self.jugadas_rival.append(index)
            print(self.jugadas_rival)
            self.colocar_simbolo(row,col)
            self.current_player = tk.StringVar(value="O")
            self.elegir_tiro()
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"¡Jugador {self.current_player.get()} gana!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "Empate. ¡Inténtalo de nuevo!")
                self.reset_game()

    def check_winner(self):
        for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_game(self):
        self.current_player.set("X")
        self.board = [""] * 9

        for button in self.buttons:
            button.config(text="", state="active")

        self.label.grid(row=0, column=0, columnspan=2)
        self.player_x_button.grid(row=1, column=0)
        self.player_o_button.grid(row=1, column=1)
        self.start_button.grid(row=2, column=0, columnspan=2)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()