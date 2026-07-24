# src/test_app.py

def normalizar_respuesta(texto):
    """
    Función de pre-procesamiento para limpiar la entrada del usuario.
    """
    if not texto:
        return ""
        
    texto_limpio = texto.lower()
    
    # 1. Quitar puntos finales
    texto_limpio = texto_limpio.replace(".", "")
    # 2. Obviar ortografía de la palabra de complemento "pizza"
    texto_limpio = texto_limpio.replace("piza", "pizza").replace("pisa", "pizza")
    # 3. Homologar apóstrofes
    texto_limpio = texto_limpio.replace("’", "'").replace("´", "'")
    # 4. Quitar problema de espaciados: Elimina dobles espacios internos y espacios al inicio/final
    texto_limpio = " ".join(texto_limpio.split())
    # 5. Problemas de mayúsculas (Corregido para no sobreescribir la variable)
    texto_limpio = texto_limpio.lower() 
    
    return texto_limpio

def evaluar_gramatica(frase_usuario, patrones_esperados):
    """
    Simula el motor de inferencia comparando la entrada normalizada 
    con las reglas de la base de conocimiento.
    """
    # Manejo del caso vacío
    if not frase_usuario or not frase_usuario.strip():
        return {"estado": "Error", "detalle": "Entrada vacía detectada"}
        
    # Manejo de solo números o caracteres especiales
    if not any(c.isalpha() for c in frase_usuario):
        return {"estado": "Error", "detalle": "Entrada inválida (solo números o símbolos)"}
        
    usuario_limpio = normalizar_respuesta(frase_usuario)
    
    # Evalúa si la entrada limpia coincide con alguna de las opciones válidas
    if usuario_limpio in patrones_esperados:
        return {"estado": "Éxito", "detalle": "Estructura gramatical correcta"}
    else:
        return {"estado": "Fallo", "detalle": "Diferencia en la estructura sintáctica"}

def ejecutar_suite_pruebas():
    # Base de conocimiento (Matriz de Patrones del sistema)
    base_conocimiento = {
        "presente_continuo": ["i am eating pizza", "i'm eating pizza"],
        "presente_perfecto": ["i have eaten pizza"],
        "pasado_continuo_neg": ["i was not eating pizza", "i wasn't eating pizza"],
        "modales_simples": ["i should eat pizza"],
        "used_to": ["i used to eat pizza"],
        "be_supposed_to": ["i am not supposed to eat pizza", "i'm not supposed to eat pizza"],
        "causative_verbs": ["i make him eat pizza"]
    }

    # Definición de la suite de pruebas (Entradas vs Comportamiento Esperado del Sistema)
    casos_prueba = [
        # Pruebas de Flujo Normal (Verdaderos Positivos)
        {"input": "I am eating pizza", "patrones": base_conocimiento["presente_continuo"], "sistema_debe_arrojar": "Éxito", "tipo": "Normal - Correcta"},
        {"input": "I have eaten pizza", "patrones": base_conocimiento["presente_perfecto"], "sistema_debe_arrojar": "Éxito", "tipo": "Normal - Correcta"},
        
        # Prueba de Error Gramatical del Alumno (Verdadero Negativo)
        {"input": "I was not eat pizza", "patrones": base_conocimiento["pasado_continuo_neg"], "sistema_debe_arrojar": "Fallo", "tipo": "Normal - Gramática Incorrecta"},
        
        # Pruebas de Casos Borde (El algoritmo debe normalizarlos y dar Éxito)
        {"input": "I'm eating piza.", "patrones": base_conocimiento["presente_continuo"], "sistema_debe_arrojar": "Éxito", "tipo": "Borde - Punto final y error en 'pizza'"},
        {"input": "I SHOULD EAT PIZZA", "patrones": base_conocimiento["modales_simples"], "sistema_debe_arrojar": "Éxito", "tipo": "Borde - Uso de Mayúsculas"},
        {"input": "   I   used to   eat  pizza   ", "patrones": base_conocimiento["used_to"], "sistema_debe_arrojar": "Éxito", "tipo": "Borde - Dobles espacios"},
        {"input": "I´m not supposed to eat pisa", "patrones": base_conocimiento["be_supposed_to"], "sistema_debe_arrojar": "Éxito", "tipo": "Borde - Apóstrofe raro y error en 'pizza'"},
        
        # Prueba de Caso Borde Crítico
        {"input": "", "patrones": base_conocimiento["causative_verbs"], "sistema_debe_arrojar": "Error", "tipo": "Borde Crítico - Entrada Vacía"},
        {"input": "12345 @#%", "patrones": base_conocimiento["presente_continuo"], "sistema_debe_arrojar": "Error", "tipo": "Borde Crítico - Solo números y símbolos"}
    ]

    total_pruebas = len(casos_prueba)
    pruebas_exitosas_algoritmo = 0

    print("=== INICIANDO SUITE DE PRUEBAS AUTOMATIZADAS - SEDANI_APP ===")
    
    for i, caso in enumerate(casos_prueba, 1):
        resultado = evaluar_gramatica(caso["input"], caso["patrones"])
        
        print(f"\nPrueba #{i} [{caso['tipo']}]")
        print(f"  - Entrada del usuario: '{caso['input']}'")
        print(f"  - Acción del sistema: {resultado['estado']} ({resultado['detalle']})")
        
        # El algoritmo pasa la prueba si se comporta como esperábamos que lo hiciera
        if resultado["estado"] == caso["sistema_debe_arrojar"]:
            print("  [✓] Prueba Superada (Comportamiento esperado)")
            pruebas_exitosas_algoritmo += 1
        else:
            print("  [x] Fallo en la prueba del algoritmo")

    # Cálculo de la Métrica de Exactitud (Accuracy)
    accuracy = (pruebas_exitosas_algoritmo / total_pruebas) * 100
    
    print("\n" + "="*50)
    print("REPORTE DE MÉTRICAS (ACCURACY):")
    print(f"  - Total de simulaciones ejecutadas: {total_pruebas}")
    print(f"  - Evaluaciones algorítmicas correctas: {pruebas_exitosas_algoritmo}")
    print(f"  - Exactitud Global (Accuracy): {accuracy:.2f}%")
    print("="*50)

if __name__ == "__main__":
    ejecutar_suite_pruebas()