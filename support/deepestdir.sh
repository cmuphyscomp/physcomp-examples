#Run this first: chmod u+rxw ./support/deepestdirectory.sh
#!/bin/bash

find . -type d -and \! -path '*/.git*'
