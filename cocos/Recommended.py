from CreateOntology import *


#Metodo per verificare la consistenza dello scenario
def consistent_scenario(line, typical_attrs, attrs, two_modifiers=False):
    onto = ManageOntology(typical_attrs, attrs, line, two_modifiers=two_modifiers)
    res = onto.is_consistent()
    return res

#Metodo per controllare che le proprietà del modifier prese in considerazione 
# in uno scenario non creino conflitto con le proprietà dell'head non prese 
# in considerazione in quello stesso scenario
def conflict(line, typical_attrs, attrs, two_modifiers=False):
    # Per ogni attributo nello scenario
    for i in range(len(typical_attrs)):
        # Se appartiene al modifier ed è incluso nello scenario
        if line[i] == '1' and not typical_attrs[i][2]:

            for j in range(len(typical_attrs)):
                # Se l'attributo è della head e non è stato scelto nello scenario
                if typical_attrs[j][2] and line[j] == '0':

                    # Verifichiamo che la proprietà del modifier non sia in conflitto con la proprietà della head
                    ontoConflict = ConflictOntology(i, j, typical_attrs, attrs, two_modifiers=two_modifiers)
                    if not ontoConflict.is_consistent():
                        return True

    return False

# Metodo che restituisce una lista di coppie scenario-numero_scenario
def recommended_tuple(table) :
    
    res = []
    l = len(table.sorted_table) - 1
    line_len = len(table.typical_attrs)

    while res == [] and l > 0 :
        
        #creo blocco
        block = []
        Max = table.sorted_table[l][line_len]

        while l > 0 and table.sorted_table[l][line_len] == Max:
            block.append(tuple([table.sorted_table[l], l]))
            l -= 1
        print(block)

        for scen in block :
            print ("\n\n /////////////////////////////////////// ")
            print (scen)
            #controllo che lo scenario sia consistente
            if consistent_scenario(scen[0][:-1], table.typical_attrs, table.attrs, two_modifiers=table.two_modifiers):
                print("...... scenario consistente: OK ........")
                # controllo se contiene tutti gli attributi head
                contains_all_h_attrs = True
                for elem in range(len(scen[0]) - 1):
                    if scen[0][elem] == '0' and table.typical_attrs[elem][2] == True:
                        contains_all_h_attrs = False
                        break
                print("...... scenario NON TRIVIALE: OK ........")
                # se non contiene tutti gli attributi head, controlla che non crei conflitti e nel caso aggiunge al result
                if not contains_all_h_attrs:
                   c = conflict(scen[0][:-1], table.typical_attrs, table.attrs, two_modifiers=table.two_modifiers)
                   if not c :
                        res.append(scen)
                        print("...... scenario senza conflitti head/modifier: OK ........")
                   else:
                       print(" ====== Scenario scartato: CONFLITTO HEAD/MODIFIER ======== ")
                else:
                    print(" ====== Scenario scartato: TRIVIALE ======== ")
            else:
                print(" ====== Scenario scartato: INCONSISTENTE ======== ")

    return res


# Metodo che restituisce una lista con i numeri degli scenari (linee)
# all'interno della tabella che sono più rappresentativi, e quindi consigliati
# Come prima cosa crea dei blocchi di scenari con stessa probabilità,
#  partendo da probabilità più alta
# Poi partendo dal primo blocco ad analizzare controlla che non
#   contenga tutti gli attributi della head (troppo banale e poco rappresentativo)
#   e che il metodo conflict restituisca false, nel qual caso vengono aggiunti
#   gli scenari rimasti alla lista risualtante, nel caso non fossero rimasti scenari,
#   si ripete finchè non se ne trova uno.
def recommended(table):
    return [t[1] for t in recommended_tuple(table)]
