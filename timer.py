import time

# 1. ESTE É O DECORATOR (A "Capinha")
def meu_timer(funcao_original):
    def envelope(*args, **kwargs):
        tempo_inicial = time.time()
        
        # Aqui ele executa a sua função de verdade
        resultado = funcao_original(*args, **kwargs)
        
        tempo_final = time.time()
        print(f"⏱️ AVISO: A função '{funcao_original.__name__}' demorou {tempo_final - tempo_inicial:.2f} segundos para rodar.")
        
        return resultado
    return envelope

# ---------------------------------------------------------

# 2. A SUA FUNÇÃO DO DIA A DIA (Com o decorator aplicado)
@meu_timer
def processar_dados_clientes():
    print("Iniciando o processamento de 10.000 clientes internacionais...")
    time.sleep(2)  # Simula que o computador demorou 2 segundos pensando
    print("Processamento finalizado!")

# 3. RODANDO O SISTEMA
processar_dados_clientes()