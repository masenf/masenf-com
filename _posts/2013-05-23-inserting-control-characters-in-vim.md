---
title: inserting control characters in vim
author: masen
layout: post
tags: technical short
redirect_from: /blog/inserting-control-characters-in-vim.html
---

There comes a time in every Unix user\'s life where they need to enter
control characters into their editor. Maybe you\'re trying to add some
ASCII BEL characters to annoy would-be cat\'ers, or add some null
characters or something, but most likely you want to search and replace!

Simply typing the control character itself is insufficient. **You need
the escape control character** to escape your control character.
Consequently, this is CTRL+V.

So to remove all the pesky \^@ from your pristine file, the keystrokes
would be:

    : % s / CTRL v CTRL @ / / g

You\'ll notice the CTRL+V adds a caret, and the CTRL+@ add the @. This
is also good for those \^M filled files that come out of script(1)
