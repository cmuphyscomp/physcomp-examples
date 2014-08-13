#Run this first: chmod u+rxw ./support/deepestdirectory.sh
#!/bin/bash

find . \! -name '*.html' -and \! -name '*.png' -and \! -name '*.html' -and \! -name '*.txt' -and \! -name '*.fzz' -and \! -name '*.pd' -and \! -name '.DS_Store' -and \! -name '*.py' -and \! -name '*.jpg' -and \! -name '*.psd' -and \! -name '*.fzpz' -and \! -name '*.svg' -and \! -name '*.ino' -and \! -name '*.md' -and \! -path '*/.*' -and \! -path '*/support*' -and \! -path '*/reference*' -and \! -path '*/misc-experiments-miles'
