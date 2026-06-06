import time 
import random 

# 1 . O DECORATOR (O Escudo de Resiliencia)
def meu_retry(tentativas = 3, espera_segundos = 2):
    def decorator(funcao_original):
        def envelope(*args, **kwargs):
            for tentativa in range (1, tentativas + 1):
                try:
                    #tenta executar a função 
                    return funcao_original(*args, **kwargs)
                except Exception as erro:
                    # Se der erro, ele captura aqui
                    print(f"⚠️ Falha na tentativa {tentativa}/{tentativas}. Erro: {erro}")
                    
                    if tentativa == tentativas:
                        print("❌ Erro Crítico: O sistema desistiu após o limite de tentativas.")
                        raise # Se acabaram as tentativas, o erro é jogado na tela
                
                    print(f"🔄 Aguardando {espera_segundos} segundos para tentar de novo...")
                    time.sleep(espera_segundos)  
        return envelope
    return decorator


#----------------------------------------------------------#

# 2. A SUA FUNÇÃO DE INTEGRAÇÃO
# Configuramos para tentar 4 vezes, esperando 1 segundo entre elas
@meu_retry(tentativas=4, espera_segundos= 1)
def conectar_api_openai():
    print('Enviando texto para analise do ChatGPT...')
    
    #Simulando umm erro de rede (falha em 70% das vezes)
    chance_de_erro = random.random()
    if chance_de_erro < 0.7:
        raise ConnectionError('Servidor sobrecarregado (TimeOut).')
    
    return '✅ Sucesso! A análise da IA foi recebida.'

# 3. TESTANDO A RESILIÊNCIA
resultado_ia = conectar_api_openai()
print(resultado_ia)