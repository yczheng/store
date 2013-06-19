import pickle, numpy

def main():
    N = input("Integer number of random numbers: ")
    F = open(raw_input("Filename to be saved as: "), 'w')
    noise = numpy.random.uniform(0, 1, N)
    
    pickle.dump(noise, F)
    F.close()
    #changes branches la di da
    
main()