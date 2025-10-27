# ============================================================
# 🧠 Teste completo para mapear_palavra_para_sinal (PoC Libras)
# ============================================================

import unicodedata
import pytest


def normalizar(palavra):
    """Remove acentos e converte para minúsculas."""
    return ''.join(
        c for c in unicodedata.normalize('NFD', palavra.lower())
        if unicodedata.category(c) != 'Mn'
    )


def mapear_palavra_para_sinal(palavra):
    dicionario_libras_conceitual = {
        "oi": ["mao_aberta_para_frente", "aceno_lateral", "sorriso_leve"],
        "ola": ["mao_aberta_para_frente", "aceno_lateral", "sorriso_leve"],
        "obrigado": ["mao_no_queixo", "move_para_frente", "olhar_grato"],
        "agua": ["dedos_unidos_em_bico", "toca_boca", "move_para_baixo_duas_vezes"],
        "comer": ["mao_fechada_polegar_na_boca", "movimento_mastigar"],
        "sim": ["mao_fechada", "polegar_para_cima", "balancar_cabeca_sim"],
        "nao": ["mao_aberta", "aceno_lateral_negativo", "balancar_cabeca_nao"],
        "ajuda": ["mao_esquerda_aberta", "mao_direita_fecha_e_levanta"],
    }

    palavra_norm = normalizar(palavra)

    if palavra_norm in dicionario_libras_conceitual:
        comandos_sinal = dicionario_libras_conceitual[palavra_norm]
        print(f"✅ '{palavra}' → {comandos_sinal}")
        return comandos_sinal
    else:
        print(f"⚠️ '{palavra}' não encontrado no dicionário conceitual.")
        return ["sinal_desconhecido"]


def test_ola():
    assert "mao_aberta_para_frente" in mapear_palavra_para_sinal("Olá")
    assert "aceno_lateral" in mapear_palavra_para_sinal("Olá")

def test_obrigado():
    assert mapear_palavra_para_sinal("Obrigado") == ["mao_no_queixo", "move_para_frente", "olhar_grato"]

def test_sim():
    assert "polegar_para_cima" in mapear_palavra_para_sinal("sim")

def test_agua_com_acento():
    assert "toca_boca" in mapear_palavra_para_sinal("Água")

def test_agua_sem_acento():
    assert "toca_boca" in mapear_palavra_para_sinal("Agua")

def test_maiusculas():
    assert "mao_direita_fecha_e_levanta" in mapear_palavra_para_sinal("AJUDA")

def test_palavra_desconhecida():
    assert mapear_palavra_para_sinal("cachorro") == ["sinal_desconhecido"]


if __name__ == "__main__":
    print("\n🔍 Rodando testes automáticos...\n")
    pytest.main(["-v", __file__])
    print("\n🏁 Testes concluídos.")
