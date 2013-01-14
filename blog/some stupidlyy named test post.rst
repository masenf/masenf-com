:author masen
:published 1357467272
:modified 1357467284
:tag pointless
:tag test
:title This is a test post
:slug my-test-post

This is a test post
===================

    It's written in **restructured** Text

    It also has a very *unfortunate* name in the filesystem

.. image:: /img/blog/poor.jpg
   :alt: african folks


.. code:: python

    # strip extraneous lists
    def flatten_list(l):
        if type(l) != list:
            return str(l)
        if len(l) < 1:
            return ""
        elif len(l) == 1:
            return flatten_list(l[0])
        else:
            return map(flatten_list, l)

