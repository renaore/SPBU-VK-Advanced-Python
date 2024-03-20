from PIL import Image


def generate_tex(*args):
    code = '\documentclass{article} \n' + '\\usepackage{graphicx} \n' + '\\begin{document} \n'
    for arg in args:
        code += arg + '\n'
    code += '\end{document}'
    return code


def generate_table(data: list):
    def align_data(data: list):
        num_cols = max(len(row) for row in data)

        return [row + [''] * (num_cols - len(row)) for row in data]

    def create_table_code(data: list):
        num_cols = len(data[0])

        table_code = '\Large \n'
        table_code += r'\begin{tabular}{|' + '|'.join(['l'] * num_cols) + '|}\n'
        table_code += '\hline \n'

        for row in data:
            table_code += ' & '.join(map(str, row)) + r'\\' + '\n'
            table_code += '\hline \n'

        table_code += '\end{tabular}'

        return table_code

    data = align_data(data)
    table_code = create_table_code(data)

    return table_code


def generate_image(image_path, max_width=300):
    with Image.open(image_path) as img:
        width, height = img.size
    scale_factor = min(1.0, max_width / float(width))

    return '\\begin{figure}[h] \n' + f"\\includegraphics[scale={scale_factor}]{{{image_path}}} \n" + '\\end{figure}'

