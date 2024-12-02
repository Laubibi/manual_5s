import os
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from PIL import Image
import numpy as np
from datetime import datetime
import random
# configuracion de la pagina como primera llamada de Streamlit
st.set_page_config(
        page_title="Manual 5S ARA", 
        page_icon="🚚", 
        layout="wide")

# Configuración de colores
COLORES_ARA = {
    'naranja_principal': '#FF6600',  # Color naranja principal
    'naranja_claro': '#FF8533',     # Naranja degradado
    'blanco': '#FFFFFF',            # Blanco para fondo de otras secciones
    'azul_oscuro': '#003366',       # Azul oscuro para textos
}

def aplicar_estilos_portada():
    """Estilos exclusivos para la portada."""
    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(180deg, {COLORES_ARA['naranja_principal']} 0%, {COLORES_ARA['naranja_claro']} 100%);
    }}
    /* Ajuste de la barra lateral */
    [data-testid="stSidebar"] {{
        background-color: #FF4500 !important; /* Fondo naranja oscuro */
        color: white !important; /* Texto blanco */
    }}
    [data-testid="stSidebar"] .css-1v3fvcr {{
        color: white !important; /* Texto del radio blanco */
    }}
    [data-testid="stSidebar"] .css-1v3fvcr:hover {{
        color: #FFD700 !important; /* Texto amarillo al pasar el ratón */
    }}
    h1, h2, h3 {{
        color: {COLORES_ARA['blanco']};
    }}
    p {{
        color: {COLORES_ARA['blanco']};
        font-size: 1.2rem;
    }}
    </style>
    """, unsafe_allow_html=True)


def aplicar_estilos_generales():
    """Estilos generales para las secciones distintas a la portada."""
    st.markdown(f"""
    <style>
    .stApp {{
        background-color: {COLORES_ARA['blanco']};
    }}
    /* Ajuste de la barra lateral */
    [data-testid="stSidebar"] {{
        background-color: {COLORES_ARA['blanco']} !important; /* Fondo blanco */
        color: {COLORES_ARA['azul_oscuro']} !important; /* Texto azul oscuro */
    }}
    [data-testid="stSidebar"] .css-1v3fvcr {{
        color: {COLORES_ARA['azul_oscuro']} !important; /* Texto del radio azul oscuro */
    }}
    [data-testid="stSidebar"] .css-1v3fvcr:hover {{
        color: {COLORES_ARA['naranja_principal']} !important; /* Texto naranja al pasar el ratón */
    }}
    h1, h2, h3 {{
        color: {COLORES_ARA['naranja_principal']};
        font-weight: bold;
    }}
    p {{
        color: {COLORES_ARA['azul_oscuro']};
        font-size: 1rem;
    }}
    </style>
    """, unsafe_allow_html=True)

def pagina_inicio():
    mostrar_logo()
    aplicar_estilos_portada()
    st.markdown("""
        <div style='text-align: center; padding: 2rem;'>
            <h1 style='font-size: 3.5rem; margin-bottom: 1rem;'>Manual de Implementación</h1>
            <h2 style='font-size: 4.5rem; margin-bottom: 2rem;'>5S - COLED</h2>
            <p>Sistema Integral de Mejora Continua</p>
        </div>
    """, unsafe_allow_html=True)

    # Grid de las 5S
    col1, col2, col3, col4, col5 = st.columns(5)
    for col, letra, texto in zip(
        [col1, col2, col3, col4, col5],
        ["C", "O", "L", "E", "D"],
        ["Clasificar", "Ordenar", "Limpiar", "Estandarizar", "Disciplinar"]
    ):
        with col:
            st.markdown(f"""
                <div style='background: rgba(255, 255, 255, 0.9); padding: 1rem; border-radius: 10px; text-align: center;'>
                    <h3 style='color: {COLORES_ARA['naranja_principal']}; font-size: 2rem;'>{letra}</h3>
                    <p style='color: {COLORES_ARA['azul_oscuro']};'>{texto}</p>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align: center; padding: 2rem;'>
            <p>
                Una guía para la implementación de la metodología 5S en centros de distribución ARA.
            </p>
            <p>Desarrollado por el equipo de proyectos de logística</p>
            <p style='margin-top: 2rem;'>
                JERÓNIMO MARTINS COLOMBIA - ARA - Alegria al mejor precio<br>
                © 2024 Todos los derechos reservados
            </p>
        </div>
    """, unsafe_allow_html=True)

def contexto_5s():
    mostrar_logo()
    st.title("🔍 Contexto de las 5S")
    
    st.markdown("""
    ## ¿Qué son las 5S?
    
    Las 5S son una metodología japonesa diseñada para transformar el entorno laboral, mejorando la organización, la limpieza y la disciplina. 
    Este sistema es fundamental para promover una cultura de **seguridad**, **mejora continua** y **eficiencia** en cualquier organización.

    ### Origen de las 5S
    - **Desarrollado en Japón:** Parte esencial del Sistema de Producción Toyota.
    - **Nombre:** Deriva de cinco palabras japonesas que describen pasos clave para la mejora del espacio de trabajo:
      1. **Seiri:** Clasificar.
      2. **Seiton:** Ordenar.
      3. **Seiso:** Limpiar.
      4. **Seiketsu:** Estandarizar.
      5. **Shitsuke:** Disciplinar.

    ### ¿Por qué implementar las 5S?
     La metodología 5S no solo organiza el espacio físico, sino que también:
    - Fomenta una **cultura de seguridad laboral**, minimizando riesgos y accidentes.
    - Crea un entorno que **apoya la mejora continua** en procesos y operaciones.
    - Refuerza los valores de **disciplina** y **trabajo en equipo**, fortaleciendo la cultura organizacional.

     ### Beneficios clave
    - **Seguridad:** Un espacio de trabajo organizado y limpio reduce riesgos, protege a los empleados y crea confianza.
    - **Eficiencia:** Menos tiempo perdido buscando herramientas o productos.
    - **Cultura:** Impulsa hábitos positivos y fomenta la participación activa del personal en el mejoramiento de su entorno laboral.
    - **Productividad:** Los procesos se vuelven más ágiles y menos propensos a errores.
    
    """)
    st.image("images/las 5s.png", caption="Contexto de las 5S en la Logística", use_container_width=True)
    
def introduccion_coled():
    """Sección: Introducción a la metodología COLED."""
    aplicar_estilos_generales()
    st.title("🚀 Metodología C.O.L.E.D")
    st.markdown("""
    ## ¿Qué es C.O.L.E.D?
    Un acrónimo fácil de recordar que representa las 5 etapas de mejora continua:
    - **C**lasificar: Separar lo necesario de lo innecesario
    - **O**rdenar: Organizar de manera eficiente
    - **L**impiar: Mantener un espacio impecable
    - **E**standardizar: Crear procedimientos consistentes
    - **D**isciplinar: Mantener y mejorar continuamente
    """)
    st.image("images/las 5s.png", caption="Metodología C.O.L.E.D",use_container_width=True )

def mostrar_logo():
    """Muestra el logo de la empresa en la parte superior de cada sección."""
    try:
        st.image("images/ARA.png", width=300, use_container_width=False)
    except FileNotFoundError:
        st.warning("No se encontró el logo en la carpeta 'images'. Verifica que el archivo esté en la ruta correcta.")

def main():
    st.sidebar.title("Manual 5S ARA")
    
    # Menú de navegación
    seccion = st.sidebar.radio(
        "Seleccione una sección:",
        ["Inicio","Contexto de las 5S"," Metodología C.O.L.E.D", "Clasificar (Seiri)", "Ordenar (Seiton)", "Limpiar (Seiso)", 
         "Estandarizar (Seiketsu)", "Disciplinar (Shitsuke)", "Auditoría 5S", "Métricas y Seguimiento 5s"]
    )
    
    # Mostrar el logo en todas las secciones
    mostrar_logo()
    
    # Aplicar estilos y lógica por sección
    if seccion == "Inicio":
        aplicar_estilos_portada()
        pagina_inicio()
    else:
        aplicar_estilos_generales()
        
        if seccion == "Contexto de las 5S":
            contexto_5s()
        elif seccion == "Metodología C.O.L.E.D":  # Llama a la función de COLED
            introduccion_coled()
        elif seccion == "Clasificar (Seiri)":
            seccion_seiri()
        elif seccion == "Ordenar (Seiton)":
            seccion_seiton()
        elif seccion == "Limpiar (Seiso)":
            seccion_seiso()
        elif seccion == "Estandarizar (Seiketsu)":
            seccion_seiketsu()
        elif seccion == "Disciplinar (Shitsuke)":
            seccion_shitsuke()
        elif seccion == "Auditoría 5S":
            seccion_auditoria()
        elif seccion == "Métricas y Seguimiento 5s":
            metricas_seguimiento()


def introduccion_coled():
    mostrar_logo() 
    st.title("🚀 Metodología C.O.L.E.D")
    
    st.markdown("""
    ## ¿Por qué C.O.L.E.D?
    
     Los nombres originales de las 5S en japonés pueden ser difíciles de recordar, por eso se adoptaron sus significados 
     en español, tomando las primeras letras de cada palabra. Así nació el acrónimo C.O.L.E.D., una forma más simple de 
     memorizar y aplicar cada paso: Clasificar, Ordenar, Limpiar, Estandarizar y Disciplinar. Esto facilita su uso diario
     y refuerza la mejora continua.
    
    - **C**lasificar: Separar lo necesario de lo innecesario
    - **O**rdenar: Organizar de manera eficiente
    - **L**impiar: Mantener un espacio impecable
    - **E**standardizar: Crear procedimientos consistentes
    - **D**isciplinar: Mantener y mejorar continuamente
    """)
    
    st.video("https://youtu.be/cnRb8jDqfe8?si=ksm0vBqjPlVpTN96")

def seccion_seiri():
    mostrar_logo()
    st.title("🔍 Clasificar (Seiri)")
    
    tab1, tab2, tab3 = st.tabs(["Teoría", "Ejercicio Práctico", "Evaluación"])

    with tab1:
        # Contenido exclusivo de la sección Teoría
        st.markdown("""

        ## Definición
        Clasificar significa **separar lo necesario de lo innecesario** para eliminar elementos que ocupan espacio 
        o generan desperdicio en el CD.

        ### ¿Qué hacer?:
        Identificar qué herramientas, materiales o productos son realmente útiles.

        ### ¿Cómo hacerlo?:
        - **Paso 1:** Recorre las áreas del CD (recepción, picking, letdown, despacho) y haz un inventario visual.
        - **Paso 2:** Usar **tarjetas rojas** para etiquetar materiales dañados, obsoletos o innecesarios. 
        - **Paso 3:** Clasifica los elementos en categorías:
            - **Útiles:** Lo que se necesita en operaciones diarias.
            - **Reparables:** Herramientas o equipos que pueden reutilizarse después de arreglarse.
            - **Desechables:** Material que no aporta valor y debe ser eliminado.

        ### ¿Qué sigue después?
        - Mantener solo lo esencial
        - Recicla cartón, plástico y otros materiales reutilizables
        - Evitar acumulación de objetos
            
        ### Ejemplo en Logística ARA
        En un centro de distribución, clasificar implica:
        - Identificar productos de alta y baja rotación
        - Determinar el estado de equipos y herramientas
        - Eliminar elementos que no aportan valor
        """)

        st.markdown(
            """
            <style>
            .stImage > img {
               width: 25%;  /* Ajusta el tamaño de la imagen */
               height: auto;
            }
            </style>
            """,
            unsafe_allow_html=True,   

        )
        st.image("images/seiri.jpeg", caption="Clasificar (Seiri)")
    
    with tab2:
        # Contenido exclusivo de la sección Ejercicio Práctico
        st.subheader("Ejercicio de Clasificación")

        # Introducción
        st.markdown("""
        **Estás en el CEDI, en la parte operacional, y tienes que clasificar los siguientes materiales.**
        **Escoge los que aún se consideran útiles. Son 3 las correctas.**
        """)

        # Elementos a clasificar 
        elementos = [
        "Pallet de madera en buen estado", 
        "Montacargas en uso", 
        "Impresora funcional", 
        "PDT que no enciende", 
        "Diadema de voice picking rota", 
        "Herramienta oxidadas"

        ]

        # Elementos correctos (útiles)
        elementos_necesarios = [
            "Pallet de madera en buen estado", 
            "Montacargas en uso", 
            "Impresora funcional"

        ]
        # Elementos incorrectos (innecesarios)
        elementos_innecesarios = [
            "PDT que no enciende", 
            "Diadema de voice picking rota",
            "Herramienta oxidada"
        ]

        # Pregunta de selección múltiple
        necesarios = st.multiselect(
            "Seleccione los elementos que aún son útiles (son 3 las correctas):",
            elementos
        )

        # Verificación de la respuesta
        if st.button("Verificar respuesta"):
            puntuacion = 0
            # Comparar las respuestas del usuario con los elementos correctos
            if set(necesarios) == set(elementos_necesarios):
                puntuacion = 3
                st.success("¡Correcto! Has seleccionado todos los elementos útiles.")
            else:
                st.error("Algunos de los elementos seleccionados no son correctos. Intenta de nuevo.")

            # Mostrar los elementos correctos
            st.write(f"Elementos correctos: {', '.join(elementos_necesarios)}")
            st.write(f"Elementos incorrectos: {', '.join(elementos_innecesarios)}")
    
    
    with tab3:
        # Contenido exclusivo de la sección Evaluación
        st.subheader("Test de Conocimiento")
        
        preguntas = [
            {
                "pregunta": "¿Cuál es el principal objetivo de la actividad de **Clasificar** en la metodología 5S?",
                "opciones": [
                    "Mejorar la calidad de los productos",
                    "Separar los elementos útiles de los innecesarios para eliminar el desperdicio",
                    "Incrementar la cantidad de materiales en el almacén",
                    "Organizar las herramientas sin eliminar elementos innecesarios"
                ],
                "respuesta_correcta": 1
            },
            {
                "pregunta": "¿Cuál de las siguientes opciones es un paso clave en el proceso de clasificación??",
                "opciones": [
                    "Hacer un inventario visual y utilizar tarjetas rojas para etiquetar materiales innecesarios",
                    "Organizar todos los materiales en una sola categoría",
                    "Reemplazar todos los productos defectuosos por nuevos",
                    "Descartar todos los materiales sin evaluarlos"
                ],
                "respuesta_correcta": 0
            },
            {
                "pregunta": "¿Qué debe hacerse con los materiales clasificados como **desechables**?",
                "opciones": [
                    "Reutilizarlos en otras áreas del centro de distribución",
                    "Guardarlos en un área de almacenamiento separado",
                    "Eliminarlos porque no aportan valor",
                    "Repararlos para su posterior uso"
                ],
                "respuesta_correcta": 2
        }
    ]
        
        
        # Variable para almacenar las respuestas
        respuestas = {}
        
        for i, p in enumerate(preguntas, 1):
            respuestas[i] = st.radio(
                f"Pregunta {i}: {p['pregunta']}", 
                p['opciones'],
                key=f"pregunta_{i}"  # Clave única para evitar conflictos
            )
        
        # Botón de envío
        if st.button("Enviar Respuestas", key="enviar_respuestas"):
            # Calcular puntuación
            puntuacion = 0
            for i, p in enumerate(preguntas, 1):
                if respuestas[i] == p['opciones'][p['respuesta_correcta']]:
                    puntuacion += 1
            
            # Mostrar resultados
            total = len(preguntas)
            st.write(f"Puntuación: {puntuacion}/{total}")
            
            # Retroalimentación
            if puntuacion == total:
                st.success("¡Excelente! Has respondido correctamente todas las preguntas")
            elif puntuacion >= total * 0.7:
                st.warning("Buen trabajo. Revisa las respuestas que no fueron correctas")
            else:
                st.error("Necesitas repasar el material. Intenta nuevamente")

def seccion_seiton():
    mostrar_logo()
    st.title("🗂️ Ordenar (Seiton)")
    
    tab1, tab2, tab3 = st.tabs(["Teoría", "Ejercicio Práctico", "Evaluación"])
    
    # Sección de Teoría
    with tab1:
        st.markdown("""
        ## Definición
        Ordenar significa **establecer un lugar para cada cosa y cada cosa en su lugar**.

        ### ¿Qué hacer?:
        Organizar las herramientas, productos y materiales según su frecuencia de uso y características.

        ### ¿Cómo hacerlo?:
        - **Paso 1:** Asigna zonas para cada tipo de material (alta rotación, baja rotación, herramientas, equipos).
        - **Paso 2:** Usar etiquetas, códigos de colores o señalización para identificar fácilmente las zonas.
        - **Paso 3:** Agrupar los objetos similares para que sea más fácil localizarlos.

         ### ¿Qué sigue después?:
         - Mantener la organización
         - Respetar los espacios definidos
         - Devolver cada cosa a su lugar 

         ### Tips
         - "Un lugar para cada cosa"
         - Usar colores para identificar 
         - Mantener cerca lo mas usado
         - Simplicidad en la organización

        """)

        st.markdown(
            """
            <style>
            .stImage > img {
               width: 25%;  /* Ajusta el tamaño de la imagen */
               height: auto;
            }
            </style>
            """,
            unsafe_allow_html=True,   

        )
        st.image("images/seiton.png", caption="Ordenar (Seiton))")
        
    
    # Sección de Ejercicio Práctico
    with tab2:
        st.subheader("Ejercicio de Organización de Almacén")
        
        productos = {
            "Producto A": "Alta rotación",
            "Producto B": "Baja rotación",
            "Producto C": "Media rotación",
            "Producto D": "Alta rotación",
            "Producto E": "Baja rotación"
        }
        
        # Crear zonas para organizar productos
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("#### Zona Cercana")
            zona_cercana = st.multiselect(
                "Productos de alta rotación:",
                list(productos.keys())
            )
            
        with col2:
            st.write("#### Zona Intermedia")
            zona_intermedia = st.multiselect(
                "Productos de media rotación:",
                list(productos.keys())
            )
            
        with col3:
            st.write("#### Zona Alejada")
            zona_alejada = st.multiselect(
                "Productos de baja rotación:",
                list(productos.keys())
            )
        
        # Botón para verificar la organización
        if st.button("Verificar Organización", key="verificar_organizacion"):
            puntuacion = 0
            total = len(productos)
            
            # Evaluar las zonas
            for producto in zona_cercana:
                if productos[producto] == "Alta rotación":
                    puntuacion += 1
                    
            for producto in zona_intermedia:
                if productos[producto] == "Media rotación":
                    puntuacion += 1
                    
            for producto in zona_alejada:
                if productos[producto] == "Baja rotación":
                    puntuacion += 1
            
            st.progress(puntuacion / total)
            st.write(f"Puntuación: {puntuacion}/{total}")
            
            if puntuacion == total:
                st.success("¡Excelente! Has organizado correctamente todos los productos")
            else:
                st.warning("Revisa la ubicación de algunos productos según su rotación")
    
    # Sección de Evaluación
    with tab3:
        st.subheader("Test de Conocimiento")
        
        preguntas = [
            {
                "pregunta": "¿Cuál es el objetivo principal de la actividad Ordenar en la metodología 5S??",
                "opciones": [
                    "Limpiar el espacio de trabajo",
                    "Establecer un lugar para cada cosa y cada cosa en su lugar",
                    "Organizar los documentos de trabajo",
                    "Clasificar los productos según su tamaño"
                ],
                "respuesta_correcta": 1
            },
            {
                "pregunta": "¿Cuál de las siguientes opciones es un paso clave en el proceso de Ordenar?",
                "opciones": [
                    "Asignar zonas para cada tipo de material según su frecuencia de uso",
                    "Eliminar productos innecesarios",
                    "Mantener los materiales en áreas alejadas de las zonas de trabajo",
                    "No utilizar señalización en las zonas de almacenamiento"
                ],
                "respuesta_correcta": 0
            },
            {
                "pregunta": "¿Qué herramienta puedes usar para identificar fácilmente las zonas en el espacio de trabajo?",
                "opciones": [
                    "Listas de verificación",
                    "Etiquetas, códigos de colores o señalización",
                    "Herramientas de medición",
                    "Ninguna de las anteriores"
                ],
                "respuesta_correcta": 1
            }
        ]

            
        # Variable para almacenar las respuestas
        respuestas = {}

        # Crear preguntas interactivas
        for i, p in enumerate(preguntas, 1):
            respuestas[i] = st.radio(
                f"Pregunta {i}: {p['pregunta']}", 
                p['opciones'],
                key=f"pregunta_{i}"  # Clave única para evitar conflictos
            )

        # Botón de envío
        if st.button("Enviar Respuestas", key="enviar_respuestas"):
            # Calcular puntuación
            puntuacion = 0
            for i, p in enumerate(preguntas, 1):
                if respuestas[i] == p['opciones'][p['respuesta_correcta']]:
                    puntuacion += 1

            # mostrar resultado
            total = len(preguntas)
            st.write(f"Puntuación: {puntuacion}/{total}")

            # Retroalimentación
            if puntuacion == total:
                st.success("¡Excelente! Has respondido correctamente todas las preguntas")
            elif puntuacion >= total * 0.7:
                st.warning("Buen trabajo. Revisa las respuestas que no fueron correctas")
            else:
                st.error("Necesitas repasar el material. Intenta nuevamente")
        
        

def seccion_seiso():
    mostrar_logo()
    st.title("🧹 Limpiar (Seiso)")
    
    tab1, tab2, tab3 = st.tabs(["Teoría", "Ejercicio Práctico", "Evaluación"])
    
    # Sección de Teoría
    with tab1:
        st.markdown("""
        
        ### Definición
        Limpiar significa **eliminar el polvo y la suciedad de todos los elementos** en el lugar de trabajo.

        ### ¿Qué hacer?:
        Realizar limpieza periódica en todas las áreas y equipos del CD.

        ### ¿Cómo hacerlo?:
        - **Paso 1:** Define un cronograma de limpieza para cada área (diario, semanal, mensual).
        - **Paso 2:** Proporciona herramientas adecuadas para limpiar
        - **Paso 3:** Crear checklist de limpieza

        ### ¿¿Qué sigue después?:
         - Fomenta la limpieza diaria como parte de la rutina
         - Hacer de la limpieza un hábito
         - Involucrar a todo el equipo 

        ### Tips
         - Limpiar mientras trabajas
         - Tener kit de limpieza cerca
         - Hacer de la limpieza un ritual diario
        
        ### Importancia en ARA
        - Mantiene los equipos en óptimas condiciones
        - Aumenta la vida útil de herramientas y maquinaria
        - Mejora la visibilidad y reduce errores
        - Crea un ambiente de trabajo más seguro y agradable
        
        ### Áreas Clave para Limpieza
        1. Zonas de almacenamiento
        2. Equipos de manipulación
        3. Áreas de tránsito
        4. Servicios y oficinas
        """)

        st.markdown(
            """
            <style>
            .stImage > img {
               width: 25%;  /* Ajusta el tamaño de la imagen */
               height: auto;
            }
            </style>
            """,
            unsafe_allow_html=True,)
        st.image("images/limpieza.jpeg", caption="Limpieza en Logística")
    
    # Sección de Ejercicio Práctico
    
    with tab2:
        # Contenido exclusivo de la sección Ejercicio Práctico
        st.subheader("Ejercicio de Limpiar (Seiso)")

        # Introducción al ejercicio
        st.markdown("""
        **Estás en el área de transporte de un centro de distribución (CEDI) y necesitas realizar la limpieza completa de varias zonas clave.**
        Clasifica las siguientes tareas en las categorías correctas:
    
        - **Tareas diarias**: Limpieza que debe realizarse todos los días.
        - **Tareas semanales**: Limpieza que se debe realizar semanalmente.
        - **Tareas mensuales**: Limpieza que se realiza una vez al mes.
        """)

        # Áreas y tareas a clasificar
        tareas = [
            "Limpieza del equipo de manipulación (montacargas y carretillas)",
            "Limpieza de las áreas de tránsito (pasillos y accesos)", 
            "Limpieza de las zonas de almacenamiento (estantes, estanterías)", 
            "Limpieza de los servicios y oficinas (escritorios, sillas, papeleras)", 
            "Revisión de filtros de aire y equipos de ventilación"
    ]

        # Clasificación de tareas por frecuencia
        seleccion = st.multiselect(
            "Clasifica las siguientes tareas según su frecuencia (diarias, semanales, mensuales):",
            tareas,
            default=[]  # Aquí puedes preseleccionar algunas si lo deseas
    )

           
        # Respuesta esperada
        correcta = {
            "Limpieza del equipo de manipulación (montacargas y carretillas)": "Diarias",
            "Limpieza de las áreas de tránsito (pasillos y accesos)": "Diarias",
            "Limpieza de las zonas de almacenamiento (estantes, estanterías)": "Semanales",
            "Limpieza de los servicios y oficinas (escritorios, sillas, papeleras)": "Semanales",
            "Revisión de filtros de aire y equipos de ventilación": "Mensuales"
    }

        # Verificación de respuesta
        if st.button("Verificar clasificación"):
            puntuacion = 0
            # Verificar si la clasificación es correcta
            for item in seleccion:
                if correcta.get(item) == "Diarias" and item == "Limpieza del equipo de manipulación (montacargas y carretillas)":
                    puntuacion += 1
                elif correcta.get(item) == "Semanales" and (item == "Limpieza de las zonas de almacenamiento (estantes, estanterías)" or item == "Limpieza de los servicios y oficinas (escritorios, sillas, papeleras)"):
                    puntuacion += 1
                elif correcta.get(item) == "Mensuales" and item == "Revisión de filtros de aire y equipos de ventilación":
                    puntuacion += 1

            # Retroalimentación
            if puntuacion == 5:
                st.success("¡Correcto! Has clasificado todas las tareas correctamente.")
            else:
                st.warning(f"Clasificaste {puntuacion} de 5 tareas correctamente. Revisa tus respuestas.")
                
                st.write("Respuestas Correctas:")
                st.write(f"1. Limpieza del equipo de manipulación: Diarias")
                st.write(f"2. Limpieza de las áreas de tránsito: Diarias")
                st.write(f"3. Limpieza de las zonas de almacenamiento: Semanales")
                st.write(f"4. Limpieza de los servicios y oficinas: Semanales")
                st.write(f"5. Revisión de filtros de aire: Mensuales")

    # Sección de Evaluación
    with tab3:
        st.subheader("Test de Conocimiento")
        
        preguntas = [
            {
                "pregunta": "¿Cuál es el objetivo principal de Seiso?",
                "opciones": [
                    "Ordenar el área de trabajo",
                    "Eliminar lo innecesario",
                    "Mantener limpio y eliminar fuentes de suciedad",
                    "Crear procedimientos"
                ],
                "respuesta_correcta": 2
            },
            {
                "pregunta": "¿Por qué es importante la limpieza en logística?",
                "opciones": [
                    "Solo por apariencia",
                    "Para mantener equipos funcionando y prevenir accidentes",
                    "Para cumplir con las normas",
                    "Para usar más productos de limpieza"
                ],
                "respuesta_correcta": 1
            }
        ]
        
        # Almacenar las respuestas
        respuestas = {}
        for i, p in enumerate(preguntas, 1):
            respuestas[i] = st.radio(
                f"Pregunta {i}: {p['pregunta']}",
                p['opciones'],
                key=f"seiso_pregunta_{i}"  # Clave única para evitar conflictos
            )
        
        # Botón para enviar respuestas
        if st.button("Enviar Respuestas", key="enviar_respuestas_seiso"):
            puntuacion = 0
            for i, p in enumerate(preguntas, 1):
                if respuestas[i] == p['opciones'][p['respuesta_correcta']]:
                    puntuacion += 1
            
            # Mostrar resultados
            total = len(preguntas)
            st.write(f"Puntuación: {puntuacion}/{total}")
            
            # Retroalimentación
            if puntuacion == total:
                st.success("¡Excelente! Has respondido correctamente todas las preguntas.")
            elif puntuacion >= total * 0.7:
                st.warning("Buen trabajo. Revisa las respuestas que no fueron correctas.")
            else:
                st.error("Necesitas repasar el material. Intenta nuevamente.")

def seccion_seiketsu():
    mostrar_logo()
    st.title("📋 Estandarizar (Seiketsu)")
    
    tab1, tab2, tab3 = st.tabs(["Teoría", "Ejercicio Práctico", "Evaluación"])
    
    with tab1:
        st.markdown("""
        
        ### Definición
        Estandarizar significa **crear procedimientos y rutinas** que mantengan las primeras 3S.

        ### ¿Qué hacer?:
        Documentar y compartir los procesos de clasificación, orden y limpieza.

        ### ¿Cómo hacerlo?:
        - **Paso 1:** Crear manuales o checklists simples para cada área.
        - **Paso 2:** Capacitar al personal sobre estas normas.
        - **Paso 3:** Usar tableros de control para monitorear el cumplimiento.

        ### ¿Qué sigue después?:
         - Actualizar los estándares regularmente según las necesidades del CD.
         - Realiza auditorías para garantizar el cumplimiento.
         
        ### Tips
         - Simplicidad en los procedimientos
         - Hacerlos visuales 
         - Actualizarlos constantemente 

        ### Importancia en Logística ARA
        - Mantiene los logros alcanzados
        - Crea rutinas claras y efectivas
        - Facilita el entrenamiento de nuevo personal
        
        ### Elementos de Estandarización
        1. Procedimientos documentados
        2. Checklist de verificación
        3. Señalización visual
        4. Roles y responsabilidades claros
        
        ### Beneficios
        - Mayor consistencia en operaciones
        - Reducción de errores
        - Facilita la detección de anomalías
        - Mejora continua sostenible
        """)
        
        st.image("images/estandarizacion.jpeg", caption="Estandarización en Logística", use_container_width=True)
    
    with tab2:
        st.subheader("Ejercicio de Creación de Procedimientos")
        
        # Ejercicio para crear un procedimiento estándar
        st.write("### Cree un procedimiento estándar para recepción de mercancía")
        
        # Pasos disponibles para ordenar
        pasos_disponibles = [
            "Verificar documentación",
            "Descargar mercancía",
            "Inspeccionar calidad",
            "Registrar en sistema",
            "Asignar ubicación",
            "Contactar al proveedor",
            "Almacenar productos",
            "Confirmar cantidades"
        ]
        
        # Usuario ordena los pasos
        orden_pasos = st.multiselect(
            "Ordene los pasos del procedimiento (en el orden correcto):",
            pasos_disponibles
        )
        
        if st.button("Verificar Procedimiento"):
            # Orden correcto de los pasos
            orden_correcto = [
                "Verificar documentación",
                "Descargar mercancía",
                "Confirmar cantidades",
                "Inspeccionar calidad",
                "Registrar en sistema",
                "Asignar ubicación",
                "Almacenar productos"
            ]
            
            # Calcular puntuación
            puntos = 0
            for i, paso in enumerate(orden_pasos):
                if i < len(orden_correcto) and paso == orden_correcto[i]:
                    puntos += 1
            
            # Mostrar resultado
            total = len(orden_correcto)
            st.progress(puntos/total)
            st.write(f"Puntuación: {puntos}/{total}")
            
            if puntos == total:
                st.success("¡Perfecto! Has creado el procedimiento correcto")
            elif puntos >= total * 0.7:
                st.warning("¡Buen intento! Revisa el orden de algunos pasos")
            else:
                st.error("Revisa el orden de los pasos y vuelve a intentarlo")
    
    with tab3:
        st.subheader("Test de Conocimiento")
        
        preguntas = [
            {
                "pregunta": "¿Cuál es el principal objetivo de Seiketsu?",
                "opciones": [
                    "Limpiar el área de trabajo",
                    "Mantener los logros de las primeras 3S",
                    "Ordenar materiales",
                    "Clasificar elementos"
                ],
                "respuesta_correcta": 1
            },
            {
                "pregunta": "¿Qué herramienta es esencial para la estandarización?",
                "opciones": [
                    "Productos de limpieza",
                    "Etiquetas de color",
                    "Procedimientos documentados",
                    "Carretillas elevadoras"
                ],
                "respuesta_correcta": 2
            }
        ]
        
        # Variable para almacenar las respuestas
        respuestas = {}
        
        for i, p in enumerate(preguntas, 1):
            respuestas[i] = st.radio(
                f"Pregunta {i}: {p['pregunta']}", 
                p['opciones']
            )
        
        # Botón de envío
        if st.button("Enviar Respuestas"):
            # Calcular puntuación
            puntuacion = 0
            for i, p in enumerate(preguntas, 1):
                if respuestas[i] == p['opciones'][p['respuesta_correcta']]:
                    puntuacion += 1
            
            # Mostrar resultados
            total = len(preguntas)
            st.write(f"Puntuación: {puntuacion}/{total}")
            
            # Retroalimentación
            if puntuacion == total:
                st.success("¡Excelente! Has respondido correctamente todas las preguntas")
            elif puntuacion >= total * 0.7:
                st.warning("Buen trabajo. Revisa las respuestas que no fueron correctas")
            else:
                st.error("Necesitas repasar el material. Intenta nuevamente")

def seccion_shitsuke():
    mostrar_logo()
    st.title("🎯 Disciplinar (Shitsuke)")
    
    tab1, tab2, tab3 = st.tabs(["Teoría", "Ejercicio Práctico", "Evaluación"])
    
    with tab1:
        st.markdown("""
    
        ### Definición
        Disciplinar significa **convertir las 5S en un hábito** y mantener una cultura de mejora continua.

         ### ¿Qué hacer?:
        Crear una cultura de mejora, capacitar y motivar al equipo para mantener la metodologia. 

        ### ¿Cómo hacerlo?:
        - **Paso 1:** Realizar capacitaciones. 
        - **Paso 2:** Establecer auditorias periodicas con indicadores claros.
        - **Paso 3:** Recompensar y reconocer buenos comportamientos.

         ### ¿Qué sigue después?:
         - Fomentar la participación de todo el equipo 
         - Ajustar las metas según las necesidades del CD. 
         - Compromiso de todos 

        ### Importancia en Logística ARA
        - Asegura la sostenibilidad del programa 5S
        - Fomenta la participación del personal
        - Promueve el desarrollo profesional
        - Mejora el ambiente laboral
        
        ### Elementos Clave
        1. Capacitación continua
        2. Auditorías regulares
        3. Reconocimiento de logros
        4. Comunicación efectiva
        
        ### Beneficios
        - Mayor compromiso del personal
        - Mejora continua sostenible
        - Ambiente de trabajo positivo
        - Cultura organizacional fortalecida
        """)
        
        # Cambio en la forma de mostrar la imagen
        st.image("images/disciplina.jpeg", caption="Disciplina en Logística", use_container_width=True)

        # Verificación de la existencia del archivo
        file_path = r"C:\Users\LURUENA\OneDrive - Grupo Jerónimo Martins\Documents\mi_manual_5s\assets\Lista de Chequeo 5S.pdf"

        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                st.download_button(
                    label="Descargar Lista de Chequeo (PDF)",
                    data=f,
                    file_name="Lista de Chequeo 5S.pdf",
                    mime="application/pdf"
                )
        else:
            st.write(f"El archivo no fue encontrado en la ruta: {file_path}")

    with tab2:
        st.subheader("Ejercicio de Seguimiento de Hábitos 5S")
        
        # Nuevo ejercicio práctico
        st.write("### Registro Semanal de Hábitos 5S")
        
        habitos = {
            "Lunes": ["Revisión inicial del área", "Verificación de orden", "Limpieza básica"],
            "Miércoles": ["Auditoría rápida", "Actualización de indicadores", "Reunión de mejora"],
            "Viernes": ["Verificación final", "Registro de incidencias", "Plan siguiente semana"]
        }
        
        # Selección del día
        dia_seleccionado = st.selectbox("Seleccione el día:", list(habitos.keys()))
        
        # Mostrar tareas del día
        st.write(f"### Tareas para {dia_seleccionado}:")
        tareas_completadas = {}
        
        for tarea in habitos[dia_seleccionado]:
            tareas_completadas[tarea] = st.checkbox(tarea)
            
            if tareas_completadas[tarea]:
                hora = st.time_input(f"Hora de realización de: {tarea}")
                comentario = st.text_input(f"Comentario para: {tarea}")
        
        if st.button("Registrar Seguimiento"):
            tareas_hechas = sum(tareas_completadas.values())
            total_tareas = len(habitos[dia_seleccionado])
            
            st.progress(tareas_hechas/total_tareas)
            st.write(f"Progreso del día: {tareas_hechas}/{total_tareas} tareas completadas")
            
            if tareas_hechas == total_tareas:
                st.success("¡Excelente! Has completado todas las tareas del día")
            else:
                st.warning(f"Aún quedan {total_tareas - tareas_hechas} tareas por completar")
    
    with tab3:
        st.subheader("Test de Conocimiento")
        
        preguntas = [
            {
                "pregunta": "¿Qué significa Shitsuke?",
                "opciones": [
                    "Limpiar el área",
                    "Mantener el orden",
                    "Crear hábitos y disciplina",
                    "Estandarizar procesos"
                ],
                "respuesta_correcta": 2
            },
            {
                "pregunta": "¿Cuál es la mejor manera de mantener la disciplina 5S?",
                "opciones": [
                    "Aplicar sanciones",
                    "Realizar auditorías regulares y capacitación",
                    "Aumentar la supervisión",
                    "Incrementar la documentación"
                ],
                "respuesta_correcta": 1
            }
        ]
        
        # Variable para almacenar las respuestas
        respuestas = {}
        
        for i, p in enumerate(preguntas, 1):
            respuestas[i] = st.radio(
                f"Pregunta {i}: {p['pregunta']}", 
                p['opciones']
            )
        
        # Botón de envío
        if st.button("Enviar Respuestas"):
            # Calcular puntuación
            puntuacion = 0
            for i, p in enumerate(preguntas, 1):
                if respuestas[i] == p['opciones'][p['respuesta_correcta']]:
                    puntuacion += 1
            
            # Mostrar resultados
            total = len(preguntas)
            st.write(f"Puntuación: {puntuacion}/{total}")
            
            # Retroalimentación
            if puntuacion == total:
                st.success("¡Excelente! Has respondido correctamente todas las preguntas")
            elif puntuacion >= total * 0.7:
                st.warning("Buen trabajo. Revisa las respuestas que no fueron correctas")
            else:
                st.error("Necesitas repasar el material. Intenta nuevamente")

def seccion_auditoria():
    mostrar_logo()
    st.title("📊 Auditoría 5S")
    
    st.write("### Realice una auditoría 5S")
    
    # Categorías para evaluar
    categorias = {
        "Clasificación": ["Elementos innecesarios eliminados", "Área libre de obstáculos", "Inventario optimizado"],
        "Orden": ["Señalización clara", "Ubicaciones definidas", "Fácil acceso a materiales"],
        "Limpieza": ["Área limpia", "Equipos mantenidos", "Cronograma de limpieza visible"],
        "Estandarización": ["Procedimientos visibles", "Checklist actualizados", "Roles definidos"],
        "Disciplina": ["Personal capacitado", "Auditorías regulares", "Mejoras implementadas"]
    }
    
    # Crear formulario de auditoría
    puntuacion_total = 0
    max_puntos = 0
    
    for categoria, items in categorias.items():
        st.write(f"#### {categoria}")
        for item in items:
            puntuacion = st.slider(
                f"{item}",
                0, 5, 3,
                help="0 = No cumple, 5 = Cumple totalmente"
            )
            puntuacion_total += puntuacion
            max_puntos += 5
    
    if st.button("Calcular Resultado"):
        porcentaje = (puntuacion_total / max_puntos) * 100
        st.write(f"Puntuación total: {puntuacion_total}/{max_puntos}")
        st.progress(puntuacion_total/max_puntos)
        
        if porcentaje >= 90:
            st.success("¡Excelente implementación 5S!")
        elif porcentaje >= 70:
            st.warning("Buena implementación, con oportunidades de mejora")
        else:
            st.error("Se requiere mayor atención a la implementación 5S")
        
        # Recomendaciones basadas en la puntuación
        st.write("### Recomendaciones:")
        for categoria, items in categorias.items():
            st.write(f"**{categoria}:**")
            for item in items:
                st.write(f"- Mantener el seguimiento de: {item}")

def metricas_seguimiento():
    mostrar_logo()
    st.title("📊 Métricas y Seguimiento 5S")

    # Función para cargar datos de evaluación
    def cargar_datos_evaluacion():
        fechas = pd.date_range(start='2024-01-01', end='2024-12-31', freq='W')
        datos_5s = {
            'Clasificar': np.random.uniform(70, 90, len(fechas)),
            'Ordenar': np.random.uniform(65, 85, len(fechas)),
            'Limpiar': np.random.uniform(60, 80, len(fechas)),
            'Estandarizar': np.random.uniform(55, 75, len(fechas)),
            'Disciplinar': np.random.uniform(50, 70, len(fechas)),
        }
        df_promedios = pd.DataFrame(datos_5s, index=fechas)
        return df_promedios

    # Cargar datos y manejar valores faltantes
    df_promedios = cargar_datos_evaluacion()
    df_promedios = df_promedios.fillna(0)  # Reemplazar NaN con 0 para evitar errores

    # Agregar un selector de rango de fechas
    st.subheader("Seleccione el Rango de Fechas para el Análisis")
    fecha_inicio = st.date_input("Fecha de Inicio", value=pd.to_datetime("2024-01-01"))
    fecha_fin = st.date_input("Fecha de Fin", value=pd.to_datetime("2024-12-31"))

    # Filtrar datos por rango de fechas
    if fecha_inicio > fecha_fin:
        st.error("La fecha de inicio no puede ser posterior a la fecha de fin.")
        return

    df_filtrado = df_promedios.loc[fecha_inicio:fecha_fin]

    if df_filtrado.empty:
        st.warning("No hay datos disponibles para el rango de fechas seleccionado.")
        return

    # Mostrar gráfico de evolución temporal
    st.subheader("Evolución Temporal")
    fig = px.line(
        df_filtrado, 
        title=f"Evolución de Implementación 5S ({fecha_inicio} a {fecha_fin})",
        labels={'value': 'Porcentaje de Cumplimiento', 'variable': 'Categoría'},
        template='plotly_white'
    )
    fig.update_layout(hovermode='x unified', yaxis_range=[0, 100])
    st.plotly_chart(fig, use_container_width=True)
    
    # **Nuevo: Gráfico de barras por última medición**
    st.subheader("Gráfico de Barras: Última Medición por Categoría")
    ultima_medicion = df_filtrado.iloc[-1]

    # Crear gráfico de barras para mostrar los valores de la última medición por categoría
    fig_barras = px.bar(
        ultima_medicion, 
        title=f"Última Medición por Categoría ({fecha_inicio} a {fecha_fin})",
        labels={'value': 'Porcentaje de Cumplimiento', 'index': 'Categoría'},
        template='plotly_white'
    )
    fig_barras.update_layout(yaxis_range=[0, 100])
    st.plotly_chart(fig_barras, use_container_width=True)

    # Mostrar tabla de datos filtrados
    st.subheader("Datos Filtrados")
    st.dataframe(df_filtrado)

    # Agregar una sección de análisis detallado
    st.subheader("Análisis Detallado por Categoría")
    categoria_seleccionada = st.selectbox(
        "Seleccione una categoría para analizar:",
        df_filtrado.columns
    )

    if categoria_seleccionada:
        fig_categoria = px.line(
            df_filtrado[categoria_seleccionada],
            title=f"Evolución de {categoria_seleccionada} ({fecha_inicio} a {fecha_fin})",
            labels={'value': 'Porcentaje de Cumplimiento', 'index': 'Fecha'},
            template='plotly_white'
        )
        fig_categoria.update_layout(hovermode='x unified', yaxis_range=[0, 100])
        st.plotly_chart(fig_categoria, use_container_width=True)


def main():
    st.sidebar.title("Manual 5S ARA")
    
    # Menú de navegación
    seccion = st.sidebar.radio(
        "Seleccione una sección:",
        ["Inicio","Contexto de las 5S"," Metodología C.O.L.E.D", "Clasificar (Seiri)", "Ordenar (Seiton)", "Limpiar (Seiso)", 
         "Estandarizar (Seiketsu)", "Disciplinar (Shitsuke)", "Auditoría 5S", "Métricas y Seguimiento 5s"]
    )
    
    # Aplicar estilos y lógica por sección
    if seccion == "Inicio":
        aplicar_estilos_portada()  # Estilos específicos para la portada
        pagina_inicio()
    else:
        aplicar_estilos_generales()  # Estilos generales para las demás secciones
        
        # Mostrar la sección correspondiente
        if seccion == "Contexto de las 5S":
            contexto_5s()
        elif seccion == " Metodología C.O.L.E.D":  # Llama a la función de COLED
            introduccion_coled()
        elif seccion == "Clasificar (Seiri)":
            seccion_seiri()
        elif seccion == "Ordenar (Seiton)":
            seccion_seiton()
        elif seccion == "Limpiar (Seiso)":
            seccion_seiso()
        elif seccion == "Estandarizar (Seiketsu)":
            seccion_seiketsu()
        elif seccion == "Disciplinar (Shitsuke)":
            seccion_shitsuke()
        elif seccion == "Auditoría 5S":
            seccion_auditoria()
        elif seccion == "Métricas y Seguimiento 5s":
            metricas_seguimiento()   



if __name__ == "__main__":
    main()
    