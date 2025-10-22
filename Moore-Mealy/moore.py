def moore_machine(inputs):
    outputs = []
    state = "A"

  
    state_output = {
        "A": "b",
        "B": "b",
        "C": "a"
    }


    transitions = {
        ("A", "0"): "B",
        ("A", "1"): "A",
        ("B", "0"): "B",
        ("B", "1"): "C",
        ("C", "0"): "B",
        ("C", "1"): "A",
    }


    outputs.append(state_output[state])

    for symbol in inputs:
        state = transitions[(state, symbol)]
        outputs.append(state_output[state])

    return "".join(outputs)


print("Input: 011001")
print("Output:", moore_machine("011001"))

print("\nInput: 110011")
print("Output:", moore_machine("110011"))
