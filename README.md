# Repository Accessibility Checker

## Version: 1.0
### Author: Larbi OUIYZME

This Python script allows you to check if a GitHub repository is exposed by automating the verification process. It reads a list of repository URLs from a text file and checks whether each repository is public or private based on the HTTP response code.

### How It Works

- The script uses the `requests` library to send an HTTP GET request to each repository URL.
- If the repository returns a `404` response, it means the repository is either private or doesn't exist.
- If the repository returns a `200` response, it means the repository is public.
- Other response codes are handled to detect potential errors.

# How to Use the Script

## 1. Create a `repos.txt` file

This file should contain one GitHub repository URL per line. Example :

- https://github.com/username/repo1
- https://github.com/username/repo2

## 2. Run the Python script

Once you have the URLs in the `repos.txt` file, run the Python script to check the accessibility of each repository :

python check_repo_accessibility.py

## 3. Requirements
- Python 3.x
- requests library: Install using pip if you don't have it already : pip install requests




