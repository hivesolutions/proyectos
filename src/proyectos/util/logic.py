#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import github

import proyectos

def get_api():
    api = github.API(
        username = appier.conf("GITHUB_USERNAME"),
        password = appier.conf("GITHUB_PASSWORD")
    )
    return api

def update_repos(full = True):
    if full: repos = proyectos.Repo.find()
    else: repos = proyectos.Repo.find(status = True)
    for repo in repos: repo.update()

def sync_repos(api = None, ensure = True):
    api = api or get_api()
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
        html_url = repo["html_url"],
        clone_url = repo["clone_url"],
        ssh_url = repo["ssh_url"],
        status = False
    )
    _repo.save()
    return _repo
