#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import github

def get_api():
    api = github.Api(
        username = appier.conf("GITHUB_USERNAME"),
        password = appier.conf("GITHUB_PASSWORD")
    )
    return api

def all_projects():
    api = get_api()
    self_repos = api.self_repos()
    self_orgs = api.self_orgs()
    for org in self_orgs:
        org_repos = api.repos_org(org["login"])
        self_repos.extend(org_repos)
    return self_repos
