import sys, subprocess, platform
import os,time
from github import Github

def create_git_repo(projectName,username, password):
    try:
        user = Github(username, password).get_user()
    except Exception as e:
        print("Username and password wrong")
        return False
    repo = user.create_repo(projectName)
    print("Succesfully created repository {}".format(projectName))
    return True

def create_project(username, password, project_directory="MyProjects", project_name="NewProject", venv_name=""):
    present_dirname, present_filename = os.path.split(os.path.abspath(__file__))
    root = os.path.dirname(present_dirname)
    gitignore_file = os.path.join(root, '.gitignore')

    print(f"root is {root}, gitignore file is {gitignore_file}\n")

    remote_url = f'https://github.com/ShaonMahmood/{project_name}.git'
    home_dir = os.path.expanduser('~')
    project_dir_path = os.path.join(home_dir, project_directory, project_name)
    if not os.path.isdir(project_dir_path):
        if create_git_repo(project_name, username, password):
            pass
        else:
            return 0
        os.makedirs(project_dir_path)
        os.chdir(project_dir_path)
        subprocess.run('git init', shell=True)
        time.sleep(2)
        python_venv_version = ""
        readme_command = ''
        copy_command = ''

        if platform.system() == "Windows":
            readme_command = 'type nul > README.md'
            copy_command = f'copy {gitignore_file} {project_dir_path}'
            python_venv_version = "python"
            
        else:
            readme_command = 'touch README.md'
            copy_command = f'cp {gitignore_file} {project_dir_path}'
            python_venv_version = "python3"

        subprocess.run(readme_command, shell=True)
        subprocess.run(f'{python_venv_version} -m venv {venv_name}_venv', shell=True)
        time.sleep(2)
        # copy_command = f'cp {gitignore_file} {project_dir_path}'
        print(f'copy command: {copy_command}')
        subprocess.run(copy_command, shell=True)
        subprocess.run(f'git remote add origin {remote_url}', shell=True)
        subprocess.run('git add .', shell=True)
        subprocess.run('git commit -m "Initial commit"', shell=True)
        subprocess.run('git push -u origin master', shell=True)
        subprocess.run('code .', shell=True)
        time.sleep(2)
        subprocess.run('exit', shell=True)
        return 1

    else:
        print(f'project with the same name was created before')
        return 2


