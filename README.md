# Ansible Repo Updater

## Description

This repository contains an Ansible playbook and a Python script for updating repositories in a GitHub organization. The playbook updates the versions of GitHub Actions used in the repositories and the Python script generates a CSV file with the list of repositories in the organization.

## Getting Started

### Dependencies

- Ansible
- Python 3
- Python's `github` library

### Installing

1. Clone this repository.
2. Install the required Python libraries with pip:

```bash
pip install PyGithub
```

### Configuration

1. Rename `env.yml.example` to `env.yml`.
2. Fill in the following variables in `env.yml`:

- `github_org_name`: The name of your GitHub organization.
- `github_access_token`: Your GitHub access token. This is required for accessing private repositories.
- `github_username`: Your GitHub username.
- `dest_folder`: The path to the destination folder where the cloned repositories will be downloaded.
- `branch`: The name of the branch to be created in each repository.
- `commit_msg`: The commit message for the changes.

### Executing program

Run the Ansible playbook with the following command:

```bash
ansible-playbook update_repos_csv.yml
```

## Help

If you encounter any issues, please open an issue on this GitHub repository.

## Authors

Matt Zonos
[@MattZonos](https://github.com/matt-zonos)

## Version History

- 0.1
  - Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details
\`\`\`
