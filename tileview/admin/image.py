# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _


class ImageTileAdminMixin(ModelAdmin):

    change_list_template = 'tileview/change_list.html'

    class Media:
        css = {
            'all': ('css/tileview.css',)
        }
        js = (
            'js/tileview.js',
        )
