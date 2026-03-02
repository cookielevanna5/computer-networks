import sys
from random import expovariate, random
from typing import List


class Simulator:
    def __init__(self, RT: int, AR: float, RR: float, probs: List[float]) -> None:
        super().__init__()
        self.runTime = RT
        self.arrivalRate = AR
        self.readRate = RR
        self.probabilities = probs
        self.amountInSystem = 0
        self.time = 0.0
        self.amountOfArrivals = 0
        self.arrival = expovariate(AR)
        self.departs = float("inf")
        self.totalWait = 0.0
        self.totalService = 0.0
        self.dumps = 0
        self.success = 0
        self.Ti = [0 for _ in range(len(self.probabilities))]

    def run(self):
        while True:
            minExit = self.departs
            minArrival = self.arrival
            if self.runTime < minArrival:
                if self.amountInSystem != 0:
                    minArrival = float("inf")
                else:
                    self.printAll()
                    return
            occurrenceTime = minArrival if minArrival < minExit else minExit
            diff = occurrenceTime - self.time
            self.totalWait += diff * self.amountInSystem
            self.Ti[self.amountInSystem] += diff
            self.time = occurrenceTime
            if minExit >= minArrival:
                self.handleArrivals()
                continue
            self.handleDeparts()

    def handleArrivals(self):
        if random() >= self.probabilities[self.amountInSystem]:
            self.dumps += 1
        else:
            self.amountInSystem += 1
            self.amountOfArrivals += 1
            if 1 >= self.amountInSystem:
                next_wind = expovariate(self.readRate)
                self.totalService += next_wind
                self.departs = self.time + next_wind
        self.arrival = self.time + expovariate(self.arrivalRate)

    def handleDeparts(self):
        self.amountInSystem -= 1
        self.success += 1
        if self.amountInSystem > 0:
            nextPacket = expovariate(self.readRate)
            self.totalService += nextPacket
            self.departs = self.time + nextPacket
        else:
            self.departs = float("inf")

    def printAll(self):
        backspace, toPrint = " ", ""
        avgServ, avgWait = 0.0, 0.0
        if 0 != self.success:
            avgWait = self.totalWait - self.totalService
            avgWait /= self.success
            avgServ = self.totalService / self.success
        toPrint += str(self.success) + backspace
        toPrint += str(self.dumps) + backspace
        toPrint += str(self.time) + backspace
        for t in self.Ti:
            toPrint += str(t) + backspace
        for t in self.Ti:
            toPrint += str(t / self.time) + backspace
        toPrint += str(avgWait) + backspace
        toPrint += str(avgServ) + backspace
        toPrint += str(self.amountOfArrivals / self.time) + backspace
        print(toPrint)


if __name__ == "__main__":
    runTime = int(sys.argv[1])
    arrivalRate = float(sys.argv[2])
    readRate = float(sys.argv[3])
    probabilities = [float(sys.argv[i]) for i in range(4, len(sys.argv))]
    Simulator(RT=runTime, AR=arrivalRate, RR=readRate, probs=probabilities).run()
