:orphan:

transmission-edit
=================

.. program:: transmission-edit

Synopsis
--------

:program:`transmission-edit` [option...] <torrent-file> ...

Description
-----------

:program:`transmission-edit` command-line utility to modify .torrent files' announce URLs.

Options
-------

.. option:: -h, --help

   Show a short help page and exit.

.. option:: -a, --add <URL>

   Add an announce URL to the torrent's announce-list if it's not already in the list.

.. option:: -d, --delete <URL>

   Remove an announce URL from the torrent's announce-list.

.. option:: -r, --replace <search> <replace>

   Substring search-and-replace inside a torrent's announce URLs. This can be used to change an announce URL when the tracker moves or your passcode changes.

Examples
--------

Update a tracker passcode in all your torrents:

.. code-block:: console

   $ transmission-edit -r old-passcode new-passcode ~/.config/transmission/torrents/*.torrent

See Also
--------

:manpage:`transmission-create(1)`, :manpage:`transmission-daemon(1)`, :manpage:`transmission-gtk(1)`, :manpage:`transmission-qt(1)`, :manpage:`transmission-remote(1)`, :manpage:`transmission-show(1)`

https://www.transmissionbt.com/
