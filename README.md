# SEDANI_APP

Aplicación web interactiva desarrollada en Python y Streamlit 
para la práctica y evaluación de estructuras gramaticales 
en el idioma inglés, orientada a adolescentes, adultos y profesionales.

---

## 1. Objetivo

Desarrollar una herramienta digital eficiente e interactiva 
que permita evaluar de forma dinámica la asimilación de 
diferentes tiempos y estructuras gramaticales en inglés, 
ofreciendo un entorno centrado en la precisión sintáctica.

---

## 2. Instalación y Ejecución

Tienes dos formas de utilizar o evaluar la aplicación:

### Opción A: Acceso Directo (Web Desplegada)
Puedes acceder directamente a la aplicación en línea de forma pública y sin instalaciones previas a través del siguiente enlace de Streamlit Cloud:
*(Inserta aquí tu enlace de Streamlit, por ejemplo: https://sedaniapp-sara-alba.streamlit.app)*

### Opción B: Ejecución Local
Si prefieres clonar y configurar el proyecto en tu entorno de desarrollo local:

1. Clona el repositorio:
   git clone https://github.com/saac1019/SEDANI_APP.git

2. Entra a la carpeta del proyecto:
   cd SEDANI_APP

3. Instala las dependencias necesarias:
   pip install -r requirements.txt

4. Ejecuta la aplicación:
   streamlit run src/app.py

---

## 3. Dataset

La base de conocimiento de la aplicación consiste en un 
banco de frases construido y estructurado de forma manual. 

Cada entrada parte de una oración base que se adapta 
sistemáticamente a través de distintos tiempos y estructuras 
gramaticales con un complemento simple, priorizando 
exclusivamente la práctica de la mecánica sintáctica 
por encima de la complejidad del vocabulario. 

El sistema no almacena ningún tipo de dato personal 
o sensible de los usuarios.

---

## 4. Métrica

La evaluación del desempeño se mide mediante:
* **Tasa de aciertos:** Porcentaje de respuestas gramaticales 
  correctas emitidas por el usuario frente al total de 
  evaluaciones realizadas en la sesión.
* **Tiempo de respuesta:** Indicador de agilidad en la 
  identificación de estructuras gramaticales.

---

## 5. Resultados

* Se logró desplegar exitosamente una interfaz gráfica 
  funcional y accesible en la nube mediante Streamlit.
* El sistema procesa de manera fluida las evaluaciones 
  gramaticales y proporciona retroalimentación inmediata 
  al estudiante.
* Se estructuró un código modular bajo el estándar 
  requerido en la carpeta `/src`.

---

## 6. Limitaciones

* **Evaluación escrita:** El sistema está acotado estrictamente a la gramática textual, por lo que **no evalúa audio, pronunciación ni comprensión oral**.
* **Público objetivo:** Está diseñado específicamente para el apoyo pedagógico de adolescentes, adultos y profesionales.
* **Control de errores:** A pesar de haber implementado validaciones y estructuras de control en el código para la gestión de campos vacíos, entradas atípicas y flujos inesperados, pueden presentarse pequeños fallos o casos borde aislados que salgan del margen previsto.
* **Conectividad:** Requiere conexión a internet activa para su uso mediante la versión desplegada en la nube.
