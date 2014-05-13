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

    html_url = appier.field(
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
