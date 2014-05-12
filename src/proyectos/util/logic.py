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

def all_repos():
    api = get_api()
    all_repos = api.self_repos()
    self_orgs = api.self_orgs()
    for org in self_orgs:
        org_repos = api.repos_org(org["login"])
        all_repos.extend(org_repos)
    return all_repos
