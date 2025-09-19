from Generer_un_csv import GenererUnCsv

if __name__ == "__main__":
    nb_lignes=int(input("Combien de lignes de lignes ? "))

    csv_gen = GenererUnCsv()
    resultat = csv_gen.generer_csv(nb_lignes)
    print(f"resultat = {resultat}")

