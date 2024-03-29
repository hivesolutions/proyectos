<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1, minimum-scale=1, maximum-scale=1" />
        {% if description %}
            <meta name="description" content="{{ description }}" />
        {% endif %}
        <title>{{ title }}</title>
        <link rel="stylesheet" type="text/css" href="//libs.bemisc.com/uxf/css/ux-min.css" />
        <link rel="stylesheet" href="{{ url_for('static', filename = 'css/markdown.css') }}" />
        <link rel="shortcut icon" href="{{ url_for('base.favicon', repo = name) }}" />
        <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.min.js"></script>
        <script type="text/javascript" src="//libs.bemisc.com/uxf/js/ux-min.js"></script>
        <script type="text/javascript" src="{{ url_for('static', filename = 'js/markdown.js') }}"></script>
    </head>
    <body class="ux wait-load side-color flat {{ theme|default('', True) }}">
        <div class="wrapper">
            {% if github %}
                <a href="{{ github }}">
                    <img class="github-fork" src="//github.blog/wp-content/uploads/2008/12/forkme_right_darkblue_121621.png?resize=298%2C298"
                         alt="Fork me on GitHub" />
                </a>
            {% endif %}
            <span class="toggler icon"></span>
            <div class="contents">{{ contents|safe }}</div>
            <div class="footer">
                <div class="product">{{ title[0] }}</div>
                <div class="slogan">Proudly built by <a href="http://hive.pt">Hive Solutions</a></div>
            </div>
        </div>
        {% include "analytics.html.tpl" %}
    </body>
</html>
