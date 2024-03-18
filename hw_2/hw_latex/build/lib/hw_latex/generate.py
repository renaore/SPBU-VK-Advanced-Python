from latex import generate_table, generate_tex

if __name__ == "__main__":
    data = input()
    table_tex = generate_tex(generate_table(data))
    with open("example_table.tex", "w") as f:
        f.write(table_tex)