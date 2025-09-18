from pygatesic.gates import *
from pygatesic.ics import *
from ic_collection.ic7400 import *

# Setup
test_gate = Gate("test_gate", gate_types["GENERAL"], 4, 1) # Initialise gate with a type of 7 (General), 4 inputs and 1 output
xor1 = Gate("xor1", gate_types["XOR"], 2, 1)
and1 = Gate("and1", gate_types["AND"], 2, 1)
xor2 = Gate("xor2", gate_types["XOR"], 2, 1)
and2 = Gate("and2", gate_types["AND"], 2, 1)
or1 = Gate("or1", gate_types["OR"], 2, 1)
nand1 = Gate("nand1", gate_types["NAND"], 2, 1)

##### HALF ADDER #####

def half_adder(gate1, gate2, inp1, inp2):
    gate1.inputs[0], gate1.inputs[1] = inp1, inp2
    gate2.inputs[0], gate2.inputs[1] = inp1, inp2
    gate1.outputs[0] = gate1.xor_logic()
    gate2.outputs[0] = gate2.and_logic()
    return gate1.outputs[0], gate2.outputs[0]

##### FULL ADDER #####

def full_adder(gate1, gate2, gate3, gate4, gate5, inp1, inp2, carryin):
    sum1, carry1 = half_adder(gate1, gate2, inp1, inp2)
    sum2, carry2 = half_adder(gate3, gate4, carryin, sum1)
    gate5.inputs[0], gate5.inputs[1] = carry1, carry2
    gate5.outputs[0] = gate5.or_logic()
    print(f"SUM: {sum2} CARRY: {gate5.outputs[0]}")
    return sum2, gate5.outputs[0]


##### GATE TESTING #####

'''
full_adder(xor1, and1, xor2, and2, or1, False, False, False)
full_adder(xor1, and1, xor2, and2, or1, True, False, False)
full_adder(xor1, and1, xor2, and2, or1, False, True, False)
full_adder(xor1, and1, xor2, and2, or1, False, False, True)
full_adder(xor1, and1, xor2, and2, or1, True, True, False)
full_adder(xor1, and1, xor2, and2, or1, True, False, True)
full_adder(xor1, and1, xor2, and2, or1, False, True, True)
full_adder(xor1, and1, xor2, and2, or1, True, True, True)
'''

##### TESTING #####

# Demo
ic_7400 = IC7400()
ic_7400.print_ports()
ic_7400.cycle()
print("")
ic_7400.print_ports()
ic_7400.p1.state, ic_7400.p2.state = True, True
ic_7400.cycle()
print("")
ic_7400.print_ports()
