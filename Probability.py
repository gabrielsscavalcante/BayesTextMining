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
        return probabilityOfB * probabilityOfA

    #
    # P(a|b) = P(a,b)/P(b)
    #
    def of_A_Given_B(self, probabilityOfA, probabilityOfB):
        return Probability.intersection_Of_A_and_B(self, probabilityOfA, probabilityOfB)/probabilityOfB

    #
    # P(a|X) = P(a|x1, x2, x3,..., xi)
    # P(a|X) = p(a) * p(x1|a) * p(x2|a) * p(xi|a)
    #
    def bayes_Theorem_with_A_given_X(self, probabilityOfA, probabilitiesOfX):
        probability = 1.0

        for i in range(0,len(probabilitiesOfX)):
            probability = probability * self.of_A_Given_B(probabilitiesOfX[i], probabilityOfA)

        return probabilityOfA * probability