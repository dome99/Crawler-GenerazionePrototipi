from MkTable import *
from Recommended import *


def stringify_attrs(attrs):
    s = ""
    for att in attrs:
        s += "combined, " + att + "\n"
    return s[:-1]


def stringify_typical_attrs(typical_attrs):
    s = ""
    for att_tuple in typical_attrs:
        s += "T(combined), " + att_tuple[0] + ", " + str(att_tuple[1]) + "\n"
    return s[:-1]


# Formatta la lista di attributi rigidi in accordo con il formato dell'input
def format_attrs(attrs):
    s = ""
    for att in attrs:
        s += att + "\n"
    return s


# Formatta la lista di attributi tipici in accordo con il formato dell'input
def format_typical_attrs(typical_attrs):
    s = ""
    for att_t in typical_attrs:
        s += att_t[0] + ", " + str(att_t[1]) + "\n"
    return s


# Output.py: permette di combinare concetti in maniera equivalente a come indicati nel file Pozz.py
# Stampa a schermo gli scenari raccomandati dalla classificazione di CoCoS
#   e scrive su un file di output lo scenario in modo che possa essere utilizzato per una nuova riclassificazione
if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Usage:\t python3 Output.py HEAD_FILE MODIFIER_FILE")
        sys.exit(1)

    head_input_data = ReadAttributesConcept(sys.argv[1], True)  # head
    modifier_input_data = ReadAttributesConcept(sys.argv[2], False)  # modifier
    del sys.argv[1]
    del sys.argv[1]

    tab = Table(head_input_data, modifier_input_data)
    print("Head Concept: " + tab.h_conc + "\tModifier Concept: " + tab.m_conc + "\n")

    rec_l = recommended_tuple(tab)

    if len(rec_l) == 0:
        print("No recommended scenarios...")
        sys.exit(0)

    print("\n///////////////////////////////////\nRecommended scenarios:\n")
    i = 0
    for scen_t in rec_l:
        title = tab.h_conc + "_" + tab.m_conc
        output_file = open(title + "_out" + str(i), "a+")
        output_file.write("# Output of the combination of " + tab.h_conc + " (head) and " + tab.m_conc +
                          " (modifier)\ntitle: " + title + "\n\n")

        # attrs = list(set([t[0] for t in tab.attrs]))  # fa si che non ci siano duplicati

        # attr tipici: eliminazione dei duplicati. Tra i duplicati si sceglie quello più probabile
        t_dict = dict()
        for j in range(len(scen_t[0][:-1])):
            if scen_t[0][j] == '1' and ((not (tab.typical_attrs[j][0] in t_dict)) or
                                        t_dict[tab.typical_attrs[j][0]] < tab.typical_attrs[j][1]):
                t_dict[tab.typical_attrs[j][0]] = tab.typical_attrs[j][1]
        typical_attrs = list(t_dict.items())

        # output_file.write(format_attrs(attrs))
        # output_file.write("\n")
        output_file.write(format_typical_attrs(typical_attrs))

        print("***** Scenario n: " + str(scen_t[1]) + ", output file: " + title + "_out" + str(i) + " *****\n" +
              # stringify_attrs(attrs) + "\n" +
              stringify_typical_attrs(typical_attrs) + "\n")
        i += 1

else:
    print("Unknown error at the very beginning...")
