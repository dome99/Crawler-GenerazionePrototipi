import json
import pathlib
import sys
from DataFromInput import ReadAttributes

MAX_PROGRAMS = 30


# Controlla se una parola(w) e' contenuta in una stringa(s)
def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')


def contains_value(lista, w):
    for p in lista:
        if str(p[0]) == w:
            return True
    return False


# Calcola la graduatoria e riclassifica tutti gli episodi offrendo la raccomandazione
def elaboraGraduatoria(prop_list, not_prop_list=[]):
    print("\nCanzoni raccomandate:\n")
    graduatoria = {}
    list_episodi = []
    chars_not_allowed_in_filename = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']

    sum = 0
    # Classificatore/
    # Verifica della lista delle parole negli episodi
    with open('data.txt') as json_file:
        data = json.load(json_file)

        # Calcolo graduatoria
        for song in data["songs"]:
            sum = sum + 1
            file_name = song["title"] + "-" + song["performer"]
            file_name = file_name.replace('"', "").replace('/', '_').replace('?', '').replace(':', '')

            if file_name not in graduatoria:
                graduatoria[file_name] = 0
                for prop in prop_list:
                    if contains_word(str(song["attributes"]), str(prop[0])):
                        graduatoria[file_name] = 0.1

                if pathlib.Path("./songs/" + file_name + ".txt").exists():
                    fileProgram = open("./songs/" + file_name + ".txt", "r")
                    for p in fileProgram:
                        word = p.split(':')
                        if contains_value(prop_list, word[0].strip()):
                            score = round(float(word[1].strip()), 2)
                            # Inserimento episodio in graduatoria
                            graduatoria[file_name] += score
                    fileProgram.close()

        # Scorrimento2 Canzoni
        for song in data["songs"]:
            file_name = song["title"] + "-" + song["performer"]
            file_name = file_name.replace('"', "").replace('/', '_').replace('?', '').replace(':', '')

            x = 1
            # Se nell'episodio compare una proprietà negata, la puntata viene scartata
            for prop in not_prop_list:
                if contains_word(str(song["attributes"]), str(prop[0])):
                    x = 0
                    break

            # Un episodio è considerato se contiene almeno il 30% delle proprietà della lista
            if x == 0:
                graduatoria[file_name] = 0

    # Graduatoria risultato
    jres = {}
    n_songs = 0
    jres["Songs"] = {}
    songs = jres["Songs"]
    # Scorrimento graduatoria ordinata per il punteggio dei programmi in modo decrescente
    for song, score in sorted(graduatoria.items(), key=lambda kv: kv[1], reverse=True):
        if score == 0 or n_songs >= MAX_PROGRAMS:
            break

        n_songs += 1
        print(song + "-" + str(score))


    if n_songs == 0:
        print("Non ci sono contenuti raccomandabili in questa categoria.")
    else:
        perc = (100 * n_songs) / sum
        print("Classificati " + str(n_songs) + " contenuti su " + str(sum) + " (" + str(perc) + "%)")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        # Lettura nome prototipo da classificare
        prototipo = sys.argv[1]
        # Lettura file prototipo - viene riutilizzato lo script "DataFromInput" di CoCoS
        f = ReadAttributes(prototipo)
        print("FRESULT: " + f.result)
        print("Generi  : " + f.head_conc + "-" + f.mod_conc + "\n\nClassificazione : \n")

        # Trasformazione risultato stringa in lista
        r = [str(s) for s in f.result.split(',')]
        print("R: " + str(r))

        # Lista delle proprietà risultato forti + tipiche
        prop_list = []
        not_prop_list = []

        # Inserimento proprietà forti nella lista
        for p in f.attrs:
            if str(p).find('-') == -1:
                print("P: " + str(p))
                prop_list.append(p)
            else:
                print("P-: " + str(p))
                not_prop_list.append(p[0].replace("-", "").strip())

        # Inserimento proprietà tipiche estratte dal risultato di COCOS
        i = 0
        for p in f.tipical_attrs:
            if r[i].strip() == "'1'":
                prop_list.append(p)
                print("Append p: " + str(p))
            i += 1
        print(prop_list)
        print(not_prop_list)

        # Calcolo graduatoria nuova categoria
        elaboraGraduatoria(prop_list, not_prop_list)
    else:
        print("Inserisci il prototipo da classificare!")
