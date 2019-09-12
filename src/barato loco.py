
class cachorro:
    nome = None
    peso = None
    idade = None
    cor = None


    def latir(self):
        print("au au")
    
    '''def latir(self):
        if self.peso<3
            print("au au")
        else
            print ("auuuu")
         '''


    def andar(self):
        print("O " + self.nome + " andou")

meu_cahcorro = cachorro()
meu_cahcorro.nome = "rex"
meu_cahcorro.peso = 4
meu_cahcorro.idade = 3
meu_cahcorro.cor = "marron"

print(meu_cahcorro.nome)
meu_cahcorro.andar()
meu_cahcorro.latir()
