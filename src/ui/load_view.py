"""moduli sisältää luokna LoadView"""
from tkinter import ttk, constants, StringVar

class LoadView:
    """luokka latausnäkymää varten

    Attributes:
        root: TKinter-elementti, johon näkymä alustetaan
        handle_show_set_param: metodiviite parametrien asetusnäkymälle
        datahandler: datahandler-luokan olio
    """

    def __init__(self, root,show_set_param_view, datahandler):
        """luokan konstruktori

        Args:
            root: TKinter-elementti, johon näkymä alustetaan
            handle_show_set_param: metodiviite parametrien asetusnäkymälle
            datahandler: datahandler-luokan olio
        """
        self._root = root
        self._show_set_param_view = show_set_param_view
        self._frame = None
        self._message = None
        self._message_label = None
        self._filter_value = 128
        self._datahandler = datahandler
        self._initialize()

    def pack(self):
        "näyttää näkymän"
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """tuhoaa näkymän
        """
        self._frame.destroy()

    def _show_message(self, message):
        """näyttää virheviestin virheellisestä suodattimen arvosta

        Args:
            message (string): virheviesti
        """
        self._message.set(message)
        self._message_label.grid()

    def _initialize_input_fields(self):
        """alustaa suodattimen asetuskentän
        """

        filter_label = ttk.Label(
            master=self._frame, text="Suodattimen arvo (0-255")
        self._filter_entry = ttk.Entry(master=self._frame)
        filter_label.grid(padx=5, pady=5, sticky=constants.W)
        self._filter_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _set_filter(self):
        """asettaa harmaasuodattimen arvon datahandler-oliolle
        """
        filter_value_input = self._filter_entry.get()
        if not filter_value_input.isnumeric():
            self._show_message("arvon oltava kokonaisluku")
            self._clear_entry_fields()
        elif int(filter_value_input) < 0 or int(filter_value_input) > 255:
            self._show_message("arvo oltava väliltä 0-255")
            self._clear_entry_fields()
        else:
            self._filter_value = int(filter_value_input)
            self.destroy()
            self._initialize()
            self.pack()

    def _load(self):
        """kutsuu datahandelrin set_filter ja read_mnist metodeja
        siirtyy parametrien asetusnäkymään
        """
        self._datahandler.set_filter(self._filter_value)
        self._datahandler.read_mnist()
        self._show_set_param_view()

    def _clear_entry_fields(self):
        """tyhjentää kentät
        """
        self._filter_entry.delete(0, 'end')

    def _initialize(self):
        """alustaa näkymän
        """
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="MNIST datan lataus")
        label.grid(row=0, column=0)

        text = ttk.Label(master=self._frame,
                         text=f"Harmaasuodattimen arvo: {self._filter_value}")
        text.grid(padx=5, pady=5, sticky=constants.EW)

        self._message = StringVar(self._frame)

        self._message_label = ttk.Label(
            master=self._frame,
            textvariable=self._message,
            foreground='red'
        )
        self._message_label.grid(padx=5, pady=5)

        self._initialize_input_fields()

        set_filter_button = ttk.Button(
            master=self._frame,
            text="Aseta suodatin",
            command=self._set_filter)
        set_filter_button.grid(padx=5, pady=5, sticky=constants.EW)

        new_user_button = ttk.Button(
            master=self._frame,
            text="Lataa MNIST data",
            command=self._load)
        new_user_button.grid(padx=5, pady=5, sticky=constants.EW)
