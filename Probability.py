class Probability:
    #
    # P(a) = n(a)/n(s)
    #
    def of_A(self, numberOfCases, numberOfPossibilities):
        return numberOfCases/numberOfPossibilities

    #
    # P(a,b) = P(a)*P(b)
    #
    def intersection_Of_A_and_B(self, probabilityOfA, probabilityOfB):
        print 'batata2'
        print probabilityOfA
        print probabilityOfB
        print 'batata1'
        print probabilityOfB * probabilityOfA
        return probabilityOfB * probabilityOfA

    #
    # P(a|b) = P(a,b)/P(b)
    #
    def of_A_Given_B(self, probabilityOfA, probabilityOfB):
        return Probability.intersection_Of_A_and_B(self, probabilityOfA, probabilityOfB)/probabilityOfB

    #
    # P(X) = P(y = 1, X) + P(y = 2, X) + P(y = 3, X)
    #
    def ofX(self, probOfSentiments, probabilitiesOfX):
        probability = 0.0

        for sentiment in probOfSentiments:
            producer = 1.0

            for x in probabilitiesOfX:
                producer = producer * self.intersection_Of_A_and_B(probOfSentiments[sentiment], probabilitiesOfX[x])

            probability = probability + producer

        return probability


    #
    # P(a|X) = P(a|x1, x2, x3,..., xi)
    # P(a|X) = p(a) * p(x1|a) * p(x2|a) * p(xi|a)
    #
    def bayes_Theorem_with_A_given_X(self, probabilityOfA, probabilitiesOfX):
        probability = 1.0

        for word in probabilitiesOfX:
            value = probabilitiesOfX[word]
            if value == 0.0:
                value = 0.1
                print value
            probability = probability * (self.of_A_Given_B(value, probabilityOfA))

        return (probabilityOfA * probability)

    def getMinFrom(self, probabilitiesOfX):
        minValue = 1000.0
        for word in probabilitiesOfX:
            if probabilitiesOfX[word] < minValue:
                minValue = probabilitiesOfX[word]

        return minValue