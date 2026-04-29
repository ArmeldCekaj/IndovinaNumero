from view import View
from model import Model
import flet as ft
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def reset(self, e):
        self._model.reset() # resetto lo stato del gioco lato modello!
        self._view._txtT.value = self._model.T
        self._view._progressBar.value = 0.0
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(
            ft.Text("Inizia il gioco! Indovina a quale numero sto pensando")
        )
        self._view.update()

    def setDifficolta(self, e):
        if self._view._ddDifficolta.value == None:
            self._view._lvOut.controls.append(ft.Text("Prima devi selezionare un livello"))
            self._view.update()
            return

        livello = self._view._ddDifficolta.value
        self._model.setDifficolta(livello)
        self._view._txtNmax.value = self._model.Nmax
        self._view._txtTmax.value = self._model.Tmax
        self._view.update()


    def play(self, e):
        if self._model.partitaFinita:
            self._view._lvOut.controls.append(ft.Text("La partita è terminata, inizia una nuova partita!"))
            self._view.update()
            return

        tentativoStr = self._view._txtInTentativo.value
        try :
            tentativo = int(tentativoStr)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Errore, devi inserire un valore numerico"))
            self._view.update()
            return

        res = self._model.play(tentativo)


        if res == 3:
            """il numero digitato è già stato inserito non posso farlo """
            self._view._lvOut.controls.append(
                ft.Text(f"Attenzione, {tentativo} è già stato usato"))
            self._view.update()
            return
        self._view._txtIntervallo.value = f"[{self._model.low}, {self._model.high}]"
        self._view._txtInTentativo.value = ""
        self._view._txtT.value = self._model.T
        # barra prograssione
        self._view._progressBar.value = 1 - (self._model.T / self._model.Tmax)

        if res == 0:
            """HO VINTO"""
            self._view._lvOut.controls.append(ft.Text(f"Hai vinto!, il valore corretto era: {tentativo}", color="green"))
            self._view.update()
            self._model.abbandona()
            return
        elif res == 2:
            """ NON HO PIU' VITE"""
            self._view._lvOut.controls.append(
                ft.Text(f"Hai perso! il valore corretto era: {self._model.segreto}",color="red"))
            self._view.update()
            self._model.abbandona()
            return
        elif res == -1:
            """Allora il segreto è più piccolo del tentativo"""
            self._view._lvOut.controls.append(
                ft.Text(f"Ritenta, il segreto è più piccolo di {tentativo}"))
            self._view.update()
            return

        else:
            """Allora il segreto è più grande del tentativo"""
            self._view._lvOut.controls.append(
                ft.Text(f"Ritenta, il segreto è più grande di {tentativo}"))
            self._view.update()
            return
    def abbandona(self, e):
        if self._model.segreto == None:
            self._view._lvOut.controls.append(ft.Text("Prima devi iniziare una partita"))
            self._view.update()
            return
        else:
            self._view._lvOut.controls.append(ft.Text(f"Partita termianta, l'utente ha abbandonato la partita. Il numero segreto è {self._model.segreto}"))
            self._view.update()
            self._model.abbandona()
            return


    def getNmax(self):
        """ fa il suo mestiere da passacarte perchè view e model non possono comunicare,
        ma devono passare per il controller
        """
        return self._model.Nmax
    def getTmax(self):
        return self._model.Tmax




