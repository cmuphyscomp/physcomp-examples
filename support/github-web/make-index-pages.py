#!/usr/bin/env python
# Create index pages for the cmuphyscomp github repository.

# import standard Python libraries
import argparse
import os
import re
import json

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
iframe_list = list()

# Generate the text for an iframe-based post.  This is transitional until the
# WordPress site can be automatically updated from the github sources.
def gen_iframe_post( folder, depth, title, html_name, image_file_names, other_files ):

    comment = "<!-- -------------------- %s  ------------------------------------- -->\n" % re.sub( "Exercise: ", "", title )

    text_iframe = """<iframe id="assignment-html" onload="resizeIframe(this)" width="100%%" frameborder="0" src="http://cmuphyscomp.github.io/physcomp-examples/%s" width="960" height="800"></iframe>\n""" % (folder + '/' + html_name)

    image_refs = list()
    for img in image_file_names:
        image_refs.append( """<img id="assignment-image" class="alignnone" src="http://cmuphyscomp.github.io/physcomp-examples/%s/%s" width="960" height="%%100" />\n""" % (folder, img ))
    
    other_refs = list()
    for name in other_files:
        other_refs.append("""      <li><a href="http://cmuphyscomp.github.io/physcomp-examples/%s/%s">%s</a></li>\n""" % ( folder, name, name ))

    if len(other_refs) > 0:
        other_parts = "<h4>Other Files</h4><ol>\n" + "\n".join(other_refs) + "</ol>\n"
    else:
        other_parts = ""

    # now assemble into a string
    record = comment + text_iframe + "\n".join(image_refs) + other_parts + "\n\n\n" 

    return record

################################################################
# Keep track of all generated posts in order to emit a single description of the whole assignments tree.

post_list = list()

def add_post_to_list( folder, depth, title, parent ):
    # generate a full URL to the post source text
    post_url = "http://cmuphyscomp.github.io/physcomp-examples/%s/post.html" % folder

    # generate a permalink with underscores converted to dashes
    permalink = "assignments/" + folder.replace("_","-")

    # create a string defining the parent; it isn't clear yet what WordPress will need
    parent = parent.replace("_","-")

    # create a dictionary and save it in the global list
    post_record = { "post": post_url, "title": title, "parent": parent, "permalink": permalink }
    post_list.append( post_record )

def write_post_list_file( dest_path ):
    with open( dest_path, "w" ) as output:
        output.write( json.dumps( post_list, indent = 0 ) )

################################################################
# Write the contents of a WordPress post for a given unit, section, part, or exercise within the assignments tree.

def write_post_file( path, folder, depth, title, html_body_text, image_file_names, other_files, subdirs ):
    with open( path, "w" ) as post_file:
        post_file.write( html_body_text )
        for img in image_file_names:
            post_file.write( """<img id="assignment-image" class="alignnone" src="http://cmuphyscomp.github.io/physcomp-examples/%s/%s" width="960" height="%%100" />\n""" % (folder, img ))

        if len(other_files) > 0:
            post_file.write("""    <h4>Other Files</h4>\n    <ol>\n""")
            for name in other_files:
                post_file.write("""      <li><a href="http://cmuphyscomp.github.io/physcomp-examples/%s/%s">%s</a></li>\n""" % ( folder, name, name ))
            post_file.write("""    </ol>\n""")

        if depth == 4 and len(subdirs) > 0:
            post_file.write("""    <h4>Sub-Folders</h4>\n    <ol>\n""")
            for name in subdirs:
                post_file.write("""      <li><a href="http://cmuphyscomp.github.io/physcomp-examples/%s/%s">%s</a></li>\n""" % ( folder, name, name ))
            post_file.write("""    </ol>\n""")

################################################################
# Write a fully self-contained HTML file to serve as a folder index.html file.
def write_index_file( path, csspath, title, html_body_text, image_file_names, other_files, subdirs ):
    with open( path, "w" ) as index_file:

        index_file.write( """<!doctype html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <link rel="stylesheet" type="text/css" href="%s" />
    <title>%s</title>
  </head>
  <body>
    <h2>%s</h2>\n""" % ( csspath, title, title) )

        index_file.write( html_body_text )
        for img in image_file_names:
            index_file.write( """<img class="alignnone" src="%s" />\n""" % img )

        if len(other_files) > 0:
            index_file.write("""    <h4>Other Files</h4>\n    <ol>\n""")
            for name in other_files:
                index_file.write("""      <li><a href="%s">%s</a></li>\n""" % ( name, name ))
            index_file.write("""    </ol>\n""")

        if len(subdirs) > 0:
            index_file.write("""    <h4>Sub-Folders</h4>\n    <ol>\n""")
            for name in subdirs:
                index_file.write("""      <li><a href="%s">%s</a></li>\n""" % ( name, name ))
            index_file.write("""    </ol>\n""")

        index_file.write( """  </body>\n</html>\n""" )

