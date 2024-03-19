FROM python

RUN apt-get update && apt-get install -y --no-install-recommends texlive

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir hw_latex==0.0.10

CMD ["python", "generate_pdf_file.py"]
