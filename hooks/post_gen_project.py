import shutil

{% if not cookiecutter.use_robot %}
shutil.rmtree("robot")
{% endif %}
