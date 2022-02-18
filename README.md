# Introduccion_A_La_Algoritmica
El link de este repositorio es [https://github.com/paulaanb/Introduccion_A_La_Algoritmica]
Como no habia que poner muchas lineas paso directamente a la explicacion del pseudicodigo
```

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
´´´

Algoritmo: Media arimética

#Calculamos un algoritmo para calcular la media aritmética de tres números dados

Entrada:
#Los números dados son N1, N2 y N3
 N1, N2, N3: REAL 
 
Precondición:
 N1, N2, N3 ≥ 0

Realización:
 Resultado <-- (N1 + N2 + n3) / 3
 
Poscondición:
 Resultado = (N1 + N2 + N3) / 3
 
Fin del cálculo de la media aritmética
 
Algoritmo: Media aritmética

#Calculamos un algoritmo para calcular la media aritmética de tres números con sus respectivos coeficientes de ponderación

Entrada:
#Los números son N1, N2 y N3
 N1, N2, N3: REAL 
#Los coeficientes son C1, C2 y C3
 C1, C2, C3: REAL 

Precondición:
 N1, N2, N3 ≥ 0

 0 < C1, C2, C3  ≤ 1 
 
 
 Realización:
 #Sumatorio del producto
  Resultado <-- Σ(n*c)
  
 Poscondición:
 #Sumatorio del producto
  Resultado <-- Σ(n*c)
  
 Fin del cálculo de la media arirmética con los coeficientes de ponderación
 ´´´
 Algoritmo: Área del triángulo

#Calculamos el área del tríangulo dados un lado y la altura de este

Entrada:
#Lado del triángulo
 l:REAL 
 #Altura del lado
 h: REAL
 
Precondición:
 l > 0
 h > 0

Realización:
 Resultado <-- (l*h)/2
 
Poscondición:
 Resultado = (l*h)/2
 
Fin de calcular el área del triángulo
 ´´´
 Algoritmo: Remuneración de las horas extra

Algoritmo: horas_extra
    # Establece la remuneración de `horas_ext' adicionales para 
    # un salario mensual bruto `salario_mensual_bruto'.

Entrada:
  # Importe del salario mensual bruto
    salario_mensual_bruto : REAL
      
   # Cantidad de horas extra del mes a remunerar
    horas_ext : ENTERO
        
Precondición:
    salario_mensual_bruto > 0
    horas_ext ≥ 0

Constante:
  # Umbral de cambio de precio de remuneración
    CANTIDAD_HORAS_MAX_1 : ENTERO ← 8
    # Precio de remuneración de CANTIDAD_HORAS_MAX_1 primeras
    # horas extra
    PRECIO_1 : REAL ← 1,25
    # Precio de remuneración de las otras horas extra
    PRECIO_2 : REAL ← 1,50
        

Variable:
    # Cantidad de horas extra con PRECIO_1 %
    horas_ext_1 : ENTERO
    # Cantidad de horas extra con PRECIO_2 %    
    horas_ext_2 : ENTERO
    # Precio hora de la remuneración bruta de base   
    precio_hora : REAL
       

Realización:
    # Cálculo del precio_hora de la remuneración bruta de base 
    precio_hora ← precio_hora_bruto(salario_mensual_bruto)

    # Cálculo de la cantidad de horas de cada categoría
    horas_ext_1 ← inf(horas_ext, CANTIDAD_HORAS_MAX_1)
    horas_ext_2 ← sup(horas_ext - CANTIDAD_HORAS_MAX_1, 0)

    # Cálculo de la remuneración de las horas extra
    Resultado ← precio_hora x (horas_ext_1 x PRECIO_1 + horas_ext_2 x PRECIO_2)

Postcondición
...
Fin de las horas_extra


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

Fin del cálculo del interés generado´´´
```Algoritmo: Definición de abrir una cuenta con descubierto autorizado durante un tiempo limitado

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
´´´
```



