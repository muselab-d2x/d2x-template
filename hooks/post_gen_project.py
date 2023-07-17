import os
import shutil

{% if not cookiecutter.use_robot %}
shutil.rmtree("robot")
{% endif %}

{% if cookiecutter.project_type == "Unpackaged" %}
os.remove(".github/workflows/beta.yml")
{% endif %}