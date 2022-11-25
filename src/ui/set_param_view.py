from tkinter import ttk, constants, Label, StringVar

class SetParamView:
    def __init__(self, root, handle_load, handle_param):
        self._root = root
        self._handle_load = handle_load
        self._handle_param = handle_param
        self._frame = None

        self._test_index_start = 1
        self._test_index_end = 1
        self._train_index_start = 0
        self._train_index_end = 100
        self._k_value = 3
        self._layers = 4 

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize_input_fields(self):


        test_data_start_label = ttk.Label(master=self._frame, text="Testidatan alkuindeksi (0-9999)")
        self._test_data_start_entry = ttk.Entry(master=self._frame)
        test_data_start_label.grid(padx=5, pady=5, sticky=constants.W)
        self._test_data_start_entry.grid(padx=5, pady=5, sticky=constants.EW)

        test_data_end_label = ttk.Label(master=self._frame, text="Testidatan loppuindeksi (0-9999)")
        self._test_data_end_entry = ttk.Entry(master=self._frame)
        test_data_end_label.grid(padx=5, pady=5, sticky=constants.W)
        self._test_data_end_entry.grid(padx=5, pady=5, sticky=constants.EW)

        train_data_start_label = ttk.Label(master=self._frame, text="Harjoitusdatan alkuindeksi (0-59999)")
        self._train_data_start_entry = ttk.Entry(master=self._frame)
        train_data_start_label.grid(padx=5, pady=5, sticky=constants.W)
        self._train_data_start_entry.grid(padx=5, pady=5, sticky=constants.EW)

        train_data_end_label = ttk.Label(master=self._frame, text="Harjoitusdatan loppuindeksi (0-59999)")
        self._train_data_end_entry = ttk.Entry(master=self._frame)
        train_data_end_label.grid(padx=5, pady=5, sticky=constants.W)
        self._train_data_end_entry.grid(padx=5, pady=5, sticky=constants.EW)    

        k_value_label = ttk.Label(master=self._frame, text="k-arvo (1-100)")
        self._k_value_entry = ttk.Entry(master=self._frame)
        k_value_label.grid(padx=5, pady=5, sticky=constants.W)
        self._k_value_entry.grid(padx=5, pady=5, sticky=constants.EW)    

        layers_label = ttk.Label(master=self._frame, text="Kerrosten määärä (1-8)")
        self._layers_entry = ttk.Entry(master=self._frame)
        layers_label.grid(padx=5, pady=5, sticky=constants.W)
        self._layers_entry.grid(padx=5, pady=5, sticky=constants.EW)    




    def _set_parameters(self):
        error = True

        self._message.set("")
        self._hide_message()
        print("parameters")
        test_start_input = self._test_data_start_entry.get()
        print("tähän?")
        print(test_start_input)
        if not test_start_input.isnumeric():
            self._show_message("arvon oltava kokonaisluku")
            self._clear_entry_fields()
        elif int(test_start_input)<0 or int(test_start_input)>9999:
            self._show_message("arvo oltava väliltä 0-9999")
            self._clear_entry_fields()
        else:
            self._test_index_start = int(test_start_input)

        test_end_input = self._test_data_end_entry.get()
        print("test end")
        print(test_end_input)
        if not test_end_input.isnumeric():
            self._show_message("arvon oltava kokonaisluku")
            self._clear_entry_fields()            
        elif int(test_end_input)<0 or int(test_end_input)>59999:
            self._show_message("arvo oltava väliltä 0-59999")
            self._clear_entry_fields()
        elif int(test_end_input) < int(test_start_input):
            self._show_message("loppuindeksin oltava suurempi kuin alkuindeksin")
            self._clear_entry_fields()
        else:
            self._test_index_end = int(test_end_input)


        train_start_input = self._train_data_start_entry.get()
        print("train start")
        print(train_start_input)
        if not train_start_input.isnumeric():
            self._show_message("arvon oltava kokonaisluku")
            self._clear_entry_fields()            
        elif int(train_start_input)<0 or int(train_start_input)>9999:
            self._show_message("arvo oltava väliltä 0-59999")
            self._clear_entry_fields()
        else:
            self._train_index_start = int(train_start_input)

        train_end_input = self._train_data_end_entry.get()
        print("train end")
        print(train_end_input)
        if not train_end_input.isnumeric():
            print("fail a")
            self._show_message("arvon oltava kokonaisluku")
            self._clear_entry_fields()            
        elif int(train_end_input)<0 or int(train_end_input)>59999:
            print("fail b")
            self._show_message("arvo oltava väliltä 0-59999")
            self._clear_entry_fields()
        elif int(train_end_input) < int(train_start_input):
            self._show_message("loppuindeksin oltava suurempi kuin alkuindeksin")
            print("fail c")
            self._clear_entry_fields()
        else:
            self._train_index_end = int(train_end_input)
            print("ok")


        k = self._k_value_entry.get()
        print("k")
        print(k)
        if not k.isnumeric():
            self._show_message("arvon oltava kokonaisluku")
            self._clear_entry_fields()               
        elif int(k) < 0 or int(k) > 100:
            self._show_message("arvo oltava väliltä 1-100")
            self._clear_entry_fields()            
        else:
            self._k_value = int(k)
        
        layers = self._layers_entry.get()
        print("layers")
        print(layers)
        if not layers.isnumeric():
            self._show_message("arvon oltava kokonaisluku")
            self._clear_entry_fields()  
        elif int(layers)<1 or int(layers)>8:
            self._show_message("arvo oltava väliltä 1-8")
            self._clear_entry_fields()                                    
        else:
            self._layers = int(layers)
            self._hide_message()
            error = False

        if not error:
            self.destroy()
            self._initialize()
            self.pack()

        if error:
            self._hide_message()
            self.pack()

    def _current_values(self):
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
                         text=f"Harjoitusdatan alkuindeksi {self._train_index_end}")
        txt4.grid(row=8, column=200, padx=5, pady=5, sticky=constants.EW)
        txt5 = ttk.Label(master=self._frame,
                         text=f"k-arvo {self._k_value}")
        txt5.grid(row=10, column=200, padx=5, pady=5, sticky=constants.EW)
        txt5 = ttk.Label(master=self._frame,
                         text=f"Kerrokset {self._layers}")
        txt5.grid(row=12, column=200, padx=5, pady=5, sticky=constants.EW)





    def _show_message(self, message):
        self._message.set(message)
        self._message_label.grid()

    def _hide_message(self):
        self._message_label.grid_remove()


    def _clear_entry_fields(self):
        self._test_data_start_entry.delete(0, 'end')
        self._test_data_end_entry.delete(0, 'end')
        self._train_data_start_entry.delete(0, 'end')
        self._train_data_end_entry.delete(0, 'end')
        self._k_value_entry.delete(0, 'end')
        self._layers_entry.delete(0, 'end')

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        print("SetParamView._initialize")
        #print(self._handle_param)

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
            command=self._handle_param)
        new_user_button.grid(padx=5, pady=5, sticky=constants.EW)


  


        set_param_button = ttk.Button(
            master=self._frame,
            text="Palaa latausnäkymään",
            command=self._handle_load
        )

        set_param_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_message()


 