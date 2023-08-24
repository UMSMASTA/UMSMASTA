import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def main():
    N =4
    localnetMeans = (20,35,30,35) #legnth of outage in minutes
    wanMeans = (25,32,34,20) #WAN length of outage (min)
    ind = np.arange(N) #the x locations for the groups
    #width of bars:
    width = 0.35

    #describe where to diplay p1
    p1 = plt.bar(ind,localnetMeans,width)
    #stack p2 on top
    p2 = plt.bar(ind,wanMeans,width,bottom=localnetMeans)

    #decribe the data
    plt.ylabel("Length of Outage in minutes")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0,81,10))
    plt.legend((p1[0], p2[0]), ("LAN,WAN"))

    #display the graph
    plt.show()

main()
