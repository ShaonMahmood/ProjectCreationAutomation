import sys, subprocess
import os,time
from github import Github

def create_git_repo(projectName,username, password):
    user = Github(username, password).get_user()
    repo = user.create_repo(projectName)
    print("Succesfully created repository {}".format(project_name))


present_dirname, present_filename = os.path.split(os.path.abspath(__file__))
root = os.path.dirname(present_dirname)
gitignore_file = os.path.join(root,'.gitignore')

print(f"root is {root}, gitignore file is {gitignore_file}\n")

project_dir_name = 'MyProjects'
project_name = 'NewProject'
remote_url = f'https://github.com/ShaonMahmood/{project_name}.git'
home_dir = os.path.expanduser('~')
project_dir_path = os.path.join(home_dir,project_dir_name,project_name)
username = "" #Insert your github username here
password = "" #Insert your github password here
if not os.path.isdir(project_dir_path):
    create_git_repo(project_name,username,password)
    os.makedirs(project_dir_path)
    os.chdir(project_dir_path)
    subprocess.run('git init',shell=True)
    time.sleep(2)
    subprocess.run('touch README.md', shell=True)
    subprocess.run('python3 -m venv venv', shell=True)
    time.sleep(2)
    copy_command =f'cp {gitignore_file} {project_dir_path}'
    print(f'copy command: {copy_command}')
    subprocess.run(copy_command, shell=True)
    subprocess.run(f'git remote add origin {remote_url}', shell=True)
    subprocess.run('git add .', shell=True)
    subprocess.run('git commit -m "Initial commit"', shell=True)
    subprocess.run('git push -u origin master', shell=True)
    subprocess.run('code .', shell=True)
    time.sleep(2)
    subprocess.run('exit', shell=True)

else:
    print(f'project with the same name was created before')



