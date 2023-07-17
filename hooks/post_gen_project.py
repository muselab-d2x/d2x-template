import os
import shutil

{% if cookiecutter.use_robot == "n" %}
shutil.rmtree("robot")
{% endif %}

{% if cookiecutter.project_type == "Unpackaged" %}
os.remove(".github/workflows/beta.yml")
{% endif %}