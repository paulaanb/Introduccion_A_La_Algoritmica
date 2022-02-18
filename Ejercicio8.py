Algoritmo: Precio con IVA 

#Vamos a calcular el precio final 

Entrada:
#Coste final
 c: REAL 
 #Impuesto sobre la venta
 i: REAL 
 
Resultado: 
#Precio final donde el IVA está incluido
REAL  

Precondición:
 c ≥ 0
 Impuesto sobre venta > 0
 
Realización:
 Resultado <-- c + (c x i)

Poscondición:
 Resultado = c + (c x i)
 
Fin del cálculo 

Algoritmo: Interés generado

#Calculamos el interés generado mediante un capital inicial, el tiempo, en meses, y el interés

Entrada:
#Importe del capital inicial
 c: REAL 
#Tiempo en meses
 t: REAL 
 #Tasa de interés
 i: REAL 

Resultado: 
REAL

Precondición:
 c ≥ 0
 t > 0
 i > 0
 
Realización:
 Resultado <-- c x t x i
 
Poscondición:
 Resultado = c x t x i

Fin del cálculo del interés generado