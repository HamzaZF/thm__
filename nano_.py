import subprocess

# Install nano using apt
install_command = ['apt', 'install', '-y', 'nano']
subprocess.run(install_command, check=True)