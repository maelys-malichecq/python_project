from python_project import python_project
# Exemple pour vérifier compute_information
information_set = info.compute_information(t)
logging.info(f"Information set at {t}: {information_set}")  # Vérifiez si les informations sont valides

portfolio = info.compute_portfolio(t, information_set)
