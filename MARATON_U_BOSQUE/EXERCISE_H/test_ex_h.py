#IMPORTAR LA LIBRERÍA DE PRUEBAS UNITARIAS
import unittest
#IMPORTAR LA FUNCIÓN A PROBAR
from exercise_h import main
#CREAR LA CLASE DE PRUEBAS
class TestExerciseH(unittest.TestCase):

    def test_1(self): 
        """PRUEBA DE CASO DE PRUEBA 1 - NO SON IGUALES"""
        # SIMULAR LA ENTRADA
        input_data = "1\n192.168.0.100\n11000000.10101000.00000000.11001000\n"
        resultado = "Case 1: NO\n"
        # REDIRECCIONAR LA ENTRADA Y SALIDA
        from io import StringIO #IMPORTAR StringIO PARA SIMULAR LA ENTRADA Y SALIDA
        import sys #IMPORTAR sys PARA REDIRECCIONAR LA ENTRADA Y SALIDA
        sys.stdin = StringIO(input_data) # REDIRECCIONAR LA ENTRADA
        sys.stdout = StringIO() # REDIRECCIONAR LA SALIDA
        # LLAMAR A LA FUNCIÓN PRINCIPAL
        main()
        # OBTENER LA SALIDA
        output = sys.stdout.getvalue()
        # COMPARAR LA SALIDA CON EL RESULTADO ESPERADO
        self.assertEqual(output, resultado)
        print("Test 1 passed")
    
    def test_2(self):
        """PRUEBA DE CASO DE PRUEBA 2 - SON IGUALES"""
        # SIMULAR LA ENTRADA
        input_data = "1\n65.254.63.122\n01000001.11111110.00111111.01111010\n"
        resultado = "Case 1: YES\n"
        # REDIRECCIONAR LA ENTRADA Y SALIDA
        from io import StringIO #IMPORTAR StringIO PARA SIMULAR LA ENTRADA Y SALIDA
        import sys #IMPORTAR sys PARA REDIRECCIONAR LA ENTRADA Y SALIDA
        sys.stdin = StringIO(input_data) # REDIRECCIONAR LA ENTRADA
        sys.stdout = StringIO() # REDIRECCIONAR LA SALIDA
        # LLAMAR A LA FUNCIÓN PRINCIPAL
        main()
        # OBTENER LA SALIDA
        output = sys.stdout.getvalue()
        # COMPARAR LA SALIDA CON EL RESULTADO ESPERADO
        self.assertEqual(output, resultado)
    print("Test 2 passed")
        