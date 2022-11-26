from tkinter import ttk, constants, Label

class ResultView:
    def __init__(self, root, handle_set_param, datahandler):
        self._root = root
        self._handle_set_param = handle_set_param
        self._datahandler = datahandler
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _calculate_knn(self):
        self._datahandler.predict()
        self._result = self._datahandler.evaluate()

    def _view_result_fields(self):

        correct_label = ttk.Label(master=self._frame, text=f"Oikein tunnistettuja {self._result['correct']}")
        correct_label.grid(padx=5, pady=5, sticky=constants.W)
 
        wrong_label = ttk.Label(master=self._frame, text=f"Väärin tunnistettuja {self._result['wrong']}")
        wrong_label.grid(padx=5, pady=5, sticky=constants.W)

        time_label = ttk.Label(master=self._frame, text=f"Suoritusaika {self._result['runtime']} sekuntia")
        time_label.grid(padx=5, pady=5, sticky=constants.W)

        wrong_ind_label = ttk.Label(master=self._frame, text=f"Väärien indeksit {self._result['wrong_ind']}")
        wrong_ind_label.grid(padx=5, pady=5, sticky=constants.W)

        wrong_ind_mnist_label = ttk.Label(master=self._frame, text=f"Väärien indeksit alkuperäisessä MNIST datassa {self._result['wrong_orig_mnist']}")
        wrong_ind_mnist_label.grid(padx=5, pady=5, sticky=constants.W)

        wrong_nos_label = ttk.Label(master=self._frame, text=f"Väärin tunnistetut numerot {self._result['wrong_nos']}")
        wrong_nos_label.grid(padx=5, pady=5, sticky=constants.W)

        predY_label = ttk.Label(master=self._frame, text=f"Ennustetut numerot {self._result['Y_predicted']}")
        predY_label.grid(padx=5, pady=5, sticky=constants.W)

        testY_label = ttk.Label(master=self._frame, text=f"Oikeat numerot \t \t {self._result['Y_test']}")
        testY_label.grid(padx=5, pady=5, sticky=constants.W)


    def _initialize(self):
        self._calculate_knn()
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="ResultView")
        label.grid(row=0, column=0)

        self._view_result_fields()

        set_param_button = ttk.Button(
            master=self._frame,
            text="Palaa parametrien asetukseen",
            command=self._handle_set_param
        )

        set_param_button.grid(padx=5, pady=5, sticky=constants.EW)

