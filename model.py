import random
class Model(object):
    def __init__(self):
         self._Nmax = 100
         self._Tmax = 6
         self._T = self._Tmax
         self._segreto = None
         self._partitaFinita = False

         self._livelli = {
             "Facile": (50, 6),
             "Medio": (100, 7),
             "Difficile": (200, 8)}

         self._low = 0
         self._high = self._Nmax
         self._tentativiGiaFatti = set()

    def reset(self):
        """
        Questo metodo resetta lo stato del gioco. Imposta
        il segreto ad un valore randomico fra 0 ed Nmax
        e ripristina il numero di tentativi rimanenti
        :return:
        """
        self._segreto = random.randint(0, self._Nmax)
        self._T = self._Tmax
        print(self._segreto)
        self._partitaFinita = False
        self._low = 0
        self._high = self._Nmax
        self._tentativiGiaFatti = set()


    def play(self, tentativo):
        """
        Questo metodo riceve come argomento un valore intero, che sarà
        il tentativo del giocatore, e lo confronta con il segreto
        :return:
        -1 se il segreto è più piccolo del tentativo
        0 se il tentativo è uguale al segreto
        1 se il segreto è più grande del tentativo
        2 se ho terminato le mie vite
        """
        if tentativo in self._tentativiGiaFatti:
            return 3
        self._tentativiGiaFatti.add(tentativo)
        self._T -= 1
        if tentativo == self._segreto:
            """ HO VINTO!"""
            return 0
        if self._T == 0:
            """ Non ho più vite, non posso più giocare"""
            return 2
        if tentativo > self._segreto:
            """ il tentativo dell'utente è più grande del segreto"""
            self._high = tentativo
            return -1
        else:
            """ Ultimo caso in cui tentativo è minore del segreto"""
            self._low = tentativo
            return 1
    def abbandona(self):
        self._partitaFinita = True

    def setDifficolta(self, livello):
        self._Nmax, self._Tmax = self._livelli[livello]

    @property
    def Nmax(self):
        """Mi serve solo la questione per avere più controllo nel mio codice
        per la questione degli underscore"""
        return self._Nmax

    @property
    def Tmax(self):
        return self._Tmax

    @property
    def T(self):
        return self._T

    @property
    def segreto(self):
        return self._segreto
    @property
    def partitaFinita(self):
        return self._partitaFinita

    @property
    def low(self):
        return self._low

    @property
    def high(self):
        return self._high



if __name__ == "__main__":
    m = Model()
    m.reset()
    print(m.play(10))
    print(m.play(20))
    print(m.play(30))
    print(m.play(70))
    print(m.play(80))
    print(m.play(60))
    print(m.play(50))



