def vida_en_segundos(fecha_nac):
    import datetime

    ahora = datetime.datetime.now()
    nac = datetime.datetime.strptime(fecha_nac, "%d/%m/%Y, %H:%M:%S")
    print(ahora - nac)
    return ahora - nac


vida_en_segundos("11/11/1992, 05:25:00")


def cuanto_falta_primavera():
    import datetime

    ahora = datetime.date.today()
    primavera = datetime.date(ahora.year, 9, 21)
    faltan = int((primavera - ahora).total_seconds() / (60 * 60 * 24))
    print("Faltan", faltan, "días para la primavera")
    return faltan


cuanto_falta_primavera()


def cuando_volver(fecha_salida, dias_licencia):
    import datetime

    salida = datetime.datetime.strptime(fecha_salida, "%d/%m/%Y")
    licencia = datetime.timedelta(days=dias_licencia)
    regreso = salida + licencia
    print(regreso)
    return regreso


cuando_volver("26/09/2020", 200)

feriados = ["12/10/2020", "23/11/2020", "7/12/2020", "8/12/2020", "25/12/2020"]


def dias_habiles(inicio, fin, feriados):
    from datetime import datetime
    from datetime import timedelta

    fecha_feriados = []
    for dia in feriados:
        fecha_feriados.append(datetime.strptime(dia, "%d/%m/%Y"))

    # print(fecha_feriados)

    habiles = 0
    dia = datetime.strptime(inicio, "%d/%m/%Y")
    while (dia >= datetime.strptime(inicio, "%d/%m/%Y")) and dia <= datetime.strptime(
        fin, "%d/%m/%Y"
    ):
        if dia.weekday() < 5 and dia not in fecha_feriados:
            habiles += 1
        dia = dia + timedelta(days=1)

    print(habiles)
    return habiles


dias_habiles("26/09/2020", "11/10/2020", [])
dias_habiles("26/09/2020", "11/10/2020", feriados)
dias_habiles("26/09/2020", "12/10/2020", feriados)
dias_habiles("26/09/2020", "12/12/2020", feriados)
dias_habiles("26/09/2020", "12/12/2020", [])
