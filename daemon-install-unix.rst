Daemon Installation Guide - Unix
================================

Generic Instructions
--------------------

Installation is platform and distribution specific. The general steps are:

1. `Download <downloads_>`_ the Binary or Source packages for :program:`transmission-daemon`
2. Install the Binary Package or [wiki:Building#OnUnix Build from Source]
3. Create a user for Transmission to run in (recommended: "transmission")
4. Create a start/stop script for your platform (e.g. :doc:`scripts`)
5. Identify where the key configuration files are located (i.e. :file:`settings.json`). Although the Transmission project has default locations, some distributions may relocate these files to comply with distribution specific guidelines. Distributions usually provide tools that can show where package files are installed.
6. Edit the :doc:`configuration file <editing-config-files>` for your site requirements (download directories etc.)

:doc:`daemon-install` covers the above setup steps in more detail.

.. seealso:: `Transmission Configuration`_ (based on Nexenta but of general use)

.. _downloads: https://transmissionbt.com/download/
.. _Transmission Configuration: http://dfusion.com.au/wiki/tiki-index.php?page=Configuring+Transmission+Bit+Torrent+Daemon

OS-Specific Instructions
------------------------

Specific daemon installation instructions have been provided for the following systems:

* :doc:`daemon-on-gentoo`
* :doc:`daemon-on-nslu2`
* :doc:`daemon-on-solaris`

If you can give a clear description of the steps required for an undocumented platform, and provide a sample start/stop script, please [/newticket open a ticket] (set Component to Wiki).
