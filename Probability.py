class Probability:
    def of_A(self, numberOfCases, numberOfPossibilities):
        return numberOfCases/numberOfPossibilities

    def intersection_Of_A_and_B(self, numberOfIntersectionAAndB, probabilityOfB):
        return numberOfIntersectionAAndB/probabilityOfB

    def intersection_independent_Of_A_and_B(self, probabilityOfA, probabilityOfB):
        return probabilityOfB * probabilityOfA

    def of_A_Given_B(self, probabilityOfA, probabilityOfB):
        return Probability.intersection_Of_A_and_B(self, probabilityOfA, probabilityOfB)/probabilityOfB

    def bayes_Theorem_with_A_given_B(self, probabilityOfA, probabilityOfB, probabilityOfBGivenA):
        return ( probabilityOfBGivenA * probabilityOfA)/probabilityOfB