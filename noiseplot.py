import matplotlib.pyplot as plt
import pickle

def main():
    F = open(raw_input("File to be opened: "))
    plt.plot(pickle.load(F))
    # plots a simple line with the array values as y, and the integers from
    # 0 to the size of the array - 1 are the x values
    
    plt.show()
    
main()
