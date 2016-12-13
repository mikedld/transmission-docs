Building From Source
====================

If you are searching for a HOWTO, covering a specific distribution or device (NAS, router, ...), have a look at the [HeadlessUsage "Running Transmission on a headless machine"] page

Getting the Source
------------------

Recommended
~~~~~~~~~~~

Source code for official releases can be found on our `download page <https://www.transmissionbt.com/download/>`_.

Experimental
~~~~~~~~~~~~

Automated source code tarballs including the newest code `are now available, too <http://build.transmissionbt.com/job/trunk-linux/>`_!

If you want to check out the source code yourself from svn, open a terminal window and type:

.. code-block:: console

   $ svn co svn://svn.transmissionbt.com/Transmission/trunk Transmission

On Mac OS X
-----------

Transmission has an Xcode project file (Transmission.xcodeproj) for building in Xcode. Make sure you have this software:

* OS X 10.8 or newer
* OS X 10.8 SDK
* Xcode 4.4 or newer

Building the project on Mac requires the source to be retrieved from SVN. Pre-packaged source code will not compile.

If building from source is too daunting for you, check out the `nightly builds <https://build.transmissionbt.com/job/trunk-mac/>`_.

.. node:: These are untested snapshots. Use them with care.

On Unix
-------

Prerequisites
~~~~~~~~~~~~~

Ubuntu
++++++

On Ubuntu, you can install the required development tools with this command:

.. code-block:: console

   $ sudo apt-get install build-essential automake autoconf libtool pkg-config intltool libcurl4-openssl-dev libglib2.0-dev libevent-dev libminiupnpc-dev libminiupnpc5 libappindicator-dev

