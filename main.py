from utils.proceso import Proceso


if __name__ == "__main__":
    # Se realiza la instancia
    transaccion: Proceso = Proceso("./data.csv")
    print("\nReporte de Transacciones")
    print("-"*50)
    print(
        "Balance Final: S/. {balance:.2f}".format(balance=transaccion.balance()))
    print("Transacción de Mayor Monto: ID {id} - S/. {monto:.2f}".format(
        id=transaccion.monto_mayor.id, monto=transaccion.monto_mayor.monto))
    print("Conteo de Transacciones: Crédito: {credito}, Débito: {debito}\n".format(
        credito=transaccion.n_credito, debito=transaccion.n_debito))
