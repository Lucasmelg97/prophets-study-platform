import streamlit as st
import pandas as pd
from typing import List, Dict

# Configuração da página
st.set_page_config(
    page_title="The Prophets - Plataforma de Estudos",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para design moderno
st.markdown("""
<style>
    /* Background escuro */
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1a2e 100%);
    }
    
    /* Cards de curso */
    .course-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.9) 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }
    
    .course-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        border-color: #FF6B35;
    }
    
    /* Títulos */
    h1, h2, h3 {
        color: white !important;
    }
    
    /* Badges */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        background: linear-gradient(135deg, #FF6B35, #e55a2b);
        color: white;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 0.5rem;
    }
    
    .level-badge {
        font-size: 1.2rem;
        margin-right: 0.5rem;
    }
    
    /* Botões */
    .stButton>button {
        background: linear-gradient(135deg, #006DB7, #003d6b);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(0,109,183,0.4);
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: rgba(10, 14, 39, 0.98);
    }
    
    /* Texto branco para melhor contraste */
    .stMarkdown, p, label {
        color: white !important;
    }
    
    /* Input fields */
    .stTextInput>div>div>input {
        background: rgba(255,255,255,0.1);
        color: white;
        border: 2px solid rgba(255,255,255,0.2);
        border-radius: 10px;
    }
    
    .stSelectbox>div>div>select {
        background: rgba(255,255,255,0.1);
        color: white;
        border: 2px solid rgba(255,255,255,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Base de dados de cursos
CURSOS_DATABASE = {
    "Cientista de Dados": {
        "Iniciante": [
            {"titulo": "Introdução ao Python", "instrutor": "TéoMeWhy", "badge": "Python", "link": "https://www.youtube.com/watch?v=OeKzVjiiRm4&list=PLvlkVRRKOYFSpRkqnR0p2A-eaVlpLnN3D"},
            {"titulo": "Pandas", "instrutor": "TéoMeWhy", "badge": "Dados", "link": "https://www.youtube.com/watch?v=9Cw7iIjFlBc&list=PLvlkVRRKOYFQHnDhjTmXLEz3HU5WTgOcF"},
            {"titulo": "Estatística Básica", "instrutor": "TéoMeWhy", "badge": "Stats", "link": "https://www.youtube.com/watch?v=4CcgZXXIl7o&list=PLvlkVRRKOYFQGIZdz7BycJet9OncyXlbq"},
            {"titulo": "SQL", "instrutor": "TéoMeWhy", "badge": "SQL", "link": "https://www.youtube.com/watch?v=VmkJG8awKqM&list=PLvlkVRRKOYFRo651oD0JptVqfQGDvMi3j"},
            {"titulo": "Machine Learning pt.1", "instrutor": "TéoMeWhy", "badge": "ML", "link": "https://www.youtube.com/watch?v=oz_rZ92Tmls&list=PLvlkVRRKOYFR6_LmNcJliicNan2TYeFO2"},
            {"titulo": "Machine Learning pt.2", "instrutor": "TéoMeWhy", "badge": "ML", "link": "https://www.youtube.com/watch?v=oj0ACpEHpS0&list=PLvlkVRRKOYFTXcpttQSZmv1wDg7F3uH7o"},
            {"titulo": "Visualização dos Dados", "instrutor": "ICMCTV", "badge": "DataViz", "link": "https://www.youtube.com/watch?v=BLIosfH2yM0&list=PLt7qVSwRVn5YEIvaMb02IJVKCpauWV-s9"},
            {"titulo": "Streamlit", "instrutor": "TéoMeWhy", "badge": "Web", "link": "https://www.youtube.com/watch?v=JLcEWe7woVk&list=PLvlkVRRKOYFRYA40hJ_V8e_iC5Lu6YPyn"},
            {"titulo": "Git & Github", "instrutor": "TéoMeWhy", "badge": "Git", "link": "https://www.youtube.com/watch?v=84FhNXNWoig&list=PLvlkVRRKOYFQyKmdrassLNxkzSMM6tcSL"},
            {"titulo": "Metodologia Ágil", "instrutor": "D1UP Academy", "badge": "Agile", "link": "https://www.youtube.com/watch?v=-2W_loW_QYw&list=PLoGDMdX4pUAfso0bQWSZFgjEBlr2H9IBU"},
        ],
        "Intermediário": [
            {"titulo": "MLFlow", "instrutor": "TéoMeWhy", "badge": "MLOps", "link": "https://www.youtube.com/watch?v=W8bxk42C9UE&list=PLvlkVRRKOYFQeQEA5Lc0US9i-EK8eGgrs"},
            {"titulo": "Panorama da Estatística", "instrutor": "A Ciência da Estatística", "badge": "Stats", "link": "https://www.youtube.com/watch?v=wAYB75xEdZQ&list=PL5Dg8nFln2eXGSjEct01QinGi4rrNthQG"},
            {"titulo": "Tipos de Dados", "instrutor": "A Ciência da Estatística", "badge": "Stats", "link": "https://www.youtube.com/watch?v=hESKcJbMCrI&list=PL5Dg8nFln2eU1g1wzazCDF6jusmWE2nIL"},
            {"titulo": "Probabilidade", "instrutor": "A Ciência da Estatística", "badge": "Stats", "link": "https://www.youtube.com/watch?v=vzzG3oaZtOA&list=PL5Dg8nFln2eWlB9DLi9drLtPcm5UANcUI"},
            {"titulo": "Teoria de Conjuntos", "instrutor": "A Ciência da Estatística", "badge": "Stats", "link": "https://www.youtube.com/watch?v=S3_3LSJqgVg&list=PL5Dg8nFln2eVou0YbxuUiYWmjPuxTLAYe"},
            {"titulo": "Valor-p", "instrutor": "A Ciência da Estatística", "badge": "Stats", "link": "https://www.youtube.com/watch?v=xv79gO5C-SE&list=PL5Dg8nFln2eUTqoWcNSV4AyVEVty_edWS"},
            {"titulo": "Modelo de Regressão", "instrutor": "A Ciência da Estatística", "badge": "Stats", "link": "https://www.youtube.com/watch?v=21txO7PN9EE&list=PL5Dg8nFln2eUTqoWcNSV4AyVEVty_edWS&index=3"},
            {"titulo": "Inferência Estatística", "instrutor": "Cibele Russo", "badge": "Stats", "link": "https://www.youtube.com/watch?v=JB8Hv8yJsIQ&list=PLt7qVSwRVn5aDu6DW-98cgk7ahkjku1B8&index=2"},
            {"titulo": "Time Series - Conceitos Básicos", "instrutor": "Professor Vinicius Lima", "badge": "Time Series", "link": "https://www.youtube.com/watch?v=rexHHx6Nwec&list=PLubmBFLX1_vgGv4sAUG9O0HUw8NzJqhyD"},
            {"titulo": "Time Series - Decomposição", "instrutor": "Professor Vinicius Lima", "badge": "Time Series", "link": "https://www.youtube.com/watch?v=Ep5x8wZI5v0&list=PLubmBFLX1_vjYSpClZuz0fVY-qkx1tMvC"},
            {"titulo": "Time Series - Suavização Exponencial", "instrutor": "Professor Vinicius Lima", "badge": "Time Series", "link": "https://www.youtube.com/watch?v=aVm0G0HTetw&list=PLubmBFLX1_vhjQjUG_rXpQ--USd102_ff"},
            {"titulo": "Time Series - ARIMA", "instrutor": "Professor Vinicius Lima", "badge": "Time Series", "link": "https://www.youtube.com/watch?v=gJEkECpgsVg&list=PLubmBFLX1_vhN50OkjdmihVzd3kdYKprw"},
            {"titulo": "Deep Learning", "instrutor": "Dalcimar Casanova", "badge": "Deep Learning", "link": "https://www.youtube.com/watch?v=0VD_2t6EdS4&list=PL9At2PVRU0ZqVArhU9QMyI3jSe113_m2-"},
            {"titulo": "Cloud", "instrutor": "Oracle Database Product Management", "badge": "Cloud", "link": "https://www.youtube.com/watch?v=ptEmLAoBET8&list=PLdtXkK5KBY57_y3Z0SW2cbCqGUPbfc94w"},
            {"titulo": "APIs (FastAPI)", "instrutor": "Hashtag Programação", "badge": "Web", "link": "https://www.youtube.com/watch?v=Eih-eCCDHW0&list=PLpdAy0tYrnKy3TvpCT-x7kGqMQ5grk1Xq&index=2"},
        ],
        "Avançado": [
            {"titulo": "Estatística Avançada", "instrutor": "A Ciência da Estatística", "badge": "Stats", "link": "https://www.youtube.com/watch?v=eYvf9ySCWcg&list=PL5Dg8nFln2eVsLUFxlYqjKh4Ps5nW2j1W"},
            {"titulo": "LLMs", "instrutor": "Vizuara", "badge": "LLMs", "link": "https://www.youtube.com/watch?v=Xpr8D6LeAtw&list=PLPTV0NXA_ZSgsLAr8YCgCwhPIJNNtexWu"},
            {"titulo": "Product Management", "instrutor": "Diogo Becker", "badge": "Product", "link": "https://www.youtube.com/watch?v=kJwvGhO6BhQ&list=PLXSOhWZ2OouWAyu2nuxz3VP5RZPx3q8uD"},
            {"titulo": "Métricas", "instrutor": "Diogo Becker", "badge": "Product", "link": "https://www.youtube.com/watch?v=7cdVqvwArkU&list=PLXSOhWZ2OouWrjuTz-6zrsMRU6wKTC5X2"},
            {"titulo": "Priorização", "instrutor": "Diogo Becker", "badge": "Product", "link": "https://www.youtube.com/watch?v=FN0M1EqdTtY&list=PLXSOhWZ2OouVIQSX1Xxt_nD85FkngBu7m"},
        ]
    },
    "Engenheiro de Dados": {
        "Iniciante": [
            {"titulo": "Introdução ao Python", "instrutor": "TéoMeWhy", "badge": "Python", "link": "https://www.youtube.com/watch?v=OeKzVjiiRm4&list=PLvlkVRRKOYFSpRkqnR0p2A-eaVlpLnN3D"},
            {"titulo": "Pandas", "instrutor": "TéoMeWhy", "badge": "Dados", "link": "https://www.youtube.com/watch?v=9Cw7iIjFlBc&list=PLvlkVRRKOYFQHnDhjTmXLEz3HU5WTgOcF"},
            {"titulo": "SQL", "instrutor": "TéoMeWhy", "badge": "SQL", "link": "https://www.youtube.com/watch?v=VmkJG8awKqM&list=PLvlkVRRKOYFRo651oD0JptVqfQGDvMi3j"},
            {"titulo": "Streamlit", "instrutor": "TéoMeWhy", "badge": "Web", "link": "https://www.youtube.com/watch?v=JLcEWe7woVk&list=PLvlkVRRKOYFRYA40hJ_V8e_iC5Lu6YPyn"},
            {"titulo": "Git & Github", "instrutor": "TéoMeWhy", "badge": "Git", "link": "https://www.youtube.com/watch?v=84FhNXNWoig&list=PLvlkVRRKOYFQyKmdrassLNxkzSMM6tcSL"},
            {"titulo": "APIs (FastAPI)", "instrutor": "Hashtag Programação", "badge": "Web", "link": "https://www.youtube.com/watch?v=Eih-eCCDHW0&list=PLpdAy0tYrnKy3TvpCT-x7kGqMQ5grk1Xq&index=2"},
            {"titulo": "MLFlow", "instrutor": "TéoMeWhy", "badge": "MLOps", "link": "https://www.youtube.com/watch?v=W8bxk42C9UE&list=PLvlkVRRKOYFQeQEA5Lc0US9i-EK8eGgrs"},
            {"titulo": "Metodologia Ágil", "instrutor": "D1UP Academy", "badge": "Agile", "link": "https://www.youtube.com/watch?v=-2W_loW_QYw&list=PLoGDMdX4pUAfso0bQWSZFgjEBlr2H9IBU"},
        ],
        "Intermediário": [
            {"titulo": "Cloud", "instrutor": "Oracle Database Product Management", "badge": "Cloud", "link": "https://www.youtube.com/watch?v=ptEmLAoBET8&list=PLdtXkK5KBY57_y3Z0SW2cbCqGUPbfc94w"},
            {"titulo": "Product Management", "instrutor": "Diogo Becker", "badge": "Product", "link": "https://www.youtube.com/watch?v=kJwvGhO6BhQ&list=PLXSOhWZ2OouWAyu2nuxz3VP5RZPx3q8uD"},
            {"titulo": "Métricas", "instrutor": "Diogo Becker", "badge": "Product", "link": "https://www.youtube.com/watch?v=7cdVqvwArkU&list=PLXSOhWZ2OouWrjuTz-6zrsMRU6wKTC5X2"},
            {"titulo": "Priorização", "instrutor": "Diogo Becker", "badge": "Product", "link": "https://www.youtube.com/watch?v=FN0M1EqdTtY&list=PLXSOhWZ2OouVIQSX1Xxt_nD85FkngBu7m"},
            {"titulo": "Estatística Básica", "instrutor": "TéoMeWhy", "badge": "Stats", "link": "https://www.youtube.com/watch?v=4CcgZXXIl7o&list=PLvlkVRRKOYFQGIZdz7BycJet9OncyXlbq"},
            {"titulo": "Machine Learning pt.1", "instrutor": "TéoMeWhy", "badge": "ML", "link": "https://www.youtube.com/watch?v=oz_rZ92Tmls&list=PLvlkVRRKOYFR6_LmNcJliicNan2TYeFO2"},
            {"titulo": "Machine Learning pt.2", "instrutor": "TéoMeWhy", "badge": "ML", "link": "https://www.youtube.com/watch?v=oj0ACpEHpS0&list=PLvlkVRRKOYFTXcpttQSZmv1wDg7F3uH7o"},
            {"titulo": "Visualização dos Dados", "instrutor": "ICMCTV", "badge": "DataViz", "link": "https://www.youtube.com/watch?v=BLIosfH2yM0&list=PLt7qVSwRVn5YEIvaMb02IJVKCpauWV-s9"},
        ],
        "Avançado": [
            {"titulo": "Panorama da Estatística", "instrutor": "A Ciência da Estatística", "badge": "Stats", "link": "https://www.youtube.com/watch?v=wAYB75xEdZQ&list=PL5Dg8nFln2eXGSjEct01QinGi4rrNthQG"},
            {"titulo": "Probabilidade", "instrutor": "A Ciência da Estatística", "badge": "Stats", "link": "https://www.youtube.com/watch?v=vzzG3oaZtOA&list=PL5Dg8nFln2eWlB9DLi9drLtPcm5UANcUI"},
            {"titulo": "Time Series - Conceitos Básicos", "instrutor": "Professor Vinicius Lima", "badge": "Time Series", "link": "https://www.youtube.com/watch?v=rexHHx6Nwec&list=PLubmBFLX1_vgGv4sAUG9O0HUw8NzJqhyD"},
            {"titulo": "Time Series - ARIMA", "instrutor": "Professor Vinicius Lima", "badge": "Time Series", "link": "https://www.youtube.com/watch?v=gJEkECpgsVg&list=PLubmBFLX1_vhN50OkjdmihVzd3kdYKprw"},
            {"titulo": "Deep Learning", "instrutor": "Dalcimar Casanova", "badge": "Deep Learning", "link": "https://www.youtube.com/watch?v=0VD_2t6EdS4&list=PL9At2PVRU0ZqVArhU9QMyI3jSe113_m2-"},
            {"titulo": "LLMs", "instrutor": "Vizuara", "badge": "LLMs", "link": "https://www.youtube.com/watch?v=Xpr8D6LeAtw&list=PLPTV0NXA_ZSgsLAr8YCgCwhPIJNNtexWu"},
        ]
    }
}

def buscar_cursos(termo_busca: str, trilha_filtro: str, nivel_filtro: str, badge_filtro: str) -> List[Dict]:
    """Busca cursos baseado nos filtros aplicados"""
    resultados = []
    
    for trilha, niveis in CURSOS_DATABASE.items():
        # Filtro de trilha
        if trilha_filtro != "Todas" and trilha != trilha_filtro:
            continue
            
        for nivel, cursos in niveis.items():
            # Filtro de nível
            if nivel_filtro != "Todos" and nivel != nivel_filtro:
                continue
                
            for curso in cursos:
                # Filtro de badge
                if badge_filtro != "Todos" and curso["badge"] != badge_filtro:
                    continue
                    
                # Busca por termo
                if termo_busca:
                    termo_lower = termo_busca.lower()
                    if (termo_lower in curso["titulo"].lower() or 
                        termo_lower in curso["instrutor"].lower() or 
                        termo_lower in curso["badge"].lower()):
                        resultados.append({**curso, "trilha": trilha, "nivel": nivel})
                else:
                    resultados.append({**curso, "trilha": trilha, "nivel": nivel})
    
    return resultados

def exibir_curso_card(curso: Dict, index: int):
    """Exibe um card de curso"""
    nivel_emoji = {
        "Iniciante": "🎯",
        "Intermediário": "🚀",
        "Avançado": "💎"
    }
    
    st.markdown(f"""
    <div class="course-card">
        <span class="badge">{curso['badge']}</span>
        <h3 style="color: #1a1a2e !important; margin: 0.5rem 0;">
            <span class="level-badge">{nivel_emoji.get(curso['nivel'], '📚')}</span>
            {curso['titulo']}
        </h3>
        <p style="color: #666 !important; margin: 0.5rem 0;">
            📹 {curso['instrutor']}
        </p>
        <p style="color: #7B1FA2 !important; font-weight: 600; font-size: 0.9rem; margin: 0.5rem 0;">
            {curso['trilha']} • {curso['nivel']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button("🎓 Acessar Curso", curso['link'], use_container_width=True)
    st.markdown("---")

def pagina_home():
    """Página inicial"""
    st.markdown("""
    # 🎓 BEM VINDO À PLATAFORMA DE ESTUDOS
    ## DO TIME DE DATA SCIENCE - THE PROPHETS
    """)
    
    st.info("""
    **Transforme sua carreira com trilhas especializadas em Data Science, Machine Learning e Inteligência Artificial.**
    
    Acesse conteúdo curado pelos melhores profissionais do mercado e evolua do básico ao avançado com metodologia comprovada.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📊 Cientista de Dados
        Domine Python, Machine Learning, Deep Learning e estatística avançada. Construa modelos preditivos e tome decisões baseadas em dados.
        
        **Cursos:** 30+ | **Níveis:** Iniciante → Avançado
        """)
    
    with col2:
        st.markdown("""
        ### ⚙️ Engenheiro de Dados
        Aprenda a construir pipelines de dados, trabalhar com Big Data, Cloud Computing e arquiteturas escaláveis.
        
        **Cursos:** 22+ | **Níveis:** Iniciante → Avançado
        """)
    
    with col3:
        st.markdown("""
        ### 👔 Gestor de Dados
        Desenvolva habilidades de liderança, gestão de projetos de dados e estratégias para liderar equipes de alta performance.
        
        **Status:** 🚧 Em desenvolvimento
        """)

def pagina_busca():
    """Página de busca com filtros"""
    st.markdown("# 🔍 Pesquisar Cursos")
    st.markdown("Encontre o curso perfeito para seu desenvolvimento profissional")
    
    # Busca
    termo_busca = st.text_input("🔎 Digite o nome do curso, tecnologia ou instrutor...", "")
    
    st.markdown("### Filtros")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        trilha_filtro = st.selectbox(
            "🎯 Trilha",
            ["Todas", "Cientista de Dados", "Engenheiro de Dados"]
        )
    
    with col2:
        nivel_filtro = st.selectbox(
            "📊 Nível",
            ["Todos", "Iniciante", "Intermediário", "Avançado"]
        )
    
    # Extrair todas as badges únicas
    todas_badges = set()
    for trilha in CURSOS_DATABASE.values():
        for nivel in trilha.values():
            for curso in nivel:
                todas_badges.add(curso["badge"])
    
    with col3:
        badge_filtro = st.selectbox(
            "🏷️ Tecnologia",
            ["Todos"] + sorted(list(todas_badges))
        )
    
    # Buscar cursos
    if st.button("🔍 Buscar", type="primary"):
        st.session_state.ultima_busca = True
    
    # Exibir resultados
    if st.session_state.get('ultima_busca', False):
        resultados = buscar_cursos(termo_busca, trilha_filtro, nivel_filtro, badge_filtro)
        
        st.markdown("---")
        st.markdown(f"### 📚 {len(resultados)} curso(s) encontrado(s)")
        
        if resultados:
            # Organizar em colunas
            for i in range(0, len(resultados), 2):
                col1, col2 = st.columns(2)
                
                with col1:
                    if i < len(resultados):
                        exibir_curso_card(resultados[i], i)
                
                with col2:
                    if i + 1 < len(resultados):
                        exibir_curso_card(resultados[i + 1], i + 1)
        else:
            st.warning("😕 Nenhum curso encontrado com os filtros aplicados.")
            st.info("💡 **Dica:** Tente remover alguns filtros ou use termos mais gerais.")

def pagina_trilha(trilha_nome: str):
    """Página de trilha específica"""
    st.markdown(f"# 🎯 Trilha de {trilha_nome}")
    
    if trilha_nome == "Gestor de Dados":
        st.info("🚧 **Conteúdo em desenvolvimento** - Em breve disponível! 🚧")
        return
    
    descricoes = {
        "Cientista de Dados": "Desenvolva habilidades completas em análise de dados, machine learning e inteligência artificial para se tornar um cientista de dados de excelência.",
        "Engenheiro de Dados": "Construa pipelines robustos, trabalhe com Big Data e domine arquiteturas de dados escaláveis para se tornar um engenheiro de dados completo."
    }
    
    st.info(descricoes.get(trilha_nome, ""))
    
    # Legenda
    st.markdown("""
    <div style='background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin: 1rem 0;'>
        <span style='font-size: 1.5rem;'>🎯</span> <strong>Iniciante</strong> - Fundamentos essenciais |
        <span style='font-size: 1.5rem;'>🚀</span> <strong>Intermediário</strong> - Especialização |
        <span style='font-size: 1.5rem;'>💎</span> <strong>Avançado</strong> - Expertise
    </div>
    """, unsafe_allow_html=True)
    
    cursos_trilha = CURSOS_DATABASE.get(trilha_nome, {})
    
    for nivel, cursos in cursos_trilha.items():
        nivel_emoji = {
            "Iniciante": "🎯",
            "Intermediário": "🚀",
            "Avançado": "💎"
        }
        
        st.markdown(f"## {nivel_emoji[nivel]} {nivel}")
        st.markdown(f"*{len(cursos)} cursos disponíveis*")
        
        # Exibir cursos em grid
        for i in range(0, len(cursos), 3):
            cols = st.columns(3)
            
            for j, col in enumerate(cols):
                if i + j < len(cursos):
                    curso = cursos[i + j]
                    with col:
                        exibir_curso_card({**curso, "trilha": trilha_nome, "nivel": nivel}, i + j)
        
        st.markdown("---")

# Sidebar para navegação
with st.sidebar:
    st.markdown("# 🎓 The Prophets")
    st.markdown("### Navegação")
    
    pagina = st.radio(
        "Escolha uma página:",
        ["🏠 Início", "🔍 Pesquisar Cursos", "📊 Cientista de Dados", "⚙️ Engenheiro de Dados", "👔 Gestor de Dados"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### 📊 Estatísticas")
    
    total_cursos = sum(len(cursos) for trilha in CURSOS_DATABASE.values() for cursos in trilha.values())
    st.metric("Total de Cursos", total_cursos)
    
    st.markdown("---")
    st.caption("© 2025 The Prophets | Time de Data Science")

# Roteamento de páginas
if pagina == "🏠 Início":
    pagina_home()
elif pagina == "🔍 Pesquisar Cursos":
    pagina_busca()
elif pagina == "📊 Cientista de Dados":
    pagina_trilha("Cientista de Dados")
elif pagina == "⚙️ Engenheiro de Dados":
    pagina_trilha("Engenheiro de Dados")
elif pagina == "👔 Gestor de Dados":
    pagina_trilha("Gestor de Dados")
