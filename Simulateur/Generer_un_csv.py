import threading
import time
import csv
import random
from datetime import datetime

class GenererUnCsv:
    def __init__(self, fichier="donnees.csv"):
        self.titre = ["timestamp", "system_id", "system_name", "id_censor", "value"]
        self.donnees = []
        self.fichier = fichier

    def generer_le_titre(self):
        """Retourne le titre du CSV"""
        return self.titre

    def crawl(self, line_number, delay=0.1):
        """Simule la génération d'une ligne de données"""
        time.sleep(delay)  # petit délai pour simuler un traitement
        result = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # timestamp
            f"SYS-{random.randint(1, 10)}",               # system_id
            f"System_{random.randint(1, 5)}",             # system_name
            f"CENSOR-{random.randint(1, 3)}",             # id_censor
            random.randint(1, 10)                         # value
        ]
        self.donnees.append(result)

    def generer_donnees(self, nb_lignes):
        """Lance des threads pour générer nb_lignes de données"""
        threads = []
        for i in range(nb_lignes):
            t = threading.Thread(target=self.crawl, args=(i,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return self.donnees

    def generer_csv(self, nb_lignes):
        """Génère le CSV complet et l'écrit dans un fichier"""
        titre = self.generer_le_titre()
        donnees = self.generer_donnees(nb_lignes)

        with open(self.fichier, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(titre)
            writer.writerows(donnees)

        return self.fichier
