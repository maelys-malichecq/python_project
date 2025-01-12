##First Committ
# Exemple d'utilisation de numpy
##array = np.array([1, 2, 3, 4, 5])
##print(array)
# Afficher les attributs disponibles du module
##Fprint(dir(pbc))

import numpy as np
import pybacktestchain as pbc
import logging
from datetime import datetime, timedelta
import pandas as pd
import logging
from dataclasses import dataclass
from datetime import datetime
import os 
import pickle
from pybacktestchain.broker import Backtest  
from pybacktestchain.utils import generate_random_name
from pybacktestchain.data_module import UNIVERSE_SEC, get_stocks_data, DataModule, Information

# Configuration de base du logging pour afficher les logs dans la console
logging.basicConfig(level=logging.INFO)



# Définir les dates de début et de fin du backtest
initial_date = datetime(2020, 1, 1)
final_date = datetime(2021, 1, 1)

# Créer une instance de la classe Backtest
backtest = Backtest(
    initial_date=initial_date,
    final_date=final_date,
    verbose=True  # Vous pouvez définir verbose à True pour activer les logs détaillés
)

# Lancer le backtest
backtest.run_backtest()



