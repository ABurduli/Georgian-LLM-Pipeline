import json
with open("..\\..\\..\\input\\input.jsonl", "r", encoding="utf-8") as infile, open("..\\..\\..\\input\\data.json", "w", encoding="utf-8") as outfile:
    outfile.write("[\n")
    first = True
    for line in infile:
        if not first:
            outfile.write(",\n")
        outfile.write(line.strip())
        first = False
    outfile.write("\n]")
