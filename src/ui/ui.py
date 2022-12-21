"""moduli käyttöliittymän pääluokkaa UI varten"""

from tkinter import Tk
from ui.set_param_view import SetParamView
from ui.result_view import ResultView
from ui.load_view import LoadView
from datahandler import DataHandler


class UI:
    """Käyttöliittymäluokka

    Attributes:
        root:  TKinter elementti, johon käyttöliittymä alustetaan
        current_view: nykyinen näkymä
        mnist: Mnist-luokan olio
        datahandler: Datahandler-luokan olio
    """    
    def __init__(self, root):
        """luokan konstruktori

        Args:
            root: TKinter elementti, johon käyttöliittymä alustetaan
        """        
        self._root = root
        self._current_view = None
        self._mnist = None
        self._datahandler = DataHandler()

    def start(self):
        """määrittää alkunäkymän
        """        
        self._show_load_view()

    def _hide_current_view(self):
        """piilottaa näkymän
        """        
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_load(self):
        """metodikahva latausnäkymälle
        """        
        self._show_load_view()

    def _handle_set_param(self):
        """metodikahva parametrien asetusnäkymälle
        """        
        self._show_set_param_view()

    def _handle_result(self):
        """metodikahva tulosnäkymälle
        """        
        self._show_result_view()

    def _show_set_param_view(self):
        """määrittää parametrien asetusnäkymän alustuksen
        """        
        self._hide_current_view()
        self._current_view = SetParamView(
            self._root,
            self._handle_load,
            self._handle_result,
            self._show_result_view,
            self._datahandler
        )
        self._current_view.pack()

    def _show_result_view(self):
        """määrittää tulosnäkymän alustuksen
        """        
        self._hide_current_view()
        self._current_view = ResultView(
            self._root,
            self._handle_set_param,
            self._datahandler
        )
        self._current_view.pack()

    def _show_load_view(self):
        """määrittää latausnäkymän alustuksen
        """        
        self._hide_current_view()
        self._current_view = LoadView(
            self._root,
            self._handle_set_param,
            self._show_set_param_view,
            self._show_result_view,
            self._datahandler
        )
        self._current_view.pack()
