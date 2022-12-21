"""moduli sisältää luokan ResultView"""

from tkinter import ttk, constants, Label
from matplotlib import pyplot as plt


class ResultView:
    """Luokka tulosnäkymää varten

    Attributes:
        root: TKinter elementti, johon näkymä alustetaan
        handle_set_param: metodikahva parametrien asetusnäkymään
        datahandler: Datahandler-luokan olio

    """

    def __init__(self, root, handle_set_param, datahandler):
        """luokan konstruktori

        Args:
            root: TKinter elementti, johon näkymä alustetaan
            handle_set_param: metodikahva parametrien asetusnäkymään
            datahandler: Datahandler-luokan olio
        """
        self._root = root
        self._handle_set_param = handle_set_param
        self._datahandler = datahandler
        self._frame = None
        self._initialize()

    def pack(self):
        """näyttää näkymän"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """tuhoaa näkymän"""
        self._frame.destroy()

    def _calculate_knn(self):
        """kutsuu datahandler-olion predict funktiota ja evaluate funktiota"""
        self._datahandler.predict()
        self._result = self._datahandler.evaluate()

    def _plot(self):
        """näyttää valitun numeron erillisessä ikkunassa
        """
        ind = self._ind_choice_entry.get()
        if ind.isdigit():
            ind = int(ind)
            if ind < len(self._datahandler.X_test_matrix):
                plt.imshow(self._datahandler.X_test_matrix[ind])
                plt.get_current_fig_manager().set_window_title(
                    f"Numero: {self._datahandler.Y_test[ind]}")
                plt.show()

    def _save(self):
        """tallentaa tulokset tiedostoon
        """
        self._datahandler.write_results_to_file()

    def _view_result_fields(self):
        """näyttää tulokset"""

        correct_label = ttk.Label(
            master=self._frame, text=f"Oikein tunnistettuja:")
        correct_label.grid(padx=5, pady=5, row=1, column=0, sticky=constants.W)

        correct_val_label = ttk.Label(
            master=self._frame, text=f"{self._result['correct']}")
        correct_val_label.grid(padx=5, pady=5, row=1,
                               column=1, sticky=constants.W)

        wrong_label = ttk.Label(
            master=self._frame, text=f"Väärin tunnistettuja: ")
        wrong_label.grid(padx=5, pady=5, row=3, column=0, sticky=constants.W)

        wrong_val_label = ttk.Label(
            master=self._frame, text=f"{self._result['wrong']}")
        wrong_val_label.grid(padx=5, pady=5, row=3,
                             column=1, sticky=constants.W)

        time_label = ttk.Label(
            master=self._frame, text=f"Suoritusaika sekuntia: ")
        time_label.grid(padx=5, pady=5, row=5, column=0, sticky=constants.W)

        time_val_label = ttk.Label(
            master=self._frame, text=f"{self._result['runtime']}")
        time_val_label.grid(padx=5, pady=5, row=5,
                            column=1, sticky=constants.W)

        wrong_ind_label = ttk.Label(
            master=self._frame, text=f"Väärien indeksit: ")
        wrong_ind_label.grid(padx=5, pady=5, row=7,
                             column=0, sticky=constants.W)

        wrong_val_ind_label = ttk.Label(
            master=self._frame, text=f"{self._result['wrong_ind']}")
        wrong_val_ind_label.grid(
            padx=5, pady=5, row=7, column=1, sticky=constants.W)

        wrong_ind_mnist_label = ttk.Label(
            master=self._frame, text=f"Väärien indeksit alkuperäisessä MNIST datassa: ")
        wrong_ind_mnist_label.grid(
            padx=5, pady=5, row=9, column=0, sticky=constants.W)

        wrong_val_ind_mnist_label = ttk.Label(
            master=self._frame, text=f"{self._result['wrong_orig_mnist']}")
        wrong_val_ind_mnist_label.grid(
            padx=5, pady=5, row=9, column=1, sticky=constants.W)

        wrong_nos_label = ttk.Label(
            master=self._frame, text=f"Väärin tunnistetut numerot: ")
        wrong_nos_label.grid(padx=5, pady=5, row=11,
                             column=0, sticky=constants.W)

        wrong_val_nos_label = ttk.Label(
            master=self._frame, text=f"{self._result['wrong_nos']}")
        wrong_val_nos_label.grid(
            padx=5, pady=5, row=11, column=1, sticky=constants.W)

        predY_label = ttk.Label(
            master=self._frame, text=f"Ennustetut numerot (50 ensimmäistä): ")
        predY_label.grid(padx=5, pady=5, row=13, column=0, sticky=constants.W)

        predY_val_label = ttk.Label(
            master=self._frame, text=f"{self._result['Y_predicted'][0:50]}")
        predY_val_label.grid(padx=5, pady=5, row=13,
                             column=1, sticky=constants.W)

        testY_label = ttk.Label(
            master=self._frame, text=f"Oikeat numerot (50 ensimmäistä): ")
        testY_label.grid(padx=5, pady=5, row=15, column=0, sticky=constants.W)

        testY_val_label = ttk.Label(
            master=self._frame, text=f"{self._result['Y_test'][0:50]}")
        testY_val_label.grid(padx=5, pady=5, row=15,
                             column=1, sticky=constants.W)

        filter_label = ttk.Label(
            master=self._frame, text=f"Harmaasuodattimen arvo: ")
        filter_label.grid(padx=5, pady=5, row=17, column=0, sticky=constants.W)

        filter_val_label = ttk.Label(
            master=self._frame, text=f"{self._result['filter']}")
        filter_val_label.grid(padx=5, pady=5, row=17,
                              column=1, sticky=constants.W)

        k_label = ttk.Label(
            master=self._frame, text=f"k-arvo: ")
        k_label.grid(padx=5, pady=5, row=19, column=0, sticky=constants.W)

        k_val_label = ttk.Label(
            master=self._frame, text=f"{self._result['k-value']}")
        k_val_label.grid(padx=5, pady=5, row=19, column=1, sticky=constants.W)

        layers_label = ttk.Label(
            master=self._frame, text=f"kerrokset: ")
        layers_label.grid(padx=5, pady=5, row=21, column=0, sticky=constants.W)

        layers_val_label = ttk.Label(
            master=self._frame, text=f"{self._result['layers']}")
        layers_val_label.grid(padx=5, pady=5, row=21,
                              column=1, sticky=constants.W)

    def _initialize(self):
        """alustaa näkymän"""
        self._calculate_knn()
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Tulokset")
        label.grid(row=0, column=0)

        self._view_result_fields()

        ind_choice_label = ttk.Label(
            master=self._frame, text="Anna näytettävän kuvan indeksi (testikuva): ")
        self._ind_choice_entry = ttk.Entry(master=self._frame)
        ind_choice_label.grid(padx=5, pady=5, column=0, sticky=constants.W)
        self._ind_choice_entry.grid(
            padx=5, pady=5, column=1, sticky=constants.EW)

        matplot_button = ttk.Button(
            master=self._frame,
            text="Näytä kuva",
            command=self._plot
        )

        matplot_button.grid(padx=5, pady=5, sticky=constants.EW)

        save_button = ttk.Button(
            master=self._frame,
            text="Tallenna tulokset",
            command=self._save
        )

        save_button.grid(padx=5, pady=5, sticky=constants.EW)

        set_param_button = ttk.Button(
            master=self._frame,
            text="Palaa parametrien asetukseen",
            command=self._handle_set_param
        )

        set_param_button.grid(padx=5, pady=5, sticky=constants.EW)
