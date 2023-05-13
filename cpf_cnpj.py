from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def criar_novo(documento):
        doc_str = str(documento)
        if len(doc_str) == 11:
            return DocCpf(doc_str)
        if len(doc_str) == 14:
            return DocCnpj(doc_str)
        if len(doc_str) == 20:
            return DocQualquer(doc_str)
        else:
            raise ValueError("Documento incorreto!")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
      mascara = CPF()
      return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

class DocQualquer:
    def __init__(self, documento):
        self.documento = documento

    def __str__(self):
        return self.documento

#------Para usar no arquivo Main--------
#from cpf_cnpj import Documento
#from validate_docbr import CNPJ

#cpf_um = Cpf("15316264754")
#print(cpf_um)

#exemplo_cnpj = "35379838000112"
#exemplo_cpf = "11111111112"
#outro_doc = "12345678910111213145"


#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))
#documento = Documento.criar_novo(outro_doc)
#print(documento)
