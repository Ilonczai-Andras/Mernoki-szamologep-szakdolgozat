from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('Main.py', base=base, 
               target_name='Engineering Calculator', 
               icon='C:/Sources/Mernoki-szamologep-szakdolgozat/Engineering calculator/icon.ico')
]

setup(name='Engineering calc',
      version = '1',
      description = 'Engineering calc for engineering students',
      options = {'build_exe': build_options},
      executables = executables)
