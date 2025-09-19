from Generer_un_csv import GenererUnCsv

if __name__ == "__main__":
    nb_lignes=int(input("Combien de lignes de lignes ? "))
    vit_rotation=50
    csv_gen = GenererUnCsv()
    resultat = csv_gen.generer_csv(vitesse_de_rotation=vit_rotation,nombres_de_lignes=nb_lignes)
    print(f"resultat = {resultat}")

