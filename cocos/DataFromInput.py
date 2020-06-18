from pprint import *


# Classe per il parsing dell'input da file
# Per prima cosa salva tutte le linee del file su una lista
# Toglie quelle di commento e quelle vuote
# Salva in delle stringhe il titolo e i nomi del concetto head e modifier
# Infine scandisce le linee rimanenti creando due liste, 
#   una con le proprietà tipiche e una con quelle forti
class ReadAttributes:

    def __init__(self, path='Input', two_modifiers=False):

        with open(path) as f:
            self.input_lines = f.readlines()

        self.input_lines = [x.strip() for x in self.input_lines
                            if x.strip() != '' and x.strip()[0] != '#']

        self.title = self.input_lines[0].split(':')[1].strip()
        self.input_lines.pop(0)

        self.head_conc = self.input_lines[0].split(':')[1].strip()
        self.input_lines.pop(0)

        self.mod_conc = self.input_lines[0].split(':')[1].strip()
        self.input_lines.pop(0)

        if two_modifiers:
            self.mod2_conc = self.input_lines[0].split(':')[1].strip()
            self.input_lines.pop(0)

        self.typical_attrs = []
        self.attrs = []

        for l in self.input_lines:
            l = [k.strip() for k in l.split(',')]

            if len(l) == 3 and l[0][0] == 'T':
                if two_modifiers:
                    num_modifier = 1  # se si tratta di un attributo head, num_modifier non ha valore
                    if l[0][2:-1] == 'modifier2':
                        num_modifier = 2
                    self.typical_attrs.append(
                        tuple([l[1], float(l[2]), (True if l[0][2:-1] == 'head' else False), num_modifier]))
                else:
                    self.typical_attrs.append(tuple([l[1], float(l[2]), (True if l[0][2:-1] == 'head' else False)]))

            if len(l) == 2:
                if two_modifiers:
                    num_modifier = 1
                    if l[0] == 'modifier2':
                        num_modifier = 2
                    self.attrs.append(tuple([l[1], (True if l[0] == 'head' else False), num_modifier]))
                else:
                    self.attrs.append(tuple([l[1], (True if l[0] == 'head' else False)]))


# Classe per il parsing dell'input da file di un solo concetto
# Per prima cosa salva tutte le linee del file su una lista
# Toglie quelle di commento e quelle vuote
# Salva in delle stringhe il titolo
# Infine scandisce le linee rimanenti creando due liste,
#   una con le proprietà tipiche e una con quelle forti
# Formato output del file Output.py
class ReadAttributesConcept:

    def __init__(self, path, is_head):

        with open(path) as file:
            self.input_lines = file.readlines()

        self.input_lines = [x.strip() for x in self.input_lines
                            if x.strip() != '' and x.strip()[0] != '#']

        self.title = self.input_lines[0].split(':')[1].strip()
        self.input_lines.pop(0)

        self.attrs = []
        self.typical_attrs = []

        for line in self.input_lines:
            line = [sect.strip() for sect in line.split(',')]

            if len(line) == 2:
                self.typical_attrs.append(tuple([line[0], float(line[1]), is_head]))

            if len(line) == 1:
                self.attrs.append(tuple([line[0], is_head]))


if __name__ == '__main__':
    # f = ReadAttributes()
    # print(f.title + '\n' + f.head_conc + '\n' + f.mod_conc)
    # pprint(f.typical_attrs)
    # pprint(f.attrs)

    # f = ReadAttributesConcept("Fish", True)
    # print(f.title)
    # pprint(f.attrs)
    # pprint(f.typical_attrs)

    f = ReadAttributes("Pet_Fish_3_concepts", True)
    print(f.title)
    print(f.head_conc)
    print(f.mod_conc)
    print(f.mod2_conc)
    pprint(f.attrs)
    pprint(f.typical_attrs)
