:orphan:

transmission-create
===================

.. program:: transmission-create

Synopsis
--------

:program:`transmission-create` [option...] <source-file | directory>

Description
-----------

:program:`transmission-create` creates BitTorrent .torrent files from the command line.

Options
-------

.. option:: -h, --help

   Show a short help page and exit.

.. option:: -o, --outfile

   Save the generated .torrent to this filename.

.. option:: -p, --private

   Flag the torrent as intended for use on private trackers.

.. option:: -c, --comment

   Add a comment to the torrent file.

.. option:: -s, --piecesize

   Set how many KiB each piece should be, overriding the preferred default.

.. option:: -t, --tracker

   Add a tracker's :term:`announce URL` to the .torrent. Most torrents will have at least one :term:`announce URL`. To add more than one, use this option multiple times.

See Also
--------

:manpage:`transmission-daemon(1)`, :manpage:`transmission-edit(1)`, :manpage:`transmission-gtk(1)`, :manpage:`transmission-qt(1)`, :manpage:`transmission-remote(1)`, :manpage:`transmission-show(1)`

https://transmissionbt.com/
