from tkinter import ttk, constants, StringVar, IntVar
from datahandler import DataHandler
from mnistdata import Mnistdata

class LoadView:
    def __init__(self, root, handle_set_param, show_set_param_view, show_result_view, datahandler):
        self._root = root
        self._handle_set_param = handle_set_param
        self._show_set_param_view = show_set_param_view
        self._show_result_view = show_result_view
        self._frame = None
        self._message = None
        self._message_label = None
        self._filter_value = 128
        self._datahandler = datahandler
    #   print(self._datahandler)
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_message(self, message):
        self._message.set(message)
        self._message_label.grid()

    def _initialize_input_fields(self):


        filter_label = ttk.Label(master=self._frame, text="Suodattimen arvo (0-255")
        self._filter_entry = ttk.Entry(master=self._frame)
        filter_label.grid(padx=5, pady=5, sticky=constants.W)
        self._filter_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _set_filter(self):
       # print("set filter function")
        filter_value_input = self._filter_entry.get()
        if not filter_value_input.isnumeric():
            self._show_message("arvon oltava kokonaisluku")
            self._clear_entry_fields()            
        elif int(filter_value_input)<0 or int(filter_value_input)>255:
            self._show_message("arvo oltava väliltä 0-255")
            self._clear_entry_fields()
        else:
            self._filter_value = int(filter_value_input)
            self.destroy()
            self._initialize()
            self.pack()


    def _load(self):
     #   print("load function functionality here")
     #   print(self._datahandler.filter_value)
        self._datahandler.set_filter(self._filter_value)
     #   print(self._datahandler.filter_value)
        self._datahandler.read_mnist()
        #print(mnist.Y_train[0])
        #lataustoiminnallisuus lisättävä tähän
        self._show_set_param_view()



    def _clear_entry_fields(self):
        self._filter_entry.delete(0, 'end')


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        #print("SetParamView._initialize")
        #print(self._handle_set_param)

        label = ttk.Label(master=self._frame, text="MNIST datan lataus")
        label.grid(row=0, column=0)


        text = ttk.Label(master=self._frame, text=f"Harmaasuodattimen arvo: {self._filter_value}")
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

        # text = Label(self, text="Just do it")
        # text.place(x=70,y=90)

        # set_param_button = ttk.Button(
        #     master=self._frame,
        #     text="Kirjaudu sisään",
        #     command=self._handle_param
        # )

        # set_param_button.grid(padx=5, pady=5, sticky=constants.EW)
        # #login_button.grid(row=4, column=0)

