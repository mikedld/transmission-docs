:orphan:

transmission-daemon
===================

.. program:: transmission-daemon

Synopsis
--------

:program:`transmission-daemon` [option...]

Description
-----------

:program:`transmission-daemon` is a daemon-based Transmission session that can be controlled via RPC commands from transmission's web interface or :manpage:`transmission-remote(1)`.

Options
-------

.. option:: -a, --allowed x.x.x.x,...

   Allow RPC access to a comma-delimited whitelist of IP addresses.  Wildcards can be specified in an address by using ``"*"``.  Default: ``"127.0.0.1"`` Example: ``"127.0.0.*,192.168.1.*"``.

.. option:: -b, --blocklist

   Enable peer blocklists. Transmission understands the bluetack blocklist file format.  New blocklists can be added by copying them into the config-dir's "blocklists" subdirectory.

.. option:: -B, --no-blocklist

   Disble blocklists.

.. option:: -c <directory>

   Directory to watch for new .torrent files to be added. As they are added to this directory, the daemon will load them into Transmission.

.. option:: -C

   Do not watch for new .torrent files.

.. option:: -d

   Dump transmission-daemon's settings to stderr.

.. option:: -f, --foreground

   Run in the foreground and print errors to stderr.

.. option:: -g, --config-dir <directory>

   Where to look for configuration files. This can be used to swap between using the CLI, daemon, GTK+, and Qt clients. See https://trac.transmissionbt.com/wiki/ConfigFiles for more information.

.. option:: -er, --encryption-required

   Encrypt all peer connections.

.. option:: -ep, --encryption-preferred

   Prefer encrypted peer connections.

.. option:: -et, --encryption-tolerated

   Prefer unencrypted peer connections.

.. option:: -gsr, --global-seedratio <ratio>

   All torrents, unless overridden by a per-torrent setting, should seed until a specific ratio.

.. option:: -GSR, --no-global-seedratio

   All torrents, unless overridden by a per-torrent setting, should seed regardless of ratio

.. option:: -h, --help

   Print command-line option descriptions.

.. option:: --incomplete-dir <dir>

   When adding new torrents, store their contents in directory until the torrent is done.

.. option:: --no-incomplete-dir

   Don't store incomplete torrents in a different directory.

.. option:: -i, --bind-address-ipv4

   Listen for IPv4 BitTorrent connections on a specific address. Only one IPv4 listening address is allowed. Default: ``"0.0.0.0"`` (all addresses).

.. option:: -I, --bind-address-ipv6

   Listen for IPv6 BitTorrent connections on a specific address. Only one IPv6 listening address is allowed. Default: ``"::"`` (all addresses).

.. option:: -r, --rpc-bind-address

   Listen for RPC connections on a specific address. This must be an IPv4 address. Only one RPC listening address is allowed. Default: ``"0.0.0.0"`` (all addresses).

.. option:: --paused

   Pause all torrents on startup.

.. option:: -L, --peerlimit-global <limit>

   Overall peer limit. Useful on embedded systems where the default might be unsuitable. Default: ``240``.

.. option:: -l, --peerlimit-torrent <limit>

   Peer limit per torrent. Useful on embedded systems where the default might be unsuitable. Default: ``60``.

.. option:: -m, --portmap

   Enable portmapping via NAT-PMP or UPnP.

.. option:: -M, --no-portmap

   Disable portmapping.

.. option:: -o, --dht

   Enable distributed hash table (DHT).

.. option:: -O, --no-dht

   Disable distribued hash table (DHT).

.. option:: -p, --port <port>

   Port to open and listen for RPC requests on. Default: ``9091``.

.. option:: -P, --peerport <port>

   Port to listen for incoming peers on. Default: ``51413``.

.. option:: -t, --auth

   Require clients to authenticate themselves. This doesn't do much good unless username and password are also set.

.. option:: -T, --no-auth

   Don't require authentication from clients.

.. option:: -u, --username <username>

   Used for client authentication.

.. option:: -v, --password <password>

   Used for client authentication.

.. option:: -V, --version

   Show version number and exit.

.. option:: --utp

   Enable uTP for peer connections.

.. option:: --no-utp

   Disable uTP for peer connections.

.. option:: -w, --download-dir

   Where to store downloaded data.

.. option:: -e, --logfile

   Where to store transmission's log messages.

.. option:: --log-error

   Show error messages.

.. option:: --log-info

   Show error and info messages.

.. option:: --log-debug

   Show error, info, and debug messages.

Environment
-----------

.. envvar:: TRANSMISSION_HOME

   Sets the default config-dir.

.. envvar:: http_proxy

   libcurl uses this environment variable when performing tracker announces.

Files
-----

:file:`~/.config/transmission-daemon`
    The config-dir used when neither :envvar:`TRANSMISSION_HOME` nor :option:`-g` is specified.  See https://trac.transmissionbt.com/wiki/ConfigFiles for more information.

See Also
--------

:manpage:`transmission-create(1)`, :manpage:`transmission-edit(1)`, :manpage:`transmission-gtk(1)`, :manpage:`transmission-qt(1)`, :manpage:`transmission-remote(1)`, :manpage:`transmission-show(1)`

https://www.transmissionbt.com/
