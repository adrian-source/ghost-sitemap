import os, urllib2

import httplib

def get_status_code(test, host, path="/"):
    """ This function retreives the status code of a website by requesting
        HEAD data from the host. This means that it only requests the headers.
        If the host cannot be reached or something else goes wrong, it returns
        None instead.
    """
    if test == False:
        return 200;

    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status
    except StandardError:
        return None


def parse_posts(f, path, extraurl="", test=True):
        for post in os.listdir(path+extraurl):
                post = "/"+extraurl+post
                print domain+post


                if get_status_code(test, domain, post) == 200:
                        print domain+post
                        f.write('<url>\n')
                        f.write('<loc>http://'+domain+post+'</loc>\n')
                        f.write('<changefreq>daily</changefreq>\n')
                        f.write('<priority>0.5</priority>\n')
                        f.write('</url>\n')
                else:
                        print domain+post
                        print get_status_code(domain, post)


domain = "sitterle.co"
path = "/opt/ghost-0.4.2-1/sitterle.co/"
sitemappath = "/opt/ghost-0.4.2-1/apps/ghost/htdocs/content/themes/ghostium/"

f = open(sitemappath+"sitemap.html", 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

parse_posts(f, path)
parse_posts(f, path, "tag/", False)

f.write('</urlset>\n')
f.close()
~        
