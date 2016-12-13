:orphan:

transmission-cli
================

.. program:: transmission-cli

Synopsis
--------

:program:`transmission-cli` [option...] <torrent-file | magnet-url>

Description
-----------

The :program:`transmission-cli` program is a lightweight, command-line BitTorrent client with scripting capabilities.

Options
-------

.. option:: -b, --blocklist

   Enable peer blocklists. Transmission understands the bluetack blocklist file format. New blocklists can be added by copying them into the config-dir's :file:`blocklists` subdirectory.

.. option:: -B, --no-blocklist

   Disble blocklists.

.. option:: -d, --downlimit <number>

   Set the maximum download speed in KB/s.

.. option:: -D, --no-downlimit

   Don't limit the download speed.

.. option:: -er, --encryption-required

   Encrypt all peer connections.

.. option:: -ep, --encryption-preferred

   Prefer encrypted peer connections.

.. option:: -et, --encryption-tolerated

   Prefer unencrypted peer connections.

.. option:: -f, --finish <script>

   Set a script to run when the torrent finishes.

.. option:: -g, --config-dir <directory>

   Where to look for configuration files. This can be used to swap between using the CLI, daemon, GTK+, and Qt clients. See https://trac.transmissionbt.com/wiki/ConfigFiles for more information.

.. option:: -h, --help

   Prints a short usage summary.

.. option:: -m, --portmap

   Enable portmapping via NAT-PMP or UPnP.

.. option:: -M, --no-portmap

   Disable portmapping.

.. option:: -n, --new <sourcefile>

   Create torrent from the specified file or directory.

.. option:: -p, --port <port>

   Set the port to listen for incoming peers. Default: 51413.

.. option:: -t, --tos <tos>

   Set the peer socket TOS for local router-based traffic shaping. Valid values are ``"default"``, ``"lowcost"``, ``"throughput"``, ``"reliability"``, ``"lowdelay"``, a decimal value (``0``-``255``) or a hexidecimal value (``0x00``-``0xff``).

.. option:: -u, --uplimit <number>

   Set the maximum upload speed in KB/s.

.. option:: -U, --no-uplimit

   Don't limit the upload speed.

.. option:: -v, --verify

   Verify the torrent's downloaded data.

.. option:: -w, --download-dir <directory>

   Where to save downloaded data.

Signals
-------

In addition to these options, sending transmission-cli a :c:macro:`SIGHUP` signal will contact the tracker for more peers.

Environment
-----------

.. envvar:: TRANSMISSION_HOME

   Sets the default config-dir.

.. envvar:: http_proxy

   libcurl uses this environment variable when performing tracker announces.

Files
-----

:file:`~/.config/transmission`
    Directory where transmission-cli keeps torrent information for future seeding and resume operations.

See Also
--------

:manpage:`transmission-create(1)`, :manpage:`transmission-daemon(1)`, :manpage:`transmission-edit(1)`, :manpage:`transmission-gtk(1)`, :manpage:`transmission-qt(1)`, :manpage:`transmission-remote(1)`, :manpage:`transmission-show(1)`

https://transmissionbt.com/
