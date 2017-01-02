# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.utils.safestring import mark_safe

import re

register = template.Library()


@register.filter
def normalize_checkbox(l):
    try:
        expression = 'name="(\w+)".*value="(\w+)"'
        m = re.search(expression, l)
        name = m.group(1)
        value = m.group(2)
        id = '{}_{}'.format(name, value)[1:]
        return mark_safe(
            '<div class="selection"><input type="checkbox" name="{}" id="{}" value="{}"/><label for="{}"></label></div>'.format(
                name,
                id,
                value,
                id
            )
        )
    except:
        return ''
