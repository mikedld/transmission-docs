:orphan:

transmission-remote
===================

.. program:: transmission-remote

Synopsis
--------

:program:`transmission-remote` [host:port | host | port] [option...]

Description
-----------

:program:`transmission-remote` is a remote control utility for :manpage:`transmission(1)` and :manpage:`transmission-daemon(1)`.

By default, :program:`transmission-remote` connects to the transmission session at ``localhost:9091``. Other sessions can be controlled by specifying a different host and/or port.

Options
-------

.. option:: -a, --add <filenames-or-URLs>

   Add torrents to transmission.

.. option:: -b, --debug

   Enable debugging mode.

.. option:: -as, --alt-speed

   Use the alternate Limits.

.. option:: -AS, --no-alt-speed

   Don't use the alternate Limits.

.. option:: -asd, --alt-speed-downlimit <limit>

   Limit the alternate download speed to limit kilobytes per second.

.. option:: -asu, --alt-speed-uplimit <limit>

   Limit the alternate upload speed to limit kilobytes per second.

.. option:: -asc, --alt-speed-scheduler

   Use the scheduled on/off times.

.. option:: -ASC, --no-alt-speed-scheduler

   Don't use the scheduled on/off days and times.

.. option:: --alt-speed-time-begin <time>

   Time to start using the alt speed limits (in ``hhmm``).

.. option:: --alt-speed-time-end <time>

   Time to stop using the alt speed limits (in ``hhmm``).

.. option:: --alt-speed-days <days>

   Set the number of days on which to enable the speed scheduler, using a list such as ``"2,4-6"``.

.. option:: --torrent-done-script <filename>

   Specify a file to run each time a torrent finishes.

.. option:: --no-torrent-done-script

   Don't run any script when a torrent finishes.

.. option:: -c, --incomplete-dir <dir>

   When adding new torrents, store their contents in directory until the torrent is done.

.. option:: -C, --no-incomplete-dir

   Don't store incomplete torrents in a different directory.

.. option:: -d, --downlimit <limit>

   Limit the maximum download speed to limit kB/s. If current torrent(s) are selected this operates on them. Otherwise, it changes the global setting.

.. option:: -D, --no-downlimit

   Disable download speed limits. If current torrent(s) are selected this operates on them. Otherwise, it changes the global setting.

.. option:: -e, --cache <size>

   Set the session's maximum memory cache size in MiB. This cache is used to reduce disk IO.

.. option:: -er, --encryption-required

   Encrypt all peer connections.

.. option:: -ep, --encryption-preferred

   Prefer encrypted peer connections.

.. option:: -et, --encryption-tolerated

   Prefer unencrypted peer connections.

.. option:: --exit

   Tell the Transmission to initiate a shutdown.

.. option:: -f, --files

   Get a file list for the current torrent(s).

.. option:: -g, --get <all | file-index | files>

   Mark file(s) for download. Literal ``all`` marks all all of the torrent's files for downloading, file-index adds a single file to the download list, and files adds multiple files to the download list, such as ``"-g1,3-5"`` to add files #1, #3, #4, and #5 to the download list.

.. option:: -G, --no-get <all | file-index | files>

   Mark file(s) for not downloading.

.. option:: -gsr, --global-seedratio <ratio>

   All torrents, unless overridden by a per-torrent setting, should seed until a specific ratio.

.. option:: -GSR, --no-global-seedratio

   All torrents, unless overridden by a per-torrent setting, should seed regardless of ratio.

.. option:: -h, --help

   Print command-line option descriptions.

.. option:: -i, --info

   Show details of the current torrent(s).

.. option:: -if, --info-files

   List the specified torrent's files.

.. option:: -ip, --info-peers

   List the specified torrent's peers.

.. option:: -ic, --info-pieces

   List the specified torrent's pieces.

.. option:: -it, --info-trackers

   List the specified torrent's trackers.

.. option:: -si, --session-info

   List session information from the server.

.. option:: -st, --session-stats

   List statistical information from the server.

.. option:: -l, --list

   List all torrents.

.. option:: -m, --portmap

   Enable portmapping via NAT-PMP or UPnP.

.. option:: -M, --no-portmap

   Disable portmapping.

