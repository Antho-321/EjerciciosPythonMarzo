jornada = 48
hTrabajadas = 49
pagoHora = 2
pagohExtra = 3.5
if hTrabajadas<=jornada:
    salario = hTrabajadas*pagoHora
else:
    salario = ((hTrabajadas//jornada)*jornada)*pagoHora+(hTrabajadas-(hTrabajadas//jornada)*jornada)*pagohExtra
print("Su salario es:",salario)