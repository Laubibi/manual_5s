import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import numpy as np
from datetime import datetime

def main():
    st.set_page_config(page_title="Manual 5S Interactivo", layout="wide")
    
    # Sidebar para navegación
    st.sidebar.title("Manual 5S")
    section = st.sidebar.radio(
        "Seleccione una sección:",
        ["Inicio", "Seiri", "Seiton", "Seiso", "Seiketsu", "Shitsuke", "Seguimiento"]
    )
    
    if section == "Inicio":
        show_home()
    elif section == "Seiri":
        show_seiri()
    elif section == "Seguimiento":
        show_tracking()

def show_home():
    st.title("Manual Interactivo 5S")
    st.subheader("Centro de Distribución Jerónimo Martins")
    
    # Descripción general
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### ¿Qué son las 5S?
        Las 5S son una metodología japonesa para la organización del trabajo:
        1. **Seiri** (Clasificar)
        2. **Seiton** (Ordenar)
        3. **Seiso** (Limpiar)
        4. **Seiketsu** (Estandarizar)
        5. **Shitsuke** (Disciplina)
        """)
    
    with col2:
        # Crear gráfico de radar para niveles de implementación
        categories = ['Seiri', 'Seiton', 'Seiso', 'Seiketsu', 'Shitsuke']
        values = [85, 72, 78, 65, 70]
        
        fig = px.line_polar(
            r=values,
            theta=categories,
            line_close=True,
            range_r=[0,100],
            title="Nivel de Implementación 5S"
        )
        st.plotly_chart(fig)

def show_seiri():
    st.title("Seiri - Clasificar")
    
    # Tabs para diferentes secciones
    tab1, tab2, tab3 = st.tabs(["Teoría", "Ejercicio Práctico", "Evaluación"])
    
    with tab1:
        st.markdown("""
        ### Concepto
        Seiri consiste en identificar y separar los materiales necesarios de los innecesarios
        y eliminar estos últimos.
        
        ### Beneficios
        - Mejor uso del espacio
        - Reducción de inventario
        - Eliminación de desperdicios
        - Mayor productividad
        """)
        
        # Mostrar proceso con checkboxes
        st.subheader("Proceso de Implementación")
        steps = [
            "Identificar el área de trabajo",
            "Fotografiar el 'antes'",
            "Crear criterios de clasificación",
            "Usar tarjetas rojas",
            "Separar lo necesario",
            "Documentar resultados"
        ]
        
        for step in steps:
            st.checkbox(step, key=f"step_{step}")
    
    with tab2:
        st.subheader("Ejercicio de Clasificación")
        
        # Crear dos columnas para clasificación
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Elementos Necesarios")
            necesarios = st.multiselect(
                "Seleccione los elementos necesarios:",
                ["Montacargas en uso", "Cajas rotas", "Scanner funcional", 
                 "Documentos obsoletos", "Pallets buenos", "Herramientas oxidadas"],
                key="necesarios"
            )
        
        with col2:
            st.markdown("### Elementos Innecesarios")
            innecesarios = st.multiselect(
                "Seleccione los elementos innecesarios:",
                ["Montacargas en uso", "Cajas rotas", "Scanner funcional", 
                 "Documentos obsoletos", "Pallets buenos", "Herramientas oxidadas"],
                key="innecesarios"
            )
        
        if st.button("Verificar Clasificación"):
            correctos_necesarios = ["Montacargas en uso", "Scanner funcional", "Pallets buenos"]
            correctos_innecesarios = ["Cajas rotas", "Documentos obsoletos", "Herramientas oxidadas"]
            
            score = 0
            for item in necesarios:
                if item in correctos_necesarios:
                    score += 1
            for item in innecesarios:
                if item in correctos_innecesarios:
                    score += 1
                    
            st.progress(score/6)
            st.write(f"Puntuación: {score}/6")
    
    with tab3:
        st.subheader("Evaluación de Conocimientos")
        
        # Preguntas de evaluación
        q1 = st.radio(
            "1. ¿Cuál es el principal objetivo de Seiri?",
            ["Limpiar el área de trabajo",
             "Clasificar y eliminar lo innecesario",
             "Organizar las herramientas",
             "Crear nuevos procedimientos"]
        )
        
        q2 = st.radio(
            "2. ¿Para qué se utilizan las tarjetas rojas?",
            ["Para marcar zonas peligrosas",
             "Para identificar elementos innecesarios",
             "Para señalar emergencias",
             "Para marcar herramientas"]
        )
        
        if st.button("Enviar Evaluación"):
            score = 0
            if q1 == "Clasificar y eliminar lo innecesario":
                score += 1
            if q2 == "Para identificar elementos innecesarios":
                score += 1
            
            st.write(f"Puntuación: {score}/2")
            if score == 2:
                st.success("¡Excelente! Has comprendido los conceptos básicos de Seiri.")
            else:
                st.warning("Revisa nuevamente el material.")

def show_tracking():
    st.title("Seguimiento y Métricas 5S")
    
    # Datos de ejemplo para el seguimiento
    dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
    scores = {
        'Seiri': np.random.normal(80, 5, len(dates)),
        'Seiton': np.random.normal(75, 5, len(dates)),
        'Seiso': np.random.normal(85, 5, len(dates)),
        'Seiketsu': np.random.normal(70, 5, len(dates)),
        'Shitsuke': np.random.normal(72, 5, len(dates))
    }
    
    df = pd.DataFrame(scores, index=dates)
    
    # Gráfico de líneas para seguimiento temporal
    fig = px.line(df, title='Evolución de Implementación 5S')
    st.plotly_chart(fig)
    
    # Métricas actuales
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Promedio General", f"{df.mean().mean():.1f}%", "+2.1%")
    with col2:
        st.metric("Mejor S", f"Seiso: {df['Seiso'].mean():.1f}%", "+3.2%")
    with col3:
        st.metric("Mayor Mejora", "Seiketsu", "+5.1%")
    
    # Formulario para registro de auditoría
    st.subheader("Registro de Auditoría")
    with st.form("auditoria_form"):
        fecha = st.date_input("Fecha de Auditoría")
        area = st.selectbox("Área", ["Recepción", "Almacenamiento", "Despacho"])
        
        col1, col2 = st.columns(2)
        with col1:
            seiri = st.slider("Seiri", 0, 100, 80)
            seiton = st.slider("Seiton", 0, 100, 75)
            seiso = st.slider("Seiso", 0, 100, 85)
        with col2:
            seiketsu = st.slider("Seiketsu", 0, 100, 70)
            shitsuke = st.slider("Shitsuke", 0, 100, 72)
        
        observaciones = st.text_area("Observaciones")
        submitted = st.form_submit_button("Registrar Auditoría")
        
        if submitted:
            st.success("Auditoría registrada exitosamente")

if __name__ == "__main__":
    main()
