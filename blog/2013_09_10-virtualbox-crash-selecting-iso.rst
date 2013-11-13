:author masen
:title virtualbox crash selecting ISO
:published 1378836816
:modified 1378836816
:slug virtualbox-crash-selecting-iso
:tag technical
:tag short
:tag fix

Fixed a sweet bug affecting VirtualBox today in a way that I really didn't expect.

I use a lot of virtualization for my work, and use both VirtualBox (4.2.18) and 
VMWare Workstation (9.0.2) on a daily basis. But setting up new virtual machines
using VirtualBox has been a painful experience over the past few weeks because
the GUI seemed very unreliable.

When selecting an ISO for the virtual cd drive, everything would work fine until
clicking the actual ISO or typing the name or full path of an ISO, at which point
the GUI would crash with this message::

    Qt FATAL: ASSERT failure in : "Got an update for an invalid inteface. Investigate this.", file atspiadaptor.cpp, line 899
    zsh: abort (core dumped)  VirtualBox

Puzzled, I searched around for the bug in VirtualBox and turned up a lot of noise
but no one reporting the issue at hand. Looking for the Qt FATAL message eventually
uncovered a `launchpad bug
<https://bugs.launchpad.net/ubuntu/+source/qt-at-spi/+bug/998012>`_,
which seemed to relate to the issue.

Long story short, the solution was simple enough::
    
    sudo apt-get remove qt-at-spi

qt-at-spi seems to be an accessibility plugin for Qt, and so far I haven't 
noticed any negative effects from not having it on my system. And most importantly,
I can select ISOs now in VirtualBox! Just goes to show that you can't make assumptions
about where a bug may be hiding.
