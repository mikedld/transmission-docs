.. include:: <isonum.txt>

.. _editing-config-files-ref:

Editing Configuration Files
===========================

It's not always possible to set all configurations from the GUI, especially on the Daemon or the Web Interface. This guide will try to give an overview of how and what you can change. For the location of these files, look at the :ref:`config-files-ref` page.

.. note:: The client *should* be closed before making changes, otherwise settings will be reverted to it's previous state.

Some of Transmission's behavior can also be customized via :ref:`environment variables <env-vars-ref>`.

GTK+ / Qt / Daemon / CLI
------------------------

Overview
~~~~~~~~

GTK+, Qt, CLI, and Daemon (both on a Mac and Linux) use a JSON_ formatted file, mainly because of its human readability.

.. _JSON: http://www.json.org/

Reload Settings
~~~~~~~~~~~~~~~

You can make the daemon reload the settings file by sending it the :c:macro:`SIGHUP` signal.
Or, simply run either of the following commands:

.. code-block:: console

   $ killall -HUP transmission-da

Or:

.. code-block:: console

   $ pkill -HUP transmission-da

Formatting
~~~~~~~~~~

Here is a sample of the three basic types, respectively Boolean, Number and String:

.. code-block:: json

    {
        "rpc-enabled": true,
        "peer-port": 51413,
        "rpc-whitelist": "127.0.0.1,192.168.*.*"
    }

Options
~~~~~~~

Bandwidth
+++++++++

.. trdata:settings_json:: alt-speed-enabled : Boolean = false

   Enable alternate Speed limits (a.k.a. "Turtle Mode").

   .. note:: Clicking the "Turtle" in the GUI when the `scheduler <scheduling_>`_ is enabled will only temporarily remove the scheduled limit until the next cycle.

.. trdata:settings_json:: alt-speed-up : Number (KB/s) = 50

   Alternate upload speed limit.

.. trdata:settings_json:: alt-speed-down : Number (KB/s) = 50

   Alternate download speed limit.

.. trdata:settings_json:: speed-limit-down : Number (KB/s) = 100

   Standard download speed limit (used if enabled).

.. trdata:settings_json:: speed-limit-down-enabled : Boolean = false

   Flag to enable the use of :trdata:settings_json:`speed-limit-down`.

.. trdata:settings_json:: speed-limit-up : Number (KB/s) = 100

   Standard upload speed limit (used if enabled). May need to be set for best performance.

.. trdata:settings_json:: speed-limit-up-enabled : Boolean = false

   Flag to enable the use of :trdata:settings_json:`speed-limit-up`.

.. trdata:settings_json:: upload-slots-per-torrent : Number = 14

Blocklists
++++++++++

.. seealso:: :ref:`blocklists-ref`

.. trdata:settings_json:: blocklist-url : String = "http://www.example.com/blocklist"

.. trdata:settings_json:: blocklist-enabled : Boolean = false

Files and Locations
+++++++++++++++++++

.. trdata:settings_json:: download-dir : String = <platform-specific>

   See :ref:`config-files-locations` for default values.

.. trdata:settings_json:: incomplete-dir : String = <platform-specific>

   Directory to keep files in until torrent is complete.
   See :ref:`config-files-locations` for default values.

.. trdata:settings_json:: incomplete-dir-enabled : Boolean = false

   When enabled, new torrents will download the files to :trdata:settings_json:`incomplete-dir`. When complete, the files will be moved to :trdata:settings_json:`download-dir`.

.. trdata:settings_json:: preallocation : Number = 1

   =====  ============================================
   Value  Meaning
   =====  ============================================
   ``0``  Off
   ``1``  Fast
   ``2``  Full (slower but reduces disk fragmentation)
   =====  ============================================

.. trdata:settings_json:: rename-partial-files : Boolean = true

   Postfix partially downloaded files with ".part".

.. trdata:settings_json:: start-added-torrents : Boolean = true

   Start torrents as soon as they are added.

.. trdata:settings_json:: trash-original-torrent-files : Boolean = false

   Delete torrents added from the watch directory.

.. trdata:settings_json:: umask : Number = 18

   Sets Transmission's file mode creation mask. See :manpage:`umask(2)` for more information. Users who want their saved torrents to be world-writable may want to set this value to ``0``. Bear in mind that the json markup language only accepts numbers in base 10, so the standard :manpage:`umask(2)` octal notation ``022`` is written in settings.json as ``18``.

