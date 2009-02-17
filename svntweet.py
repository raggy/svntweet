#!/usr/bin/env python
#
# Copyright 2009 Benjamin Davis
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
"""Wrapper for SVN which posts any log messages to twitter"""

import warnings
warnings.simplefilter("ignore", DeprecationWarning)

import os
import os.path
import sys
import twitter

USERNAME = ''
PASSWORD = ''
# POST_LIMIT should be 140 unless Twitter change the limit
POST_LIMIT = 140
# PREFIX is prepended to the update
# Set to current directory
PREFIX = os.path.basename(os.getcwd()) + ': '
# SVN is the path to the svn executable;
# if left blank, svntweet will search in PATH
SVN = '/usr/bin/svn'

def tweet(args, username, password):
    """Checks the args; if the they contain 'ci' or 'commit', it will attempt
    to post to twitter with username, password."""
    # If user is committing
    if ('ci' in args) or ('commit' in args):
        # Iterate through the arguments
        for i, e in zip(range(len(args)), args):
            # If user specified a message in-line
            if e == '-m':
                # Post the message to twitter
                try:
                    print "Posting to twitter... ",
                    api = twitter.Api(username=username, password=password)
                    try:
                        # Try to set the source (from svnTweet)
                        api.SetSource('svntweet')
                    except NameError:
                        # Unless python.twitter < v0.6
                        pass
                    api.PostUpdate(PREFIX + args[i + 1]\
                    [:POST_LIMIT - len(PREFIX)])
                except:
                    print "failed."
                else:
                    print "success."

def svn(args):
    """Become an svn process with args"""
    try:
        os.execv(SVN, args)
    except NameError:
        os.execvp('svn', args)

if __name__ == "__main__":
    tweet(sys.argv, USERNAME, PASSWORD)
    svn(sys.argv)

