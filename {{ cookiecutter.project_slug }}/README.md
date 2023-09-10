# {{ cookiecutter.project_name }}
Enter a description for your project

# Project Setup
This project is preconfigured with D2X for a comprehensive Development-to-Delivery Experience including CI/CD using GitHub Actions and development environments using GitHub Codespaces.

D2X requires some minimal configuration of your GitHub organization or repository to complete the setup and enable builds:
* [Configure Secrets](https://d2x.readthedocs.io/en/latest/tutorial/#secrets)
* [Develop Your First Change](https://d2x.readthedocs.io/en/latest/tutorial/#develop)
* [Merge Your First Change](https://d2x.readthedocs.io/en/latest/tutorial/#merge)
* [Release Your First Change](https://d2x.readthedocs.io/en/latest/tutorial/#release)

You can check the status of your setup by monitoring the status of the following GitHub Actions workflows:
* [![{% if cookiecutter.project_type != "Unpackaged" %}2GP {% endif %}Feature Test]({{ cookiecutter.repo_url }}/actions/workflows/feature.yml/badge.svg)]({{ cookiecutter.repo_url }}/actions/workflows/feature.yml)
{% if cookiecutter.project_type != "Unpackaged" %}* [![Beta Test]({{ cookiecutter.repo_url }}/actions/workflows/beta.yml/badge.svg)]({{ cookiecutter.repo_url }}/actions/workflows/beta.yml)
* [![Production Release]({{ cookiecutter.repo_url }}/actions/workflows/release.yml/badge.svg)]({{ cookiecutter.repo_url }}/actions/workflows/release.yml){% endif %}
