import subprocess

# Install the package using apt
install_command = ['sudo', 'apt', 'install', '-y', 'gedit']
subprocess.run(install_command, check=True)

# Launch gedit
gedit_command = ['gedit']
subprocess.run(gedit_command)
