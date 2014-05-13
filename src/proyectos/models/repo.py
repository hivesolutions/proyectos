#!/usr/bin/python
# -*- coding: utf-8 -*-

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

    status = appier.field(
        type = bool,
        index = True
    )

    @classmethod
    def validate(cls):
        return super(Repo, cls).validate() + [
            appier.not_null("name"),
            appier.not_empty("name"),

            appier.not_null("full_name"),
            appier.not_empty("full_name"),

            appier.not_null("status")
        ]

    @classmethod
    def list_names(cls):
        return ["full_name", "status"]
