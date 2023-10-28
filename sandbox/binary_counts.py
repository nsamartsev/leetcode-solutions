def counts(input):
    out = [0] * 256

    for i in range(len(input)):
        symbol = input[i]
        out_index = ord(symbol)
        out[out_index] = out[out_index] + 1

    return out


print(counts("AAAAABBAHHBCBGCCC"))
