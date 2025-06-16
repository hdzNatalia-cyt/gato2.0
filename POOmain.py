class JuegoDelGato:
    def __init__(self):
        self.tablero = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]
        self.jugador_actual = "X"
        self.contador_jugadas = 0
        self.juego_activo = True

    def mostrar_tablero(self):
        print("\n-------------")
        for fila in range(3):
            print(f"| {self.tablero[fila][0]} | {self.tablero[fila][1]} | {self.tablero[fila][2]} |")
            print("-------------")

    def hacer_jugada(self, numero_casilla):
        if not self.juego_activo:
            print("¡Juego Terminado! Inicia uno nuevo.")
            return False

        fila = (numero_casilla - 1) // 3
        columna = (numero_casilla - 1) % 3

        if self.tablero[fila][columna] != "X" and self.tablero[fila][columna] != "O":
            self.tablero[fila][columna] = self.jugador_actual
            self.contador_jugadas += 1

            self.verificar_final_del_juego()

            if self.juego_activo:
                if self.jugador_actual == "X":
                    self.jugador_actual = "O"
                else:
                    self.jugador_actual = "X"
            return True
        else:
            print("¡Esa casilla ya está ocupada! Elige otra.")
            return False

    def verificar_final_del_juego(self):
        lineas_ganadoras = [
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
        ]

        for linea in lineas_ganadoras:
            (r1, c1), (r2, c2), (r3, c3) = linea

            if (self.tablero[r1][c1] == self.jugador_actual and
                    self.tablero[r2][c2] == self.jugador_actual and
                    self.tablero[r3][c3] == self.jugador_actual):

                self.mostrar_tablero()
                print(f"¡GANÓ: {self.jugador_actual}!")
                self.juego_activo = False
                return

        if self.contador_jugadas == 9:
            self.mostrar_tablero()
            print("¡Es un empate! Nadie ganó.")
            self.juego_activo = False

    def reiniciar_juego(self):
        self.tablero = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]
        self.jugador_actual = "X"
        self.contador_jugadas = 0
        self.juego_activo = True
        print("\n--- ¡Juego Reiniciado! ---")

class JuegoPrincipal:
    def __init__(self):
        self.juego_del_gato = JuegoDelGato()

    def obtener_eleccion_valida(self):
        eleccion = None
        while eleccion is None:
            entrada_usuario = input("Elige un número de casilla (1-9): ")
            if entrada_usuario.isdigit():
                numero_ingresado = int(entrada_usuario)
                if 1 <= numero_ingresado <= 9:
                    eleccion = numero_ingresado
                else:
                    print("Por favor, ingresa un número entre 1 y 9.")
            else:
                print("Entrada inválida. Por favor, ingresa un número.")
        return eleccion

    def iniciar_juego(self):
        print("¡Bienvenido al Juego del Gato!")
        while self.juego_del_gato.juego_activo:
            self.juego_del_gato.mostrar_tablero()
            print(f"Es el turno de {self.juego_del_gato.jugador_actual}.")

            eleccion = self.obtener_eleccion_valida()
            self.juego_del_gato.hacer_jugada(eleccion)

            if not self.juego_del_gato.juego_activo:
                respuesta = input("¿Quieres jugar de nuevo? (s/n): ").lower()
                if respuesta == 's':
                    self.juego_del_gato.reiniciar_juego()
                else:
                    print("¡Gracias por jugar! Adiós.")
                    break

if __name__ == "__main__":
    juego_principal = JuegoPrincipal()
    juego_principal.iniciar_juego()