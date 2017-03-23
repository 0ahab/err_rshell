from errbot import BotPlugin, botcmd
import subprocess
import sys

class RShell(BotPlugin):
	"""Errbot plugin to run reverse shell"""
	@botcmd
	def rshell(self, msg, args):
		run_shell_cmd = 'cat /Users/eric/rshell.sh'
		get_shell, err = subprocess.Popen(run_shell_cmd, shell=True, stdout=subprocess.PIPE).communicate()

		return(get_shell)
