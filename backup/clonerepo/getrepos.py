import requests
import subprocess
import os


github_user = 'user_github'

url = f'https://api.github.com/users/{github_user}/repos'

response = requests.get(url)

if response.status_code == 200:
    repos = response.json()
    clone_dir = " Local aonde os repositorios serao clonados path dir"
    os.makedirs(clone_dir, exist_ok=True)

    for repo in repos:
        repo_full_name = repo["full_name"]
        repo_url = f"git@github.com:{repo_full_name}.git"
        clone_path = os.path.join(clone_dir, repo_full_name.split('/')[-1])
        print(f"Cloning {repo_url} into {clone_path}")

        subprocess.run(['git', 'clone', repo_url, clone_path])


    print("Cloning completed.")
else:
    print(f"Erro ao acessar a API do GitHub: {response.status_code}")




