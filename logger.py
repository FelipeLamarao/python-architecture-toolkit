import datetime

# 1. O DECORATOR (O Vigilante/Diário de Bordo)
def meu_logger(funcao_original):
    def envelope ( *args, **kwargs):
        # 1. Anota a hora exata que a função foi acionada
        hora_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"[{hora_atual}] 📝 LOG: A função '{funcao_original.__name__}' foi chamada.")
        print(f"[{hora_atual}] 📝 LOG: Dados que entraram na função: args={args}, kwargs={kwargs}")
        
        # 2. Executa a função de negócio real
        resultado = funcao_original(*args, **kwargs)
        
        # 3. Anota o que a função devolveu (o resultado)
        print(f"[{hora_atual}] 📝 LOG: A função retornou o valor: {resultado}")
        print("-" * 50) # Linha para separar visualmente       
        
        return resultado
    return envelope
 
 
 #----------------------------------------------------------------------#
 
 #2 Minha função de negocio 
 
@meu_logger
def calcular_desconto_internacional(valor_compra, cupom=None):
    # Essa função faz APENAS o cálculo financeiro, não se preocupa em imprimir logs
    if cupom == "VIP10":
        return valor_compra * 0.90 # 10% de desconto
    return valor_compra

# 3. TESTANDO O SISTEMA (Simulando duas compras)
calcular_desconto_internacional(500)
calcular_desconto_internacional(1000, cupom="VIP10")