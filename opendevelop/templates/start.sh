#! bin/bash

{% for command in commands %}
{{ command }} &&
{% endfor %}
{{ last_cmd }}
