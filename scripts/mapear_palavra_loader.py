import json
import unicodedata
from pathlib import Path

DEFAULT_PATH = Path(__file__).parent / "dicionario_libras.json"

def remover_acentos(texto: str) -> str:
    texto_nfkd = unicodedata.normalize("NFKD", texto)
    return "".join([c for c in texto_nfkd if not unicodedata.combining(c)])

def normalizar_texto(texto: str) -> str:
    texto = texto.strip().lower()
    texto = remover_acentos(texto)
    return texto

class DicionarioLibras:
    def __init__(self, path: Path = DEFAULT_PATH):
        self.path = path
        self._carregar()

    def _carregar(self):
        if not self.path.exists():
            self.data = {}
        else:
            with open(self.path, "r", encoding="utf-8") as f:
                self.data = json.load(f)

    def lookup(self, palavra: str):
        chave = normalizar_texto(palavra)
        if chave in self.data:
            return self.data[chave]
        if chave.endswith("s") and chave[:-1] in self.data:
            return self.data[chave[:-1]]
        return ["sinal_desconhecido"]

    def adicionar(self, palavra: str, comandos):
        chave = normalizar_texto(palavra)
        self.data[chave] = comandos
        self._salvar()

    def _salvar(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)