#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import appier
import appier_extras

import proyectos

class BaseController(appier.Controller):

    @appier.route("/render/<str:repo>/<regex('[\:\.\/\s\w-]+'):page>.md", "GET")
    @appier.route("/render/<str:repo>/?", "GET")
    def render(self, repo, page = None):
        if page: title = "%s / %s" % (repo, page.split("/")[-1])
        else: title = repo

        buffer = appier.StringIO()

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
            title = title,
            contents = value
        )

    @appier.route("/render/<str:repo>/<regex('[\:\.\/\s\w-]+'):reference>", "GET")
    def resource(self, repo, reference):
        buffer = appier.StringIO()

        _repo = proyectos.Repo.get(name = repo)
        repo_path = _repo.repo_path()
        resource_path = os.path.join(repo_path, reference)

        file = open(resource_path, "rb")
        try: contents = file.read()
        finally: file.close()

        return contents
