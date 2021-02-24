try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'Mandelbrot Set Viewer',
    'author' : 'Zach THomsd',
    'url' : 'URL to get it at.',
    'download_url' : 'Where to download it.',
    'author_email' : 'My Email',
    'version' : '0.1',
    'install_requires' : ['Pyside2'],
    'packages' : ['NAME'],
    'scripts' : [],
    'name' : 'Mandelbrot Set Viewer'
}

set(**config)
