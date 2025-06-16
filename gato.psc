Proceso Gato
	
    // Inicializa dos matrices 3x3: una con valores (Tab1) y otra con las fichas visibles (Tab2)
    Dimension Tab1[3,3]
    Dimension Tab2[3,3]
    
    Para i <- 1 Hasta 3 Hacer
        Para j <- 1 Hasta 3 Hacer
            Tab1[i,j] <- 0
            Tab2[i,j] <- " "
        FinPara
    FinPara
	
    TurnoJugador1 <- Verdadero
    Terminado <- Falso
    Ganador <- Falso
    CaTurnos <- 0
	
    Mientras ~Terminado Hacer
		
        // Dibuja el tablero
        Borrar Pantalla
        Escribir " "
        Escribir "      |     |     "
        Escribir "   ", Tab2[1,1], "  |  ", Tab2[1,2], "  |  ", Tab2[1,3]
        Escribir "     1|    2|    3"
        Escribir " =====++=====++======"
        Escribir "      |     |     "
        Escribir "   ", Tab2[2,1], "  |  ", Tab2[2,2], "  |  ", Tab2[2,3]
        Escribir "     4|    5|    6"
        Escribir " =====++=====++======"
        Escribir "      |     |     "
        Escribir "   ", Tab2[3,1], "  |  ", Tab2[3,2], "  |  ", Tab2[3,3]
        Escribir "     7|    8|    9"
        Escribir " "
		
        Si ~Ganador y CantTurnos < 9 Entonces
			
            // Dice a qué jugador le toca
            Si TurnoAlJugador1 Entonces
                Ficha <- 'X'
                Valor <- 1
                Escribir "Turno del jugador 1 X"
            Sino
                Ficha <- 'O'
                Valor <- 2
                Escribir "Turno del jugador 2 O"
            FinSi
			
            // Pide y valida posición
            Escribir "Ingrese el lugar (1-9):"
            Repetir
                Leer Pos
                Si Pos < 1 o Pos > 9 Entonces
                    Escribir "Lugar incorrecto, ingrese nuevamente: "
                    Pos <- 99
                Sino
                    i <- trunc((Pos - 1) / 3) + 1
                    j <- ((Pos - 1) MOD 3) + 1
                    Si Tab1[i,j] <> 0 Entonces
                        Escribir "Ese lugar ya está ocupado, intente otro."
                        Pos <- 99
                    FinSi
                FinSi
            Hasta Que Pos <> 99
			
            // Coloca la ficha
            CantTurnos <- CantTurnos + 1
            Tab1[i,j] <- Valor
            Tab2[i,j] <- Ficha
			
            // hay 3 valores iguales en filas, columnas o diagonales
            Para k <- 1 Hasta 3 Hacer
                // Filas
                Si Tab1[k,1] = Valor y Tab1[k,2] = Valor y Tab1[k,3] = Valor Entonces
                    Ganador <- Verdadero
                FinSi
                // Columnas
                Si Tab1[1,k] = Valor y Tab1[2,k] = Valor y Tab1[3,k] = Valor Entonces
                    Ganador <- Verdadero
                FinSi
            FinPara
			
            // Diagonales
            Si Tab1[1,1] = Valor y Tab1[2,2] = Valor y Tab1[3,3] = Valor Entonces
                Ganador <- Verdadero
            FinSi
            Si Tab1[1,3] = Valor y Tab1[2,2] = Valor y Tab1[3,1] = Valor Entonces
                Ganador <- Verdadero
            FinSi
			
            // Cambia el turno 
            Si ~Ganador Entonces
                TurnoJugador1 <- ~TurnoAlJugador1
            FinSi
			
        Sino
			
            //  resultado final
            Si Ganador Entonces
                Escribir "Ganador: "
                Si TurnoAlJugador1 Entonces
                    Escribir "Jugador 1!"
                Sino
                    Escribir "Jugador 2!"
                FinSi
            Sino
                Escribir "¡Empate!"
            FinSi
            Terminado <- Verdadero
			
        FinSi
		
    FinMientras
	
FinProceso

