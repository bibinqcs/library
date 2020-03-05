from __future__ import unicode_literals
from frappe import _

def get_data():
        return [
		{
                        "label": _("Library"),
                        "icon": "fa fa-star",
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Books",
                                        "description": _("Books"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Books Transaction",
                                        "description": _("Books Transaction"),
                                },

                        ]
                },
        	]


