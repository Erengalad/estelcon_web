# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response

def statichtml(request, html_id='index'):
    return render_to_response('static_pages/' + html_id + '.html')

