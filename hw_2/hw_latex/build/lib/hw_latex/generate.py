# посмотреть в записи лекции 2 как импорты организованы
from latex import generate_table, generate_image, generate_tex

data = input()
table_tex = generate_tex(generate_table(data))
with open("example_table.tex", "w") as f:
    f.write(table_tex)

image_path = input()
image_tex = generate_tex(generate_image(image_path))

with open("table_with_image.tex", "w") as f:
    f.write(generate_tex(generate_table(data), generate_image(image_path)))
