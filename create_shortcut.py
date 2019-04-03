"""
Create Windows desktop shortcut.
This must be run in the correct conda environment for the package.
"""
import os
from pathlib import Path

import win32com.client


home = Path.home()
desktop = home / 'Desktop'
link_path = desktop / 'liikelaajuus.lnk'

# for some reason CONDA_ROOT is not set, so get root from executable path
anaconda_python = Path(os.environ['CONDA_PYTHON_EXE'])
envdir = Path(os.environ['CONDA_PREFIX'])
anaconda_root = anaconda_python.parent

pythonw = anaconda_root / 'pythonw.exe'
cwp = anaconda_root / 'cwp.py'
pythonw_env = envdir / 'pythonw.exe'
script = envdir / 'Scripts' / 'liikelaaj-script.py'

assert cwp.is_file()
assert envdir.is_dir()
assert pythonw.is_file()
assert pythonw_env.is_file()
assert script.is_file()

args = '%s %s %s %s' % (cwp, envdir, pythonw_env, script)

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(link_path)
shortcut.Targetpath = pythonw
shortcut.arguments = args
shortcut.save()
