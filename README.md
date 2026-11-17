# Auditoria de segurança com IA (OWASP & ISO 27001)

Ferramenta de automação desenvolvida para acelerar a triagem de incidentes de segurança e a conformidade regulatória utilizando Inteligência Artificial Generativa.

## O Problema
Em auditorias de segurança corporativa, o tempo gasto para analisar logs brutos de testes de intrusão (como falhas do OWASP Top 10) e correlacioná-los com frameworks de governança (ISO 27001) costuma ser totalmente manual e lento.

## A Solução 
Este script em Python automatiza o fluxo:
1. Lê arquivos de evidências de testes práticos (ex: Kali Linux / Burp Suite).
2. Conecta-se via API a um modelo de linguagem (Gemini) aplicando engenharia de prompt especializada em GRC.
3. Gera de forma automatizada o relatório de mitigação de riscos alinhado à ISO 27001.

## Tecnologias Utilizadas
* Python
* Google GenAI SDK (Gemini)
* Automação de Processos e Análise de Dados com IA
