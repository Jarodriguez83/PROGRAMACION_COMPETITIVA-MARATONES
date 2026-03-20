import exercise_h
#DEFINIMOS LOS CASOS DE PRUEBA
def test_ip():
    #CASO 1: CORRECTO
    assert exercise_h.main(
        "192.168.0.1",
        "11000000.10101000.00000000.00000001"
    ) == "Case 1: YES\n"
    #CASO 2: INCORRECTO
    assert exercise_h.main(
        "10.0.0.1",
        "00001010.00000000.00000000.00000010"
    ) == "Case 2: NO\n"
    print("Todos los casos de prueba pasaron exitosamente.")
#EJECUTAMOS LOS CASOS DE PRUEBA
if __name__ == "__main__":
    test_case_1()
