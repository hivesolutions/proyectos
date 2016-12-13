#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import appier
import appier_extras

import proyectos

class BaseController(appier.Controller):

    @appier.route("/render/<str:repo>", "GET")
    def render_base(self, repo):
        return self.redirect(
            self.url_for("base.render", repo = repo)
        )

    @appier.route("/render/<str:repo>/", "GET")
    @appier.route("/render/<str:repo>/<regex('[\:\.\/\s\w-]+'):page>.md", "GET")
    def render(self, repo, page = None):
        theme = appier.conf("THEME", None)
        theme = self.get_field("theme", theme)

        buffer = appier.legacy.StringIO()

        repos = (repo, repo.replace("_", "-"), repo.replace("-", "_"))
        _repo = None

        for repo in repos:
            _repo = proyectos.Repo.get(
                name = repo,
                enabled = True,
                raise_e = False
            )
            if _repo: break

        name = _repo.name
        description = _repo.description
        github = None if page else _repo.html_url
        ga = _repo.ga or appier.conf("GA")
        repo_path = _repo.repo_path()
        index_path = _repo.index_path()
        page_path = os.path.join(repo_path, page + ".md") if page else index_path

        if page: title = "%s / %s" % (_repo.repr(), page.split("/")[-1])
        else: title = _repo.repr()

        if not os.path.exists(page_path): raise appier.NotFoundError(
            message = "Page '%s' not found in repository" % page_path,
            code = 404
        )

        parser = appier_extras.MarkdownParser()
        generator = appier_extras.MarkdownHTML(file = buffer, encoding = None)

        file = open(page_path, "rb")
        try: contents = file.read()
        finally: file.close()

        nodes = parser.parse(contents)
        generator.generate(nodes)

        value = buffer.getvalue()
        buffer.close()

        return self.template(
            "markdown.html.tpl",
            theme = theme,
            name = name,
            title = title,
            description = description,
            contents = value,
            github = github,
            ga = ga
        )

    @appier.route("/render/<str:repo>/favicon.ico", "GET")
    def favicon(self, repo):
        _repo = proyectos.Repo.get(
            fields = ("favicon",),
            rules = False,
            name = repo
        )
        favicon = _repo.favicon
        if not favicon: return self.send_static("images/favicon.ico")
        else: return self.send_file(
            favicon.data,
            content_type = favicon.mime,
            etag = favicon.etag
        )

    @appier.route("/render/<str:repo>/<regex('[\:\.\/\s\w-]+'):reference>", "GET")
    def resource(self, repo, reference):
        _repo = proyectos.Repo.get(name = repo)
        repo_path = _repo.repo_path()
        resource_path = os.path.join(repo_path, reference)
        return self.send_path(resource_path, url_path = reference)
