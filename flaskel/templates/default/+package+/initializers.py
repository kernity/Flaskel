import logging.config
log = logging.getLogger(__name__)

from cStringIO import StringIO
from datetime import datetime

from werkzeug.debug import get_current_traceback
from flask import request, got_request_exception

def init_app(app):
	init_jinja(app)
	init_logging(app)
	init_exception(app)

def init_jinja(app):
	# Change the default markup of jinja
	app.jinja_env.trim_blocks=True
	app.jinja_env.block_start_string="<%"
	app.jinja_env.block_end_string="%>"
	app.jinja_env.variable_start_string="${"
	app.jinja_env.variable_end_string="}"
	app.jinja_env.comment_start_string="<#"
	app.jinja_env.comment_end_string="#>"
	app.jinja_env.line_statement_prefix="%"
	app.jinja_env.line_comment_prefix="##"

access_log = logging.getLogger('access')
def init_logging(app):
	# Configure logging
	logging_config = app.config.get('LOGGING')
	if logging_config:
		logging.config.fileConfig(StringIO(logging_config))

	# Setup a hook to log outgoing request/responses
	@app.after_request
	def log_request(response):
		route = request.access_route
		if route:
			remote_addr = route[0]
		else:
			remote_addr = request.remote_addr

		access_log.info(
			'%s - [%s] "%s %s" %d "%s" "%s"',
			remote_addr,
			datetime.utcnow(),
			request.method,
			request.url,
			response.status_code,
			request.referrer or '',
			request.user_agent or ''
		)
		return response

def init_exception(app):
	def report_exception(app, exception=None):
		tb = get_current_traceback()
		logging.exception("%s" % tb.exception)
	got_request_exception.connect(report_exception, weak=False)