import streamlit as st

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title=" Sistema Experto de Diagnóstico Adaptativo del Idioma Inglés (SEDANI) ", page_icon="🇺🇸📖🇬🇧")

# --- BASE DE CONOCIMIENTOS (Reglas y Preguntas) ---
KNOWLEDGE_BASE = {
    "Básico": [
        {
            "estimulo": "Yo estoy comiendo pizza",
            "respuestas_esperadas": ["i am eating pizza", "i'm eating pizza"]
        },
        {
            "estimulo": "Yo he comido pizza",
            "respuestas_esperadas": ["i have eaten pizza", "i've eaten pizza"]
        },
        {
            "estimulo": "Yo no estaba comiendo pizza",
            "respuestas_esperadas": ["i was not eating pizza", "i wasn't eating pizza"]
        },
        {
            "estimulo": "Yo debería comer pizza",
            "respuestas_esperadas": ["i should eat pizza"]
        }
    ],
    "Intermedio": [
        {
            "estimulo": "Yo solía comer pizza",
            "respuestas_esperadas": ["i used to eat pizza"]
        },
        {
            "estimulo": "Se supone que yo no coma pizza",
            "respuestas_esperadas": ["i am not supposed to eat pizza", "i'm not supposed to eat pizza"]
        },
        {
            "estimulo": "Yo lo obligo a comer pizza",
            "respuestas_esperadas": ["i make him eat pizza"]
        }
    ]
}

# INICIALIZACIÓN DE VARIABLES (Memoria de la app)
if 'fase' not in st.session_state:
    st.session_state.fase = 'inicio'
if 'nivel_idx' not in st.session_state:
    st.session_state.nivel_idx = 0
if 'pregunta_idx' not in st.session_state:
    st.session_state.pregunta_idx = 0
if 'niveles' not in st.session_state:
    st.session_state.niveles = list(KNOWLEDGE_BASE.keys())
if 'nivel_final' not in st.session_state:
    st.session_state.nivel_final = ""

# Variables Blandas y de Memoria
if 'nombre_estudiante' not in st.session_state:
    st.session_state.nombre_estudiante = ""
if 'clases_previas' not in st.session_state:
    st.session_state.clases_previas = ""
if 'motivo_aprendizaje' not in st.session_state:
    st.session_state.motivo_aprendizaje = ""
if 'historial_respuestas' not in st.session_state:
    st.session_state.historial_respuestas = []

# MANEJO DE ERRORES
def normalizar_respuesta(texto):
    texto_limpio = texto.lower()
    
    # 1. Quitar puntos finales
    texto_limpio = texto_limpio.replace(".", "")
    # 2. Obviar ortografía de la palabra de complemento "pizza"
    texto_limpio = texto_limpio.replace("piza", "pizza").replace("pisa", "pizza")
    # 3. Homologar apóstrofes
    texto_limpio = texto_limpio.replace("’", "'").replace("´", "'")
    # 4. Quitar problema de espaciados: Elimina dobles espacios internos y espacios al inicio/final
    texto_limpio = " ".join(texto_limpio.split())
    # 5. Problemas de mayúsculas: Esta línea agarra el texto ya procesado y asegura las minúsculas
    texto_limpio = texto_limpio.lower() 
    
    return texto_limpio

# INTERFAZ DE USUARIO 
st.title("Sistema Experto de Diagnóstico Adaptativo del Idioma Inglés 🇺🇸📖🇬🇧")
st.write("SEDANI")
st.divider()

# NUEVO: Nota de Transparencia Ética
st.info("💡 **Nota del Sistema:** Esta evaluación está enfocada estrictamente en tu dominio de la **gramática**. Si cometes un error ortográfico menor en la palabra de complemento (por ejemplo, escribir 'piza' o 'pisa' en lugar de 'pizza'), el algoritmo lo pasará por alto para no penalizarte injustamente y se enfocará en evaluar la estructura correcta de tus tiempos verbales.")

# FASE 1: INICIO (Recopilación de Perfil Conceptual) 
if st.session_state.fase == 'inicio':
    st.subheader("Recopilación de Perfil Conceptual")
    st.write("Por favor, completa tus datos para personalizar la evaluación.")
    
    st.session_state.nombre_estudiante = st.text_input("Nombre completo:")
    
    st.session_state.clases_previas = st.selectbox(
        "¿Has tomado clases de inglés anteriormente?",
        ["Selecciona una opción...", "Sí", "No"]
    )
    
    st.session_state.motivo_aprendizaje = st.selectbox(
        "Motivo por el cual buscas aprender el idioma:",
        ["Selecciona una opción...", "Viaje", "Trabajo", "Estudio", "Hobby", "Otro"]
    )
    
    if st.button("Comenzar Evaluación"):
        if st.session_state.nombre_estudiante and st.session_state.clases_previas != "Selecciona una opción..." and st.session_state.motivo_aprendizaje != "Selecciona una opción...":
            st.session_state.fase = 'prueba'
            st.rerun()
        else:
            st.warning("⚠️ Por favor, completa todos los campos del perfil conceptual para continuar.")

