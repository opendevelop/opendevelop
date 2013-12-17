#! bin/bash

cd data
{% for command in commands %}
{{ command|safe }} &&
{% endfor %}
{{ last_cmd }}