''After you install those you can skip [#Buildingfromatarball to this section].''

Debian Squeeze
++++++++++++++

Sometimes you have a need to stay current with upstream releases, even though you would like to rely on the stability of your base distribution. Here is how this can be accomplished in "quick and dirty" fashion. Lines started with a # are to be executed as root, lines starting with $ can be run as a regular user.

1. Dependencies

First let us install every dependency Transmission needs and for which there is a usable version in the Debian repository.

.. code-block:: console

   # apt-get install ca-certificates libcurl4-openssl-dev libssl-dev pkg-config build-essential checkinstall

2. libevent

Traditionally, libevent is also needed, but Transmission depends on version numbers only rarely found in Debian. So let us start by compiling libevent in a directory of your choice. Browse to http://libevent.org/ and get the latest version.

.. code-block:: console

   $ cd /var/tmp
   $ wget https://github.com/downloads/libevent/libevent/libevent-2.0.18-stable.tar.gz
   $ tar xzf libevent-2.0.18-stable.tar.gz
   $ cd libevent-2.0.18-stable
   $ CFLAGS="-Os -march=native" ./configure && make

Now, we would really like to be able to upgrade to a new version in the future, so there should be a mechanism other than the classic :command:`make install` which keeps count of what went where (and ideally this is not a piece of paper). So we build a very simple Debian package from the compiled files and install it. Basically you just enter the following command and hit return until a nice text message tells you that all is done.

.. code-block:: console

   # checkinstall

3. Transmission

Now we need to prepare Transmission for compilation by configuring the source, the same as with libevent.

.. code-block:: console

   $ cd /var/tmp
   $ wget http://download-origin.transmissionbt.com/files/transmission-2.51.tar.bz2
   $ tar xjf transmission-2.51.tar.bz2
   $ cd transmission-2.51
   # CFLAGS="-Os -march=native" ./configure && make && checkinstall

*Thanks to josen at http://falkhusemann.de/blog/2012/05/compiling-transmission-bittorrent-for-debiand/ for the original Debian Squeeze howto section.*

CentOS 5.4
++++++++++

The packages you need are:

* gcc
* gcc-c++
* m4
* make
* automake
* libtool
* gettext
* openssl-devel

Or simply run the following command:

.. code-block:: console

   $ yum install gcc gcc-c++ m4 make automake libtool gettext openssl-devel

However, Transmission needs other packages unavailable in {{{yum}}}:

* `pkg-config <http://pkg-config.freedesktop.org/wiki/>`_
* `libcurl <http://curl.haxx.se/>`_
* `intltool <http://ftp.gnome.org/pub/gnome/sources/intltool/>`_

Before building Transmission, you need to set the pkgconfig environment setting:

.. code-block:: console

   $ export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig

''After you install those you can skip [#Buildingfromatarball to this section].''

Normal
++++++

If this is your first time compiling on Unix, you'll need a few basic tools:

* gcc
* libtool
* gettext 0.14.1 or newer
* intltool 0.40 or newer

If you're planning to build from SVN:

* automake 1.9 or newer
* autoconf 2.54 or newer

Once you've got the basics out of the way, here are the libraries that Transmission needs to have in order to build:

* OpenSSL 0.9.8 or newer, preferably ssl or gnutls support.
* libcurl 7.16.3 or newer
* GTK+ 2.6 or newer (only needed by the GTK+ gui)
* libnotify 0.4.4 (optional, and only needed by the GTK+ gui)
* DBUS 0.70 (optional, and only needed by the GTK+ gui)

RPM users
+++++++++

*You'll also need to install the corresponding ``-devel`` packages.*

Building from a tarball
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

   $ tar xvjf transmission-1.76.tar.bz2
   $ cd transmission-1.76
   $ ./configure -q && make -s
   $ su # if necessary for the next line
   $ make install

Building from an SVN snapshot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First Time
++++++++++

.. code-block:: console

   $ svn co svn://svn.transmissionbt.com/Transmission/trunk Transmission
   $ cd Transmission
   $ ./autogen.sh && make -s
   $ su # if necessary for the next line
   $ make install

Updating
++++++++

.. code-block:: console

   $ cd Transmission
   $ make clean
   $ svn up
   $ make -s
   $ su # if necessary for the next line
   $ make install

On Windows
----------

For Windows XP and above there are several choices:

Cygwin environment
~~~~~~~~~~~~~~~~~~

With `Cygwin <http://cygwin.com/>`_ installed, the CLI tools (transmission-remote, transmissioncli, etc.) and the daemon can be built easily.

No patches needed(*), all the recent versions of Transmission built almost out-of-the-box (you need to install the prerequisites), and the CLI tools work better under Cygwin that those built with MinGW.

(*) At the release time of version 2.0, **libevent** is not bundled and it's also not in Cygwin distribution (but was added later)... so you need to build it (which is as easy as ./configure, make install).  To build transmission you may need to add LDFLAGS="-L/usr/local/lib" to the configure script (LIBEVENT_LIBS doesn't seem to work when it comes to build all the test programs). Additionally **libutp** needs deleting -ansi on the Makefile.

With version 2.51 miniupnpc fails to build, see http://miniupnp.tuxfamily.org/forum/viewtopic.php?t=1130.

Version 2.80 breaks building on Cygwin, adding this https://github.com/adaptivecomputing/torque/blob/master/src/resmom/cygwin/quota.h file to Cygwin's :file:`/usr/include/sys` solves the problem. This is no longer needed after version 2.82 (Cygwin added the header).

Version 2.81 with the above workaround needs a one line patch, see ticket #5692.

Version 2.82, same as 2.81.

Version 2.83, no need to add quota.h, Cygwin added it.

Native Windows
~~~~~~~~~~~~~~

With a `MinGW <http://mingw.org/>`_ development environment, the Gtk and the Qt GUI applications can be built. The CLI tools can also be built, and in general work fine, but may fail if you use foreign characters as parameters (MinGW uses latin1 in parameters).

The procedure: wiki:BuildingTransmissionQtWindows

Switches
--------

The transmission {{{./configure}}} (or {{{./autogen.sh}}}) script allows you to switch on/off certain parts. To use these, you'll either use :option:`--enable-*` or :option:`--disable-*`. E.g. to disable the GTK client: :option:`--disable-gtk`.

The switches that are available are:

* **gtk** = enables GTK+ client (default)
* **daemon** = enables transmission-daemon and \*-remote client (default)
* **cli** = enables cli client (default. deprecated, consider using the daemon)
* **libnotify** = enables lib notify (default)
* **nls** = enables native language support (default)
* **mac** = enables Mac client (default, if possible)
* **wx** = enables wxWidgets client (unsupported)
* **beos** = enables beos client (unsupported)

.. note:: :option:`--disable-nls` removes the dependancy on gettext and intltool. It's designed for, and should only be used on, [HeadlessUsage embedded devices]. If you do have GTK+ installed on your box, you must also specify :option:`--disable-gtk`.
