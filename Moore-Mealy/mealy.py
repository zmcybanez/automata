def mealy_machine(inputs):
    state = "A"
    outputs = []

    for i in inputs:
        if state == "A":
            if i == "0":
                state = "B"
                outputs.append("b")
            else:  # i == "1"
                state = "A"
                outputs.append("b")

        elif state == "B":
            if i == "0":
                state = "B"
                outputs.append("b")
            else:  # i == "1"
                state = "C"
                outputs.append("a")

        elif state == "C":
            if i == "0":
                state = "A"
                outputs.append("b")
            else:  # i == "1"
                state = "C"
                outputs.append("b")

    return "".join(outputs)


print("Input: 011001")
print("Output:", mealy_machine("011001"))

print("\nInput: 110011")
print("Output:", mealy_machine("110011"))
