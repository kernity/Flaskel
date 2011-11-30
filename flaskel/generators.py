
from paste.script.templates import Template, var
from tempita import paste_script_template_renderer

class FlaskelTemplate(Template):
	_template_dir = ('flaskel', 'templates/default')
	summary = 'Flaskel application template'
	egg_plugins = ['PasteScript', 'Flaskel']
	vars = [
		var('version', '0.1'),
		var('description', 'One-line description'),
		var('author', 'Author name'),
		var('author_email', 'Author email'),
		var('url', 'URL of homepage'),
	]
