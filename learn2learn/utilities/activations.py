
def relu(inputs):
    return (inputs > 0) * inputs

def drelu(outputs):
    return outputs > 0
    