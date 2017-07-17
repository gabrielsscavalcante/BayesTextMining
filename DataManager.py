# -*- coding: utf-8 -*-

import csv
import unicodedata
import re
import random
from StopWords import StopWords

class DataManager:
    data = []
    trainingData = []
    testData = []
    stopWords = StopWords().list

    #Training Data
    titles = []
    texts = []
    sentiments =[]
    words = []

    countingWords = {}
    badWords = {}
    neutralWords = {}
    goodWords = {}

    #Test Data
    phrases = []
    textsTest = []
    sentimentsTest = []

    def __init__(self):
        self.data = self.getData()
        self.separateData()
        self.organizeTrainingData()
        self.separateTrainingWords()
        self.separateTestPhrases()

    def getData(self):
        read = []
        with open('chennai.csv', 'r') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';')

            for row in readCSV:
                read.append(row)

        #random.shuffle(read)
        return read

    def separateData(self):
        sizeTraining = int(0.8*len(self.data))
        size = len(self.data)
        self.data.pop(0)
        random.shuffle(self.data)
        self.trainingData = self.data[1:sizeTraining]
        self.testData = self.data[sizeTraining:size]

    def organizeTrainingData(self):
        for row in self.trainingData:
                self.titles.append(row[1])
                self.texts.append(row[2])
                self.sentiments.append(row[3])

    def addToArrayUnique(self, word, local):
        if word.lower() not in local and word.lower() not in DataManager.stopWords:
            finalWord = self.removeCharacters(word.lower())
            if finalWord != "":
                local.append(finalWord)

    def addToDictionary(self, words, local):
        for word in words:
            if local.has_key(word):
                local[word] = local[word] + 1
            else:
                local[word] = 1

    def separateTrainingWords(self):
        for i in range(0, len(self.texts)):
            wordsPerText = self.texts[i].split()
            for word in wordsPerText:
                self.addToArrayUnique(word,self.words)

            if self.sentiments[i] == '1':
                self.addToDictionary(self.words, self.badWords)
            elif self.sentiments[i] == '2':
                self.addToDictionary(self.words, self.neutralWords)
            elif self.sentiments[i] == '3':
                self.addToDictionary(self.words, self.goodWords)

            self.addToDictionary(self.words, self.countingWords)
            self.cleanData()

    def separateTestPhrases(self):
        a = 1
        dictionaryRow = {}
        dictionaryWords = {}
        for row in self.testData:
            if a == 2:
                dictionaryRow['titles'] = row[1]
                self.addToDictionary(self.separeteWords(row[2]), dictionaryWords)
                dictionaryRow['probabilityWords'] = dictionaryWords
                dictionaryRow['sentiments'] = row[3]
                self.phrases.append(dictionaryRow)
                dictionaryRow = {}
                dictionaryWords = {}
            else:
                a = 2

    def separeteWords(self, text):
        separatedWords = []
        wordsPerText = text.split()
        for word in wordsPerText:
            self.addToArrayUnique(word, separatedWords)

        return separatedWords

    def removeCharacters(self, word):

        # Unicode normalize transforma um caracter em seu equivalente em latin.
        # nfkd = unicodedata.normalize('NFKD', word)
        # palavraSemAcento = u''.join([c for c in nfkd if not unicodedata.combining(c)])

        # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
        return re.sub('[^a-zA-Z0-9 \\\]', '', word)

    def cleanData(self):
        self.words = []