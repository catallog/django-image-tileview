# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.contrib.admin.templatetags.admin_list import result_list

register = template.Library()


@register.inclusion_tag('tileview/change_list_results.html')
def result_list_tiles(cl):
    return result_list(cl)
