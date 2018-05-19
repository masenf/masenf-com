---
title: A Stupid Way to Brick an Awesome Router
author: masen
layout: post
tags: classic technical
redirect_from: /blog/a-stupid-way-to-brick-an-awesome-router.html
---

<span class="image left" style="width: 220px; height: 220px">
![WRT54GL Router by Linksys]({{ "assets/img/blog/wrt54gl_router.jpg" | relative_url }})</span>
The Linksys WRT54GL is arguably one of the most rock solid home/office
routers that one can buy today. Even though the hardware is becoming
more and more dated running one with a custom firmware can give someone
like me (a nerdy hobbyist) an extremely powerful router for a relatively
low price.

I recently traded my dad my never WRT110N wireless-N router for his
older WRT54GL purely for the ability to run custom firmware.
Unfortunately I also learned something pretty interesting about how
these routers behave.

On my way back from home where I picked up the 54GL, I was also
transporting a set of computer speakers. Consequently, the two devices
have remarkably similar power supplies. Here\'s the main difference: the
Linksys adapter outputs **12V DC** and the CyberAcoustics adapter
outputs **9V AC**. Other than that the two adapters look identical from
a quick glance and here\'s the kicker, *they have the exact same plug on
the other end*. If they were obviously different sized then I could have
avoided a few hours of headache.

Now as the story goes, I of course grabbed the wrong one and fired up my
\"new\" router. I will say that I had already tested it before I left
and it was in perfect working order. Somehow between there and here the
device broke. With the other power supply the lights still flashed and
everything seemed to work, except for the fact that the little blue and
black box had a constantly flashing power LED was resetting itself every
20 seconds.

After reading numerous posts and trying different things, someone
finally mentioned that using the wrong power supply can cause strange
behavior in these Linksys routers. (Of course at this time, I had not
realized my error and brushed off the suggestion). I had reflashed the
stock firmware, nothing\... Nothing was working.

It was about 2 hours while unpacking the rest of my stuff that I noticed
the shiny Linksys sticker on a power supply in my bag and *knew* that
had to be the cause of my problem.

Well after plugging in the correct power supply and trying again the
router stopped rebooting but was essentially dead to the outside world.
It appeared that using the wrong power supply *corrupted the firmware of
my device!* As a last resort when the stock firmware would not boot the
device I tried a long shot and used TFTP to flash the \"recommended\"
build of [DD-WRT](http://dd-wrt.org) to it. On the PC console there was
a success message, but the router still didn\'t spring back to life. I
noticed one more piece of important instruction: *please wait at least 2
minutes after flashing for the router to load the new firmware*. Sure
enough, after all that headache I was finally up and running again.
Ughh. That was fun =\]

The instructions I followed can be found here:

-   <http://mariuszczyz.wordpress.com/tag/unbrick-wrt54gl/>
-   <http://www.dd-wrt.com/wiki/index.php/Recover_from_a_Bad_Flash>
-   <http://www.dd-wrt.com/wiki/index.php/Recover_from_a_Bad_Flash#Recovering_with_TFTP>
