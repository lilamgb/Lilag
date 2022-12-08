"""
Lila Guzman
22-0638
Refinando código
aqui, se refinará un código dado y se publicará en un repositorio de Github
"""
import sys 

def costos_lista():
    """Función que devuelve una lista de costos del archivo gift_costs.txt"""
    with open('gift_costs.txt', 'r', encoding='UTF-8') as archive:
        gift_costs = list(archive)
    try:
      gift_costs = [int(c) for c in gift_costs]  # convierte strings a int
    except ValueError:
      print('Los datos deben ser dígitos.')
      sys.exit()
        
    return gift_costs


def total(gift_costs):
    """Función que suma los precios de la lista de costos para conseguir un total"""
    total_price = 0
    for cost in gift_costs:
        if cost > 1000:
            total_price += cost * 1.16  # agrega impuestos
        else:
            total_price += cost  # los costos menores a 1000 no se le agrega impuesto

    return total_price


def main():
    """Función principal que llama ambas funciones e imprime el total"""
    print(total(costos_lista()))
  
if __name__ == '__main__':
    main()
