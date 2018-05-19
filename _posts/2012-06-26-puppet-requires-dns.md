---
title: puppet requires DNS
author: masen
layout: post
tags: technical lengthy fix
redirect_from:
  - /blog/puppet-requires-dns.html
  - /blog/13
---

<span class="image left" style="width: 150px">![Puppet]({{ "assets/img/blog/puppet_labs_400.png" | relative_url }})</span>
Working at ResTek over the summer is a much different experience than working
during the school year. For one: I am now working 40 hours per week (up
from 15), and also many more people are working in the office regularly
which makes collaboration easier. All this leads to an environment where
things get done in a third or less of the time it would \'normally\'
take to complete. And the bugfixing is very intense.

The first big project that\'s nearing completion is a new deployment of
office workstations for staff to use. We have about 17 machines which
dual boot between Windows 7 Enterprise (deployed with Symantec Ghost)
and Lubuntu 12.04 (deployed with puppet 2.7). We have a much more
uniform configuration than we previously did, but there are still many
faults to discover and fix.

I feel like everything about this story comes back to DNS because we as
people do not like to remember numbers, especially not ones which may
change on a daily basis. That\'s why DNS was created! So the goal is to
have puppet periodically refresh the configuration on each host, and in
the process notify the server of its current IP address. We can later
use this information to feed the DNS server and have up-to-date dynamic
dns for all machines in our office. We deployed the manifest in a simple
way that makes a GET request to the puppetmaster server with the
client\'s hostname. A PHP script then aggregates that information into
the database. *Surprisingly,* this part of the system worked just fine.
After pushing the change and manually refreshing puppet, I was able to
get all the hosts to report their IP address every 30 minutes\...Or so I
thought.

Upon arriving the next day, I noticed that some of the computers were no
longer refreshing their configuration from the puppetmaster, or the
script to update their IP was not working. After the checking the log on
an affected server, I saw a message like this:

    Jun 21 08:52:47 Kiwi-Strawberry puppet-agent[1186]: Did not receive certificate

Repeating over and over in the logs, every 2 minutes. It had to be a
puppet issue. I restarted the puppet agent...and it refreshed normally.
After restarting the agent, it continued to work just fine. Meanwhile, I
continued to puzzle about it and search google, only to uncover 3 year
old posts and other worthless information. I was going to have to solve
this one myself.

After these seemingly random puppet failures continued to happen over
the next few days on different servers I began to notice a pattern:
machines that had been restarted didn\'t work until the puppet service
was restarted separately and later. A freshly booted machine will sit
there and wait for a certificate despite the fact that it already has
one signed and working! I could now reproduce the issue and started
looking for other clues.

I noticed on the puppetmaster that several certificates were in the
signing cache waiting to be signed. They corresponded to the bare
(non-FQDN) hostname of each client which was experiencing post reboot
issues. It started to click in my mind.

I restarted the workstation and then fired up my editor to look at the
logs. Sure enough, the puppet-agent (which is started via a sysv init.d
script on Ubuntu) was starting BEFORE the network was up. This was
causing puppet to see a different hostname (without the DHCP
supplied domain suffix) and consequently generate a different
certificate. When puppet finally got network access it was requesting
that the puppetmaster sign its new certificate; of course this is not
the right thing and our site.pp manifest is not set up to manage nodes
without a fully qualified domain name.

Several solutions were proposed to tackle this problem from: having cron
restart puppet occasionally to renaming init.d scripts. However, nothing
seemed quite as nice as moving to an event-based startup for puppet. It
was easy enough to hack together an upstart configuration file for
puppet:

    respawn
    console log

    start on (local-filesystems and net-device-up IFACE=eth0)
    stop on runlevel [!12345]

    pre-start script
            test -z $UPSTART_EVENTS || echo Puppet started by: $UPSTART_EVENTS >> /var/log/puppetd.log
    end script

    exec /usr/bin/puppet agent --no-daemonize

After placing this in /etc/init/puppet.conf, I disabled the init.d
startup script:

    # chmod 644 /etc/init.d/puppet

On the next reboot, puppet waited until the network was fully up and
communication active before being started. The problem was resolved! I
quickly added the solution to our office manifest and pushed the
changes.

Everything seemed to be going fine until the very next day (today)...I
still have more troubleshooting to do because now puppet randomly dies
throughout the evening without so much as a peep in the logs. Stay tuned
for part 2.
