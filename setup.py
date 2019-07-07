import cx_Freeze
from cx_Freeze import *

exe = [Executable("DodgeItv1_2.py")]

setup(name="DodgeIt v1.2",
      version="1.2",
      description="Dodge It created by JCLOH",
      options={"build_exe":{"packages":["pygame"]}},
      executables=exe
      )
