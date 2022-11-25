from tkinter import ttk, constants, Label

class ParamView:
    def __init__(self, root, handle_set_param, handle_result):
        self._root = root
        self._handle_set_param = handle_set_param
        self._handle_result = handle_result
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        print("ParamView._initialize")

        label = ttk.Label(master=self._frame, text="ParamView")
        label.grid(row=0, column=0)


        new_user_button = ttk.Button(
            master=self._frame,
            text="Eteenpäin tulosnäkymään",
            command=self._handle_result)
        new_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        set_param_button = ttk.Button(
            master=self._frame,
            text="Palaa parametrien asetusnäkymään",
            command=self._handle_set_param
        )

        set_param_button.grid(padx=5, pady=5, sticky=constants.EW)
