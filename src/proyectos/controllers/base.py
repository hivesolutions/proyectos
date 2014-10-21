#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import mimetypes

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

        if not os.path.exists(page_path): raise appier.NotFoundError(
            message = "Page '%s' not found in repository" % page_path,
            code = 404
        )

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
        _repo = proyectos.Repo.get(name = repo)
        repo_path = _repo.repo_path()
        resource_path = os.path.join(repo_path, reference)

        if not os.path.exists(resource_path): raise appier.NotFoundError(
            message = "Resource '%s' not found in repository" % reference,
            code = 404
        )

        type, _encoding = mimetypes.guess_type(
            resource_path, strict = True
        )
        self.request.set_content_type(type)

        size = os.path.getsize(resource_path)
        yield size

        file = open(resource_path, "rb")
        try:
            while True:
                contents = file.read(4096)
                if not contents: break
                yield contents
        finally:
            file.close()
