from crewai import Crew, Task, Process
from src.agents.researcher import create_researcher
from src.agents.writer import create_writer
from src.agents.reviewer import create_reviewer

def run_post_generator(topic: str, tone: str) -> str:
    researcher = create_researcher()
    writer = create_writer()
    reviewer = create_reviewer()

    research_task = Task(
        description=(
            f"Pesquise na internet posts e tendências relevantes sobre: '{topic}'. "
            "Identifique os ganchos mais usados, estrutura dos posts com mais engajamento "
            "e os subtemas mais discutidos. Retorne um resumo estruturado com essas informações."
        ),
        expected_output=(
            "Um resumo com: principais tendências do tema, exemplos de ganchos que funcionam, "
            "estrutura comum dos posts mais engajantes e subtemas relevantes."
        ),
        agent=researcher,
    )

    write_task = Task(
        description=(
            f"Com base na pesquisa, escreva um post para o LinkedIn sobre '{topic}'. "
            f"Use o tom: {tone}. "
            "O post deve ter: uma primeira linha impactante que pare o scroll, "
            "desenvolvimento com valor real em tópicos curtos e um CTA no final que gere comentários. "
            "Escreva em português brasileiro. Tamanho ideal: entre 150 e 300 palavras."
        ),
        expected_output=(
            "Um post completo e formatado para o LinkedIn com gancho, desenvolvimento e CTA."
        ),
        agent=writer,
        context=[research_task],
    )

    review_task = Task(
        description=(
            "Revise o post escrito. Verifique: "
            "1) O gancho da primeira linha é forte o suficiente para parar o scroll? "
            "2) O conteúdo entrega valor real? "
            "3) O tom está consistente do início ao fim? "
            "4) O CTA é natural e convida ao engajamento? "
            "Retorne a versão final melhorada do post, pronta para publicar."
        ),
        expected_output=(
            "A versão final e revisada do post, pronta para ser publicada no LinkedIn."
        ),
        agent=reviewer,
        context=[write_task],
    )

    crew = Crew(
        agents=[researcher, writer, reviewer],
        tasks=[research_task, write_task, review_task],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()
    return str(result)