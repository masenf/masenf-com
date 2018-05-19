---
title: iTunes crashes the OS X Dock
icon: fa-music
author: masen
layout: post
tags: technical short
redirect_from: /blog/itunes-crashes-the-dock.html
---

<span class="image right">![itunes 11 icon]({{ "assets/img/blog/itunes-11-icon.png" | relative_url}})</span>
Since this is the second time I\'ve had this happen to me, I figured
I\'d post the relevant fix here for my future benefit. Essentially what
happens is, everytime the song changes in iTunes, the Dock process gets
an unhandled exception and is forced to restart. I have observed this
under OS X 10.7.4 and OS X 10.7.5 and under iTunes 10.6 and iTunes 11.0.
It only happens when I reformat my disk and then restore my files via
rsync (I don\'t use TimeMachine actually so I\'m not sure if that\'s a
factor or not).

Here\'s the fix:

```
defaults write com.apple.dock itunes-notifications -bool FALSE; killall Dock
```

What\'s going on is the remnants of a hack (hidden) feature of the Dock
in OS X 10.7.\[123\]. In the earlier versions of Lion you could enable a
little dock popup notification everytime the song changed by following
directions
[here](http://osxdaily.com/2011/11/19/show-a-now-playing-itunes-notification-in-the-os-x-dock/)

Unfortunately, Apple broke this feature in the latest Dock builds. Since
it was never a documented feature in the first place, they must have
assumed that defensive coding was unnecessary. Or, perhaps the feature
simply broke, but not enough people are testing it for the bug to be
fixed. At any rate, it was a great feature that I hate to see go. I
suppose now I\'ll have to get GrowlTunes set up for something.
