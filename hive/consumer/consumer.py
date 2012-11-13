# Copyright (C) 2012 Johnny Vestergaard <jkv@unixcluster.dk>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gevent
import os

from loggers import loggerbase
from loggers import consolelogger
from loggers import sqlitelogger

class Consumer:

	def __init__(self, sessions):
		print "instance created"
		self.sessions = sessions

	def start_handling(self):
		active_loggers = self.get_loggers()

		while True:
			print "Current sessions count: %i" % (len(self.sessions),)
			for session_id in self.sessions.keys():
				session = self.sessions[session_id]
				if not session['connected']:
					for logger in active_loggers:
						logger.log(session)
					del self.sessions[session_id]
			gevent.sleep(5)

	def stop_handling(self):
		pass

	def get_loggers(self):
		loggers = []
		for l in loggerbase.LoggerBase.__subclasses__():
			print l
			logger = l()
			loggers.append(logger)
		return loggers