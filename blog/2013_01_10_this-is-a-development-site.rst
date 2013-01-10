:author masen
:title This is a Development Site
:published 1357842911
:modified 1357842925
:slug this-is-a-development-site
:tag technical
:tag site

After a weekend hack-a-thon which extended to this morning (and perhaps throughout
the rest of my life), I deployed my latest version of this site this morning.

Although it doesn't look much different, the way it's edited, generated, and 
rendered is mostly new. As I describe on my projects_ page, I've been working
on going static since about July, but I've been working especially since
last Friday. 

The result is that now my site doesn't *require* python on the webserver. Although
python is used to build out all the html pages, all of the site is assembled
once when a change is made and then served without any dynamic code running
on each request. This is a great benefit to scale as well as simplicity. However,
the largest benefit comes from the archiving of content written here, from here on
out. Instead of being locked away in a proprietary SQLite database, all content,
templates, code, and files will be versioned on github_ in plaintext, human-readable_
format.

With my excitement to move to the new platform, there are some neglects:

  * RSS feeds no longer update (i'm working on this)
  * Old permalinks like "/blog/3" still point to the old CMS and old templates
    and old links. I have migrated the old url data to my new files, but
    haven't yet created a good redirect method. (Right now leaning toward
    mod_rewrite's [L] option)
  * Comments are gone: the fb social comment system was never one that I 
    liked. Since I didn't want to sign up for a fb API key, it was a pain
    to manage and no one really used it. A new comment system will be
    written that meshes better with the feel of the site (i.e. is static based)
    and allows anon comments.
  * Documentation for the generation platform is out of date and sparse. 
    I need to write it up before it leaves my head, or I may have to scrap 
    the site again and start over. Ha.

Thanks loyal fans,
Masen

.. _projects: /page/projects.html

.. _github: http://github.com/masenf/masenf-com

.. _human-readable: http://docutils.sourceforge.net/rst.html
