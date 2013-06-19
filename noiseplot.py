import matplotlib.pyplot as plt
import pickle

def main():
    F = open(raw_input("File to be opened: "))
    plt.plot(pickle.load(F))
    plt.show()
    
main()
