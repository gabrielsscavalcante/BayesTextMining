import csv
from StopWords import StopWords

sentiments = []
texts = []
titles = []
dictCountWords = {}

arrayTests = []

# Aqui ele verifica se o array ja possui uma palavra, se n tiver ele add.
# Assim da pra evitar adicionar 2x uma palavra que apareceu 2x no mesmo texto
def addToDict(words,local):
    for word in words:
        if local.has_key(word):
            local[word] = local[word]+1
        else:
            local[word] = 1

def addToArrayUnique(word, local):
    if word.lower() not in local:
        local.append(word.lower())

# Separando o arquivo de um jeito bonitinho
def separateArray( text, local ):
   local.append(text)
   return

# Abrindo arquivo
with open('chennai.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')

    # Separando arquivo em arrays pra cada coluna importante
    for row in readCSV:
        separateArray(row[1],titles)
        separateArray(row[2],texts)
        separateArray(row[3],sentiments)

    for row in texts:
        palavraCortada = row.split( )
        for word in palavraCortada:
            addToArrayUnique(word,arrayTests)
        addToDict(arrayTests,dictCountWords)
        arrayTests = []

    print dictCountWords
    #palavraCortada = dictCountWords['teste'].split( )
    #print dictCountWords['teste'].split( )

    #for i in range(0,len(palavraCortada)):
     #   addToDict(palavraCortada[i],arrayTests)
    #print arrayTests


StopWords().printList()