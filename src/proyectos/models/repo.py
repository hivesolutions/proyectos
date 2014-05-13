#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier
import appier_extras

class Repo(appier_extras.admin.Base):

    name = appier.field(
        index = True,
        immutable = True
    )

    status = appier.field(
        type = bool,
        index = True
    )

    @classmethod
    def validate(cls):
        return super(Repo, cls).validate() + [
            appier.not_null("name"),
            appier.not_empty("s_name"),

            appier.not_null("status")
        ]

    @classmethod
    def list_names(cls):
        return ["name", "status"]
