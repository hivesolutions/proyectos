#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import appier
import appier_extras

import proyectos

class BaseController(appier.Controller):

    def __init__(self, owner, *args, **kwargs):
        appier.Controller.__init__(self, owner, *args, **kwargs)
        self.api = None

    @appier.route("/<str:repo>/<str:page>.md", "GET")
    @appier.route("/<str:repo>/?", "GET")
    def render(self, repo, page = None):
        buffer = appier.BytesIO()

        _repo = proyectos.Repo.get(name = repo)
        repo_path = _repo.repo_path()
        index_path = _repo.index_path()
        page_path = os.path.join(repo_path, page + ".md") if page else index_path

        parser = appier_extras.MarkdownParser()
        generator = appier_extras.MarkdownHTML(file = buffer)

        file = open(page_path, "rb")
        try: contents = file.read()
        finally: file.close()

        nodes = parser.parse(contents)
        generator = generator.generate(nodes)

        value = buffer.getvalue()
        buffer.close()

        return self.template(
            "markdown.html.tpl",
            title = page or repo,
            contents = value
        )

    @appier.route("/render/<str:repo>/<str:page>.md", "GET")
    @appier.route("/render/<str:repo>/?", "GET")
    def _render(self, repo, page = None):
        return self.render(repo = repo, page = page)