################################################################
html_pattern     = re.compile( ".*\.html$" ).match
index_pattern    = re.compile( "index.html$" ).match
post_pattern     = re.compile( "post.html$" ).match
png_pattern      = re.compile( ".*\.png$" ).match
jpg_pattern      = re.compile( ".*\.jpg$" ).match
ignore_pattern   = re.compile( "(.*~|.DS_Store)$" ).match

unit_pattern     = re.compile( "([1-9])_(.*)$" ).match
section_pattern  = re.compile( "([a-z])_(.*)$" ).match
part_pattern     = re.compile( "([iv]+)_(.*)$" ).match
exercise_pattern = re.compile( "(.*)_(.*)$" ).match

################################################################
# generate a title prefix based on the position in the syllabus
def title_prefix( folder, depth ):
    if depth == 1:
        match = unit_pattern( folder )
        if match:
            return "Unit %s: " % match.group(1)

    elif depth == 2:
        match = section_pattern( folder )
        if match:
            return "Section %s: " % match.group(1).upper()

    elif depth == 3:
        match = part_pattern( folder )
        if match:
            return "Part %s: " % match.group(1)

    elif depth == 4:
        match = exercise_pattern( folder )
        if match:
            return match.group(1) + " "

    return ""

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

        # find the folder path within the repository naming scheme
        relpath = os.path.relpath( root, "../../")

        # compute the path to the css file to include in every index file for styling
        path_parts = relpath.split('/' )
        depth = len( path_parts )
        csspath = "/".join( [ ".." for i in range(depth) ] ) + "/support/github-web/physcomp.css"

        # print "Processing ",root,"at depth",depth

        for file in files:
            if html_pattern( file ):
                if not index_pattern( file ) and not post_pattern(file):
                    html_files.append( file )
            elif png_pattern( file ) or jpg_pattern( file ):
                images.append( file )
            elif not ignore_pattern( file ):
                other_files.append( file )

        if len(html_files) > 1:
            print "Warning, folder has more than one html file: ", root
            index_file_name = root + '/index.html'
            write_index_file( index_file_name, csspath = csspath, title = relpath, html_body_text = "", image_file_names = images, \
                              other_files = html_files + other_files, subdirs = dirs )

        elif len(html_files) < 1:

            # folders at depth 5 and greater are within exercises and may just be data files, so suppress the warning:
            if depth < 5: print "Warning, folder has no html file: ", root

            index_file_name = root + '/index.html'
            relpath = os.path.relpath( root, "../../")
            write_index_file( index_file_name, csspath = csspath, title = relpath , html_body_text = "", image_file_names = images, \
                              other_files = other_files, subdirs = dirs )

        elif len(html_files) == 1:
            index_file_name = root + '/index.html'
            body_text, title = extract_html_elements( root + '/' + html_files[0] )
            write_index_file( index_file_name, csspath = csspath, title = title, html_body_text = body_text, image_file_names = images, \
                              other_files = other_files, subdirs = dirs )

            # folders at depths up to four generate WordPress posts
            if depth <= 4:
                post_file_name = root + '/post.html'
                prefix = title_prefix( path_parts[-1], depth )
                write_post_file( post_file_name, folder=relpath, depth=depth, title = prefix+title, html_body_text = body_text, image_file_names = images, \
                                 other_files = other_files, subdirs = dirs )

                parent = "/".join( path_parts[0:-1] )
                add_post_to_list( relpath, depth, prefix+title, parent )

                iframe_list.append (gen_iframe_post( folder=relpath, depth=depth, title = prefix+title, html_name = html_files[0], image_file_names = images, \
                                          other_files = other_files ))


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

    if os.path.basename(os.getcwd()) != 'github-web':
        print "Error: this script must be run from within the github-web folder."
        exit(1)

    walk_unit_pages( "../../1_energy-information-transduction" )
    # walk_unit_pages( "../../1_energy-information-transduction/b_arduino-starter")

    write_post_list_file( "assignments.json" )

    with open( "iframe_posts.html",  "w" ) as output:
        for i in iframe_list:
            output.write( i )
