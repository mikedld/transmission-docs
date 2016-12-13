.. _env-vars-ref:

Environment Variables
=====================

Users can set environmental variables to override Transmission's default behavior and for debugging.

Transmission-Specific Variables
-------------------------------

.. envvar:: TRANSMISSION_HOME

   If set, Transmission will look there for its settings instead of in the :ref:`default location <config-files-locations>`.

.. envvar:: TRANSMISSION_WEB_HOME

   If set, Transmission will look there for the :doc:`Web Interface <web-interface>` files, such as the javascript, html, and graphics files.

.. envvar:: TR_CURL_VERBOSE

   If set, debugging information for libcurl will be enabled. More information about libcurl's debugging mode `is available here <curloptverbose_>`_.

.. envvar:: TR_DEBUG

   .. todo:: Add description.

.. envvar:: TR_DEBUG_FD

   If set to an integer, that integer is treated as a `file descriptor`_ and very verbose debugging information is written to it. For example, here is how to turn on debugging and save it to a file named :file:`runlog` when running Transmission from a bash shell:

   .. code-block:: console

      $ export TR_DEBUG_FD=2
      $ transmission 2>runlog

.. envvar:: TR_DHT_VERBOSE

   If set, then Transmission will log all of the DHT's activities in excrutiating detail to standard error.

.. _curloptverbose: https://curl.haxx.se/libcurl/c/curl_easy_setopt.html#CURLOPTVERBOSE
.. _file descriptor: https://en.wikipedia.org/wiki/File_descriptor

Standard Variables Used By Transmission
---------------------------------------

* If :envvar:`TRANSMISSION_WEB_HOME` is *not* set, non-Mac platforms will look for the :doc:`Web Interface <web-interface>` files in :envvar:`XDG_DATA_HOME` and in :envvar:`XDG_DATA_DIRS` as described in `the XDG Base Directory Specification`_. :envvar:`XDG_DATA_HOME` has a default value of :file:`$HOME/.local/share/`.
* If :envvar:`TRANSMISSION_HOME` is *not* set, Unix-based versions of Transmission will look for their settings in :file:`$XDG_CONFIG_HOME/transmission/`. :envvar:`XDG_CONFIG_HOME` has a default value of :file:`$HOME/.config/`.
* If :envvar:`HOME` is set, it's used in three ways:

  1. by the :abbr:`XDG (X Desktop Group)` variables, as described above
  2. If :envvar:`TRANSMISSION_HOME` is *not* set, Mac-based versions of Transmission will look for their settings in :file:`$HOME/Library/Application Support/Transmission`
  3. :file:`$HOME/Downloads` is the default download directory.

.. _the XDG Base Directory Specification: https://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html#variables

Standard Variables Used By Other Tools
--------------------------------------

Transmission uses the libcurl_ library for http- and https-based tracker announces and scrapes. Transmission doesn't support proxies, but libcurl itself honors `a handful of environment variables <curloptproxy_>`_ to customize *its* proxy behavior.

.. _libcurl: https://curl.haxx.se/libcurl/
.. _curloptproxy: https://curl.haxx.se/libcurl/c/curl_easy_setopt.html#CURLOPTPROXY
