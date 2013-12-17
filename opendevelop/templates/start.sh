#! bin/bash

{% for command in commands %}
    {{ command }}
	EXITCODE=$?
	if [ $EXITCODE -gt 0]; then
		exit $EXITCODE;
	fi
{% endfor %}
{{ last_cmd }}
