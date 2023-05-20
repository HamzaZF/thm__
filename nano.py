import subprocess

# Install nano using apt
install_command = ['sudo', 'apt', 'install', '-y', 'nano']
subprocess.run(install_command, check=True)
