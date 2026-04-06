import streamlit as st
from src.crew import run_post_generator
from src.chains.profile_chain import run_profile_analyzer
from src.chains.repurpose_chain import run_repurpose

st.set_page_config(
    page_title="LinkedIn AI Copilot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 LinkedIn AI Copilot")
st.caption("Seu assistente de IA para criar e otimizar conteúdo no LinkedIn")

st.divider()

feature = st.selectbox(
    "O que você quer fazer?",
    options=[
        "✍️ Gerar post",
        "🔍 Analisar perfil",
        "♻️ README → Post",
    ]
)

st.divider()

# ──────────────────────────────────────────
# FEATURE 1 — Gerar post
# ──────────────────────────────────────────
if feature == "✍️ Gerar post":
    st.subheader("✍️ Gerador de posts")
    st.caption("Descreva um tema e o agente pesquisa na internet e escreve o post pra você.")

    topic = st.text_input(
        "Sobre o que é o post?",
        placeholder="Ex: como agentes de IA estão automatizando processos empresariais"
    )

    tone = st.radio(
        "Tom do post",
        options=["Educativo", "Storytelling", "Técnico"],
        horizontal=True
    )

    if st.button("🚀 Gerar post", use_container_width=True):
        if not topic.strip():
            st.warning("Digite um tema para o post.")
        else:
            with st.spinner("Agentes trabalhando... isso pode levar alguns segundos ⚙️"):
                try:
                    result = run_post_generator(topic=topic, tone=tone.lower())
                    st.success("Post gerado com sucesso!")
                    st.divider()
                    st.markdown("### 📋 Seu post")
                    st.text_area("Copie e cole no LinkedIn:", value=result, height=350)
                except Exception as e:
                    st.error(f"Erro ao gerar post: {e}")

# ──────────────────────────────────────────
# FEATURE 2 — Analisar perfil
# ──────────────────────────────────────────
elif feature == "🔍 Analisar perfil":
    st.subheader("🔍 Analisador de perfil")
    st.caption("Cole o texto do seu perfil e receba uma análise com melhorias concretas.")

    profile_text = st.text_area(
        "Cole aqui o texto do seu perfil (Sobre, cargo, experiências):",
        placeholder="Ex: Sou desenvolvedor de software, trabalho com Java...",
        height=250
    )

    if st.button("🔍 Analisar perfil", use_container_width=True):
        if not profile_text.strip():
            st.warning("Cole o texto do seu perfil antes de continuar.")
        else:
            with st.spinner("Analisando seu perfil... ⚙️"):
                try:
                    result = run_profile_analyzer(profile_text=profile_text)
                    st.success("Análise concluída!")
                    st.divider()
                    st.markdown("### 📋 Resultado")
                    st.markdown(result)
                except Exception as e:
                    st.error(f"Erro ao analisar perfil: {e}")

# ──────────────────────────────────────────
# FEATURE 3 — README → Post
# ──────────────────────────────────────────
elif feature == "♻️ README → Post":
    st.subheader("♻️ README → Post LinkedIn")
    st.caption("Cole o README do seu projeto e transforme em um post pronto para publicar.")

    readme_text = st.text_area(
        "Cole aqui o README do seu projeto:",
        placeholder="# Meu Projeto\nDescrição do projeto, tecnologias, como funciona...",
        height=250
    )

    tone = st.radio(
        "Tom do post",
        options=["Educativo", "Storytelling", "Técnico"],
        horizontal=True
    )

    if st.button("♻️ Transformar em post", use_container_width=True):
        if not readme_text.strip():
            st.warning("Cole o README antes de continuar.")
        else:
            with st.spinner("Transformando seu README em post... ⚙️"):
                try:
                    result = run_repurpose(readme_text=readme_text, tone=tone.lower())
                    st.success("Post gerado com sucesso!")
                    st.divider()
                    st.markdown("### 📋 Seu post")
                    st.text_area("Copie e cole no LinkedIn:", value=result, height=350)
                except Exception as e:
                    st.error(f"Erro ao gerar post: {e}")