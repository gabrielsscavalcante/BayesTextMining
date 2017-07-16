# -*- coding: utf-8 -*-
import csv
from Probability import Probability
from DataManager import DataManager

probability = Probability()

sentimentsCount = []

probWords = {}
probSentiments = {}

def addToProb(word,probability,dict):
    dict[word] = probability

dataManager = DataManager()
# Criar probabilidade de cada palavra e de cada classe aparecer
# P(palavra) = palavra/total
# P(Bom) = bom/total

for word in dataManager.countingWords:
    prob = probability.of_A(float(dataManager.countingWords[word]),float(len(dataManager.sentiments)))
    addToProb(word,prob,probWords)

print probWords

count1 = 0
count2 = 0
count3 = 0
for sentiment in dataManager.sentiments:
    if sentiment == '1':
        count1+=1
    elif sentiment == '2':
        count2 += 1
    else:
        count3 += 1

print dataManager.sentiments
sentimentsCount.append(count1)
sentimentsCount.append(count2)
sentimentsCount.append(count3)
print sentimentsCount

for i in range(0,3):
    prob = probability.of_A(float(sentimentsCount[i]),float(len(dataManager.sentiments)))
    addToProb(i+1,prob, probSentiments)

print probSentiments

# Calcular e criar um novo dicionario, pra adicionar a probabilidade de cada palavra pra cada classe
# P(palavra | bom) = P(palavra)*P(bom)/P(bom)

# Calcular a probabilidade da classe, dado o conjunto de palavras
# P(bom | palavras) = P(palavra1 | bom) * P(palavra2 | bom)

#probabilidade do array de X com aquele somatorio
probX = probability.ofX(probSentiments,probWords)
print probX

probGood = probability.bayes_Theorem_with_A_given_X(probSentiments[1],probWords, probX)
print probGood