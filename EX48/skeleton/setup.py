
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'LearnPythonTheHardWay_ex48',
    'author':'Ao Rick',
    'url':'URL to get it at.',
    'download_url':'Where to download it.',
    'author_email':'arrrr110@163.com',
    'version':'0.1',
    'install_requires':['nose'],
    'packages':['ex48'],
    'scripts':[],
    'name':'projectname'
}

setup(**config)