import subprocess

# Nome do arquivo de entrada e saída
input_file = "TEC00-PlanoEnsino.ipynb"
output_file = "TEC00-PlanoEnsino.html"

# Comando para converter o notebook para slides em HTML
subprocess.run([
    "python", "-m", "nbconvert", "--to", "slides", input_file, "--output", output_file
])