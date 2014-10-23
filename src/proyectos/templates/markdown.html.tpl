<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, user-scalable=no" />
        {% if description %}
            <meta name="description" content="{{ description }}" />
        {% endif %}
        <title>{{ title }}</title>
        <link rel="stylesheet" type="text/css" href="//libs.bemisc.com/uxf/css/ux-min.css" />
        <link rel="stylesheet" href="{{ url_for('static', filename = 'css/markdown.css') }}" media="all" />
        <link rel="shortcut icon" href="{{ url_for('base.favicon', repo = name) }}" />
        <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
        <script type="text/javascript" src="//libs.bemisc.com/uxf/js/ux-min.js"></script>

    </head>
    <body class="ux">
        {% if github %}
            <a href="{{ github }}">
                <img style="position: fixed; top: 0; right: 0; border: 0;"
                     src="http://s3.amazonaws.com/github/ribbons/forkme_right_gray_6d6d6d.png"
                     alt="Fork me on GitHub">
            </a>
        {% endif %}
        <div class="contents">{{ contents|safe }}</div>
        <div class="footer">
            <div class="product">{{ title[0] }}</div>
            <div class="slogan">proudly built by <a href="http://hive.pt">Hive Solutions</a></div>
        </div>
        {% include "analytics.html.tpl" %}
    </body>
</html>
