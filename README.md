# Twin LLM Project by IIT J Students

# Setup Steps

manoj@MSI:~/projects/TwinLLMbyIITJ$ pyenv local 3.11.8
manoj@MSI:~/projects/TwinLLMbyIITJ$ poetry init

This command will guide you through creating your pyproject.toml config.

Package name [twinllmbyiitj]:  
Version [0.1.0]:  
Description []:  LLM Engineers Handbook learning replication
Author [None, n to skip]:  IIT Jodhpur Students    
License []:  MIT License 
Compatible Python versions [>=3.11]:  

Would you like to define your main dependencies interactively? (yes/no) [yes] yes
        You can specify a package in the following forms:
          - A single name (requests): this will search for matches on PyPI
          - A name and a constraint (requests@^2.23.0)
          - A git url (git+https://github.com/python-poetry/poetry.git)
          - A git url with a revision         (git+https://github.com/python-poetry/poetry.git#develop)
          - A file path (../my-package/my-package.whl)
          - A directory (../my-package/)
          - A url (https://example.com/packages/my-package-0.1.0.tar.gz)
        
Package to add or search for (leave blank to skip): pandas
Found 104 packages matching pandas
Showing the first 10 matches

Enter package # to add, or the complete package name if it is not listed []:
 [ 0] pandas
 [ 1] 
 > 0
Enter the version constraint to require (or leave blank to use the latest version): 
Using version ^2.2.3 for pandas

Add a package (leave blank to skip): 

Would you like to define your development dependencies interactively? (yes/no) [yes] 
Package to add or search for (leave blank to skip): 

Generated file

[project]
name = "twinllmbyiitj"
version = "0.1.0"
description = "LLM Engineers Handbook learning replication"
authors = [
    {name = "IIT Jodhpur Students"}
]
license = {text = "MIT License"}
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "pandas (>=2.2.3,<3.0.0)"
]


[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] yes
manoj@MSI:~/projects/TwinLLMbyIITJ$ poetry install
Creating virtualenv twinllmbyiitj-GVDLSPbW-py3.11 in /home/manoj/.cache/pypoetry/virtualenvs
Updating dependencies
Resolving dependencies... (0.4s)

Package operations: 6 installs, 0 updates, 0 removals

  - Installing six (1.17.0)
  - Installing numpy (2.2.3)
  - Installing python-dateutil (2.9.0.post0)
  - Installing pytz (2025.1)
  - Installing tzdata (2025.1)
  - Installing pandas (2.2.3)

Writing lock file

Installing the current project: twinllmbyiitj (0.1.0)
Error: The current project could not be installed: Readme path `/home/manoj/projects/TwinLLMbyIITJ/README.md` does not exist.
If you do not want to install the current project use --no-root.
If you want to use Poetry only for dependency management but not for packaging, you can disable package mode by setting package-mode = false in your pyproject.toml file.
If you did intend to install the current project, you may need to set `packages` in your pyproject.toml file.

manoj@MSI:~/projects/TwinLLMbyIITJ$ poetry install
Installing dependencies from lock file

No dependencies to install or update

Installing the current project: twinllmbyiitj (0.1.0)
Error: The current project could not be installed: No file/folder found for package twinllmbyiitj
If you do not want to install the current project use --no-root.
If you want to use Poetry only for dependency management but not for packaging, you can disable package mode by setting package-mode = false in your pyproject.toml file.
If you did intend to install the current project, you may need to set `packages` in your pyproject.toml file.

manoj@MSI:~/projects/TwinLLMbyIITJ$ poetry install 
Installing dependencies from lock file

No dependencies to install or update

Installing the current project: twinllmbyiitj (0.1.0)
manoj@MSI:~/projects/TwinLLMbyIITJ$ git init
Reinitialized existing Git repository in /home/manoj/projects/TwinLLMbyIITJ/.git/
manoj@MSI:~/projects/TwinLLMbyIITJ$ git add .
manoj@MSI:~/projects/TwinLLMbyIITJ$ git commit -m "initial commit"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: empty ident name (for <manoj@MSI.>) not allowed
manoj@MSI:~/projects/TwinLLMbyIITJ$ git config --global user.name "ManojKumarTiwari"
git config --global user.email "manojtiwari1.1v@gmail.com"
manoj@MSI:~/projects/TwinLLMbyIITJ$ git commit -m "initial commit"
[main (root-commit) 9431ddc] initial commit
 5 files changed, 229 insertions(+)
 create mode 100644 .python-version
 create mode 100644 README.md
 create mode 100644 poetry.lock
 create mode 100644 pyproject.toml
 create mode 100644 twinllmbyiitj/__init__.py
manoj@MSI:~/projects/TwinLLMbyIITJ$ git branch -M main
manoj@MSI:~/projects/TwinLLMbyIITJ$ git remote add origin https://github.com/ManojKumarTiwari/TwinLLMbyIITJ.git
error: remote origin already exists.
manoj@MSI:~/projects/TwinLLMbyIITJ$ git push -u origin main
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 28 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (8/8), 6.95 KiB | 6.95 MiB/s, done.
Total 8 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/ManojKumarTiwari/TwinLLMbyIITJ.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
manoj@MSI:~/projects/TwinLLMbyIITJ$ 