# -*- coding: utf-8 -*-
import csv
from Probability import Probability
from DataManager import DataManager

probability = Probability()

sentimentsCount = []

probWords = {}
probSentiments = {}
dictCountWords = {}

def addToProb(word,probability,dict):
    dict[word] = probability

dataManager = DataManager()
# Criar probabilidade de cada palavra e de cada classe aparecer
#  P(palavra) = palavra/total
# P(Bom) = bom/total

for word in dictCountWords:
    prob = probability.of_A(float(dictCountWords[word]),float(len(dataManager.sentiments)))
    addToProb(word,prob,probWords)

count1 = 0
count2 = 0
count3 = 0
for sentiment in dataManager.sentiments:
    if sentiment == 1:
        count1+=1
    elif sentiment == 2:
        count2 += 1
    else:
        count3 += 1

sentimentsCount.append(count1)
sentimentsCount.append(count2)
sentimentsCount.append(count3)

for i in range(0,3):
    prob = probability.of_A(float(sentimentsCount[i]),float(len(dataManager.sentiments)))
    addToProb(i+1,prob, probSentiments)

# Calcular e criar um novo dicionario, pra adicionar a probabilidade de cada palavra pra cada classe
# P(palavra | bom) = P(palavra)*P(bom)/P(bom)

# Calcular a probabilidade da classe, dado o conjunto de palavras
# P(bom | palavras) = P(palavra1 | bom) * P(palavra2 | bom)

probX = probability.ofX(probSentiments,probWords)
print probX
# probGood = probability.bayes_Theorem_with_A_given_X(probSentiments[1],probWords, probX)
# print probGood

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

# print('No lançamento de um dado, um numero par pode ocorrer de 3 maneiras diferentes dentre 6 igualmente provaveis')
# print probability.of_A(3.0,6.0)
# print('Numa urna há 20 bolinhas numeradas de 1 a 20. Retiram-se duas bolinhas dessa urna, uma após a outra, sem reposição. Qual a probabilidade de ter saído um número par e um múltiplo de 5?')
# print probability.intersection_Of_A_and_B(probability.of_A(10.0,20.0), probability.of_A(4.0,19.0))
# print('Palavras - P(bom = 1) = 0.75 P(maravilhoso = 1) = 0.5, P(pessimo = 1) = 0.4')
# print probability.bayes_Theorem_with_A_given_X(0.5, [0.75, 0.5, 0.4])

# print probability.bayes_Theorem_with_A_given_X((5.0/10.0), {'a':(1.0/5.0), 'b':(2.0/5.0), 'c':(5.0/5.0), 'd':(1.0/5.0)})