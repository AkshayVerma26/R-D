file = open("Translate_Benchmark2.txt", 'r')
P2V_map = {}
for line in file:
    if not line.split():
        continue
    if line.split()[0] != "Translated":
        continue
    paddr = int(line.split()[-1])
    vaddr = int(line.split()[-3])
    if paddr not in P2V_map:
        P2V_map[paddr] = [1,[vaddr]]
    else:
        if vaddr not in P2V_map[paddr][1]:
            P2V_map[paddr][0] += 1
            P2V_map[paddr][1].append(vaddr)
synonyms = {}
for key in P2V_map.keys():
    if P2V_map[key][0]>1:
        synonyms[key] = P2V_map[key]
print("Synonyms Map:\n", synonyms)
print("Physical to Virtual Address Map:")
for key in P2V_map.keys():
    print(key, "\t:\t", P2V_map[key])