comprobante = "boleta"
monto = 100

if comprobante == "factura":
    igv = monto * 0.18
    pagar = monto + igv
    print(f"El monto total a pagar con factura es: {pagar}")
elif comprobante == "boleta":
    print(f"El monto total a pagar con boleta es: {monto}")
else:
    print("Debe elegir un comprobante válido")
