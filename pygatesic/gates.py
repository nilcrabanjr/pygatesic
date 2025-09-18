gate_types = {"NOT": "NOT", "NAND": "NAND", "AND": "AND","NOR": "NOR", "OR": "OR", "XNOR": "XNOR", "XOR": "XOR", "GENERAL": "GENERAL"}

class Gate:
    def __init__(self, name, gate_type, inputs, outputs):
        self.name = name
        self.gate_type = gate_type
        self.inputs = [False] * inputs
        self.outputs = [False] * outputs

    def __str__(self):
        return f"Name: {self.name} Type: {self.gate_type} Inputs: {self.inputs} Outputs: {self.outputs}"

    def not_logic(self, value):
        return not value

    def and_logic(self):
        return all(self.inputs)

    def nand_logic(self):
        return not all(self.inputs)

    def or_logic(self):
        return any(self.inputs)

    def nor_logic(self):
        return not any(self.inputs)

    def xor_logic(self):
        return (sum(self.inputs) % 2) == 1

    def xnor_logic(self):
        return (sum(self.inputs) % 2) == 0

def bin_to_list(binary):
    return [c == "1" for c in binary]

def list_to_bin(target):
    return "".join("1" if b else "0" for b in target)

def binary_output(value, length):
    return (f'{value:0{length}b}')

def binary_counter(length):
    i = 0
    out = []
    while True:
        b = binary_output(i, length)
        if len(b) > length:
            break
        out.append(b)
        i += 1
    return out

def truth_table_generator(target_gate):
    count_values = binary_counter(len(target_gate.inputs))
    print(f"\n{target_gate.name} ({target_gate.gate_type}) Truth Table")
    print("Inputs | Output")
    print("-" * (len(target_gate.inputs) + 10))
    for value in count_values:
        target_gate.inputs = bin_to_list(value)
        if target_gate.gate_type == "NOT":
            result = target_gate.not_logic(target_gate.inputs[0])
        elif target_gate.gate_type == "NAND":
            result = target_gate.nand_logic()
        elif target_gate.gate_type == "AND":
            result = target_gate.and_logic()
        elif target_gate.gate_type == "NOR":
            result = target_gate.nor_logic()
        elif target_gate.gate_type == "OR":
            result = target_gate.or_logic()
        elif target_gate.gate_type == "XNOR":
            result = target_gate.xnor_logic()
        elif target_gate.gate_type == "XOR":
            result = target_gate.xor_logic()
        else:
            result = "N/A"
        print(f"{value} | {int(result) if isinstance(result, bool) else result}")
