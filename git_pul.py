import subprocess

# Substitua espaços e caracteres especiais por underscores
repo_url = 'https://github.com/seu-repo-git'
local_path = "seu-repo-local"

# Comando Git para realizar o pull no repositório já clonado
pull_command = ['git', '-C', local_path, 'pull']

# Execute o comando de pull usando o subprocesso
subprocess.run(pull_command)