.. trdata:settings_json:: watch-dir : String

   Directory to watch for new .torrent files to autoload.

.. trdata:settings_json:: watch-dir-enabled : Boolean = false

   Watch a directory for torrent files and add them to Transmission.

   .. note:: When :trdata:settings_json:`watch-dir-enabled` is ``true``, only the :program:`transmission-daemon`, :program:`transmission-gtk`, and :program:`transmission-qt` applications will monitor :trdata:settings_json:`watch-dir` for new .torrent files and automatically load them.

Misc
++++

.. trdata:settings_json:: cache-size-mb : Number (MB) = 4

   Size to allocate for Transmission's memory cache. The cache is used to help batch disk IO together, so increasing the cache size can be used to reduce the number of disk reads and writes. Default is ``2`` if configured with :option:`--enable-lightweight`.

.. trdata:settings_json:: dht-enabled : Boolean = true

   Enable `Distributed Hash Table (DHT) <DHT_>`_.

.. trdata:settings_json:: encryption : Number = 1

   Encryption_ preference. Encryption may help get around some ISP filtering, but at the cost of slightly higher CPU use.

   =====  ==============================
   Value  Meaning
   =====  ==============================
   ``0``  Prefer unencrypted connections
   ``1``  Prefer encrypted connections
   ``2``  Require encrypted connections
   =====  ==============================

.. trdata:settings_json:: lazy-bitfield-enabled : Boolean = true

   May help get around some ISP filtering. `Vuze specification`_.

.. trdata:settings_json:: lpd-enabled : Boolean = false

   Enable `Local Peer Discovery (LPD) <LPD_>`_.

.. trdata:settings_json:: message-level : Number = 2

   Set verbosity of transmission messages.

   =====  =======
   Value  Meaning
   =====  =======
   ``0``  None
   ``1``  Error
   ``2``  Info
   ``3``  Debug
   =====  =======

.. trdata:settings_json:: pex-enabled : Boolean = true

   Enable `Peer Exchange (PEX) <PEX_>`_.

.. trdata:settings_json:: prefetch-enabled : Boolean = true

   When enabled, Transmission will hint to the OS which piece data it's about to read from disk in order to satisfy requests from peers. On Linux, this is done by passing :c:macro:`POSIX_FADV_WILLNEED` to :manpage:`posix_fadvise(2)`. On OS X, this is done by passing :c:macro:`F_RDADVISE` to :manpage:`fcntl(2)`. This defaults to ``false`` if configured with :option:`--enable-lightweight`.

.. trdata:settings_json:: scrape-paused-torrents-enabled : Boolean = true

.. trdata:settings_json:: script-torrent-done-enabled : Boolean = false

   Run a script at torrent completion.

.. trdata:settings_json:: script-torrent-done-filename : String = ""

   Path to script.

.. trdata:settings_json:: utp-enabled : Boolean = true

   Enable `Micro Transport Protocol (µTP) <UTP_>`_.

.. _DHT: http://wiki.theory.org/BitTorrentSpecification#Distributed_Hash_Table
.. _LPD: http://en.wikipedia.org/wiki/Local_Peer_Discovery
.. _PEX: http://en.wikipedia.org/wiki/Peer_exchange
.. _Encryption: http://wiki.vuze.com/w/Message_Stream_Encryption
.. _Vuze specification: http://wiki.vuze.com/w/Commandline_options#Network_Options
.. _UTP: http://en.wikipedia.org/wiki/Micro_Transport_Protocol

Peers
+++++

.. trdata:settings_json:: bind-address-ipv4 : String = "0.0.0.0"

   Where to listen for peer connections.

.. trdata:settings_json:: bind-address-ipv6 : String = "::"

   Where to listen for peer connections.

.. trdata:settings_json:: peer-congestion-algorithm : String

   This is documented on http://www.pps.jussieu.fr/~jch/software/bittorrent/tcp-congestion-control.html.

.. trdata:settings_json:: peer-id-ttl-hours : Number = 6

   Recycle the peer id used for public torrents after *N* hours of use.

.. trdata:settings_json:: peer-limit-global : Number = 240

   Maximum number of connected peers.

.. trdata:settings_json:: peer-limit-per-torrent : Number = 60

   Maximum number of connected peers for an individual torrent.

