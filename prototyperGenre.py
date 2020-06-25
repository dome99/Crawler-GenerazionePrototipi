# Crea i prototipi per i generi musicali

import json

def writeWordInf(file, word, value):
    spaces = 35 - len(word) + 1
    stri = word + ":"
    for idx in range(spaces):
        stri = stri + " "

    stri = stri + str(value)
    file.write(stri + "\n")


genres = {}

numOfSongs = {}
with open('data.txt') as json_file:
    data = json.load(json_file)

    for s in data['songs']:

        if s['genre'] not in genres:
            genres[s['genre']] = {}
            numOfSongs[s['genre']] = {}
            numOfSongs[s['genre']]['nums'] = 0
        else:
            numOfSongs[s['genre']]['nums'] += 1

        for i in range(len(s['attributes'])):
            attribute = s['attributes'][i].split(" (")[0]

            if attribute not in genres[s['genre']]:
                genres[s['genre']][attribute] = 0
            genres[s['genre']][attribute] += 1


#print(numOfSongs)

for g in genres:

    attributes = genres[g]


    for key in attributes:
        if numOfSongs[g]['nums'] != 0:
            freq = float(attributes[key]/numOfSongs[g]['nums'])
            if freq > 0.80:
                numOfSongs[g][key] = str(freq) , ' - ' , attributes[key] , ' - ' , numOfSongs[g]['nums']

#print(numOfSongs)


    MAX_SCORE = 0.9
    MIN_SCORE = 0.6
    minFreq = 1
    maxFreq = 0

    for key in attributes:
        freq = int(attributes[key]) / len(attributes)
        minFreq = min(minFreq, freq)
        maxFreq = max(maxFreq, freq)

    rangeFreq = maxFreq - minFreq
    rangeScore = MAX_SCORE - MIN_SCORE
    f = open("genres/" + g + ".txt", "w+")


    for key, value in sorted(genres[g].items(), key=lambda kv: kv[1], reverse=True):
        freq = int(attributes[key]) / len(attributes)

        score = MAX_SCORE
        if rangeFreq > 0:
            score = MIN_SCORE + (rangeScore * (freq - minFreq) / rangeFreq)
            writeWordInf(f, key, str(score))

    f.close()