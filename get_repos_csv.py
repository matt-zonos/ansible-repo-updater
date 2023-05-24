import os
import csv
from github import Github

def get_org_repos(org_name, access_token):
    g = Github(access_token)
    org = g.get_organization(org_name)
    repos = org.get_repos()
    repo_list = []
    ignored_repos = ["JenkinsManagedAPIs", "JenkinsSharedLibrary"]
    
    for repo in repos:
        if repo.name in ignored_repos or repo.archived:
            continue  # Skip the current repo if it's in the ignored_repos list or archived

        permission = 'write' if repo.permissions.push else 'read'
        repo_list.append({
            'repo_name': repo.name,
            'ssh_url': repo.ssh_url,
            'permission': permission,
            'default_branch': repo.default_branch,
            'repo_url': repo.html_url
        })
    return repo_list

if __name__ == "__main__":
    org_name = os.environ["GITHUB_ORG_NAME"]
    access_token = os.environ["GITHUB_ACCESS_TOKEN"]
    repos = get_org_repos(org_name, access_token)
    
    with open("repo_list.csv", "w", newline='') as csvfile:
        fieldnames = ['repo_name', 'ssh_url', 'permission', 'default_branch', 'repo_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for repo in repos:
            writer.writerow(repo)
