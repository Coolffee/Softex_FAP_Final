from abc import ABC, abstractmethod

class Documento(ABC):
    @abstractmethod
    def criar(self):
        pass

class DocumentoPDF(Documento):
    def criar(self):
        print("Criando documento PDF...")
        return "Documento PDF criado"

class DocumentoWord(Documento):
    def criar(self):
        print("Criando documento Word...")
        return "Documento Word criado"

class FabricaDeDocumentos:
    def criar_documento(self, tipo):
        if tipo == "pdf":
            return DocumentoPDF()
        elif tipo == "word":
            return DocumentoWord()
        else:
            return None

fabrica = FabricaDeDocumentos()
pdf = fabrica.criar_documento("pdf")
word = fabrica.criar_documento("word")

print(pdf.criar())
print(word.criar())
