import numpy as np

class Sample:
    def __init__(self, X, y):
        self.X = X
        self.y = y

def perceptron_two_classes( samples, C, W):
    
    for sample in samples:
        sample.X.append(1)

    for sample in samples:
        if sample.y == 2:
            for i in range(len(sample.X)):
                sample.X[i] *= -1
    num = 0
    it = 0
    id = 0
    while True:
        print("\n{0}th iteration\n".format(it))
        for idx, sample in enumerate(samples):
            if np.dot(W, sample.X) <= 0:
                print("Weight correction for the {0} th sample.\n".format(idx+1))
                W = np.add(W, C*sample.X)
                print("W{0} = W{1} + {2}*X{3} = {4}".format(id+1,id,C,idx+1,W))
                num = 0
            else:
                print("W{0} = W{1}".format(id+1, id))
                num += 1
            id += 1

        if num >= len(samples):
            break
        it+=1

    print("Done")
    print("Final weights are: ", W)

def perceptron_N_classes( samples, C, W):
    
    for sample in samples:
        sample.X.append(1)

    it = 0
    num = 0
    num_of_classes = len(W)

    while True:
        print("{0}th iteration\n\n".format(it))
        
        for idx, sample in enumerate(samples):
            max_val = float("-inf")
            for i in range((num_of_classes)):
                val = np.dot(W[i], sample.X)
                if val > max_val:
                    max_val = val
            found = False
            for i in range((num_of_classes)):
                val = np.dot(W[i], sample.X)
                if val == max_val:
                    if i != sample.y: #Wrong classification
                        found = True
                        num = 0
                        W[i] = np.add(W[i], (-1)*C*np.array(sample.X))
                        W[sample.y] = np.add(W[sample.y], C*sample.X)
                        print("W{0} = W{1} -{2} * X{3}".format(i,i, C, idx+1))
                        print("W{0} = W{1} + {2} * X{3}".format(sample.y, sample.y, C, idx+1))
            if not found: 
                num += 1
            if num >= len(samples):
                break
        if num >= len(samples):
            break
        it += 1
    print("Done")
    print(W)

def main():

    C = 1
    samples = []
    samples.append(Sample([0,0],0))
    samples.append(Sample([1,0], 0))
    samples.append(Sample([0,1],1))
    W = [0,0,0]
    W2 = [[0,0,0],[0,0,0]]
    #perceptron_two_classes(samples, C, W)
    perceptron_N_classes(samples, C, W2)


if __name__ == "__main__":
    main()
