#! bin/bash

cd /var/opendevelop/bucket/data 
{% for command in commands %}
{{ command|safe }} &&
{% endfor %}
{{ last_cmd }}
