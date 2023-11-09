import subprocess

# Substitua espaços e caracteres especiais por underscores
repo_url = 'https://github.com/seu-repo-git'
local_path = "seu-repo-local"

# Comando Git para clonar o repositório
command = f'git clone {repo_url} "{local_path}"'

# Execute o comando usando o subprocesso
subprocess.run(command, shell=True)
