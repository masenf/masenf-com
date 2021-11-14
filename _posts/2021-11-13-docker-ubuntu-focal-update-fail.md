---
title: docker: ubuntu focal update fail
author: masen
layout: post
tags: technology
---

While attempting to rebuild a docker container
`FROM` [`phusion/baseimage`](https://github.com/phusion/baseimage-docker)
on my old Raspberry Pi 3 Debian Buster host I ran into the following error:

```
W: GPG error: http://ports.ubuntu.com/ubuntu-ports focal InRelease: At least one invalid signature was encountered.
E: The repository 'http://ports.ubuntu.com/ubuntu-ports focal InRelease' is not signed.
```

Didn't make sense at first, but a [StackOverflow
answer](https://askubuntu.com/a/1264921) pointed me in a direction to
[a bug in `libseccomp2`](https://github.com/moby/moby/issues/40734) -- a
package I've never actually heard of. Short story long, the problem is fixed,
and has been fixed for _years_, but because debian stable is, well, _stable_,
the fix didn't land in the buster repos.

However, installing libseccomp2 2.5.1 from buster-backports on the
host didn't actually resolve the issue.

Another post on the `moby` github issue suggested that docker > 19 has
worked around the issue internally. So I uninstalled all of my previous
docker images and reinitialized via the bootstrap script and was
able to successfully run `apt-get update` on focus-based containers!
