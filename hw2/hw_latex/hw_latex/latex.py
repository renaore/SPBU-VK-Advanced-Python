import json
from PIL import Image

def align_data(data: list):
    num_cols = max(len(row) for row in data)

    return [row + [''] * (num_cols - len(row)) for row in data]


def create_table_code(data: list):
    num_cols = len(data[0])

    # table_code = '\documentclass{article} \n' + '\\begin{document} \n'
    table_code = '\Large \n'
    table_code += r'\begin{tabular}{|' + '|'.join(['l'] * num_cols) + '|}\n'
    table_code += '\hline \n'


    for row in data:
        table_code += ' & '.join(map(str,row)) + r'\\' + '\n'
        table_code += '\hline \n'

    table_code += '\end{tabular}'
    # table_code += '\end{document}'

    return table_code


def generate_tex(*args):
    code = '\documentclass{article} \n' + '\\usepackage{graphicx} \n' + '\\begin{document} \n'
    for arg in args:
        code += arg + '\n'
    code += '\end{document}'
    return code

def generate_table(data: list):
    data = json.loads(data)
    data = align_data(data)
    table_code = create_table_code(data)

    return table_code


def generate_image(image_path, max_width=300):
    with Image.open(image_path) as img:
        width, height = img.size
    scale_factor = min(1.0, max_width / float(width))

    return '\\begin{figure}[h] \n' + f"\\includegraphics[scale={scale_factor}]{{{image_path}}} \n" + '\\end{figure}'


if __name__ == "__main__":
    data = input()
    # table_tex = generate_table(data)
    # print(table_tex)

    image_path = input()
    # image_tex = generate_image(image_path)
    # with open("imble.tex", "w") as f:
    #     f.write(table_tex)
    #     f.write(image_tex)

    print(generate_tex(generate_table(data), generate_image(image_path)))