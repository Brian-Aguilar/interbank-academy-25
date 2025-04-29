from decimal import Decimal
from models.transacciones import Transaccion


class Proceso:
    # Clase donde tiene toda la funcionalidad de Proceso
    def __init__(self, ruta: str = "data.csv") -> None:
        # OPCIONAL: crear la variable transacciones
        self.transacciones: list[Transaccion] = []
        self.monto_mayor: Transaccion = Transaccion()
        self.credito: float = 0
        self.debito: float = 0
        self.n_credito: int = 0
        self.n_debito: int = 0
        self.path: str = ruta
        self.__load()

    # INFO: Funcion privada para leer el archivo
    def __load(self) -> None:
        # INFO: Se utiliza open en modo 'r' => solo lectura, para obtener los datos del archivo en formato utf-8
        # TODO: Se puede utilizar la libreria pandas para almacenar la información en vectores
        # pandas.read_csv("data.csv")
        with open(self.path, 'r', encoding='utf-8') as data:
            # INFO: Omite la cabecera [ID - TIPO - MONTO]
            data.readline()
            for x in data:
                # INFO: Con split en "," convertimos los datos en una lista separada por la coma.
                datos_crudos: list = x.rstrip().split(',')
                transaccion: Transaccion = Transaccion(
                    int(datos_crudos[0]),
                    str(datos_crudos[1]),
                    float(datos_crudos[2]))
                # OPCIONAL: Agregar a la lista transacciones
                self.transacciones.append(transaccion)
                if self.monto_mayor.monto < transaccion.monto:
                    self.monto_mayor = transaccion
                # INFO: Con la libreria pandas con el dataframe se realiza la suma y el conteo de los tipos de una manera más facil
                # pd[["TIPO"]].values_count() => Crédito: n Débito: n
                # pd[["TIPO".str.contains("Crédito")]]["TIPO"].sum()
                # pd[["TIPO".str.contains("Débito")]]["TIPO"].sum()
                if transaccion.tipo == "Crédito":
                    self.n_credito += 1
                    self.credito = Decimal(str(self.credito)) \
                        + Decimal(str(transaccion.monto))
                if transaccion.tipo == "Débito":
                    self.n_debito += 1
                    self.debito = Decimal(
                        str(self.debito)) + Decimal(str(transaccion.monto))

    # INFO: Función para obtener el balance de los datos obtenidos
    def balance(self) -> float:
        return abs(Decimal(str(self.credito)) - Decimal(str(self.debito)))
