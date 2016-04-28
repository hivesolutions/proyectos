#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import proyectos

class RepoController(appier.Controller):

    @appier.route("/repos", "GET")
    @appier.ensure(token = "admin")
    def list(self):
        repos = proyectos.Repo.find(sort = [("full_name", 1),])
        return self.template(
            "repo/list.html.tpl",
            link = "repos",
            repos = repos
        )

    @appier.route("/repos/<int:id>/enable", "GET")
    @appier.ensure(token = "admin")
    def enable(self, id):
        repo = proyectos.Repo.get(id = id)
        repo.enable_s()
        return self.redirect(
            self.url_for("repo.list")
        )

    @appier.route("/repos/<int:id>/disable", "GET")
    @appier.ensure(token = "admin")
    def disable(self, id):
        repo = proyectos.Repo.get(id = id)
        repo.disable_s()
        return self.redirect(
            self.url_for("repo.list")
        )
