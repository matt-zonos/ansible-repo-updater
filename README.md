# Ansible Repo Updater

## Description

This repository contains an Ansible playbook and a Python script for automating the process of updating repositories in a GitHub organization. The Ansible playbook (`update_repos_csv.yml`) performs several operations including cloning repositories with write permissions, creating a new branch, running GitHub Actions updates, committing and pushing changes, and creating pull requests if necessary. The Python script (`get_repos_csv.py`) generates a CSV file with the list of repositories in the organization, excluding certain and archived repositories.

## Getting Started

### Dependencies

- Ansible
- gh api
- Python 3
- Python's `github` library

### Installing

1. Clone this repository.
2. Install the required Python libraries with pip:

```bash
pip install PyGithub
```

### Configuration

Rename `env.yml.example` to `env.yml` and fill in the following variables:

- `github_org_name`: The name of your GitHub organization.
- `github_access_token`: Your GitHub access token. This is required for accessing private repositories.
- `github_username`: Your GitHub username.
- `dest_folder`: The path to the destination folder where the cloned repositories will be downloaded.
- `branch`: The name of the branch to be created in each repository.
- `github_commit_msg`: The commit message for the changes.

### Executing the Program

Run the Ansible playbook with the following command:

```bash
ansible-playbook update_repos_csv.yml
```

### Command Options

- To update the CSV file only:

```bash
ansible-playbook update_repos_csv.yml --tags update_csv
```

  This option executes only the tasks related to generating the CSV file containing the list of repositories and skips the tasks related to updating GitHub Actions in the repositories.

- To skip updating the CSV file:

```bash
ansible-playbook update_repos_csv.yml --skip-tags update_csv
```

  This option skips the tasks related to updating the CSV file but executes the tasks related to updating GitHub Actions in the repositories.

- To skip specific tasks:

```bash
ansible-playbook update_repos_csv.yml --skip-tags update_csv --skip-tags update
```

  This option allows you to skip specific tasks in the playbook. In this example, it skips both the tasks related to updating the CSV file and updating GitHub Actions.

- To perform a dry run without making changes:

```bash
ansible-playbook update_repos_csv.yml --skip-tags update_csv --skip-tags update --check
```

  The `--check` option runs the playbook in check mode, which performs a dry run without making any changes. It allows you to preview the changes that would be made without actually modifying the repositories.

## Help

If you encounter any issues, please open an issue on this GitHub repository.

## Authors

Matt Zonos [@MattZonos](https://github.com/matt-zonos)

## Version History

- 0.1
  - Initial Release