.. option:: -n, --auth <username:password>

   Set the username and password for authentication.

.. option:: -ne, --authenv

   Set the authentication information from the :envvar:`TR_AUTH` environment variable which must be formatted as username:password.

.. option:: -N, --netrc <filename>

   Set the authentication information from a netrc file. See :manpage:`netrc(5)` for more information.

.. option:: -o, --dht

   Enable distributed hash table (DHT).

.. option:: -O, --no-dht

   Disable distribued hash table (DHT).

.. option:: -p, --port <port>

   Set the port for use when listening for incoming peer connections.

.. option:: -Bh, --bandwidth-high

   Give this torrent first chance at available bandwidth.

.. option:: -Bn, --bandwidth-normal

   Give this torrent the bandwidth left over by high priority torrents.

.. option:: -Bl, --bandwidth-low

   Give this torrent the bandwidth left over by high and normal priority torrents.

.. option:: -ph, --priority-high <all | file-index | files>

   Try to download the specified file(s) first. Literal ``all`` marks all of the torrent's files as normal priority, file-index sets a single file's priority as normal, and files sets multiple files' priorities as normal, such as ``"-pn1,3-5"`` to normalize files #1, #3, #4, and #5.

.. option:: -pn, --priority-normal <all | file-index | files>

   Try to download the specified files normally.

.. option:: -pl, --priority-low <all | file-index | files>

   Try to download the specified files last.

.. option:: -pr, --peers number

   Set the maximum number of peers. If current torrent(s) are selected this operates on them. Otherwise, it changes the global setting.

.. option:: -r, --remove

   Remove the current torrent(s). This does not delete the downloaded data.

.. option:: -rad, --remove-and-delete

   Remove the current torrent(s) and delete their downloaded data.

.. option:: --reannounce

   Reannounce the current torrent(s). This is the same as the GUI's :guilabel:`Ask tracker for more peers` button.

.. option:: --move

   Move the current torrents' data from their current locations to the specified directory.

.. option:: --find

   Tell Transmission where to look for the current torrents' data.

.. option:: -sr, --seedratio <ratio>

   Let the current torrent(s) seed until a specific ratio.

.. option:: -SR, --no-seedratio

   Let the current torrent(s) seed regardless of ratio.

.. option:: -srd, --seedratio-default

   Let the current torrent(s) use the global seedratio settings.

.. option:: -td, --tracker-add <tracker>

   Add a tracker to a torrent.

.. option:: -tr, --tracker-remove <tracker-id>

   Remove a tracker from a torrent.

.. option:: -s, --start

   Start the current torrent(s).

.. option:: -S, --stop

   Stop the current torrent(s) from downloading or seeding.

.. option:: --start-paused

   Start added torrents paused.

.. option:: --no-start-paused

   Start added torrents unpaused.

.. option:: -t, --torrent <all | active | id | torrent-hash>

   Set the current torrent(s) for use by subsequent options. The literal ``all`` will apply following requests to all torrents; the literal ``active`` will apply following requests to recently-active torrents; and specific torrents can be chosen by id or hash. To set more than one current torrent, join their ids together in a list, such as ``"-t2,4,6-8"`` to operate on the torrents whose IDs are 2, 4, 6, 7, and 8.

.. option:: --trash-torrent

   Delete torrents after adding.

.. option:: --no-trash-torrent

   Do not delete torrents after adding.

.. option:: -hl, --honor-session

   Make the current torrent(s) honor the session limits.

.. option:: -HL, --no-honor-session

   Make the current torrent(s) not honor the session limits.

.. option:: -u, --uplimit <limit>

   Limit the maximum upload speed to limit kB/s. If current torrent(s) are selected this operates on them. Otherwise, it changes the global setting.

.. option:: -U, --no-uplimit

   Disable upload speed limits.

.. option:: --utp

   Enable uTP for peer connections.

.. option:: --no-utp

   Disable uTP for peer connections. If current torrent(s) are selected this operates on them. Otherwise, it changes the global setting.

.. option:: -v, --verify

   Verify the current torrent(s).

.. option:: -V, --version

   Show version number and exit.

.. option:: -w, --download-dir <directory>

   When used in conjunction with :option:`--add`, set the new torrent's download folder. Otherwise, set the default download folder.