.. trdata:settings_json:: peer-socket-tos : String = "default"

   Set the `Type-Of-Service (TOS) <TOS_>`_ parameter for outgoing TCP packets. The value ``"lowcost"`` is recommended if you're using a smart router, and shouldn't harm in any case.

   =================  ===================
   Value              Meaning
   =================  ===================
   ``"default"``
   ``"lowcost"``
   ``"throughput"``
   ``"lowdelay"``
   ``"reliability"``
   =================  ===================

.. _TOS: http://en.wikipedia.org/wiki/Type_of_Service

Peer Port
+++++++++

.. trdata:settings_json:: peer-port : Number = 51413

   Port to listen on for incoming Peer connections.

.. trdata:settings_json:: peer-port-random-high : Number = 65535

   Highest permitted value for a randomly assigned :trdata:settings_json:`peer-port`.

.. trdata:settings_json:: peer-port-random-low : Number = 1024

   Lowest permitted value for a randomly assigned :trdata:settings_json:`peer-port`.

.. trdata:settings_json:: peer-port-random-on-start : Boolean = false

   If true then assign a random :trdata:settings_json:`peer-port` between the :trdata:settings_json:`peer-port-random-low` and :trdata:settings_json:`peer-port-random-high` values.

.. trdata:settings_json:: port-forwarding-enabled : Boolean = true

   Enable UPnP_ or NAT-PMP_ protocols to try and negotiate opening of selected :trdata:settings_json:`peer-port` with firewalls that support such negotiation. Security-conscious or advanced users may want to disable this feature.

.. _UPnP: http://en.wikipedia.org/wiki/Universal_Plug_and_Play
.. _NAT-PMP: http://en.wikipedia.org/wiki/NAT_Port_Mapping_Protocol

Queuing
+++++++

.. trdata:settings_json:: download-queue-enabled : Boolean = true

   When ``true``, Transmission will only download :trdata:settings_json:`download-queue-size` non-stalled torrents at once.

.. trdata:settings_json:: download-queue-size : Number = 5

   See :trdata:settings_json:`download-queue-enabled`.

.. trdata:settings_json:: queue-stalled-enabled : Boolean = true

   When ``true``, torrents that have not shared data for :trdata:settings_json:`queue-stalled-minutes` are treated as "stalled" and are not counted against the :trdata:settings_json:`download-queue-size` and :trdata:settings_json:`seed-queue-size` limits.

.. trdata:settings_json:: queue-stalled-minutes : Number = 30

   See :trdata:settings_json:`queue-stalled-enabled`.

.. trdata:settings_json:: seed-queue-enabled : Boolean = false

   When ``true``, Transmission will only seed :trdata:settings_json:`seed-queue-size` non-stalled torrents at once.

.. trdata:settings_json:: seed-queue-size : Number = 10

   See :trdata:settings_json:`seed-queue-enabled`.

RPC
+++

.. seealso:: :ref:`rpc-ref`

.. trdata:settings_json:: rpc-authentication-required : Boolean = false

   If set, then a username and password are required to access the remote control services.

.. trdata:settings_json:: rpc-bind-address : String = "0.0.0.0"

   Where to listen for RPC connections.

.. trdata:settings_json:: rpc-enabled : Boolean = true

   Enables remote control services.

