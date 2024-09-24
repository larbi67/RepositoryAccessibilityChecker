# Version: 1.0
# Author: Larbi OUIYZME
# License: MIT

import requests

# Function to check if a repository is accessible
def check_repo_accessibility(repo_url):
    response = requests.get(repo_url)
    
    # If the repository returns a 404, it's either private or doesn't exist
    if response.status_code == 404:
        print(f"[PRIVATE or NON-EXISTENT] The repository {repo_url} is not accessible (404).")
    # If the repository returns a 200, it's public
    elif response.status_code == 200:
        print(f"[PUBLIC] The repository {repo_url} is public.")
    # For any other response code, print the error
    else:
        print(f"[ERROR] Unable to check {repo_url}. Response code: {response.status_code}")

# Load repository URLs from the repos.txt file
def load_repos_from_file(filename):
    with open(filename, 'r') as file:
        # Read each line and strip any extra whitespace or newline characters
        repos = [line.strip() for line in file if line.strip()]
    return repos

# Load the URLs from the 'repos.txt' file
repo_file = 'repos.txt'
repos = load_repos_from_file(repo_file)

# Check the accessibility of each repository
for repo_url in repos:
    check_repo_accessibility(repo_url)
