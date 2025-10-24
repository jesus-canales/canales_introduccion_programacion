def obtenerDatosEmpleado():
    # Recibimos los datos del usuario
    nombre = input("Ingresa el nombre del colaborador: ");
    salarioBruto = input(f"Ingresa el salario bruto de {nombre} en S/. ");
    porcentajeDescuento = input("Ingresa el porcentaje de descuento en %");

    # Convertir los datos a float para los cálculos
    salarioBrutoValor = float(salarioBruto)
    porcentajeDescuentoValor = float(porcentajeDescuento)
    
    return nombre, salarioBrutoValor, porcentajeDescuentoValor