.. trdata:settings_json:: rpc-password : String

   The ssha1 encrypted password (starts with a ``{``) needed for remote access. A new password can be entered via command line utilities or directly in plain text and will be replaced with the encrypted version when the configuration file is next saved.

.. trdata:settings_json:: rpc-port : Number = 9091

   The port Transmission listens on for remote services.

.. trdata:settings_json:: rpc-url : String = "/transmission/"

   Added in v2.2.

.. trdata:settings_json:: rpc-username : String

   The username required to access remote services when :trdata:settings_json:`rpc-authentication-required` is enabled.

.. trdata:settings_json:: rpc-whitelist : String = "127.0.0.1"

   Comma-delimited list of IP addresses from which remote control is permitted. Wildcards allowed using ``"*"``. Example: ``"127.0.0.*,192.168.*.*"``.

.. trdata:settings_json:: rpc-whitelist-enabled : Boolean = true

   If enabled use :trdata:settings_json:`rpc-whitelist`. Other IP addresses will be denied remote access.

Scheduling
++++++++++

.. trdata:settings_json:: alt-speed-time-enabled : Boolean = false

   .. note:: When enabled, this will toggle the :trdata:settings_json:`alt-speed-enabled` setting.

.. trdata:settings_json:: alt-speed-time-begin : Number (minutes from midnight) = 540 (9am)

.. trdata:settings_json:: alt-speed-time-end : Number (minutes from midnight) = 1020 (5pm)

.. trdata:settings_json:: alt-speed-time-day : Number/bitfield = 127 (all days)

   Start with ``0``, then for each day you want the scheduler enabled, add:

   =========  =======  ===========
   Day        Decimal  Binary
   =========  =======  ===========
   Sunday     ``1``    ``0000001``
   Monday     ``2``    ``0000010``
   Tuesday    ``4``    ``0000100``
   Wednesday  ``8``    ``0001000``
   Thursday   ``16``   ``0010000``
   Friday     ``32``   ``0100000``
   Saturday   ``64``   ``1000000``
   =========  =======  ===========

   Examples:

   ========  =======  ===========
   Days      Decimal  Binary
   ========  =======  ===========
   Weekdays  ``62``   ``0111110``
   Weekends  ``65``   ``1000001``
   All days  ``127``  ``1111111``
   ========  =======  ===========

.. trdata:settings_json:: idle-seeding-limit : Number = 30

   Stop seeding after being idle for *N* minutes.

.. trdata:settings_json:: idle-seeding-limit-enabled : Boolean = false

.. trdata:settings_json:: ratio-limit : Number = 2.0

   Ratio of uploads:downloads for a torrent before torrent is deemed complete. Ratio should be at least ``1.0`` for normal use, ``2.0`` is considered "good".

.. trdata:settings_json:: ratio-limit-enabled : Boolean = false

   By default torrents will seed forever (i.e. Ratio |rarr| infinity).

Legacy Options
~~~~~~~~~~~~~~

Only keys that differ from above are listed here. These options have been replaced in newer versions of Transmission.

2.31 (and older)
++++++++++++++++

.. trdata:settings_json:: open-file-limit : Number = 32

1.5x (and older)
++++++++++++++++

Bandwidth
`````````

.. trdata:settings_json:: download-limit : Number (KB/s) = 100

.. trdata:settings_json:: download-limit-enabled : Boolean = false

.. trdata:settings_json:: upload-limit : Number (KB/s) = 100

.. trdata:settings_json:: upload-limit-enabled : Boolean = false

Peer Port
`````````

.. trdata:settings_json:: peer-port-random-enabled : Boolean = false

1.4x (and older)
++++++++++++++++

Proxy
`````

.. trdata:settings_json:: proxy-authentication : String

.. trdata:settings_json:: proxy-authentication-required : Boolean = 0

.. trdata:settings_json:: proxy-port : Number = 80

.. trdata:settings_json:: proxy-server : String

.. trdata:settings_json:: proxy-server-enabled : Boolean = 0

.. trdata:settings_json:: proxy-type : Number = 0

   =====  =======
   Value  Meaning
   =====  =======
   ``0``  HTTP
   ``1``  SOCKS4
   ``2``  SOCKS5
   =====  =======

.. trdata:settings_json:: proxy-username : String

Peers
`````

.. trdata:settings_json:: max-peers-global : Number = 240

.. trdata:settings_json:: max-peers-per-torrent : Number = 60

1.3x (and older)
++++++++++++++++

RPC
```

.. seealso:: :ref:`rpc-ref`

.. trdata:settings_json:: rpc-access-control-list : String = "+127.0.0.1"

   Comma-delimited list of IP addresses prefixed with ``"+"`` or ``"-"``. Wildcards allowed using ``"*"``. Example: ``"+127.0.0.*,-192.168.*.*"``.

Mac OS X
--------

Overview
~~~~~~~~

Mac OS X has a standardized way of saving user preferences files using XML_ format. These files are called plist_ (short for property list) files. Usually there is no need to modify these files directly, since Apple provided a :manpage:`defaults(1)` command-line tool to reliably change settings. You do need to restart Transmission before these changes have effect.

In short:

* To set a key:

  .. code-block:: console

     $ defaults write org.m0k.transmission <key> <value>

* To reset a key:

  .. code-block:: console

     $ defaults delete org.m0k.transmission <key>

.. _XML: http://en.wikipedia.org/wiki/XML
.. _plist: http://en.wikipedia.org/wiki/Plist

Options
~~~~~~~

.. trdata:settings_plist:: PeerSocketTOS : Number = 0
