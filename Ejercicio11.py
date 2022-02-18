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
