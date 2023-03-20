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
pagos = 0

# pago_extra_mes_comienzo = int(input("Mes comienzo de pago extra: "))
# pago_extra_mes_fin = int(input("Mes fin de pago extra: "))
# pago_extra = int(input("Pago extra: "))

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while deuda > 0:
    if pagos >= pago_extra_mes_comienzo and pagos <= pago_extra_mes_fin:
        deuda = deuda - pago_extra
        pagado = pagado + pago_extra

    if deuda < pago:
        pago = deuda
        deuda = 0

    else:
        deuda = deuda*(1+(tasa/12)) - pago
    pagado = pagado + pago

    pagos = pagos+1
    print((pagos), "\t", round(pagado, 2), "\t", round(deuda, 2))

print("Total pagado:", round(pagado, 2))
print("Meses:", round(pagos))
