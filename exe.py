import os
from shutil import rmtree


REMOVE_SPEC = True
REMOVE_BUILD = True


scripts = [script for script in os.listdir() if script.endswith('.py') and script != 'exe.py']


for script in scripts:
    try: 
        print(f'Generating executable for {script}...')
        os.system(f'python -m PyInstaller {script} --onefile')

        if REMOVE_SPEC:
            print(f'Removing {script[:-3]}.spec file...')
            os.remove(f'{script[:-3]}.spec')

        if REMOVE_BUILD:
            print('Removing build directory...')
            rmtree('build')

    except Exception as e:
        print(f'Error generating executable for {script}: {e}')

    else:
        print(f'Executable file generated: {script[:-3]}.exe')
