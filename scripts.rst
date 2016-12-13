Scripts
=======

Introduction
------------

Thanks to the powerful :doc:`RPC <rpc>`, :program:`transmission-remote` can talk to any client that has the RPC enabled. This means that a script written using :program:`transmission-remote` or RPC can, without rewrite, comunicate with all the Transmission clients: GTK+ client, Mac client and the daemon.

Mac OS users may wonder wether there will be Applescript scripts, the answer is *no*. Although Applescript is a nice technology, it's a pain to implement. However, Mac OS X is a Unix after all, so any script you find here will also work on the Mac. Even from within Applescript, you can run these scripts by typing:

.. code-block:: applescript

   do shell script "path/to/script"

How-To
------

If you are interested at writing scripts for Transmission, have a look at the following pages:

* [wiki:man Transmission man pages]
* :doc:`config-files`
* :doc:`editing-config-files`
* :doc:`env-vars`
* :doc:`rpc`

For those who need more information how to use the scripts, have a look at the following links:

* `Cron How-To <https://help.ubuntu.com/community/CronHowto>`_: Run scripts at a regular interval

Start/Stop Scripts
------------------

* [wiki:Scripts/initd init.d script] (Debian, Ubuntu and BSD deratives)
* [wiki:Scripts/runscript runscript] (Gentoo and other runscript-compatible systems)

Scripts On Torrent Completion
-----------------------------

Transmission can be set to invoke a script when downloads complete. The environment variables supported are:

.. envvar:: TR_APP_VERSION

   .. todo:: Add description.

.. envvar:: TR_TIME_LOCALTIME

   .. todo:: Add description.

.. envvar:: TR_TORRENT_DIR

   .. todo:: Add description.

.. envvar:: TR_TORRENT_HASH

   .. todo:: Add description.

.. envvar:: TR_TORRENT_ID

   .. todo:: Add description.

.. envvar:: TR_TORRENT_NAME

   .. todo:: Add description.

[https://trac.transmissionbt.com/browser/trunk/extras/send-email-when-torrent-done.sh Here is an example script] that sends an email when a torrent finishes.

Obsolete Scripts
----------------

Functionality of these scripts has been implemented in libtransmission and is thus available in all clients.

* [wiki:Scripts/EmailNotifier Email Notification Script]
* [wiki:Scripts/BlockListUpdater Block List Updater]
* [wiki:Scripts/Watchdog Watch Directory Script]
* [wiki:Scripts/Scheduler Bandwidth Scheduler]

Contributed Scripts
-------------------

Tomas Carnecky (a.k.a. wereHamster) is maintaining a set of scripts in his `github repository <http://github.com/wereHamster/transmission/tree/master/contrib/scripts/>`_.

Falk Husemann (a.k.a. hxgn) is maintaining scripts in his `blog <http://falkhusemann.de/blog/category/tcp_ip/transmission-tcp_ip/>`_.

oguz wrote `on his blog <http://oguzarduc.blogspot.com/2012/05/transmission-quit-script-in-php.html>`_ a PHP script to stop Transmission after it finishes downloading and seeding.

Scripts which have not yet been ported and may not work with the latest version:

* http://pastie.org/338556: Python - Fetch new torrents from tvrss
* http://pastie.org/338555: PHP - Stop finished torrents
* http://pastie.org/443058: Perl - Network traffic graph, based on rrdtool (example: http://skitch.com/werehamster/bmjg8/bittorrent-traffic)
* http://transmission.pastebin.com/QzVxQDtM: Bash - (cron)script to keep a maximum number of torrents running; starting and pausing torrents as necessary
* https://github.com/jaboto/Transmission-script - (cron)script set network limits according to the number of clients in the network
