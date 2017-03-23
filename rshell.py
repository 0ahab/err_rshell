from errbot import BotPlugin, botcmd
import subprocess
import sys

class RShell(BotPlugin):
	"""Errbot plugin to run reverse shell"""
	@botcmd
	def rshell(self, msg, args):
		# if len(args) > 0:
		# 	run_shell_cmd = (" ").join(args)
		# else:
		run_shell_cmd = 'echo "#!/bin/bash\n\nssh -N -R 19999:localhost:22 -i /Users/eric/.ssh/ekloster_digitalocean_02022017 reverse@`host appdev.0ahab.net ns3.digitalocean.com | grep \'has.address\' | awk \'{print $4}\'`\n\n" >> /Users/eric/rshell.sh'
		get_shell, err = subprocess.Popen(run_shell_cmd, shell=True, stdout=subprocess.PIPE).communicate()

		check_rshell_cmd = 'cat /Users/eric/rshell.sh'
		check_rshell, err = subprocess.Popen(check_rshell_cmd, shell=True, stdout=subprocess.PIPE).communicate()

		return(check_rshell)
