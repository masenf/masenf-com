:author masen
:title simplifying
:published 1508224361
:modified 1508224361
:slug simplifying
:tag technical
:tag infra

.. figure:: /img/blog/rock-karen.jpeg
   :alt: a simple stack of rocks
   :figclass: float-right

In the past, I've been fascinated by the abstraction of complexity. I drooled over complexity for complexity's sake, which is why my "simple" online presence had ballooned across 5 virtual servers, 1 internal server, self-hosted mail, dns, xmpp, self-hosted dynamic dns, and an extremely brittle set of ansible scripts tying everything together. It was, uh, let's call it fun.

Then things started to become untenable. I have a day job. It was different in college when my side-job was managing servers -- I used to eat sleep and breathe this stuff. But now, I'm starting to build a life and the amount of time I had to fiddle with years-old ArchLinux installations was drawing very thin. As well, all of the complexity was starting to get unmanagable at the same time I was really coming to rely on some of my services, particularly email, calendars, and contacts (the reason I don't outsource those is probably the subject of another post). It's uncomfortable having the lynchpin of your virtual life running on who knows what unpatched software that can't be patched because the newer kernels aren't even supported in your virtualization environment.

If you're still following me, great. The short of it is, I needed to drastically simplify my infrastructure in order to increase robustness and reduce my attack surface. I'm writing this post now, almost as a proof of concept to see if it's even possible for me to still update my technical blog. The game plan is to reduce all the complexity down to 2 servers:

  * outer: serves everything internet-facing - email, web sites, and reverse proxying back to
  * inner: holds everything sensitive on a raspberry pi in my closet - private repositories, backups, personal NAS

In the process of transitioning everything, I've been straight up jettisoning projects which are no longer interesting, or pose too much of a security risk. I'm no longer managing my own DNS -- what was the point of that? DigitalOcean does a great job of DNS hosting, and if I trust them enough to run my VPS, then I can trust them enough to resolve my names. I'm no longer running XMPP -- there's just no point.

I've also been standardizing everything into (hopefully) more robust ansible playbooks. There's no point in deploying a service I care about in a oneoff way. VPS providers change, priorities change, everything changes all the time. If I've learned anything over the past 5 years it's that maintaining one off configurations is a huge nightmare. I may save a few hours up front, but I pay dearly for them the longer I need to keep something online. I've found with the playbooks I already created, it's been straightforward to transition things over to the new infrastructure. Even in cases where I was previously running in docker containers, migrating the playbooks to run on the host directly was trivial. And in cases where it wasn't trivial, the exact steps with commented rationale and all configuration files were directly available for inspection. Config management just makes everything a breeze.

The other big improvement has been embracing encryption. Data at rest is stored on dm-crypt/luks formatted volumes and containers which I unlock after boot. Data in transit is almost universally protected by HTTPS thanks to the easy and automation of letsencrypt and certbot. In cases where I'm reverse proxying, the data is protected by SSH encryption. Backups are protected with a randomly generated AES256 key, which is then encrypted with my PGP public key and subsequently downloaded to an offsite location. It goes a long way toward my piece of mind.                                                     

So as I've grown into a more mature engineer, I've picked up a few lessons along the way. Complexity for complexity's sake is an immature viewpoint -- fun for the moment, but unrealistic. A huge part of engineering, which is never taught in school is the principle of maintainability. Nothing is reused quarter to quarter or semester to semester, but almost everything in the real world needs to last for at least some period of time. Even when you're sure it doesn't need to last, I've been surprised more than once to find a one-off hack being relyed on by hundreds of people. Well, I shouldn't be surprised anymore.

Part of growing as an engineer is recognizing the lifecycle of the projects that I'm working on and being realistic about maintainability, which mainly breaks down into three components:

  * simplicity
  * readability
  * documentation
