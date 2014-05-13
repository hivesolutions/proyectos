#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import threading
import traceback

import appier
import github
import proyectos

LOOP_TIMEOUT = 60.0
""" The time value to be used to sleep the main sequence
loop between ticks, this value should not be too small
to spend many resources or to high to create a long set
of time between external interactions """

class Scheduler(threading.Thread):
    """
    Scheduler class that handles all the async tasks
    relates with the house keeping of the proyectos
    infra-structure. The architecture of the logic
    for the class should be modular in the sense that
    new task may be added to it through a queue system.
    """

    def __init__(self, owner):
        threading.Thread.__init__(self)
        self.owner = owner
        self.daemon = True

    def run(self):
        self.running  = True
        self.load()
        while self.running:
            try:
                self.tick()
            except BaseException as exception:
                self.owner.logger.critical("Unhandled proyectos exception raised")
                self.owner.logger.error(exception)
                lines = traceback.format_exc().splitlines()
                for line in lines: self.owner.logger.warning(line)
            time.sleep(LOOP_TIMEOUT)

    def stop(self):
        self.running = False

    def tick(self):
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
        self.owner.logger.debug("Checking github repos ...")
        proyectos.sync_repos(api = self.github, ensure = True)

    def update_repos(self):
        self.owner.logger.debug("Updating github repos ...")
        proyectos.update_repos()
