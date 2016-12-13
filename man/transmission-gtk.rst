:orphan:

transmission-gtk
================

.. program:: transmission-gtk

Synopsis
--------

:program:`transmission-gtk` [option...] [torrent-file | magnet-url] ...

Description
-----------

:program:`transmission-gtk` is a fast and easy BitTorrent client.

BitTorrent is a peer-to-peer file transfer protocol which uses a metainfo file (usually with the .torrent file extension) and a central tracker to distribute file data amongst a group of peers. For more information on the Bit‐Torrent protocol see http://www.bittorrent.org/.

Options
-------

.. option:: -h, --help

   Show help options.

.. option:: -p, --paused

   Start with all torrents paused.

.. option:: -m, --minimized

   Start minimized in notification area.

.. option:: -g, --config-dir <directory>

   Where to look for configuration files. This can be used to swap between using the cli, daemon, gtk, and qt clients. See https://trac.transmissionbt.com/wiki/ConfigFiles for more information.

   Multiple .torrent files may be added at startup by appending them on the command line. If :program:`transmission-gtk` is already running, the torrents will be added to the running instance.

Environment
-----------

.. envvar:: TRANSMISSION_HOME

   Sets the default config-dir.

.. envvar:: http_proxy

   libcurl uses this environment variable when performing tracker announces. If set, this overrides the GNOME proxy preferences.

Files
-----

:file:`~/.config/transmission`
    The config-dir used when neither :envvar:`TRANSMISSION_HOME` nor :option:`-g` is specified.

See Also
--------

:manpage:`transmission-create(1)`, :manpage:`transmission-daemon(1)`, :manpage:`transmission-edit(1)`, :manpage:`transmission-qt(1)`, :manpage:`transmission-remote(1)`, :manpage:`transmission-show(1)`

https://www.transmissionbt.com/
