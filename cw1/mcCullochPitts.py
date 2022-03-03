def mcCullochPitts(u, gate_type):
    if gate_type == "not":
        w = [-1.5, 1]
    elif gate_type == "and":
        w = [0.8, 0.8, -1]
    elif gate_type == "nand":
        w = [-0.8, -0.8, 1]
    elif gate_type == "or":
        w = [1.5, 1.5, -1]

    e = sum(u[i] * w[i] for i in range(len(u)))
    return +(e > 0)


while True:
    gate_type = input("Enter gate type: ").lower().strip()
    u_input = input("Enter input eg. \"1 0 1\": ").split()
    u_input = [float(x) for x in u_input]

    print(mcCullochPitts(u_input, gate_type))
