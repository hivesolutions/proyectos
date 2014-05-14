#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import github
import proyectos

LOOP_TIMEOUT = 1800.0
""" The time value to be used to sleep the main sequence
loop between ticks, this value should not be too small
to spend many resources or to high to create a long set
of time between external interactions """

class Scheduler(appier.Scheduler):

    def __init__(self, *args, **kwargs):
        appier.Scheduler.__init__(
            self,
            timeout = LOOP_TIMEOUT,
            *args,
            **kwargs
        )

    def tick(self):
        appier.Scheduler.tick(self)
        self.check_repos()
        self.update_repos()

    def load(self):
        self.load_github()

    def load_github(self):
        self.github = github.Api(
            username = appier.conf("GITHUB_USERNAME"),
            password = appier.conf("GITHUB_PASSWORD")
        )

    def check_repos(self):
        self.logger.debug("Checking github repos ...")
        proyectos.sync_repos(api = self.github, ensure = True)

    def update_repos(self):
        self.logger.debug("Updating github repos ...")
        proyectos.update_repos()
