---
title: HP dv6000 Series AC Power Adapter Debacle
author: masen
layout: post
tags: classic lengthy
redirect_from: /blog/hp-dv6000-series-ac-power-adapter-debacle.html
---

<span class="image left">![]({{ "assets/img/blog/hp_dv6000.jpg" | relative_url }})</span>
In August 2007 I bought my first modern laptop, an HP dv6000m with specs
about like this:

<span class="image right">![]({{ "assets/img/blog/intel.jpg" | relative_url }})</span>
-   Genuine Windows Vista Home Premium
-   Intel(R) Core(TM) 2 Duo T5600(1.83GHz/2MB L2Cache)
-   15.4\" WXGA BrightView Widescreen (1280x800)
-   Intel(R) Graphics Media Accelerator 950 - Core
-   2GB DDR2 System Memory
-   200GB 5400RPM SATA Hard Drive
-   LightScribe Super Multi 8X DVD+/-RW w/Double Layer
-   Intel(R) PRO/Wireless 3945ABG Network Connection
-   6 Cell Lithium Ion Battery

There are **ALOT** of similar HP laptops that I believe suffer from the
AC Power Adapter issue that I\'m about to describe below (in fact I
believe that any HP laptop from this era could be subject to this
problem, it\'s just hard to say).

The tricky part about this problem is that its symptoms do not
reasonably lead even a savvy user, like me, to the direct cause. The
first day I started using my laptop I noticed a strange non-constant
background buzzing sound that seemed to be coming from the speakers. (I
will clarify that everyone\'s idea of a buzz is different and that the
sound I\'m describing could be called a whine, squeal, or squeek as
well). The difference with this sound was that it *was not coming from
the OS*. After turning the volume all the way down in the operating
system, the high pitched buzz remained. The buzz was also present in the
Line/Mic in signals as well as the Headphone output.

Naturally, this was annoying. But it\'s not the kind of issue that you
send your laptop back to the manufacturer for (and wait 8 weeks in the
interim). All in all, it wasn\'t THAT loud and if you had music or other
audio playing it was essentially inaudable. I searched around on the
internet in \'07 and \'08 and found that numerous other people were
experiencing similar issues with their recent model HP laptops. It just
didn\'t add up; how could HP not realize that their laptops, or a
percentage of them at least, were buzzing whenever they were on?

For the next two years, I accepted the noise and largely forgot about
it. It wasn\'t until about a month ago (July 2010) when the same issue
began to manifest itself in another way. Ever since the thermal sensors
went out on my IBM Intellistation desktop, my 1080p 23\" monitor had
been sitting dormant in my room getting no use, so I decided to start
using my laptop to drive the display. When I plugged the external
monitor in to the laptop (VGA cable) I instantly saw tons of horizontal
scanlines jumping all over the display. After a few moments of study and
careful listening, I noticed that the scanlines seemed to correlate and
move in relation to the high pitch buzz which was still present. Both
Windows 7 and Ubuntu 10.4 behaved identically in this regard.

Again, I took to the internet to see if anyone else had ever experienced
such a thing before. Sure enough tons of the same people with the
buzzing sound issue had the flickering external monitor issue as well,
go figure. Fortunately by this time, someone had devised an inconvenient
work around: drive the display on battery power. Once the laptop was
unplugged from the wall, the flickering and scanlines instantly went
away! What a miracle, I could finally use my screen, but it wasn\'t
convenient and desktop-like as I had hoped. The laptop constantly had to
be charged, and I couldn\'t just leave it on for extended periods of
time. There had to be a better way, but at this point, I was happy
enough and decided to give it a rest

<span class="image left">![]({{ "assets/img/blog/hp_adapter_price.jpg" | relative_url }})</span>
As they say, luck finds you in the most mysterious ways...Not more than
2 weeks after my battery workaround discovery, did I notice that my
official [OEM HP branded AC Power
Adapter](http://www.shopping.hp.com/product/computer/categories/ac_adapters/1/accessories/DL606A%2523ABA)
*\[link broken\]* had been apparently chewed through. While I cannot
confirm how it happened I will say that the frayed adapter was toast
(and I was without a laptop for a week). If you clicked that link in the
last sentence, you\'ll see that HP wants the outrageous price of
\$59.49USD + S&h (and that\'s even with a \$10.50 instant rebate!). Now
as a reasonable individual I happen to know that the fine folks over in
the People\'s Republic of China produce notebook power adapters for
every laptop ever made and they DON\'T over charge for them (fancy
that...).

A quick jaunt over to Amazon found me this little puppy: [NEW AC
Adapter/Power Supply+Cord for HP Pavilion DV2000 dv1000 dv4000 dv5000
dv6000 dv8000
ze2000](http://www.amazon.com/gp/product/B003E2XYKO/ref=oss_product). As
you can see, the total price including shipping comes in at around
\$10USD.

<span class="image right">![]({{ "assets/img/blog/knock_off_adapter.jpg" | relative_url }})</span>
When it finally arrived in my mailbox (2 days earlier than quoted even!)
it was a blessing in disguise. After plugging it in to power the laptop,
I noticed that magically, some how, both *the audio buzz AND the monitor
flicker* were no more! The problem all along was HP shipping (some of?)
their laptops with defective power adapters.

Upon making this realization, I figured it would be worthwhile to share
it with the world, so here it is: The power adapter makes a difference!
I\'ll say that again: the power adapter makes a difference! Ironically,
in this case, *the knock-off power adapter performed more reliably than
the OEM one ever did*. Which just goes to show you, you don\'t always
get what you pay for.

When it comes to electronics accessories, it is my personal belief, that
there is nothing more overpriced and overrated than name brand cables
and adapters. For cables, if they\'re digital signals (USB, 1394, HDMI)
and shielded, they\'re good enough. I\'ve personally bought two \$7USD
6\' HDMI cables which work flawlessly. I don\'t even know if you can get
ANY HDMI cable at radioshack or the like for under \$10, especially not
a six footer.

I\'m not sure what the moral of the story is, but its a mix between
manufacturers cheaping out on OEM parts, lack of effective support and
recall for widespread problems, and realizing that a power adapter issue
can even cause the kinds of symptoms described above...ultimately
however: keep your eyes open, and when troubleshooting always start from
the ground up!