.. option:: -x, --pex

   Enable peer exchange (PEX).

.. option:: -X, --no-pex

   Disable peer exchange (PEX).

.. option:: -y, --lds

   Enable local peer discovery (LPD).

.. option:: -Y, --no-lds

   Disable local peer discovery (LPD).

.. option:: -pi, --peer-info

   List the current torrent's connected peers. In the "status" section of the list, the following shorthand is used:

    .. only:: format_man

       | D: Downloading from this peer
       | d: We would download from this peer if they would let us
       | E: Encrypted connection
       | H: Peer was found through DHT
       | I: Peer is an incoming connection
       | K: Peer has unchoked us but we are not interested
       | O: Optimistic unchoked
       | T: Peer is connected over uTP
       | U: Uploading to peer
       | u: We would upload to this peer if they asked
       | X: Peer was discovered through Peer Exchange (PEX)
       | ?: We unchoked this peer but they are not interested

   .. only:: not format_man

      =====  =====================================================
      `` ``  Description
      =====  =====================================================
      ``D``  Downloading from this peer
      ``d``  We would download from this peer if they would let us
      ``E``  Encrypted connection
      ``H``  Peer was found through DHT
      ``I``  Peer is an incoming connection
      ``K``  Peer has unchoked us but we are not interested
      ``O``  Optimistic unchoked
      ``T``  Peer is connected over uTP
      ``U``  Uploading to peer
      ``u``  We would upload to this peer if they asked
      ``X``  Peer was discovered through Peer Exchange (PEX)
      ``?``  We unchoked this peer but they are not interested
      =====  =====================================================

.. option:: --blocklist-update

   Update blocklist from URL specified in remote client's settings with blocklist-url key.

Examples
--------

List all torrents:

.. code-block:: console

   $ transmission-remote -l

List all active torrents:

.. code-block:: console

   $ transmission-remote -tactive -l

Set download and upload limits to 400 kB/sec and 60 kB/sec:

.. code-block:: console

   $ transmission-remote -d400 -u60
   $ transmission-remote --downlimit=400 --uplimit=60

Set alternate download and upload limits to 100 kB/sec and 20 kB/sec:

.. code-block:: console

   $ transmission-remote -asd100 -asu20
   $ transmission-remote --alt-speed-downlimit=100 --alt-speed-uplimit=20

Set the scheduler to use the alternate speed limits on weekdays between 10AM and 11PM:

.. code-block:: console

   $ transmission-remote --alt-speed-time-begin=1000
   $ transmission-remote --alt-speed-time-end=2300
   $ transmission-remote --alt-speed-days=1-5
   $ transmission-remote --alt-speed-scheduler

List all torrents' IDs and states:

.. code-block:: console

   $ transmission-remote -l

List all torrents from a remote session that requires authentication:

.. code-block:: console

   $ transmission-remote host:9091 --auth=username:password -l

Start all torrents:

.. code-block:: console

   $ transmission-remote -tall --start

Add two torrents:

.. code-block:: console

   $ transmission-remote -a one.torrent two.torrent

Add all torrents in ~/Desktop:

.. code-block:: console

   $ transmission-remote -a ~/Desktop/*torrent

Get detailed information on the torrent whose ID is '1':

.. code-block:: console

   $ transmission-remote -t1 -i

Get a list of a torrent's files:

.. code-block:: console

   $ transmission-remote -t1 -f

Download only its second and fourth files:

.. code-block:: console

   $ transmission-remote -t1 -Gall -g2,4

Set all torrents' first two files' priorities to high:

.. code-block:: console

   $ transmission-remote -tall -ph1,2

Set all torrents' files' priorities to normal:

.. code-block:: console

   $ transmission-remote -tall -pnall

Environment
-----------

.. envvar:: http_proxy

   Sets the proxy to use for http tracker announces.

See Also
--------

:manpage:`transmission-create(1)`, :manpage:`transmission-daemon(1)`, :manpage:`transmission-edit(1)`, :manpage:`transmission-gtk(1)`, :manpage:`transmission-qt(1)`, :manpage:`transmission-show(1)`

https://www.transmissionbt.com/
