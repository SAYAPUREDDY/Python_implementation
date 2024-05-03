def activation(out, threshold):
    if out >= threshold:
        return 1
    else:
        return 0

def perceptron(orInput):
    A = [0, 0, 1, 1]
    B = [0, 1, 0, 1]
    orOutput = [0, 1, 1, 1]
    weights = [0.3, 0.7]

    threshold = 1
    learningRate = 0.1

    # Perceptron training
    print('Perceptron training for OR gate')
    print("____________________")

    numIteration = 4
    for iteration in range(numIteration):
        summation = A[iteration] * weights[0] + B[iteration] * weights[1]
        output = activation(summation, threshold)

        print("learning rate = " + str(learningRate))
        print("Inputs = " + str(A[iteration]) + " , " + str(B[iteration]))
        print("Weights = " + str(weights[0]) + " , " + str(weights[1]))
        print("Summation = " + str(summation) + " Threshold " + str(threshold))
        print("Actual output = " + str(orOutput[iteration]) + " Predicted Output " + str(output))
        print("__________________________")

        if output != orOutput[iteration]:
            weights[0] = weights[0] + learningRate * (orOutput[iteration] - output) * A[iteration]
            weights[1] = weights[1] + learningRate * (orOutput[iteration] - output) * B[iteration]
            print("Updated Weights = " + str(weights[0]) + " " + str(weights[1]))

        print("Weights updated: Training again")
        print("-----------------------------------")

    # Perceptron prediction
    print("Perceptron prediction")
    summation = orInput[0] * weights[0] + orInput[1] * weights[1]
    return activation(summation, threshold)


# Test for OR gate with input [0, 0]
orInput = [0, 0]
print("OR input " + str(orInput) + ": " + str(perceptron(orInput)))
orInput = [0, 1]
print("OR input " + str(orInput) + ": " + str(perceptron(orInput)))
orInput = [1, 0]
print("OR input " + str(orInput) + ": " + str(perceptron(orInput)))
orInput = [1, 1]
print("OR input " + str(orInput) + ": " + str(perceptron(orInput)))
