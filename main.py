from módulos.função import *
from módulos.voz import perg
import configparser
from pathlib import Path

class jarvis(funções):
    def __init__(self):
        self.config = config['VOZ']
        match self.pergunta():
            case 'função':
                self.funcao1()
            case 'função 2':     
                self.funcao2()
            case 'função 3':
                self.funcao3()
            case _:
                self.erro()
        

if '__main__' == __name__:
    config = configparser.ConfigParser()
    config.read('config.ini', encoding="utf-8")
    jarvis()
    