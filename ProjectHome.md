svntweet is a wrapper for SVN which aims to spread your updates to a wider audience. Currently, it will only post messages specified in-line with '-m'.

To use it, just drop svntweet.py into somewhere within your path and, when using svn, replace 'svn' with 'svntweet.py'.

Personally, I've set up an alias in bash as such:
alias svn='svntweet.py'