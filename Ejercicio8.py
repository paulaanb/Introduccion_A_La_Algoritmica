Algoritmo: precio con IVA 

#Vamos a calcular el precio final del producto con el IVA incluido

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
