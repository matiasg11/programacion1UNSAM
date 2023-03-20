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

# pago_extra_mes_comienzo = int(input("Mes comienzo de pago extra: "))
# pago_extra_mes_fin = int(input("Mes fin de pago extra: "))
# pago_extra = int(input("Pago extra: "))

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while deuda > 0:

    if pagos >= pago_extra_mes_comienzo and pagos <= pago_extra_mes_fin:
        deuda = deuda*(1+(tasa/12)) - pago - pago_extra
        pagado = pagado + pago + pago_extra
    else:
        deuda = deuda*(1+(tasa/12)) - pago
        pagado = pagado + pago
    pagos = pagos+1
print("Pagado: $", round(pagado, 2), "Pagos:", round(pagos), "\n")


print("Ejercicio 1.10\nTablas")

tasa = 0.05
monto_i = 500000
deuda = monto_i
pagado = 0
pago = 2684.11
periodo = 1
pagos = 0

# pago_extra_mes_comienzo = int(input("Mes comienzo de pago extra: "))
# pago_extra_mes_fin = int(input("Mes fin de pago extra: "))
# pago_extra = int(input("Pago extra: "))

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while deuda > 0:

    if pagos >= pago_extra_mes_comienzo and pagos <= pago_extra_mes_fin:
        deuda = deuda*(1+(tasa/12)) - pago - pago_extra
        pagado = pagado + pago + pago_extra
    else:
        deuda = deuda*(1+(tasa/12)) - pago
        pagado = pagado + pago
    pagos = pagos+1
    print((pagos), "\t", round(pagado, 2), "\t", round(deuda, 2))

print("Pagado: $", round(pagado, 2), "Meses:", round(pagos), "\n")
