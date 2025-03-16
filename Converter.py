import subprocess
import os

# Caminho do arquivo de entrada e saída
input_file = "Exemplo.ipynb"
output_file = "Exemplo.html"

# Comando para converter o notebook para HTML usando o template customizado
command = [
    "python", "-m", "jupyter", "nbconvert", input_file, "--to", "html",
    "--template", "custom.tpl"
]

# Executar o comando
process = subprocess.run(command, capture_output=True, text=True)

# Exibir saída do processo
print("STDOUT:", process.stdout)
print("STDERR:", process.stderr)
