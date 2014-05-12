#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

import proyectos

class BaseController(appier.Controller):

    def __init__(self, owner, *args, **kwargs):
        appier.Controller.__init__(self, owner, *args, **kwargs)
        self.api = None

    @appier.route("/repos", "GET")
    def repos(self):
        return self.template(
            "repos.html.tpl"
        )

    @appier.route("/repos.json", "GET", json = True)
    def repos_json(self):
        projects = proyectos.all_projects()
        return projects

    @appier.route("/<str:page>.md", "GET")
    def render(self, page):
        buffer = appier.BytesIO()

        parser = appier_extras.MarkdownParser()
        generator = appier_extras.MarkdownHTML(file = buffer)

        file = open("c:/users/joamag/desktop/readme.md", "rb")
        try: contents = file.read()
        finally: file.close()

        nodes = parser.parse(contents)
        generator = generator.generate(nodes)

        value = buffer.getvalue()
        buffer.close()

        return self.template(
            "markdown.html.tpl",
            title = page,
            contents = value
        )
