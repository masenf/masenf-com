:author masen
:title running a private mail server
:published 1369281540
:modified 1369281540
:slug running-a-private-mailserver
:tag technical

*disclaimer: I am not a lawyer, nothing in this post should be vaguely considered
legal advice*

Recently, I've been more interested in reducing my dependence on third-party 
cloud services. For those of us following the security and privacy trends
in the industry, it's pretty unclear whether you retain 4th ammendement 
protection over data on 3rd party servers. As far as the FBI is concerned, they
think they should have `easy access to any online account`_, preferably without
a warrant and other red tape. Although these services provide SSL, in many cases
they don't really have a choice when it comes to turning over your information.

Although I follow the law to the letter in my day to day life, I'm still a bit 
uncomfortable with the government vacuuming up my data just because it can.
The reason I think more people aren't upset about this is that it's
not intrusive enough. Sure someone can find out a lot about your life with access
to your email account, but in many cases, companies are not allowed to disclose
to users when they release their information to government entities. If you 
don't know you've been violated, then there's nothing to be upset about.

So coming off of a nice rant and venting, I resolved to set up my own email
server for several reasons:

  * liberal aliasing: I can use a different email address for all services. This
    allows me to trap spam and identify which service has 'lost' my email address.
  * separate points of failure: well if someone roots my server, then I'm hosed,
    but otherwise, my accounts are less linked together. Compromising one account
    will not be sufficient to take over my online id.
  * protection from the gmail inbox form: the FBI or whoever, can't just fill
    out a form and get all my emails, they'll need to obtain a warrant for my
    server disk, no free candy.
  * it's also a good learning experience, running a mail server teaches you a
    lot about system administration.

I just finished setting up my shiny new internal mail server on 0x26.net. And 
started creating aliases for my various web accounts. So far everything seems
to be going smoothly. There are a few pain points to note, that mail requires 
maintenance. I must ensure that mail is being sent and received properly, that
the server remains accessible to me and not others, and avoiding DoS and spam.

I'll be using postgrey_ for greylisting, which I've heard is extremely effective
against spam. Although I plan to manually control spam as much as possible by 
utilizing aliases in all public communication. When I get spammed on a certain
address, I'll redirect it to junk and potentially create a new similar alias
for the same purposes.

In the near future, I plan to move the primary MX to a RasPi on my home network,
which will require a warrant for anyone to obtain the mails. Then I'll use a VPS
as the backup MX to ensure that messages get delivered. And all this for what?
**Freedom.**

If you want to help me test out my mail server, say hi: mf - [at] - 0x26 - net

.. _`easy access to any online account`: http://www.rttnews.com/2085746/fbi-hopes-to-gain-access-to-gmail-dropbox-by-year-s-end.aspx

.. _postgrey: http://postgrey.schweikert.ch/
