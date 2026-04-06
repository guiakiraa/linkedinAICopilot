from crewai import Agent
from src.tools.search_tool import get_search_tool

def create_researcher():
    return Agent(
        role="LinkedIn Content Researcher",
        goal=(
            "Pesquisar na internet os posts e tendências mais relevantes "
            "sobre o tema fornecido, identificando estrutura, tom e ganchos "
            "que geram mais engajamento no LinkedIn."
        ),
        backstory=(
            "Você é especialista em pesquisa de conteúdo para LinkedIn. "
            "Sabe identificar padrões em posts virais, entende o que funciona "
            "para profissionais de tecnologia e IA, e sempre traz referências "
            "concretas e atuais para embasar a criação de conteúdo."
        ),
        tools=[get_search_tool()],
        verbose=True,
        allow_delegation=False,
    )