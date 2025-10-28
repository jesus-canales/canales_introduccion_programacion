# Reto

# Elaborar un programa que solicite al usuario 5 nombres de países desde la consola
# estos elementos deben irse almacenando en una lista
# luego debe imprimir los elementos de la lista en la consola

# 1. Creamos una lista vacía para guardar los ítems
lista_compras = []

print("Por favor, ingresa 3 ítems para tu lista de compras.")

# 2. Usamos un bucle 'for' para repetir la pregunta 3 veces
for i in range(3):
    # 3. Pedimos el dato al usuario
    item = input(f"Ingresa el ítem #{i+1}: ")
    
    # 4. Usamos .append() para agregar el ítem a la lista
    lista_compras.append(item)

# 5. Imprimimos la lista final
print("\n¡Lista de compras completa!")
print(lista_compras)