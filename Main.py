# -*- coding: utf-8 -*-
import csv
from Probability import Probability
from DataManager import DataManager

probability = Probability()
dataManager = DataManager()

sentimentsCount = []
probWords = {}
probSentiments = {}

probabilityTestWords = {}

def addToProb(word,probability,dict):
    dict[word] = probability

def probabilityOfWords(words, sentiments, probabilities):
    for word in words:
        prob = probability.of_A(float(words[word]), float(len(sentiments)))
        addToProb(word, prob, probabilities)

#TREINAMENTO
#Necessario apenas pegar o valor
probabilityOfWords(dataManager.countingWords, dataManager.sentiments, probWords)

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

sentimentsCount.append(count1)
sentimentsCount.append(count2)
sentimentsCount.append(count3)

for i in range(0,3):
    prob = probability.of_A(float(sentimentsCount[i]),float(len(dataManager.sentiments)))
    addToProb(i+1,prob, probSentiments)

# P(word|class)

print probWords
probabilityWordClass = {}
for word in probWords:
    probabilities = []
    for i in range(0, 3):
        givenProbability = probability.of_A_Given_B(float(probWords[word]), float(probSentiments[i+1]))
        #
        #
        #
        #
        #OS VALORES ESTAO FICANDO IGUAIS
        #
        #TENTA VER QUAL O PROBLEMA
        #
        #
        #
        #
        probabilities.append(givenProbability)

    probabilityWordClass[word] = probabilities


#TEST
#Verificando a probabilidade de cada palavra por cada frase e colocando em um dicionario com probabilityWords, title e sentiment
for row in dataManager.phrases:
    probabilityRow = {}
    probabilityOfWords(row['probabilityWords'], row['probabilityWords'], probabilityRow)
    row['probabilityWords'] = probabilityRow
    #FALTANDO PEGAR AS PROBABILIDADES DELAS

classProbability = (5.0/10.0)
wordsProbabilities = {'a': (1.0/5.0), 'b': (2.0/5.0), 'c': (5.0/5.0), 'd' : (1.0/5.0)}
print probability.bayes_Theorem_with_A_given_X(classProbability, wordsProbabilities)