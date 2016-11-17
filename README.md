AptUndo
=================

This is just a simple script to search /var/log/apt/history.log and print out
a space-separated list of packages that were installed with a given package.
The purpose of this is to facilitate completely uninstalling all dependencies
of a package without resorting to `apt-get autoremove`.
