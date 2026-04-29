import flet as ft

class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):

        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)
        # ROW 1
        self._txtNmax = ft.TextField(label="Numero Max",value=self._controller.getNmax(),
                                     disabled=True)
        self._txtTmax = ft.TextField(label="Tentativi Max", value=self._controller.getTmax(),
                                     disabled=True)
        self._txtT = ft.TextField(label="Tentativi Rimanenti",
                                  disabled=True)

        self._row1 = ft.Row(controls=[self._txtNmax, self._txtTmax, self._txtT])

        # ROW 2
        self._txtInTentativo = ft.TextField(label="Valore")
        self._btnReset = ft.ElevatedButton(text="Nuova Partita", on_click=self._controller.reset)
        self.btnPlay = ft.ElevatedButton(text="Indovina", on_click=self._controller.play)
        self._row2 = ft.Row(controls=[self._txtInTentativo,self._btnReset, self.btnPlay])

        # ROW 3
        self._btnAbbandona = ft.ElevatedButton(text="Abbandona Partita", on_click=self._controller.abbandona)
        self._progressBar = ft.ProgressBar(value=0.0, width=400)
        self._row3 = ft.Row(controls=[self._btnAbbandona, self._progressBar])

        # ROW 4
        self._ddDifficolta = ft.Dropdown(
            label="Difficoltà",
            on_change=self._controller.setDifficolta,
            options=[
                ft.dropdown.Option("Facile"),
                ft.dropdown.Option("Medio"),
                ft.dropdown.Option("Difficile"),
            ]
        )
        self._txtIntervallo = ft.TextField(label="Intervallo", disabled=True)
        self._row4 = ft.Row(controls=[self._ddDifficolta, self._txtIntervallo])

        # Layout
        self._lvOut = ft.ListView(expand=True) # expand = True cosi possiamo scrollarlo!

        self._page.add(self._row1, self._row2, self._row3, self._row4, self._lvOut)

        self._page.update()

    def setController(self,controller):
        self._controller = controller

    def update(self):
        self._page.update()