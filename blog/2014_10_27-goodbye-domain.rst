:author masen
:title goodbye domain
:published 1414479305
:modified 1414479305
:slug goodbye-domain
:tag technical
:tag infra

Over the past several months, I've been slowly trying to reduce my dependence on
external (read: out of my control) services as much as feasibly reasonable. Given
that I was a server admin in a past life, this gets egregious pretty quickly.

I'm running several websites, mail server, xmpp, monitoring, backups, and
code repositories; and there is never enough time to 'keep up' with my main gig
and life responsibilities. But recently, I started to feel the Dynamic DNS strain
when I began to have more hosts to update than my free account allowed.

When I started the pursuit of running my own infrastructure on a VPS back in 2013,
I elected to use freedns.afraid.org to create a hostname pointing at the box.
Although I had masenf.com at the time, DigitalOcean didn't yet offer DNS hosting,
and it seemed like a quick and easy go seeing as I've been using the service for
updating a dynamic IP on my home network for a few years prior. I registered 
mashed-potatoes.with-linux.com and I was off to the races.

Since this was the first VPS that I purchased, it became a central piece linking
nearly all of the infrastructure that came after it. Next up was my mail server
at corn-bread.with-linux.com. At this point, DigitalOcean began offering DNS
hosting, however the with-linux.com suffix was sufficiently distributed in my 
config files that I didn't bother to change it (and i thought it was kind of 
cool and not associated with me personally). You can probably see where this is
going...

I finally got around to setting up my own DNS servers in Florida and Seattle,
and enabling self-hosted DDNS (a story for another post). Given my limited time,
the process of transitioning mashed-potatoes and corn-bread to my own domain
sort of stalled. Until tonight. As I went to log into mashed-potatoes, I noticed
immediately that it was resolving the wrong address. I tried a couple different
DNS servers, and all corroborated the new address of oname-expired.com (122.10.91.51).
And sure enough, the whois records had been updated today and the domain is gone.
I logged into freedns and found that the subdomains, which had hapily been the 
cornerstone of my digital existence for over a year, had disappeared without so
much as an email.

Then I read the FAQ:

    Use of the shared domains are not personally owned by me, but rather other
    members of this service. "Your mileage may vary" if you use domains owned by
    other members of this service. Be smart, do not create a dependency on them.
    You can use the 'Registry' link on the left hand side to find out how long
    domains have been hosted here, and how many subdomains are attached to each
    domain to help you gauge their reliability.

    Keep in mind the shared concept is primarly designed for use of 'vhosts' (or
    any other non-permanent use). The domain you choose may last for years and
    years, or it may disappear next week. Beware of this.

Lesson time:

    * DON'T rely on free services for things which you care about
    * DON'T put all of your digital eggs in one basket: I shouldn't have used the
      same domain for both servers, this became a single point of failure.
    * DON'T trust a third party to run your DNS. I really should have known this
      one, but if they own your DNS, they pretty much own you.
    * DON'T be lazy about security issues. I sort of forsaw the day when this
      would come, so I thankfully had a backup DNS zone ready to go. I just wish
      I could have implemented it in a more controlled manner, rather than in a
      tired rush at 23:45 on a Monday.
    * DO regularly test DNS resolution -- I haven't been doing this, but will start
      with Nagios next weekend. (Maybe I'll test for SSL certificate expiry as well xD)

All in all, this could have been worse, but I think it would have been nice to 
at least get an email from the freedns.afraid.org admin. I'm guessing that their
system knows when a domain is expiring, because afterward it did not appear in my
subdomain list nor in the domain registry. Simply sending an email to everyone
with a subdomain registered with a sort of 'Heads up, your domain will be going 
away' could really go a long way.
