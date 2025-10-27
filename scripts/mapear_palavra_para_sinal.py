# mapeamento conceitual simples: palavra -> comandos de sinal
# Use este arquivo como exemplo/PoC; em produção substitua por DB/ML.

def mapear_palavra_para_sinal(palavra):
    # Dicionário conceitual de palavras para "comandos de sinal"
    # Na vida real, isto seria um banco de dados com movimentos, expressões, variantes, tempo, etc.
    dicionario_libras_conceitual = {
        "oi": ["mao_aberta_para_frente", "aceno_lateral", "sorriso_leve"],
        "olá": ["mao_aberta_para_frente", "aceno_lateral", "sorriso_leve"],
        "obrigado": ["mao_no_queixo", "move_para_frente", "olhar_grato"],
        "água": ["dedos_unidos_em_bico", "toca_boca", "move_para_baixo_duas_vezes"],
        "comer": ["mao_fechada_polegar_na_boca", "movimento_mastigar"],
        "sim": ["mao_fechada", "polegar_para_cima", "balancar_cabeca_sim"],
        "não": ["mao_aberta", "aceno_lateral_negativo", "balancar_cabeca_nao"],
        "ajuda": ["mao_esquerda_aberta", "mao_direita_fecha_e_levanta"],
        # ... muitas outras palavras e frases
    }

    # Normaliza entrada (minúsculas). Em etapas posteriores, adicionar normalização de acentos/stopwords.
    palavra_min = palavra.lower()

    if palavra_min in dicionario_libras_conceitual:
        comandos_sinal = dicionario_libras_conceitual[palavra_min]
        print(f"Comandos de sinal para '{palavra}': {comandos_sinal}")
        return comandos_sinal
    else:
        print(f"Sinal para '{palavra}' não encontrado no dicionário conceitual.")
        # Em um app real, usar PLN/IA para decompor a frase ou gerar sinal aproximado.
        return ["sinal_desconhecido"]

# Testes rápidos
if __name__ == "__main__":
    print("\n--- Testando Mapeamento de Sinais ---")
    mapear_palavra_para_sinal("Olá")
    mapear_palavra_para_sinal("Obrigado")
    mapear_palavra_para_sinal("cachorro")  # Esta palavra não está no dicionário
    mapear_palavra_para_sinal("Água")
    mapear_palavra_para_sinal("sim")
