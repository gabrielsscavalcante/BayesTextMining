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
#print dataManager.goodWords
#print probWords
probabilityWordClass = {}

# Encontrando as P(palavra / sentimento)
# SE CONSEGUIR DEIXAR ISSO MAIS BONITO
probGoodWords = {}
probNeutralWords = {}
probBadWords = {}

for word in dataManager.goodWords:
    probabilitie = float(dataManager.goodWords[word])/float(sentimentsCount[2])
    probGoodWords[word] = probabilitie
for word in dataManager.neutralWords:
    probabilitie = float(dataManager.neutralWords[word])/float(sentimentsCount[1])
    probNeutralWords[word] = probabilitie
for word in dataManager.badWords:
    probabilitie = float(dataManager.badWords[word])/float(sentimentsCount[0])
    probBadWords[word] = probabilitie


# Calculando P(Sentimento / palavras)
# SE CONSEGUIR DEIXAR ISSO MAIS BONITO
# SE O SENTIMENTO NÃO POSSUI DETERMINADA PALAVRA EU IGNORO PRA NÃO ZERAR (MESMA COISA QUE MULTIPLICAR POR 1 EU ACHO)
acertos = 0
for i in range(1,len(dataManager.texts)):
    text = dataManager.separeteWords(dataManager.texts[i])

    probTextGood = 1
    probTextNeutral = 1
    probTextBad = 1

    for word in text:
        if probGoodWords.has_key(word):
            probTextGood = probTextGood*probGoodWords[word]
        else:
            probTextGood = probTextGood*0.001
        if probNeutralWords.has_key(word):
            probTextNeutral = probTextNeutral*probNeutralWords[word]
        else:
            probTextNeutral = probTextNeutral * 0.001
        if probBadWords.has_key(word):
            probTextBad = probTextBad*probBadWords[word]
        else:
            probTextBad = probTextBad * 0.001
    resultado = 0
    if probTextGood > probTextNeutral and probTextGood > probTextBad:
        resultado = 3
    if probTextNeutral > probTextGood and probTextNeutral > probTextBad:
        resultado = 2
    if probTextBad > probTextNeutral and probTextBad > probTextGood:
        resultado = 1

    if int(resultado) == int(dataManager.sentiments[i]):
        acertos = acertos+1
print float(acertos)/float(len(dataManager.texts))

# ------------------------------------------ FIM DO TREINO E INICIO DO TESTE -------------------------------------------
hitsTest = 0
for row in dataManager.phrases:
    phrase = row['probabilityWords']

    probTextGood = 1
    probTextNeutral = 1
    probTextBad = 1

    for word in phrase:
        if probGoodWords.has_key(word):
            probTextGood = probTextGood * probGoodWords[word]
        else:
            probTextGood = probTextGood * 0.001
        if probNeutralWords.has_key(word):
            probTextNeutral = probTextNeutral * probNeutralWords[word]
        else:
            probTextNeutral = probTextNeutral * 0.001
        if probBadWords.has_key(word):
            probTextBad = probTextBad * probBadWords[word]
        else:
            probTextBad = probTextBad * 0.001
    result = 0
    if probTextGood > probTextNeutral and probTextGood > probTextBad:
        result = 3
    if probTextNeutral > probTextGood and probTextNeutral > probTextBad:
        result = 2
    if probTextBad > probTextNeutral and probTextBad > probTextGood:
        result = 1
    if int(result) == int(row['sentiments']):
        hitsTest = hitsTest+1
print float(hitsTest)/float(len(dataManager.phrases))
#print frase['probabilityWords']
# for word in probWords:
#     probabilities = []
#     for i in range(0, 3):
#         givenProbability = probability.of_A_Given_B(float(probWords[word]), float(probSentiments[i+1]))
#         #
#         #
#         #
#         #
#         #OS VALORES ESTAO FICANDO IGUAIS
#         #
#         #TENTA VER QUAL O PROBLEMA
#         #
#         #
#         #
#         #
#         probabilities.append(givenProbability)
#
#     probabilityWordClass[word] = probabilities
# print probSentiments


#TEST
#Verificando a probabilidade de cada palavra por cada frase e colocando em um dicionario com probabilityWords, title e sentiment
for row in dataManager.phrases:
    probabilityRow = {}
    probabilityOfWords(row['probabilityWords'], row['probabilityWords'], probabilityRow)
    row['probabilityWords'] = probabilityRow
    #FALTANDO PEGAR AS PROBABILIDADES DELAS

classProbability = (5.0/10.0)
wordsProbabilities = {'a': (1.0/5.0), 'b': (2.0/5.0), 'c': (5.0/5.0), 'd' : (1.0/5.0)}
#print probability.bayes_Theorem_with_A_given_X(classProbability, wordsProbabilities)