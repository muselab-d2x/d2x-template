import os
import shutil

{% if cookiecutter.project_type == "Unpackaged" %}
os.remove(".github/workflows/beta.yml")
{% endif %}
