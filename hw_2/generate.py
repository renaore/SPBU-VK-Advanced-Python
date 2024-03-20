from latex import generate_table, generate_tex

if __name__ == "__main__":
    data = [["aloha","cat"],[4444, 666666, "aaaaaa"],["hmm suspicious"]]
    table_tex = generate_tex(generate_table(data))
    with open("example_table.tex", "w") as f:
        f.write(table_tex)