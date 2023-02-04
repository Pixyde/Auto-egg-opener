from pyautogui import *
import pyautogui
import time
def nb_rendus(montant, pieces):
 if montant < 0 or len(pieces) == 0:
    return 0
 if montant > 0:
    return nb_rendus(montant, pieces[:-1]) + nb_rendus(montantpieces[-1], pieces)
 return 1

nb_rendus(81, [1, 5, 10, 25, 50])  
        