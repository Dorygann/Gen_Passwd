
# ============================================================================
# Autor   : Dorygann
# Version  : 1.3 (29/11/2025)
# ============================================================================
# Licence  : MIT
# ============================================================================
# Options disponibles :
#   -l, --length N         : Longueur du mot de passe (défaut: 12)
#   -c, --count N          : Nombre de mots de passe à générer (défaut: 1)
#   -o, --output           : Sauvegarder dans output.txt
#   -S, --no-special       : Désactiver les caractères spéciaux
#   -U, --no-uppercase     : Désactiver les majuscules
#   -L, --no-lowercase     : Désactiver les minuscules
#   -D, --no-digits        : Désactiver les chiffres
#   -A, --ambigus          : Désactiver les caractères ambigus
# ============================================================================

import string
import random
import argparse
import subprocess

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", '--length',
                        type=int,
                        default=12,
                        help='Longueur du mot de passe (défaut: 12)')
 
    parser.add_argument("-S", '--no-special',
                        action='store_true',
                        help='Désactiver les caractères spéciaux')

    parser.add_argument("-A", '--no-ambigus',
                        action='store_true',
                        help='Désactiver les caractères ambigus')

    parser.add_argument("-U", '--no-uppercase',
                        action='store_true',
                        help='Désactiver les majuscules')
 
    parser.add_argument("-L", '--no-lowercase',
                        action='store_true',
                        help='Désactiver les minuscules')   
 
    parser.add_argument("-D", '--no-digits',
                        action='store_true',
                        help='Désactiver les nombres')

    parser.add_argument("-c", '--count',
                        type=int,
                        default=1,
                        help='Définir x nombre de mot de passe (défaut: 1)')
                            
    parser.add_argument("-o", '--output',
                        action='store_true',
                        help='Sauvegarde du / des mot de passe dans un fichier .txt')

    return parser.parse_args()

args = parse_args()
nbr_digit = args.length
no_special = args.no_special
no_uppercase = args.no_uppercase
no_lowercase = args.no_lowercase
no_digits = args.no_digits
no_ambigus = args.no_ambigus
count = args.count
output = args.output


def main():

    caracters = ""
    ambigus_caracters = "oO01lIi"

    if no_ambigus:
        string.ascii_lowercase = ''.join(c for c in string.ascii_lowercase if c not in ambigus_caracters)
        string.ascii_uppercase = ''.join(c for c in string.ascii_uppercase if c not in ambigus_caracters)
        string.digits = ''.join(c for c in string.digits if c not in ambigus_caracters)

    if not no_lowercase:
        caracters += string.ascii_lowercase
            
    if not no_uppercase:
        caracters += string.ascii_uppercase

    if not no_digits:
        caracters += string.digits
    
    if not no_special:
        caracters += string.punctuation

    if no_lowercase and no_digits and no_special and no_uppercase:
        print("Erreur : Au moins un type de caractère doit être activé")
        exit(1)

    if output:
        text_file = open("output.txt", "w")

    for _ in range(count):
        
        password = ""
        
        for _ in range(nbr_digit):
            password += random.choice(caracters)

        if output:
            text_file.write(password + '\n')

        print(password)

    copy_to_clipboard(password)

    if output:
        text_file.close()

        if count == 1:
            print("Votre mot de passe a bien été enregistré dans ./output.txt")
        else:
            print("Vos mot de passe ont bien étés enregistrés dans ./output.txt")

def copy_to_clipboard(text):
    try:
        subprocess.run(['xclip', '-selection', 'clipboard'], 
                      input=text.encode(), check=True)
    except FileNotFoundError:
        try:
            subprocess.run(['xsel', '--clipboard', '--input'], 
                          input=text.encode(), check=True)
        except FileNotFoundError:
            print("xclip ou xsel non installé, copie impossible")


if __name__ == "__main__":
    main()
