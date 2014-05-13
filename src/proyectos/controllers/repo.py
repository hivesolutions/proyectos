#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import proyectos

class RepoController(appier.Controller):

    def __init__(self, owner, *args, **kwargs):
        appier.Controller.__init__(self, owner, *args, **kwargs)
        self.api = None

    @appier.route("/repos", "GET")
    def list(self):
        repos = proyectos.Repo.find(sort = (("full_name", -1),))
        return self.template(
            "repo/list.html.tpl",
            repos = repos
        )

    @appier.route("/repos/<int:id>/enable", "GET")
    def enable(self, id):
        repo = proyectos.Repo.get(id = id)
        repo.enable_s()
        return self.redirect(
            self.url_for("repo.list")
        )

    @appier.route("/repos/<int:id>/disable", "GET")
    def disable(self, id):
        repo = proyectos.Repo.get(id = id)
        repo.disable_s()
        return self.redirect(
            self.url_for("repo.list")
        )
