#! bin/bash

{% for command in commands %}
{{ command|safe }} &&
{% endfor %}
{{ last_cmd }}
