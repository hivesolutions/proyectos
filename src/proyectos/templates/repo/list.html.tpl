{% extends "base.html.tpl" %}
{% block title %}Repos{% endblock %}
{% block name %}Repos{% endblock %}
{% block content %}
    <div class="quote">
        We're showing both your private and public GitHub repositories below.<br/>
        Enable your projects below by flicking the switch.
    </div>
    <ul class="repos">
        {% for repo in repos %}
            <li>
                <a href="{{ repo.html_url }}">{{ repo.full_name }}</a>
                {% if repo.status %}
                    <input class="button button-no-style float-right" type="checkbox" name="{{ repo.full_name }}" checked="1"
                           data-link="{{ url_for('repo.disable', id = repo.id) }}" />
                {% else %}
                    <input class="button button-no-style float-right" type="checkbox" name="{{ repo.full_name }}"
                           data-link="{{ url_for('repo.enable', id = repo.id) }}" />
                {% endif %}
                <div class="clear"></div>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
