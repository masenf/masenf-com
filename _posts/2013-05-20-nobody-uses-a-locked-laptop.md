---
title: nobody uses a locked laptop
icon: fa-lock
author: masen
layout: post
tags: technical
redirect_from: /blog/nobody-uses-a-locked-laptop.html
---

I\'ve had a small obsession lately of watching DEFCON videos from years
past on YouTube when I get a free moment. It\'s mostly been good aside
from making me paranoid to use my computer. Mostly these guys and gals
bring up great ideas for protecting yourself from
Ahem\...\"Adversaries\" with things like drive encryption, rapid drive
destruction, secure communication, strong passwords, long keys, etc. All
these are great things! They keep unauthorized users far from your data
and I wouldn\'t advocate against them.

Here is the particular video that inspires this post:

<iframe width="560" height="315" src="https://www.youtube.com/embed/Jwpg-AwJ0Jc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

\"Pwned By the owner: What happens when you steal a hackers computer\".
Although he commits a cardinal error in leaving his data totally open
and unprotected, it\'s ultimately this oversight which allows him to
retrieve his computer, much later and in one piece. Had he employed full
disk encryption, the thieves wouldn\'t have been able to use the
computer and thus would have hocked it or formatted the disk. That\'s
what they never tell you about disk encryption (perhaps because it\'s
obvious), but nothing stops an adversary from wiping the disk. If the
perp seeks to profit from your gear, not your data, you\'re out of luck.

This got me thinking about how I would go about a similar recovery of
some boxes that I own, and I realized that if my equipment ever got
lifted, I\'d never get it back. BIOS passwords and FDE are brick walls
when it comes to locating my devices on a strange network. However, I
like the privacy and protection of FDE and I wanted the best of both
worlds.

So I repartitioned my hard drive. Main part is CS/Filevault 2, secondary
is just plain HFS.

Now when a thief walks off with my computer, they\'ll need my long,
secure password to open my main part. BUT, if the computer is restarted,
it will boot to a pretty default OS X Lion desktop and allow the user to
pretty much use my laptop to their hearts content.

**This is good**, because they will not realize that there is actually a
kernel keylogger, ddns client, and remote access trojan just watching
and waiting (and taking pictures). Many people swiping laptops are
morons, and will use them to access email accounts, facebook, and
perhaps even online banking. I have a lot more confidence that in the
unfortunate event of personal theft, not only will I be able to track
and identify the perp, but I might get a good DEFCON story out of it as
well.
