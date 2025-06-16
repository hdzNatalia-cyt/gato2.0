import tkinter as tk
from tkinter import messagebox

class JuegoDelGatoApp:
    def __init__(self, master_ventana):
        self.master_ventana = master_ventana
        master_ventana.title("El Gato");
        master_ventana.geometry("340x500")
        master_ventana.resizable(False, False);
        master_ventana.configure(bg='lightgray')

        self.tablero = [[""] * 3 for _ in range(3)]  
        self.jugador_actual = "X";
        self.contador_jugadas = 0
        self.juego_activo = True;
        self.puntaje_x = 0;
        self.puntaje_o = 0

        self.etiqueta_estado = tk.Label(master_ventana, font=('Arial', 16, 'bold'), bg='lightgray', fg='navy')
        self.etiqueta_puntaje = tk.Label(master_ventana, font=("Arial", 14), bg='lightgray')
        self.etiqueta_estado.pack(pady=10);
        self.etiqueta_puntaje.pack(pady=5)
        self._actualizar_info_panel()

        marco_tablero = tk.Frame(master_ventana, bg='darkgray', bd=3, relief='raised')
        marco_tablero.pack(pady=5)
        self.botones_del_juego = []
        for fila in range(3):
            fila_botones = []  
            for col in range(3):  
                boton = tk.Button(marco_tablero, text="", font=("Arial", 40), width=3, height=1,
                                  bg='white', fg='black',
                                  command=lambda r=fila, c=col: self.clic_en_casilla(r, c))
                boton.grid(row=fila, column=col, padx=4, pady=4)
                fila_botones.append(boton)
            self.botones_del_juego.append(fila_botones)

        self.boton_reiniciar = tk.Button(master_ventana, text="Reiniciar Juego", font=('Arial', 12), bg='skyblue',
                                         fg='white', command=self.reiniciar_interfaz)
        self.boton_reiniciar.pack(pady=15)

    def hacer_jugada(self, fila, columna):
        if not self.juego_activo or self.tablero[fila][columna]: return None

        self.tablero[fila][columna] = self.jugador_actual
        self.contador_jugadas += 1
        return self.jugador_actual

    def verificar_estado_juego(self):
        for i in range(3):
            if all(self.tablero[i][j] == self.jugador_actual for j in range(3)): return self._finalizar_juego(
                "ganador")
            if all(self.tablero[j][i] == self.jugador_actual for j in range(3)): return self._finalizar_juego(
                "ganador")

        if (all(self.tablero[i][i] == self.jugador_actual for i in range(3)) or  
                all(self.tablero[i][2 - i] == self.jugador_actual for i in range(3))): return self._finalizar_juego(
            "ganador")

        if self.contador_jugadas == 9: return self._finalizar_juego("empate")

        return "sigue_jugando"

    def _finalizar_juego(self, estado):
        self.juego_activo = False
        if estado == "ganador":
            if self.jugador_actual == "X":
                self.puntaje_x += 1
            else:
                self.puntaje_o += 1
        return estado

    def cambiar_turno(self):
        self.jugador_actual = "O" if self.jugador_actual == "X" else "X"

    def reiniciar_juego_logica(self):
        self.tablero = [[""] * 3 for _ in range(3)]
        self.jugador_actual = "X";
        self.contador_jugadas = 0;
        self.juego_activo = True

    def obtener_texto_puntaje(self):
        return f"Puntos - X: {self.puntaje_x}    O: {self.puntaje_o}"

    def _actualizar_info_panel(self):
        self.etiqueta_estado.config(text=f"Turno de: {self.jugador_actual}")
        self.etiqueta_puntaje.config(text=self.obtener_texto_puntaje())

    def clic_en_casilla(self, fila, columna):
        if not self.juego_activo:
            messagebox.showinfo("Juego Terminado", "¡Haz clic en 'Reiniciar Juego' para volver a jugar!")
            return

        simbolo = self.hacer_jugada(fila, columna)
        if simbolo:
            self.botones_del_juego[fila][columna].config(text=simbolo, state=tk.DISABLED)
            estado = self.verificar_estado_juego()

            if estado == "ganador":
                self.etiqueta_estado.config(text=f"¡GANÓ: {self.jugador_actual}!", fg='green')
                messagebox.showinfo("Juego Terminado", f"¡El jugador {self.jugador_actual} ha ganado!")
                self._deshabilitar_todos_los_botones()
            elif estado == "empate":
                self.etiqueta_estado.config(text="¡EMPATE!", fg='orange')
                messagebox.showinfo("Juego Terminado", "¡Es un empate!")
                self._deshabilitar_todos_los_botones()
            else:
                self.cambiar_turno();
                self._actualizar_info_panel()
        else:
            messagebox.showwarning("Casilla Ocupada", "¡Esa casilla ya está ocupada! Elige otra.")

    def _deshabilitar_todos_los_botones(self):  # Método auxiliar privado
        for fila_botones in self.botones_del_juego:
            for boton in fila_botones: boton.config(state=tk.DISABLED)

    def reiniciar_interfaz(self):
        self.reiniciar_juego_logica()
        self._actualizar_info_panel()
        for fila in range(3):
            for col in range(3):
                self.botones_del_juego[fila][col].config(text="", state=tk.NORMAL, bg='white', fg='black')


if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = JuegoDelGatoApp(ventana_principal)
    ventana_principal.mainloop()
