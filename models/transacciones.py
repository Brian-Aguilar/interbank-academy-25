class Transaccion:
    # Clase para mapear (serealizar) los datos obtenidos del archivo csv
    def __init__(self, id: int = 0, tipo: str = "", monto: float = 0.0) -> None:
        self.id: int = id
        self.tipo: str = tipo
        self.monto: float = monto

    # Se modifica la respuesta cuando se llama solo la variable tipo Transaccion
    def __str__(self) -> str:
        return "{\"id\": " + str(self.id) + ", \"tipo\": " + self.tipo + ", \"monto\": " + str(self.monto) + "}"
