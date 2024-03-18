import hw_latex as lt
import os


def generate_pdf(latex_code: str) -> None:
    with open("table_image.tex", "w") as f:
        f.write(latex_code)

    os.system("pdflatex table_image.tex")
    os.remove("table_image.log")
    os.remove("table_image.aux")
    os.remove("table_image.tex")


if __name__ == "__main__":
    data = input() # '[["somebody", 0, "nce"],["told"],["me","the world","is","wonderful"]]'
    image_path = input() # 'lead.png'

    latex_code = lt.generate_tex(lt.generate_table(data), lt.generate_image(image_path))
    generate_pdf(latex_code)


