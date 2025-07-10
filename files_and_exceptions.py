def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    try:
        with open(filename, "r") as file:
            reader = file.read()
            pairs_string = reader.split(";")
            pairs = []
            for string in pairs_string:
                if ":" in string:
                    key, value = string.split(":")
                    pairs.append((key, value))
            data_dict = {}
            for key, value in pairs:
                if key not in data_dict:
                    data_dict[key] = [round(float(value), 1)]
                else:
                    data_dict[key].append(round(float(value), 1))
        return data_dict
    except FileNotFoundError:
        raise FileNotFoundError("El archivo no existe")


def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    for producto, precios in data.items():
        prod_sum = sum(precios)
        prod_avg = prod_sum / len(precios)
        print(f"{producto}: ventas totales ${prod_sum:.2f}, promedio ${prod_avg:.2f}")
