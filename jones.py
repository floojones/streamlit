import streamlit as st


st.sidebar.title(" Navegación")
pagina = st.sidebar.radio("Ir a:", ["Inicio", "Historia", "Rutinas", "Competencias", "Quiénes somos"])


if pagina == "Inicio":
    st.title(" Bienvenido al Mundo Cheerleader")
    agree = st.checkbox("¿Estas preparado para conocer este deporte?")

if agree:
    st.write("Vamos!")
    st.image("navarro.jpg", caption="La energía del cheer")
    color = st.color_picker("selecciona el color mas parecido al traje", "#00f900")
    st.write("el color es ", color)
    st.write("El cheerleading es más que un deporte: es disciplina, trabajo en equipo y pasión. 💖✨")
    st.write("Es una disciplina la cual combina baile, gimnasia y acrobacias para animar a equipos deportivos y tambien para competir, No se trata solo de gritar, sino de crear rutinas llenas de energia")
    st.write("En resumen, la tematica gira en torno a la alegria, motivacion y la union del grupo, mostrando siempre entusiasmo y fuerza para contagiar a los demas")
    st.video("topgun.mp4") 


elif pagina == "Historia":
    st.header("Historia del Cheerleading")
    st.write("El cheerleading es una actividad deportiva que combina la danza, la gimnasia y la acrobacia. Aunque se ha popularizado en los últimos años, su historia se remonta a principios del siglo XX en Estados Unidos. En sus inicios, el cheerleading era una actividad exclusivamente masculina y se limitaba a animar al equipo de fútbol americano durante los partidos. Sin embargo, con el tiempo, se fue abriendo a las mujeres y se convirtió en una actividad independiente, con su propia competición y reglas.")
    st.image("cheerantiguo.jpg")
    st.header("primeros equipos")
    st.write("universidad de minnesota en 1898: Se considera el lugar en donde nacio el cheerleader. Un estudiante llamado johnny campbell fue el primero en durugur una animacion")
    st.write("Este equipo al inicio era solo comformado por hombres, en la decada de 1920 empiezan a entrar mujeres.")


elif pagina == "Rutinas":
    st.header("Rutinas y Técnicas")
    dificultad = st.slider("Selecciona el nivel de dificultad:", 1, 5, 3)
    st.write("Mostrando rutinas de dificultad nivel 3")
    st.video("summit.mp4")
    st.write("La estructura de una rutina de cheerleader incluye varios elementos clave que deben ser ejecutados con precisión y coordinación. Estos elementos son Stunts: Movimientos acrobáticos que requieren la habilidad de levantar y sostener a uno o varios compañeros en el aire. Tumbling: Secuencias de gimnasia y saltos que requieren destreza y control. Pirámides: Formaciones humanas en varios niveles, donde uno o más miembros del equipo son elevados por otros. Danza y movimientos de mano: Coreografías de movimientos coordinados que requieren ritmo y expresión.La duración de la rutina es generalmente de 2:30 a 3 minutos, dividida en segmentos de acrobacia, danza y pirámides. Las rutinas deben cumplir con criterios de dificultad, sincronización, creatividad y presentación, y deben incluir elementos obligatorios como pirámides, saltos y acrobacias. La evaluación por jueces se basa en la dificultad y ejecución, sincronización, originalidad y presentación de la rutina.")
    


elif pagina == "Competencias":
    st.header(" Competencias y Cultura Cheer")
    torneo = st.selectbox("Elige un torneo:", ["ICU Worlds", "UCA Nationals", "NCA All-Star"])
    if torneo == "ICU Worlds":
        st.write("Es la competencia más importante a nivel mundial, realizada en Orlando, Florida.")
        st.write("Los Mundiales ICU son el Campeonato Mundial oficial para equipos nacionales de cheerleading Juvenil, Junior y Senior de diferentes países. Solo compiten los equipos nacionales oficiales, enfrentando a los países entre sí en un evento muy competitivo.")
        st.image("icu.jpg")
    elif torneo == "UCA Nationals":
        st.write("Evento de nivel escolar y universitario en EE.UU.")
        st.write("El Campeonato Nacional UCA All Star es una de las competiciones nacionales de porristas más prestigiosas del país y marca la parada final en el viaje de Triple Corona de su programa. Equipos de animación de todo el país se reunirán para competir por plazas para los Cheerleading Worlds y los Campeonatos The Summit. ¡El Campeonato Nacional UCA All Star también es el ÚNICO evento en el Walt Disney World Resort donde los atletas Tiny, Mini, Youth, Prep y Novice pueden competir!")
        st.image("uca.jpg")
    else:
        st.write("Una de las competencias más populares de all-star cheerleading.")
        st.write("")
        st.image("nca.jpg")


elif pagina == "Quiénes somos":
    st.header("‍ CheerPower Talagante")
    st.write("Somos un equipo ficticio creado para este proyecto. Nuestro lema: *'Fly high, shine bright'* 🌟")
    st.image("equipo.jpg")
    st.write(" Ubicación: Talagante, Chile")

    st.write(" Contacto: cheerpower@ficticio.com")



