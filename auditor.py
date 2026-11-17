import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

print("[+] Lendo arquivo de evidência...")
f = open("evidencia_sqli.txt", "r", encoding="utf-8")
log_data = f.read()
f.close()

prompt = f"""
Analise o log de segurança abaixo e aponte os riscos e controles ISO 27001:
{log_data}
"""

print("[+] Enviando para o Gemini...")
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
)

rel = open("relatorio_iso27001.md", "w", encoding="utf-8")
rel.write(response.text)
rel.close()

print("[+] Relatório gerado com sucesso!")
