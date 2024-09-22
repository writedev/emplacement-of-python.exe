import sys
import subprocess
import os

class Test:

    def emplacement():
        
        subprocess.run(['explorer', '/select,', os.path.abspath(sys.executable)])