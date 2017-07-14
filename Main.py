# -*- coding: utf-8 -*-
import csv
from StopWords import StopWords
from Probability import Probability

sentiments = []
texts = []
titles = []
dictCountWords = {}
dictWordGood = {}
dictWordNeutral = {}
dictWordBad = {}

arrayUniqueWords = []
arrayStop = StopWords().list

# Aqui ele verifica se o array ja possui uma palavra, se n tiver ele add.
# Assim da pra evitar adicionar 2x uma palavra que apareceu 2x no mesmo texto
def addToDict(words,local):
    for word in words:
        if local.has_key(word):
            local[word] = local[word]+1
        else:
            local[word] = 1

def addToArrayUnique(word, local):
    if word.lower() not in local and word.lower() not in arrayStop:
        local.append(word.lower())

# Separando o arquivo de um jeito bonitinho
def separateArray( text, local ):
   local.append(text)
   return

# Abrindo arquivo
with open('chennai.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')

    # Separando arquivo em arrays pra cada coluna importante
    a = 1
    for row in readCSV:
        if a == 2:
            separateArray(row[1],titles)
            separateArray(row[2],texts)
            separateArray(int(row[3]),sentiments)
        else:
            a = 2

    for i in range(0, len(texts)):
        palavraCortada = texts[i].split( )
        for word in palavraCortada:
            addToArrayUnique(word,arrayUniqueWords)
        if sentiments[i] == 1:
            addToDict(arrayUniqueWords, dictWordBad)
        elif sentiments[i] == 2:
            addToDict(arrayUniqueWords, dictWordNeutral)
        elif sentiments[i] == 3:
            addToDict(arrayUniqueWords, dictWordGood)
        addToDict(arrayUniqueWords,dictCountWords)
        arrayUniqueWords = []

    # Criar probabilidade de cada palavra e de cada classe aparecer
    # P(palavra) = palavra/total
    # P(Bom) = bom/total

    # Calcular e criar um novo dicionario, pra adicionar a probabilidade de cada palavra pra cada classe
    # P(palavra | bom) = P(palavra)*P(bom)/P(bom)

    # Calcular a probabilidade da classe, dado o conjunto de palavras
    # P(bom | palavras) = P(palavra1 | bom) * P(palavra2 | bom)

    # print dictCountWords
    # print dictWordGood
    # print dictWordNeutral
    # print dictWordBad
    #palavraCortada = dictCountWords['teste'].split( )
    #print dictCountWords['teste'].split( )

    #for i in range(0,len(palavraCortada)):
     #   addToDict(palavraCortada[i],arrayTests)
    #print arrayTests

#TESTE
probability = Probability()
print('No lançamento de um dado, um numero par pode ocorrer de 3 maneiras diferentes dentre 6 igualmente provaveis')
print probability.of_A(3.0,6.0)
print('Numa urna há 20 bolinhas numeradas de 1 a 20. Retiram-se duas bolinhas dessa urna, uma após a outra, sem reposição. Qual a probabilidade de ter saído um número par e um múltiplo de 5?')
print probability.intersection_Of_A_and_B(probability.of_A(10.0,20.0), probability.of_A(4.0,19.0))
print('Palavras - P(bom = 1) = 0.75 P(maravilhoso = 1) = 0.5, P(pessimo = 1) = 0.4')
print probability.bayes_Theorem_with_A_given_X(0.5, [0.75, 0.5, 0.4])

print probability.bayes_Theorem_with_A_given_X(5.0/10.0, [(1.0/5.0), (2.0/5.0), (5.0/5.0),(1.0/5.0)])