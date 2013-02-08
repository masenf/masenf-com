:title Questionable SNI Support in older IE
:author masen
:published 1360354908
:modified 1360354908
:slug questionable-sni-support
:tag technical

Background
==========

In my current job, I tend to take on the maintenence responsibility for a large
obsolete code base which is still being used, but doesn't currently have active
maintainers on staff. It's usually low impact work, a few bug fixes here and
there, and people stay happy. The software in question is a PHP survey app, which is
still is frequent use my various departments at the University. It's one of 
those pieces of software that other folks would consider to be a lot more important
that we do. So naturally, when it doesn't work we hear about it.

The Issue
=========

This week we heard about a new issue, a Security Error relating to our certificate.
Previously we had encountered mixed content issues where users would include external
images which were served over HTTP, so without a sample URL or an error message, 
this assumption was where we started. There was a twist however, the initial 
report implicated 'some' surveys while viewed in IE. Later we realized that the 
issue was affecting all requests to the server in question from IE.

With that information, we reproduced the bug using Internet Explorer 8. Despite 
not being able to *examine* the 'bad' cert until accepting it and connecting
to the site, upon examination it was obvious that the server was handing back 
a cert for a *different* domain! 

In December we deployed two redundant reverse
proxy servers which handled proper forwarding to our backend servers, we also
offloaded SSL processing to these proxies. Because our public IP options were limited
this move also meant swallowing the SNI pill and going to Named SSL Virtual Hosts
on nginx. Our testing showed us that this was not an issue, however our testing 
was mainly limited to Firefox and Chrome, not everyone's favorite browser, IE.

It's been published that all modern browsers come with SNI support, however the 
compatability of IE8's implementation is a bit questionable, while the proper 
page for the requested vhost was returned, the server didn't know which cert
to send back to the client, hence the domain mismatch error.

The Solution
============

Since WWU uses a wildcard certificate, we decided to use Subject Alternate names 
to our advantage. We minted a *proxy* cert which includes the names of the SSL hosts
that we serve from the proxies. This provides us with a few advantages:

  * only one cert and key to manage/serve/replace
  * SNI bugs like this are no problem, the cert works for all domains
  * simplifies the configuration and deployment of additional HA nodes

There are of course the problems such as increasing the value of our private
key, and making it more difficult to add a new SSL host (although not too bad).

We deployed the new cert to our staging proxy and tested against an old XP/IE8
box. After a few snags, we were able to test the configuration and confirm that
with the multi-name wildcard cert (*consolicert*), SNI behavior was working
as expected in IE8 and presumably later versions of IE!

Side note about HOSTS and Internet Explorer
===========================================

In the process of testing the solution on the staging server, I needed to add a
HOSTS entry to the XP system to point our problem domain to the staging IP.

So I added a line to the HOSTS file::

    140.160.x.y     depts.restek.wwu.edu

After flushing the DNS with ``ipconfig /flushdns`` and clearing the temporary 
internet files in IE, I was able to ping depts.restek.wwu.edu and it returned
the override address. In Firefox, when I havigated to depts.restek.wwu.edu it
made a request to the staging server. But in IE, the problem persisted, in the
staging server logs, there were no requests from IE! I thought that IE must not
be respecting the hosts file, I tried a few different things to no prevail.

It turns out that IE doesn't do DNS lookups if it finds an autoconfigurable 
proxy! That's right, if a proxy is found, the request is sent directly to the
proxy to lookup/deal with. If you rely on autoconfigure for network access, 
then you must disable 'Automatically Detect Settings' and instead directly
enter the web proxy address. Finally, under the advanced box, enter the 
override hosts in the box labeled "Do not use proxy server for addresses 
beginning with". You must also ensure that these hosts are accessible 
behind the proxy. I'm not sure that HOSTS overrides will work if you *must* 
use the proxy to access the overridden address!

For those of us with a direct connection and an optional proxy, simply disabling
the proxy seems to cause host overrides to work!
