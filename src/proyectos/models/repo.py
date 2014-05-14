#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess

import appier
import appier_extras

class Repo(appier_extras.admin.Base):

    name = appier.field(
        index = True,
        immutable = True
    )

    full_name = appier.field(
        index = True,
        immutable = True
    )

    html_url = appier.field(
        immutable = True,
        meta = "url"
    )

    clone_url = appier.field(
        immutable = True,
        meta = "url"
    )

    status = appier.field(
        type = bool,
        index = True,
        meta = "enum",
        enum = appier_extras.admin.Base.ENABLE_S
    )

    @classmethod
    def validate(cls):
        return super(Repo, cls).validate() + [
            appier.not_null("name"),
            appier.not_empty("name"),

            appier.not_null("full_name"),
            appier.not_empty("full_name"),

            appier.not_null("html_url"),
            appier.not_empty("html_url"),

            appier.not_null("clone_url"),
            appier.not_empty("clone_url"),

            appier.not_null("status")
        ]

    @classmethod
    def list_names(cls):
        return ["full_name", "status"]

    def enable_s(self):
        self.status = True
        self.save()

    def disable_s(self):
        self.status = False
        self.save()

    def update(self, force = False):
        if not self.status and not force: return

        repo_path = self.repo_path()

        is_new = not os.path.exists(repo_path)
        if is_new: os.makedirs(repo_path)

        if is_new: self.logger.debug(
            "Cloning '%s' into '%s' ..." %\
            (self.full_name, repo_path)
        )
        else: self.logger.debug(
            "Git pulling '%s' into '%s' ..." %\
            (self.full_name, repo_path)
        )

        if is_new: subprocess.call(["git", "clone", self.clone_url, repo_path])
        else: subprocess.call(["git", "-C", repo_path, "pull"])

    def repo_path(self):
        repos_path = appier.conf("REPOS_PATH", "repos")
        repos_path = os.path.abspath(repos_path)
        return os.path.join(repos_path, self.name)

    def index_path(self):
        repo_path = self.repo_path()

        lower_path = os.path.join(repo_path, "readme.md")
        if os.path.exists(lower_path): return lower_path

        upper_path = os.path.join(repo_path, "README.md")
        if os.path.exists(upper_path): return upper_path

        raise appier.OperationalError(message = "No index path found")
