from tkinter import ttk, constants, Label

class ResultView:
    def __init__(self, root, handle_set_param, datahandler):
        self._root = root
        self._handle_set_param = handle_set_param
        self._datahandler = datahandler
        self._frame = None
        print(self._datahandler)        
        print(self._datahandler.filter_value)

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _calculate_knn(self):


        print("parametrit asettu ja knn initialisoitu")
        # print(self._datahandler.k)
        # print(self._datahandler.layers)
        self._datahandler.predict()
        print(self._datahandler.evaluate())




    def _initialize(self):
        self._calculate_knn()
        #print(self._datahandler.knn.)
        self._frame = ttk.Frame(master=self._root)
        print(self._datahandler.evaluate())

        label = ttk.Label(master=self._frame, text="ResultView")
        label.grid(row=0, column=0)

        # text = Label(self, text="Tähän tulee jotain tekstiä, joka selittää mitä tapahtuu")
        # text.place(x=70,y=90)

        set_param_button = ttk.Button(
            master=self._frame,
            text="Palaa parametrien asetukseen",
            command=self._handle_set_param
        )

        set_param_button.grid(padx=5, pady=5, sticky=constants.EW)

