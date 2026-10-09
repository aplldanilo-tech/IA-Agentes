import sys
import os
import requests
import json

class AgenteIA:
    def __init__(self, nome, funcao, instrucao_mestre):
        self.nome = nome
        self.funcao = funcao
        self.instrucao = instrucao_mestre

    def pensar_e_responder(self, prompt_usuario, api_key):
        # Conexão direta com a API do Gemini 1.5 Flash (Leve e rápida na nuvem)
        url = f"https://googleapis.com{api_key}"
        headers = {'Content-Type': 'application/json'}
        
        contexto_completo = f"Você é o {self.nome}, especialista em {self.funcao}. Sua diretriz é: {self.instrucao}. Responda ao seguinte comando: {prompt_usuario}"
        
        payload = {
            "contents": [{"parts": [{"text": contexto_completo}]}]
        }
        
        try:
            resposta = requests.post(url, headers=headers, json=payload, timeout=30)
            resultado = resposta.json()
            # Extrai o texto limpo gerado pela IA
            texto_ia = resultado['candidates'][0]['content']['parts'][0]['text']
            return texto_ia
        except Exception as e:
            return f"⚠️ Erro ao acionar a IA para o {self.nome}: {str(e)}"

def rodar_sala_de_agentes_real(pergunta):
    print("================================================================")
    print("🧠 INICIANDO SALA MULTI-AGENTE COM IA REAL (GEMINI CLOUD)")
    print("================================================================")
    print(f"🎯 Pergunta do Usuário: {pergunta}\n")
    
    # Pegando a chave de API salva com segurança nas configurações da nuvem
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ ERRO: A chave 'GEMINI_API_KEY' não foi configurada no GitHub Actions.")
        return

    # Definindo nossa equipe de IA real
    agente_osint = AgenteIA("Agente_OSINT", "Varredura Pública e Reconhecimento", "Analise o alvo e indique quais ferramentas e comandos de OSINT (como Sherlock ou theHarvester) devem ser usados.")
    agente_auditor = AgenteIA("Agente_Auditor", "Análise de Código de Máquina", "Com base nas ferramentas de OSINT indicadas, crie um plano de segurança detalhado contra vulnerabilidades.")

    # Execução em cadeia: O primeiro agente pensa...
    print(f"🔄 Ativando {agente_osint.nome}...")
    resposta_osint = agente_osint.pensar_e_responder(pergunta, api_key)
    print(f"\n[📝 RESPOSTA DO AGENTE OSINT]:\n{resposta_osint}\n")
    print("-" * 60)
    
    # O segundo agente recebe o relatório do primeiro e complementa com IA de verdade!
    print(f"🔄 Ativando {agente_auditor.nome}...")
    resposta_auditoria = agente_auditor.pensar_e_responder(resposta_osint, api_key)
    print(f"\n[📝 RESPOSTA DO AGENTE AUDITOR]:\n{resposta_auditoria}\n")
    
    print("================================================================")
    print("🎉 EXECUÇÃO CONCLUÍDA COM IA REAL NA NUVEM!")
    print("================================================================")

if __name__ == "__main__":
    comando = sys.argv[1] if len(sys.argv) > 1 else "Fazer varredura de OSINT no domínio alvo.com"
    rodar_sala_de_agentes_real(comando)
