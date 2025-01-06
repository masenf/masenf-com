---
title: high safari cpu usage on macOS Sequoia 15.2
author: masen
layout: post
tags: technology
---

After upgrading to macOS 15.2, I noticed that Safari CPU usage was consistently around 100%
despite the not having any tabs open or extensions enabled.

To resolve the issue, I removed `Favicon Cache` directory from `~/Library/Safari`.

1. Make sure Safari is closed
2. Open `~/Library/Safari`
    1. From Terminal, `open ~/Library/Safari`
    2. From Finder, ⇧⌘G, `~/Library/Safari`
3. Move `Favicon Cache` to the trash

## Investigation

I tried the usual clear browsing data trick and that didn't seem to have any effect.

Checking the output of `fs_usage -w Safari` shows a lot of `read` traffic on a particular `F=73`
that unfortunately I didn't catch the `open` of in all of my samples.

```console
11:29:17.236585  read              F=73   B=0xa8      0.000002   Safari.40840
11:29:17.236587  read              F=73   B=0x8       0.000001   Safari.40840
11:29:17.236589  read              F=73   B=0x78      0.000001   Safari.40840
11:29:17.236594  read              F=73   B=0x8       0.000001   Safari.40840
11:29:17.236596  read              F=73   B=0x78      0.000001   Safari.40840
11:29:17.236599  read              F=73   B=0x8       0.000001   Safari.40840
11:29:17.236601  read              F=73   B=0x88      0.000001   Safari.40840
11:29:17.236606  read              F=73   B=0x8       0.000001   Safari.40840
11:29:17.236608  read              F=73   B=0x88      0.000001   Safari.40840
```

Eventually found the Stack Overflow Question
[Safari causes high CPU load for no reason, launchservicesd active](https://apple.stackexchange.com/a/475195)
and noticed a lot more `open` calls to the favicon cache database when Safari should have been
essentially idle.

Thankfully this is a cache, not a data directory. So removing it as a test was enough to drop Safari
back into idle usage with no otherwise ill effect.
