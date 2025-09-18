from pygatesic.gates import *
from pygatesic.ics import *

class IC7400(IC):
    def __init__(self):
        super().__init__(7400)

        # Pins 1..14
        self.ports = [Port(str(i), False) for i in range(1, 15)]
        (self.p1, self.p2, self.p3,
         self.p4, self.p5, self.p6,
         self.p7, self.p8, self.p9,
         self.p10, self.p11, self.p12,
         self.p13, self.p14) = self.ports

        self.nand1 = Gate("nand1", gate_types["NAND"], 2, 1)
        self.nand2 = Gate("nand2", gate_types["NAND"], 2, 1)
        self.nand3 = Gate("nand3", gate_types["NAND"], 2, 1)
        self.nand4 = Gate("nand4", gate_types["NAND"], 2, 1)

    def cycle(self):
        self.nand1.inputs = [self.p1.state, self.p2.state]
        self.p3.state = self.nand1.nand_logic()
        self.nand2.inputs = [self.p4.state, self.p5.state]
        self.p6.state = self.nand2.nand_logic()
        self.nand3.inputs = [self.p9.state, self.p10.state]
        self.p8.state = self.nand3.nand_logic()
        self.nand4.inputs = [self.p12.state, self.p13.state]
        self.p11.state = self.nand4.nand_logic()
