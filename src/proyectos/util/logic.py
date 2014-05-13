#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import github

import proyectos

def get_api():
    api = github.Api(
        username = appier.conf("GITHUB_USERNAME"),
        password = appier.conf("GITHUB_PASSWORD")
    )
    return api

def all_repos(ensure = True):
    api = get_api()
    all_repos = api.self_repos()
    self_orgs = api.self_orgs()
    for org in self_orgs:
        org_repos = api.repos_org(org["login"])
        all_repos.extend(org_repos)
    if ensure: return ensure_repos(all_repos)
    return all_repos

def ensure_repos(repos):
    _repos = []
    for repo in repos:
        _repo = ensure_repo(repo)
        _repos.append(_repo)
    return _repos

def ensure_repo(repo):
    _repo = proyectos.Repo.get(
        full_name = repo["full_name"],
        raise_e = False
    )
    if _repo: return _repo
    _repo = proyectos.Repo(
        name = repo["name"],
        full_name = repo["full_name"],
        status = False
    )
    _repo.save()
    return _repo
