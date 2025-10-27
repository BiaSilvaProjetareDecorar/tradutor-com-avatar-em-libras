from mapear_palavra_loader import DicionarioLibras

# Exemplo de integração simples: reconhecimento de fala -> dicionário -> comandos

def pipeline_exemplo(texto_reconhecido: str):
    dicio = DicionarioLibras()
    palavras = texto_reconhecido.split()
    resultado = []
    for p in palavras:
        comandos = dicio.lookup(p)
        resultado.append({"palavra": p, "comandos": comandos})
    return resultado

# Uso (integre com seu reconhecer_fala_do_microfone):
# from reconhecimento_audio import reconhecer_fala_do_microfone
# texto = reconhecer_fala_do_microfone()
# if texto:
#     print(pipeline_exemplo(texto))