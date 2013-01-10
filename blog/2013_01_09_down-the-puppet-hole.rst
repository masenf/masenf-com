:author masen
:title down the puppet hole
:published 1357803009
:modified 1341293302
:modified 1357803009
:permalink 15
:tag technical
:tag lengthy
:slug down-the-puppet-hole

.. figure:: /img/blog/spiral.jpg
   :alt: down the puppet hole
   :figclass: float-right


In my post a few months back, I was discussing some DNS issues we were experiencing while 
deploying puppet to some workstations in the ResTek office. Unfortunately, after
the issue with the faulty init.d start scripts was resolved, half of the machines
were still not 'calling in' to the puppetmaster. I should mention at this point 
that the current version of puppet in the Ubuntu repositories is 2.7.11;
naively, this is the version that we are running.

After sifting through bug reports and working on other things, Brenan showed me 
a bug report affecting our version of puppet, which was supposedly fixed in 2.7.17. 
That bug report however is so elusive that I couldn't even find it again to link from here!

First, we wanted to determine if the latest version of puppet would even resolve
our issues, then we needed to come up with a way to deploy it.

Initially, we were going to use the prebuilt apt.puppetlabs repositories, but since 
this isn't the first bug we've had to fix in our Ubuntu packages (a story for
another post) we decided it would be worthwhile to set up our own internal 
APT repository for all custom built packages. So we backported puppet 2.7.17 on 
Ubuntu 12.04 and tested against the previously buggy behavior to find the problem
resolved. Yay!

Now I'm not happy to admit it, but before this package, we've
built and deployed 6 or 7 other custom built binary packages which were deficient 
as-built in the Ubuntu repos. Our primary method for deployment was to copy the 
.deb packages to the puppetmaster server and use a File resource to copy them to
the host and a Package { ...: provider => dpkg } to install them. This seems 
like a cheap easy solution at first, but it has a variety of interesting issues:
packages install over and over again, custom packages get overwritten by repo
packages during upgrades, etc. Long story short, the dpkg configuration was bringing
suffering to my usual administration contentment. Digression aside, we resolved
to create our own APT repository.

Given that APT was designed by the debian folks, the only suggestion I found for
hosting an APT repo easily and simply on FreeBSD (our primary server environment) 
was to use NFS and remotely manage the repo on a debian box. Okay, but to me that
sounded like more trouble than it was worth. Nearly all the debian tutorials were
using a program made for APT repo management, reprepro_ (formerly mirrorer). 
I cloned the git repository and starting hacking at the code to make it run on 
FreeBSD. After a few dependencies were satisfied, we were up and running with our
shiny APT repo. For those following along, here is a patch_ for the latest 
release of reprepro source. Configuration is relatively straightforward, and
I ran into no issues following debian tutorials.

This may sound like a lot of trouble to go through, but we now have the control
to push out our own versions of packages and manage them nicely using APT and 
puppet. This expedites bug fixes, especially for critical issues such as LDAP
which are show-stopping in many environments.

.. _reprepro: http://mirrorer.alioth.debian.org/

.. _patch: /downloads/blog/reprepro-4.13.0-fbsd.patch
