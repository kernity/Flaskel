from setuptools import setup
setup(
	name='flaskel',
	version='0.1-beta',
	url='http://github.com/kernity/flaskel',
	license='MIT',
	author='Khalid Yagoubi',
	author_email='kernity@gmail.com',
	description='A full skeleton for Flask framework',
	packages=['flaskel'],
	include_package_data=True,
	zip_safe=False,
	platforms='any',
	install_requires=[
		"PasteScript>=1.7.4.2", "Tempita>=0.5.1",
	],
	entry_points={
		"paste.paster_create_template": [
			"flaskel = flaskel.generators:FlaskelTemplate"
		],
		"console_scripts": [
			"flaskel = flaskel.scripts.main:main"
		]
	}
)
