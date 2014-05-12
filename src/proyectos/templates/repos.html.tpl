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
    <div class="quote">
        We're only showing your public repositories below, you can find your private projects on GitHub.<br/>
        Enable your projects below by flicking the switch.
    </div>
    <ul class="repos">
        {% for repo in repos %}
            <li>
                <a href="{{ repo.html_url }}">{{ repo.full_name }}</a>
                <input class="float-right" type="checkbox" name="{{ repo.full_name}}" checked="1" />
                <div class="clear"></div>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
