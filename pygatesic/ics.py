class Port:
    def __init__(self, name, state: bool):
        self.name = name
        self.state = state

class IC:
    def __init__(self, name):
        self.name = name
        self.ports = []

    def __str__(self):
        return f"{self.name} {self.ports}"

    def add_port(self, port):
        self.ports.append(port)

    def remove_port(self, port):
        self.ports.remove(port)

    def print_ports(self):
        # single consistent style everywhere
        for port in self.ports:
            print(f"Port Name: {port.name} Port State: {port.state}")
