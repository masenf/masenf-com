:author masen
:title gnupg arch pinentry
:published 1384302267
:modified 1428727236
:slug gnupg-arch-pinentry
:tag technical
:tag fix

.. figure:: /img/blog/gnupg.png
   :alt: gnupg logo
   :figclass: float-right

I always get a pleasant feeling when I recieve a PGP encrypted file or message,
but the message isn't much good if I can't read it. Unfortunately, as I receive
so few of such messages, my setup decays without daily use and becomes broken.

Case in point: Decrypting a message using GnuPG on a headless Arch Linux box:

**Case in point 2 (added 2015-04-10): this just happened again, I should maybe 
submit a patch?**

* gnupg has a dependency on pinentry_ 
* the pinentry package in Arch has this `closed bug`_ (closed as 'not a bug',
  you need to install the appropriate optdepends -- my ass)
* "The PKGBUILD deletes pinetry and symlinks it to pinentry-gtk-2"
* This is still an issue with the latest packages
* Today manifesting itself in the following error message::

    pinentry: error while loading shared libraries: libgtk-x11-2.0.so.0: cannot open shared object file: No such file or directory
    gpg-agent[1652]: can't connect to the PIN entry module: End of file
    gpg-agent[1652]: command get_passphrase failed: No pinentry
    gpg: problem with the agent: No pinentry

The solution is ridiculously simple, and I'm surprised that no action was taken
to resolve the bug three years ago when it was reported. At any rate::

    # rm /usr/bin/pinentry && ln -s pinentry-curses /usr/bin/pinentry

You may also need to set the TTY if you see the following message when trying
to use gpg (source_)::

    pinentry-curses: no LC_CTYPE known assuming UTF-8

Ensure that you are the owner of the current TTY::
    
    ls -l $(tty)

Take ownership if necessary::
    
    chown masen $(tty)

Tell gpg where to tell pinentry to draw its box::

    export GPG_TTY=$(tty)

After that, I was able to use gpg to enter my key passphrase. If you don't use a
passphrase, this obviously won't be a problem for you. If you don't use a passphrase,
**you should**. If you have questions or comments, `encrypt and send`_

.. _pinentry: https://www.archlinux.org/packages/core/i686/pinentry/
.. _closed bug: https://bugs.archlinux.org/task/21199
.. _source: http://superuser.com/questions/148313/gpg-symmetric-encryption-using-pipes
.. _encrypt and send: /page/contact.html
