#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

from proyectos import scheduler

class ProyectosApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "proyectos",
            parts = (
                appier_extras.AdminPart,
            ),
            *args, **kwargs
        )
        self.scheduler = scheduler.Scheduler(self)

    def start(self):
        appier.WebApp.start(self)
        self.scheduler.start()

    def _version(self):
        return "0.1.1"

    def _description(self):
        return "Proyectos"

    def _observations(self):
        return "Project page generation from GitHub repository"

if __name__ == "__main__":
    app = ProyectosApp()
    app.serve()
else:
    __path__ = []
