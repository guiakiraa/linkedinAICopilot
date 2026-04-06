from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def run_repurpose(readme_text: str, tone: str) -> str:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    prompt = PromptTemplate(
        input_variables=["readme_text", "tone"],
        template="""
Você é um copywriter especializado em transformar conteúdo técnico em posts
engajantes para o LinkedIn, focado em profissionais de tecnologia e IA.

Transforme o README abaixo em um post para o LinkedIn.

Regras:
- Tom: {tone}
- Primeira linha deve parar o scroll — não comece com "Eu" ou "Olá"
- Explique o problema que o projeto resolve, não só o que ele faz
- Destaque as tecnologias usadas de forma natural
- Finalize com um CTA que convide a ver o projeto ou deixar comentário
- Tamanho ideal: entre 150 e 300 palavras
- Escreva em português brasileiro

---
README:
{readme_text}
"""
    )

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"readme_text": readme_text, "tone": tone})