import string 
from unidecode import unidecode 
#### Fonction secondaire

def ispalindrome(p):

    p = unidecode(p)
    p = p.upper()
    p = p.replace(" ","")
    p = p.translate(str.maketrans('','',string.punctuation))
    if len(p) == 1 : return True
    if p == "" : return True
    if p[0] == p[-1] : 
        return ispalindrome(p[1:-1])
    else :
        return False


#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()