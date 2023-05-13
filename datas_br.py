from datetime import datetime, timedelta


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = [
            "Janeiro", "Fevereiro", "Março",
            "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro",
            "Outubro", "Novembro", "Dezembro"
        ]

        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana_lista = [
            "Segunda-feira", "Terça-feira",
            "Quarta-feira", "Quinta-feira", "Sexta-feira",
            "Sábado", "Domingo"
        ]

        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro


class Cadastro:
    def __init__(self):
        self.data_cadastro = datetime.today()

    def tempo_cadastro(self):
        agora = datetime.today() + timedelta(days=15, minutes=20, seconds=30)
        return agora - self.tempo_cadastro


''' ------- Usar no arquivo Main ------------------------------
from datetime import datetime, timedelta
from datas_br import DatasBr, Cadastro

hoje = DatasBr()
cadastro = Cadastro()
print(hoje.tempo_cadastro())
print(cadastro.tempo_cadastro())



cadastro = DatasBr()
print(cadastro.format_data())


hoje = datetime.today()
hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M")

print(hoje)
print(hoje_formatada)
print(type(hoje_formatada))
'''

