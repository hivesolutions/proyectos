{% extends "partials/layout.static.html.tpl" %}
{% block title %}repos{% endblock %}
{% block name %}Repos{% endblock %}

{% block head %}
	{{ super() }}
	<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename = 'css/layout.css') }}" />
{% endblock %}


{% block links %}
    <a class="selected" href="#">repos</a>
{% endblock %}


{% block content %}
    <ul class="repos">
    	{% for repo in repos %}
	        <li>
	        	{{ repo.full_name }}
	        </li>
	    {% endfor %}
    </ul>
{% endblock %}
