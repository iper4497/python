import cartas
 
mibaraja=cartas.BarajaEspanola()
mibaraja.Barajar()
 
jugada_jugador=cartas.Mazo()
jugada_jugador.SetdeCartas(mibaraja.DarCartas(1))
jugada_maquina=cartas.Mazo()
jugada_maquina.SetdeCartas(mibaraja.DarCartas(1))
 
jugada_jugador.ImprimeMazo()
print('Tu puntuación es '+str(jugada_jugador.PuntuacionBasica()))
 
while input('¿Quieres más cartas?')=='Si':
    jugada_jugador.SetdeCartas(mibaraja.DarCartas(1))
    jugada_jugador.ImprimeMazo()
    print('Tu puntuación es '+str(jugada_jugador.PuntuacionBasica()))
    if jugada_jugador.PuntuacionBasica() >=21:
        break
 
    if jugada_maquina.PuntuacionBasica()<jugada_jugador.PuntuacionBasica():
        jugada_maquina.SetdeCartas(mibaraja.DarCartas(1))
        print('La maquina pide carta...')
 
if jugada_jugador.PuntuacionBasica()<=21:
 
    while jugada_maquina.PuntuacionBasica()<jugada_jugador.PuntuacionBasica():
        jugada_maquina.SetdeCartas(mibaraja.DarCartas(1))
        print('La maquina pide carta...')
 
 
    print('Tu puntuación es de '+str(jugada_jugador.PuntuacionBasica()))
    print('La puntuación de la máquina es  '+str(jugada_maquina.PuntuacionBasica()))
 
 
    if jugada_maquina.PuntuacionBasica()<=21:
        print('Gana la máquina')
 
    else:
        print('Has forzado a la maquina a arriesgarse y ganas. Enhorabuena!')
 
else:
    print('¡Te has pasado de 21! Gana la máquina')
 
print('CARTAS JUGADOR')
jugada_jugador.ImprimeMazo()
print('CARTAS MAQUINA')
jugada_maquina.ImprimeMazo()
