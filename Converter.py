import subprocess

# Nome do arquivo de entrada e saída
input_file = "slides_python.ipynb"
output_file = "apresentacao_slides.html"

# Comando para converter o notebook para slides em HTML
subprocess.run([
    "python", "-m", "nbconvert", "--to", "slides", input_file, "--output", output_file
])