# FASE 2: MOTOR DE INFERENCIA (Prueba)
elif st.session_state.fase == 'prueba':
    nivel_actual = st.session_state.niveles[st.session_state.nivel_idx]
    reactivo = KNOWLEDGE_BASE[nivel_actual][st.session_state.pregunta_idx]
    
    st.subheader(f"Traduce al inglés: '{reactivo['estimulo']}'")
    
    with st.form(key='form_prueba', clear_on_submit=True):
        respuesta_usuario = st.text_input("Tu traducción:")
        enviado = st.form_submit_button("Enviar traducción")
        
        if enviado:
            # Validaciones Críticas (respuestas vacías, números o caraácteres especiales)
            if not respuesta_usuario.strip():
                st.warning("Escribe una respuesta antes de enviar.")
            elif not any(c.isalpha() for c in respuesta_usuario):
                st.error("Error: Ingrese una oración válida. No se permiten solo números ni caracteres especiales.")
            else:
                respuesta_limpia = normalizar_respuesta(respuesta_usuario)
                
                if respuesta_limpia in reactivo['respuestas_esperadas']:
                    # Guardar acierto en el historial
                    st.session_state.historial_respuestas.append({
                        "estimulo": reactivo['estimulo'],
                        "respuesta_usuario": respuesta_usuario,
                        "esperadas": reactivo['respuestas_esperadas'],
                        "acierto": True
                    })
                    
                    st.session_state.pregunta_idx += 1
                    
                    if st.session_state.pregunta_idx >= len(KNOWLEDGE_BASE[nivel_actual]):
                        st.session_state.nivel_idx += 1
                        st.session_state.pregunta_idx = 0
                        
                        if st.session_state.nivel_idx >= len(st.session_state.niveles):
                            st.session_state.nivel_final = "AVANZADO"
                            st.session_state.fase = 'resultado'
                else:
                    # Guardar fallo en el historial
                    st.session_state.historial_respuestas.append({
                        "estimulo": reactivo['estimulo'],
                        "respuesta_usuario": respuesta_usuario,
                        "esperadas": reactivo['respuestas_esperadas'],
                        "acierto": False
                    })
                    
                    st.session_state.nivel_final = nivel_actual.upper()
                    st.session_state.fase = 'resultado'
                
                st.rerun()

# FASE 3: RESULTADO E INFORME DIAGNÓSTICO 
elif st.session_state.fase == 'resultado':
    st.success("¡Evaluación completada con éxito!")
    
    # 1. Mostrar el Perfil Conceptual y el Diagnóstico Final
    st.header(f"Diagnóstico Final: Nivel {st.session_state.nivel_final}")
    st.divider()
    
    st.subheader("📄 Perfil Conceptual del Estudiante")
    st.write(f"**Nombre:** {st.session_state.nombre_estudiante}")
    st.write(f"**¿Ha tomado clases previas?:** {st.session_state.clases_previas}")
    st.write(f"**Motivo de Aprendizaje:** {st.session_state.motivo_aprendizaje}")
    
    st.divider()
    
    # 2. Mostrar el Informe Diagnóstico (Explicabilidad)
    st.subheader("📊 Informe Diagnóstico Detallado")
    st.write("Desglose de tus respuestas frente al patrón esperado:")
    
    for item in st.session_state.historial_respuestas:
        if item['acierto']:
            st.success(f"✅ **{item['estimulo']}**\n\nTu respuesta: *{item['respuesta_usuario']}*")
        else:
            # Unimos las opciones válidas con una barra para mostrarlas
            patrones_validos = " / ".join(item['esperadas'])
            st.error(f"❌ **{item['estimulo']}**\n\nTu respuesta: *{item['respuesta_usuario']}*\n\n**Patrón gramatical esperado:** *{patrones_validos}*")
    
    st.divider()
    
    # Botón para reiniciar
    if st.button("Evaluar a otro estudiante"):
        st.session_state.fase = 'inicio'
        st.session_state.nivel_idx = 0
        st.session_state.pregunta_idx = 0
        st.session_state.nivel_final = ""
        st.session_state.nombre_estudiante = ""
        st.session_state.clases_previas = ""
        st.session_state.motivo_aprendizaje = ""
        st.session_state.historial_respuestas = [] # Vaciamos la memoria
        st.rerun()