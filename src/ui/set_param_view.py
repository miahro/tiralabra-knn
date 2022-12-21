"""moduli sisältää luokan SetParamView"""
from tkinter import ttk, constants, Label, StringVar
from datahandler import datahandler
from config import parameters


class SetParamView:
    """Luokka SetParamView laskentaparametrien asetusta varten
    """

    def __init__(self, root, handle_load, handle_result, show_result_view, datahandler):
        """luokan konstruktori

        Args:
            root: TKinter elementti, johon  näkymä alustetaan
            handle_load: metodikahva latausnäkymälle
            handle_result: metodikahva tulosnäkymälle
            show_result_view (_type_): metodikahva tulosnäkymälle
            datahandler: Datahandler-luokan olio
        """
        self._root = root
        self._handle_load = handle_load
        self._handle_result = handle_result
        self._show_result_view = show_result_view
        self._frame = None

        self._datahandler = datahandler
        if self._datahandler.initialized:
            self._test_index_start = self._datahandler.test_index_start
            self._test_index_end = self._datahandler.test_index_end
            self._train_index_start = self._datahandler.train_index_start
            self._train_index_end = self._datahandler.train_index_end
            self._k_value = self._datahandler.k
            self._layers = self._datahandler.layers
        else:
            self._test_index_start = parameters["test_index_start"]
            self._test_index_end = parameters["test_index_end"]
            self._train_index_start = parameters["train_index_start"]
            self._train_index_end = parameters["train_index_end"]
            self._k_value = parameters["k_value"]
            self._layers = parameters["layers"]

        self._datahandler.set_parameters(self._test_index_start, self._test_index_end,
                                         self._train_index_start, self._train_index_end, self._k_value, self._layers)
        self._datahandler.init_knn()

        self._initialize()

    def pack(self):
        """näyttää näkymän
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """tuhoaa näkymän
        """
        self._frame.destroy()

    def _initialize_input_fields(self):
        """alustaa kentät parametrien syöttöä varten
        """

        test_data_start_label = ttk.Label(
            master=self._frame, text="Testidatan alkuindeksi (0-9999)")
        self._test_data_start_entry = ttk.Entry(master=self._frame)
        test_data_start_label.grid(padx=5, pady=5, sticky=constants.W)
        self._test_data_start_entry.grid(padx=5, pady=5, sticky=constants.EW)

        test_data_end_label = ttk.Label(
            master=self._frame, text="Testidatan loppuindeksi (1-10000)")
        self._test_data_end_entry = ttk.Entry(master=self._frame)
        test_data_end_label.grid(padx=5, pady=5, sticky=constants.W)
        self._test_data_end_entry.grid(padx=5, pady=5, sticky=constants.EW)

        train_data_start_label = ttk.Label(
            master=self._frame, text="Harjoitusdatan alkuindeksi (0-59999)")
        self._train_data_start_entry = ttk.Entry(master=self._frame)
        train_data_start_label.grid(padx=5, pady=5, sticky=constants.W)
        self._train_data_start_entry.grid(padx=5, pady=5, sticky=constants.EW)

        train_data_end_label = ttk.Label(
            master=self._frame, text="Harjoitusdatan loppuindeksi (100-60000)")
        self._train_data_end_entry = ttk.Entry(master=self._frame)
        train_data_end_label.grid(padx=5, pady=5, sticky=constants.W)
        self._train_data_end_entry.grid(padx=5, pady=5, sticky=constants.EW)

        k_value_label = ttk.Label(master=self._frame, text="k-arvo (1-100)")
        self._k_value_entry = ttk.Entry(master=self._frame)
        k_value_label.grid(padx=5, pady=5, sticky=constants.W)
        self._k_value_entry.grid(padx=5, pady=5, sticky=constants.EW)

        layers_label = ttk.Label(
            master=self._frame, text="Kerrosten määärä (1-8)")
        self._layers_entry = ttk.Entry(master=self._frame)
        layers_label.grid(padx=5, pady=5, sticky=constants.W)
        self._layers_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _set_parameters(self):
        """lukee parametrikentät ja asettaa parametrit
        """
        error = True

        self._message.set("")
        self._hide_message()
        test_start_input = self._test_data_start_entry.get()
        if not test_start_input.isnumeric():
            self._show_message("arvon oltava kokonaisluku")
            self._clear_entry_fields()
        elif int(test_start_input) < 0 or int(test_start_input) > 9999:
            self._show_message("arvo oltava väliltä 0-9999")
            self._clear_entry_fields()
        else:
            self._test_index_start = int(test_start_input)

        test_end_input = self._test_data_end_entry.get()
        if not test_end_input.isnumeric():
            self._show_message("arvon oltava kokonaisluku")
            self._clear_entry_fields()
        elif int(test_end_input) < 0 or int(test_end_input) > 59999:
            self._show_message("arvo oltava väliltä 0-59999")
            self._clear_entry_fields()
        elif int(test_end_input) < int(test_start_input):
            self._show_message(
                "loppuindeksin oltava suurempi kuin alkuindeksin")
            self._clear_entry_fields()
        else:
            self._test_index_end = int(test_end_input)

        train_start_input = self._train_data_start_entry.get()

        if not train_start_input.isnumeric():
            self._show_message("arvon oltava kokonaisluku")
            self._clear_entry_fields()
        elif int(train_start_input) < 0 or int(train_start_input) > 9999:
            self._show_message("arvo oltava väliltä 0-59999")
            self._clear_entry_fields()
        else:
            self._train_index_start = int(train_start_input)

        train_end_input = self._train_data_end_entry.get()
        if not train_end_input.isnumeric():
            self._show_message("arvon oltava kokonaisluku")
            self._clear_entry_fields()
        elif int(train_end_input) < 100 or int(train_end_input) > 59999:
            self._show_message("arvo oltava väliltä 100-59999")
            self._clear_entry_fields()
        elif int(train_end_input) < int(train_start_input):
            self._show_message(
                "loppuindeksin oltava suurempi kuin alkuindeksin")
            self._clear_entry_fields()
        else:
            self._train_index_end = int(train_end_input)

        k = self._k_value_entry.get()
        if not k.isnumeric():
            self._show_message("arvon oltava kokonaisluku")
            self._clear_entry_fields()
        elif int(k) < 0 or int(k) > 100:
            self._show_message("arvo oltava väliltä 1-100")
            self._clear_entry_fields()
        else:
            self._k_value = int(k)

        layers = self._layers_entry.get()
        if not layers.isnumeric():
            self._show_message("arvon oltava kokonaisluku")
            self._clear_entry_fields()
        elif int(layers) < 1 or int(layers) > 8:
            self._show_message("arvo oltava väliltä 1-8")
            self._clear_entry_fields()
        else:
            self._layers = int(layers)
            self._hide_message()
            error = False

        if not error:
            self._datahandler.set_parameters(self._test_index_start, self._test_index_end,
                                             self._train_index_start, self._train_index_end, self._k_value, self._layers)
            self._datahandler.init_knn()

            self.destroy()
            self._initialize()
            self.pack()

        if error:
            self._hide_message()
            self.pack()

    def _current_values(self):
        """näyttää nykyiset parametrien arvot
        """
        txt0 = ttk.Label(master=self._frame,
                         text=f"Nykyiset arvot")
        txt0.grid(row=2, column=200, padx=5, pady=5, sticky=constants.EW)
        txt1 = ttk.Label(master=self._frame,
                         text=f"Testidatan alkuindeksi {self._test_index_start}")
        txt1.grid(row=2, column=200, padx=5, pady=5, sticky=constants.EW)
        txt2 = ttk.Label(master=self._frame,
                         text=f"Testidatan loppu {self._test_index_end}")
        txt2.grid(row=4, column=200, padx=5, pady=5, sticky=constants.EW)
        txt3 = ttk.Label(master=self._frame,
                         text=f"Harjoitusdatan alkuindeksi {self._train_index_start}")
        txt3.grid(row=6, column=200, padx=5, pady=5, sticky=constants.EW)
        txt4 = ttk.Label(master=self._frame,
                         text=f"Harjoitusdatan loppuindeksi {self._train_index_end}")
        txt4.grid(row=8, column=200, padx=5, pady=5, sticky=constants.EW)
        txt5 = ttk.Label(master=self._frame,
                         text=f"k-arvo {self._k_value}")
        txt5.grid(row=10, column=200, padx=5, pady=5, sticky=constants.EW)
        txt5 = ttk.Label(master=self._frame,
                         text=f"Kerrokset {self._layers}")
        txt5.grid(row=12, column=200, padx=5, pady=5, sticky=constants.EW)
        txt6 = ttk.Label(master=self._frame,
                         text=f"MNIST data luettu suodattimen arvolla {self._datahandler.filter_value}")
        txt6.grid(row=14, column=200, padx=5, pady=5, sticky=constants.EW)


# TÄTÄ EI VISSIIN TARVITA OLLENKAAN?

    def _calculate_knn(self):
        """asettaa datahandler-olion KNN-laskentaparametrit 
        ja kutsuu datahandler predict metodio
        siirty tulosnäkymään
        """
        self._datahandler.set_parameters(self._test_index_start, self._test_index_end,
                                         self._train_index_start, self._train_index_end, self._k_value, self._layers)
        self._datahandler.init_knn()
        self._datahandler.predict()
        self._show_result_view()

    def _show_message(self, message):
        """näyttää virheviestin (virheellisistä paremetreista)

        Args:
            message (string): virheviesti
        """
        self._message.set(message)
        self._message_label.grid()

    def _hide_message(self):
        """piilottaa viestin
        """
        self._message_label.grid_remove()

    def _clear_entry_fields(self):
        """tyhjentää parametrien asetuskentät
        """
        self._test_data_start_entry.delete(0, 'end')
        self._test_data_end_entry.delete(0, 'end')
        self._train_data_start_entry.delete(0, 'end')
        self._train_data_end_entry.delete(0, 'end')
        self._k_value_entry.delete(0, 'end')
        self._layers_entry.delete(0, 'end')

    def _initialize(self):
        """alustaa näkymän
        """
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Parametrien asetus")
        label.grid(row=0, column=0)

        self._message = StringVar(self._frame)

        self._message_label = ttk.Label(
            master=self._frame,
            textvariable=self._message,
            foreground='red'
        )
        self._message_label.grid(padx=5, pady=5)

        self._initialize_input_fields()

        set_parameters_button = ttk.Button(
            master=self._frame,
            text="Aseta parametrit",
            command=self._set_parameters)
        set_parameters_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._current_values()

        new_user_button = ttk.Button(
            master=self._frame,
            text="Suorita laskenta annetuilla parametreilla",
            command=self._handle_result)
        new_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        set_param_button = ttk.Button(
            master=self._frame,
            text="Palaa latausnäkymään",
            command=self._handle_load
        )

        set_param_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_message()
