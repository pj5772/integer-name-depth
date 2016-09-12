from distutils.core import setup
import py2exe

setup(console=['myscript.py'],
	  options = {
			'py2exe': {
					'packages' : ['inflect']
				}
	  }
)