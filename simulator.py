import sys
from typing import List


class Simulator:

    def __init__(self, RT: int, AR: float, RR: float, probs: List[float]) -> None:
        super().__init__()
        self.runTime = RT
        self.arrivalRate = AR
        self.readRate = RR
        self.probabilities = probs

    def run(self):
        pass


if __name__ == "__main__":
    runTime = int(sys.argv[1])
    arrivalRate = float(sys.argv[2])
    readRate = float(sys.argv[3])
    probabilities = [float(sys.argv[i]) for i in range(4, len(sys.argv))]
    sim = Simulator(RT=runTime, AR=arrivalRate, RR=readRate, probs=probabilities)
    sim.run()
