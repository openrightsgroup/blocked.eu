
import logging
import psycopg2
import jinja2

from flask import Blueprint, render_template, redirect, request, \
    g, url_for, abort, config, current_app, session, Response

from utils import *

cms_pages = Blueprint('cms', __name__,
    template_folder='templates')


@cms_pages.route('/')
@cms_pages.route('/legal-blocks')
@cms_pages.route('/legal-blocks/<region>')
@cms_pages.route('/legal-blocks/<int:page>')
@cms_pages.route('/legal-blocks/<region>/<int:page>')
def legal_blocks(region='eu', page=1):
    data = request.api.recent_blocks(page-1, region)
    blocks = data['results']
    count = data['count']
    urlcount = data['urlcount']
    return render_template('legal-blocks.html',
            page=page, count=count, blocks=blocks, urlcount=urlcount,
            pagecount = get_pagecount(count, 25)
            )


@cms_pages.route('/legal-blocks/export')
def export_blocks():
    pass
