from tkinter import Tk
from ui.set_param_view import SetParamView
from ui.param_view import ParamView
from ui.result_view import ResultView
from ui.load_view import LoadView
from datahandler import DataHandler

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._mnist = None
        self._datahandler = DataHandler()
        #print(self._datahandler)


    def start(self):
        self._show_load_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_load(self):
        self._show_load_view()

    def _handle_set_param(self):
        self._show_set_param_view()

    def _handle_param(self):
        self._show_param_view()

    def _handle_result(self):
        self._show_result_view()

    def _show_set_param_view(self):
        self._hide_current_view()
        self._current_view = SetParamView(
        self._root,
        self._handle_load,
        self._handle_result,
        self._show_result_view,
        self._datahandler
        #self._show_set_param_view
        )
        self._current_view.pack()

    def _show_param_view(self):
        self._hide_current_view()
        self._current_view = ParamView(
        self._root,
        self._handle_set_param,
        self._handle_result
        )
        self._current_view.pack()

    def _show_result_view(self):
        self._hide_current_view()
        self._current_view = ResultView(
        self._root,
        self._handle_set_param,
        self._datahandler
        )
        self._current_view.pack()

    def _show_load_view(self):
        self._hide_current_view()
        self._current_view = LoadView(
        self._root,
        self._handle_set_param,
        self._show_set_param_view,
        self._show_result_view,
        self._datahandler
        )
        self._current_view.pack()
