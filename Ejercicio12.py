Algoritmo: Definición de abrir una cuenta con descubierto autorizado durante un tiempo limitado

Algoritmo abrir:
    # Inicializar `c' mediante un `saldo_inicial' y un 
    # `descubierto_MAX' durante una `duración_max'.

Entrada:
    c : CUENTA
    saldo_inicial : REAL
    descubierto_MAX : REAL
    duración_max : FECHA

Precondición:
    saldo_inicial > 0
    descubierto_MAX ≥ 0
    duración_max ≥ 0

Realización:
    c.descubierto ← descubierto_MAX
    c.saldo ← saldo_inicial
    c.fecha_descubierto ← 0
    c.duración_max ← duración_max

Postcondición:
    c.descubierto = descubierto_MAX
    c.saldo = saldo_inicial
    c.duración_max = duración_max
    c.fecha_descubierto = 0

Fin de abrir
