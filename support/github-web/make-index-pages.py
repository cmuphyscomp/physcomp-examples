#!/usr/bin/env python
# Create index pages for the cmuphyscomp github repository.

# import standard Python libraries
import argparse
import os
import re

# under Macports, use py27-lxml
import lxml.etree

################################################################
def extract_html_elements( path ):
    """Returns major elements of an html file: (body, title)."""

    parser = lxml.etree.HTMLParser()

    # parse the html file into a new ElementTree object
    page = lxml.etree.parse( path, parser )

    # find the title element and extract the text
    title_string = page.find('/head/title').text

    # extract all elements from the body element and return the contents as a string without the body tags
    body = page.find('/body')
    strings = [ lxml.etree.tostring(child) for child in body ]
    body_string = "".join(strings) 

    return (body_string, title_string)

################################################################
def write_index_file( path, title, html_body_text, image_file_names, other_files, subdirs ):
    with open( path, "w" ) as index_file:

        index_file.write( """<!doctype html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <title>%s</title>
    <style type="text/css">body { margin: 36pt; max-width: 50em; } span.eqn { white-space: nowrap; }</style>
  </head>
  <body>
    <h1>%s</h1>        
""" % (title, title) )

        index_file.write( html_body_text )
        for img in image_file_names:
            index_file.write( """<img class="alignnone" src="%s" />\n""" % img )

        if len(other_files) > 0:
            index_file.write("""<h4>Other Files</h4><ol>""")
            for name in other_files:
                index_file.write("""<li><a href="%s">%s</a></li>""" % ( name, name ))
            index_file.write("""</ol>\n""")

        if len(subdirs) > 0:
            index_file.write("""<h4>Sub-Folders</h4><ol>""")
            for name in subdirs:
                index_file.write("""<li><a href="%s">%s</a></li>""" % ( name, name ))
            index_file.write("""</ol>\n""")


################################################################
html_pattern     = re.compile( ".*\.html$" ).match
index_pattern    = re.compile( "index.html$" ).match
png_pattern      = re.compile( ".*\.png$" ).match
jpg_pattern      = re.compile( ".*\.jpg$" ).match
ignore_pattern   = re.compile( "(.*~|.DS_Store)$" ).match

unit_pattern     = re.compile( "([1-9])_(.*)$" ).match
section_pattern  = re.compile( "([a-z])_(.*)$" ).match
part_pattern     = re.compile( "([iv]+)_(.*)$" ).match
exercise_pattern = re.compile( "(.*)_(.*)$" ).match

################################################################
def walk_unit_pages( base_input_path ):
    """Recursively descend the tree of files for a particular course unit, rewriting the index.html files."""

    for root, dirs, files in os.walk( base_input_path ):
        # root is a string with the full path of the current folder
        # dirs is a list of directory names, possibly empty
        # files is a list of files, possibly empty

        # check if this is an exercise folder
        # exercise_folder_match = exercise_pattern( os.path.basename(root))
        # if exercise_folder_match:
        # print "Found exercise", root

        images = list()
        html_files = list()
        other_files = list()

        for file in files:
            if html_pattern( file ):
                if not index_pattern( file ):
                    html_files.append( file )
            elif png_pattern( file ) or jpg_pattern( file ):
                images.append( file )
            elif not ignore_pattern( file ):
                other_files.append( file )

        if len(html_files) > 1:
            print "Warning, folder has more than one html file: ", root
            index_file_name = root + '/index.html'
            write_index_file( index_file_name, title = "physcomp", html_body_text = "", images, html_files + other_files, dirs )

        elif len(html_files) < 1:
            print "Warning, folder has no html file: ", root
            index_file_name = root + '/index.html'
            write_index_file( index_file_name, title = "physcomp", html_body_text = "", images, other_files, dirs )

        elif len(html_files) == 1:
            index_file_name = root + '/index.html'
            body_text, title = extract_html_elements( root + '/' + html_files[0] )
            write_index_file( index_file_name, title, body_text, images, other_files, dirs )

################################################################
if __name__ == "__main__":
    parser = argparse.ArgumentParser( description = """Build a set of page fragments suitable for WordPress from a tree of html files.""")

    parser.add_argument( '-v', '--verbose', action='store_true', help='Enable more detailed output.' )
    # required argument
    # parser.add_argument( 'filename', help = 'Filename to process.' )

    args = parser.parse_args()

    # body = get_body_as_string( args.filename )
    # print "file is '%s'" % args.filename
    # print "body is '%s'" % body

    # walk_unit_pages( "../../1_energy-information-transduction" )
    walk_unit_pages( "../../1_energy-information-transduction/b_arduino-starter")
