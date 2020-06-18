from sys import exit, argv

from DataFromInput import ReadAttributes
from MkTable import Table
from Output import stringify_typical_attrs
from Recommended import recommended_tuple

if __name__ == '__main__':
    if len(argv) < 2:
        input_data = ReadAttributes('Pet_Fish_3_concepts', two_modifiers=True)
    else:
        input_data = ReadAttributes(argv[1], two_modifiers=True)

    table = Table(input_data, two_modifiers=True)

    recomm = recommended_tuple(table)

    if len(recomm) == 0:
        print("No recommended scenarios...")
        exit(0)

    print("\n///////////////////////////////////\ncombined = " +
          table.h_conc + "_" + table.m_conc + "_" + table.m2_conc + "\nRecommended scenarios:\n")
    i = 0
    for scen_t in recomm:

        # attr tipici: eliminazione dei duplicati. Tra i duplicati si sceglie quello più probabile
        t_dict = dict()
        for j in range(len(scen_t[0][:-1])):
            if scen_t[0][j] == '1' and ((not (table.typical_attrs[j][0] in t_dict)) or
                                        t_dict[table.typical_attrs[j][0]] < table.typical_attrs[j][1]):
                t_dict[table.typical_attrs[j][0]] = table.typical_attrs[j][1]
        typical_attrs = list(t_dict.items())

        print("***** Scenario n: " + str(scen_t[1]) + " *****\n" + stringify_typical_attrs(typical_attrs) + "\n")
        i += 1

else:
    print("Unknown error at the very beginning...")
