"""
Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. 
Informar:
- Las cantidades totales de cada artículo.
- La cantidad de artículos en la sucursal 2.
- La cantidad del artículo 3 en la sucursal 1.
- La recaudación total de cada sucursal.
- La recaudación total de la empresa.
- La sucursal de mayor recaudación.
"""
def verMatriz(matriz):
    for linea in matriz:
        print(linea)

def verEmpresa(empresa):
    print("Empresa: ")
    for i in range(len(empresa)):
        print(f"Sucursal {i+1}: ", end="")
        print(empresa[i])

empresa = []

#defino los precios de los articulos
articulos = []
for i in range(5):
    valor_articulo = float(input(f"Valor del articulo {i+1}: "))
    articulos.append(valor_articulo)

#defino lo vendido de cada articulo en cada sucursal
for sucursal in range(1,5):
    sucursal_cantidades = []

    for articulo in range(len(articulos)):
        cantidad_vendido = int(input(f"Cantidad vendida del articulo {articulo+1} en la sucursal {sucursal}: "))
        sucursal_cantidades.append(cantidad_vendido)
    print("\n")
    empresa.append(sucursal_cantidades)


verEmpresa(empresa)
print("\n")

#cantidades totales de cada artículo
for articulo in range (len(articulos)):
    cantidades_totales_articulo = 0
    for sucursal in empresa:
        cantidades_totales_articulo += sucursal[articulo]
    print(f"Cantidad total del articulo {articulo+1}: {cantidades_totales_articulo}")

#cantidad de artículos en la sucursal 2.
print(f"Cantidad de articulos en la sucursal 2: {sum(empresa[1])}")

#cantidad del artículo 3 en la sucursal 1.
print(f"Cantidad del articulo 3 en la sucursal 1: {empresa[0][2]}")

#recaudación total de cada sucursal. y recaudacion total de la empresa
recaudacion_total = 0
mayor = -1
for sucursal in empresa:
    recaudacion_sucursal = 0
    
    for i in range(len(sucursal)):
        recaudacion_sucursal += articulos[i]*sucursal[i]
    print(f"Cantidad recaudada por la sucursal {empresa.index(sucursal)+1}: {recaudacion_sucursal}")

    recaudacion_total += recaudacion_sucursal

    #mayor recaudado
    if recaudacion_sucursal > mayor:
        mayor = recaudacion_sucursal
        sucursal_mayor = empresa.index(sucursal)+1

print(f"Cantidad recaudada por la empresa: {recaudacion_total}")

print(f"La sucursal que mas recaudo fue la Sucursal {sucursal_mayor}")






