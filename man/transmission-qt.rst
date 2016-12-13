:orphan:

transmission-qt
===============

.. program:: transmission-qt

Synopsis
--------

:program:`transmission-qt` [option...] [torrent-file | magnet-url] ...

Description
-----------

:program:`transmission-qt` is a fast and easy BitTorrent client.

BitTorrent is a peer-to-peer file transfer protocol which uses a metainfo file (usually with the .torrent file extension) and a central tracker to distribute file data amongst a group of peers. For more information on the Bit‐Torrent protocol see http://www.bittorrent.org/.

Options
-------

.. option:: -h, --help

   Show help options.

.. option:: -g, --config-dir <directory>

   Where to look for configuration files. This can be used to swap between using the CLI, daemon, GTK+, and Qt clients. See https://trac.transmissionbt.com/wiki/ConfigFiles for more information.

.. option:: -m, --minimized

   Start minimized in notification area.

.. option:: -p, --port <port>

   Port to use when connecting to an existing session.

.. option:: -r, --remote <host>

   Connect to an existing session at the specified hostname.

.. option:: -u, --username <username>

   Username to use when connecting to an existing session.

.. option:: -v, --version

   Show version number and exit.

.. option:: -w, --password <password>

   Password to use when connecting to an existing session.

Multiple .torrent files may be added at startup by appending them on the command line. If :program:`transmission-qt` is already running, the torrents will be added to the running instance.

Environment
-----------

.. envvar:: TRANSMISSION_HOME

   Sets the default config-dir.

Files
-----

:file:`~/.config/transmission`
    The config-dir used when neither :envvar:`TRANSMISSION_HOME` nor :option:`-g` is specified.

See Also
--------

:manpage:`transmission-create(1)`, :manpage:`transmission-daemon(1)`, :manpage:`transmission-edit(1)`, :manpage:`transmission-gtk(1)`, :manpage:`transmission-remote(1)`, :manpage:`transmission-show(1)`

https://www.transmissionbt.com/
