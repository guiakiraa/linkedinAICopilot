from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def run_profile_analyzer(profile_text: str) -> str:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    prompt = PromptTemplate(
        input_variables=["profile_text"],
        template="""
Você é um especialista em personal branding e otimização de perfis no LinkedIn,
com foco em profissionais de tecnologia e IA.

Analise o perfil abaixo e retorne sua resposta em duas partes:

## 🔍 Análise
Aponte os pontos fracos do perfil atual. Seja direto e específico.
Avalie: clareza do título, seção "Sobre", descrição de experiências e uso de palavras-chave técnicas.

## ✅ Versão Melhorada
Reescreva as partes fracas com melhorias concretas.
Mantenha o tom profissional e autêntico. Escreva em português brasileiro.

---
PERFIL ATUAL:
{profile_text}
"""
    )

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"profile_text": profile_text})