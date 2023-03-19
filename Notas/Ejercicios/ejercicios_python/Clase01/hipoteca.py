# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca
print("Ejercicio de Hipoteca - Clase 1\n")

"""David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%. Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.

El siguiente es un programa que calcula el monto total que pagará David a lo largo de los años:"""

tasa = 0.05
monto_i = 500000
deuda = monto_i
pagado = 0
pago = 2684.11


while deuda > 0:
    deuda = deuda*(1+(tasa/12)) - pago
    pagado = pagado + pago

print("Ejercicio 1.7")
print("Pagado: $", round(pagado, 1), "Pagos:", round(pagado/pago), "\n")


print("Ejercicio 1.8\nAdelantos de $1000 por los primeros 12 meses")

tasa = 0.05
monto_i = 500000
deuda = monto_i
pagado = 0
pago = 2684.11
periodo = 1
pagos = 0

while deuda > 0:

    if periodo <= 12:
        deuda = deuda*(1+(tasa/12)) - pago - 1000
        periodo = periodo + 1
        pagado = pagado + pago + 1000
    else:
        deuda = deuda*(1+(tasa/12)) - pago
        pagado = pagado + pago
    pagos = pagos+1
print("Pagado: $", round(pagado, 2), "Pagos:", round(pagos), "\n")


print("Ejercicio 1.9\nCalculadora de adelantos")

tasa = 0.05
monto_i = 500000
deuda = monto_i
pagado = 0
pago = 2684.11
periodo = 1
pagos = 0

while deuda > 0:

    if pagos > 5*12 and pagos < 9*12:
        deuda = deuda*(1+(tasa/12)) - pago - 1000
        pagado = pagado + pago + 1000
    else:
        deuda = deuda*(1+(tasa/12)) - pago
        pagado = pagado + pago
    pagos = pagos+1
print("Pagado: $", round(pagado, 2), "Pagos:", round(pagos), "\n")
