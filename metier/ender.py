import os
import shutil


def generate(results):
    """
    methode pour generer une arbo de dossier pour sortir les noms cachés
    :param results:
    :return:
    """
    if not results:
        print("aucun resultat à afficher")
        return
    print("****  Génération des fichiers  ****")
    first_dir = "Resultats"

    if os.path.exists(first_dir):
        shutil.rmtree(first_dir)
        print("retrait de l'ancien dossier")

    os.mkdir(first_dir)
    print("genere...")
    for couple in results:
        sous_dir = first_dir + "/" + couple
        os.mkdir(sous_dir)
        path_fichier = sous_dir + "/" + couple + ".txt"
        with open(path_fichier, "a") as fichier:
            fichier.write(f"Votre personne associée est: {results[couple]}")

    print("Fin")
    print(f"Dans le dossier {first_dir}, chaque participant trouvera un dossier à son nom avec un fichier "
          "ou est inscrit la personne qui lui est associé")
