import os
import subprocess

repos_file = 'repos.txt'

clone_dir = 'cloned_repos'

os.makedirs(clone_dir, exist_ok=True)

with open(repos_file, 'r') as file:
    repos = file.readlines()

repos = [repo.strip() for repo in repos]

for repo in repos:
    repo_url = f"git@github.com:{repo}.git"
    clone_path = os.path.join(clone_dir, repo.split('/')[-1])
    print(f"Cloning {repo_url} into {clone_path}")
    
    subprocess.run(['git', 'clone', repo_url, clone_path])

print("Cloning completed.")
