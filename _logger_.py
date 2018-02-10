# ===================================
# Filename: _logger_.py
# Purpose: To log data to a log file as part of the docx-diary program.
#
#
# docx-diary
# Copyright (C) 2018  Joshua Peter Booth
#
# This file is part of docx-diary.
#
# docx-diary is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# docx-diary is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with docx-diary (see LICENSE.md).
# If not, see <http://www.gnu.org/licenses/>.
#
# Contact me:
# Email: joshb00th@icloud.com
# ===================================

import logging

# Create logger called 'Debugger'
logger = logging.getLogger('Debugger')
logger.setLevel(logging.DEBUG)

# Create file handler which logs even debug messages
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)

# Create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# Create formatter and add it to the handlers
formatter_format = "%(asctime)s - %(name)s - %(levelname)s - " + \
    "%(funcName)s - Line: %(lineno)s - %(message)s"
formatter = logging.Formatter(formatter_format)
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
