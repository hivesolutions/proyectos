<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>TEst</title>
        <link rel="stylesheet" type="text/css" href="//libs.bemisc.com/uxf/css/ux-min.css" />
        <link rel="stylesheet" href="{{ url_for('static', filename = 'css/layout.css') }}" media="all" />
        <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
        <script type="text/javascript" src="//libs.bemisc.com/uxf/js/ux-min.js"></script>
    </head>
    <body class="ux">
        <div class="contents">{{ contents|safe }}</div>
        <div class="footer">
            <div class="product">n</div>
            <div class="slogan">proudly built by <a href="http://hive.pt">Hive Solutions</a></div>
        </div>
    </body>
</html>
