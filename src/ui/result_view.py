from tkinter import ttk, constants, Label

class ResultView:
    def __init__(self, root, handle_param):
        self._root = root
        self._handle_param = handle_param
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        print("ResultView._initialize")

        label = ttk.Label(master=self._frame, text="ResultView")
        label.grid(row=0, column=0)

        # text = Label(self, text="Tähän tulee jotain tekstiä, joka selittää mitä tapahtuu")
        # text.place(x=70,y=90)

        set_param_button = ttk.Button(
            master=self._frame,
            text="Palaa suoritusnäkymään",
            command=self._handle_param
        )

        set_param_button.grid(padx=5, pady=5, sticky=constants.EW)

