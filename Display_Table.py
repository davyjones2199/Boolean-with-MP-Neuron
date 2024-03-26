inputs = [[1,1],[1,0],[0,1],[0,0]]
m = MPNeuron()
print("\t  LOGIC TABLE ")
print("| Input|AND|NAND| OR |XNOR|XOR|")
for inp in inputs:
    print(f"|{inp}| {m.AND(inp)} | {m.NAND(inp)}  | {m.OR(inp)}  | {m.XNOR(inp)}  | {m.XOR(inp)} |")

print("\n")
print(" LOGIC TABLE for NOT gate")
print("|Input|Output|")
for value in inputs[1]:
    print(f"|{value}    |  {m.NOT(value)}   |")
