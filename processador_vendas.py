import time

# ==========================================
# 1. A INFRAESTRUTURA (Decorator)
# ==========================================
def medir_tempo_processamento(funcao_original):
    def envelope(*args, **kwargs):
        tempo_inicio = time.time()
        
        # Roda a função principal
        resultado = funcao_original(*args, **kwargs)
        
        tempo_fim = time.time()
        print(f"⏱️ AUDITORIA: O processamento levou {tempo_fim - tempo_inicio:.4f} segundos no total.")
        return resultado
    return envelope


# ==========================================
# 2. A EXTRAÇÃO DE DADOS (Generator)
# ==========================================
def ler_arquivo_gigante_simulado(total_linhas):
    for i in range(1, total_linhas + 1):
        # O 'yield' entrega apenas uma linha por vez (A catraca do metrô)
        # O sistema não guarda as milhões de linhas na memória RAM
        yield f"Venda_ID_{i} | Valor: R$ 150.00 | Status: Aprovado"


# ==========================================
# 3. A REGRA DE NEGÓCIO (O Arquiteto em Ação)
# ==========================================
@medir_tempo_processamento
def executar_pipeline_vendas(quantidade_vendas):
    print(f"🚀 Iniciando processamento de {quantidade_vendas} registros de vendas...")
    
    # Prepara o gerador
    extrator_dados = ler_arquivo_gigante_simulado(quantidade_vendas)
    
    registros_processados = 0
    
    # Consome os dados um por um de forma segura
    for linha_venda in extrator_dados:
        # Aqui, no mundo real, você enviaria essa linha para o Banco de Dados (SQL)
        registros_processados += 1
        
    print(f"✅ Sucesso: {registros_processados} registros foram processados sem travar a memória do servidor.")

# ==========================================
# 4. EXECUTANDO O SISTEMA
# ==========================================
# Vamos testar com 5 Milhões de linhas!
executar_pipeline_vendas(5000000)