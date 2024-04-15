import argparse
import json
import os

def generate_empty_json_files(n):
    """Génère n fichiers JSON vides dans le répertoire courant."""
    for i in range(n):
        file_name = f"{i+1}.json"
        with open(file_name, 'w') as json_file:
            json.dump({}, json_file)
        print(f"Le fichier {file_name} a été créé.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Génère des fichiers JSON vides.")
    parser.add_argument('n', type=int, help="Le nombre de fichiers JSON à générer.")
    
    args = parser.parse_args()
    
    # Vérifie si la valeur de n est positive
    if args.n > 0:
        generate_empty_json_files(args.n)
    else:
        print("Veuillez entrer un nombre positif.")
