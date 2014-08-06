======================
ROSA - ROS Accessories
======================

Commands for quickly performing common operations in `ROS <http://ros.org>`_.

.. image:: https://travis-ci.org/abencz/rosa.svg?branch=master
    :target: https://travis-ci.org/abencz/rosa

Installation
============

To install, run the following::

    pip install rosa

Or, if you wish to install the latest from source::

    git clone https://github.com/abencz/rosa
    cd rosa
    python setup.py install

Usage & Examples
================

ROSA installs a new command (``rosa``) which includes subcommands for doing
common ROS tasks. And, of course, there's a ``--help``::

    rosa --help

Creating a Workspace
--------------------
To create a workspace, source your ``setup.{bash,zsh,sh}`` of choice from
either ``opt/ros`` or from an existing workspace if using
`overlays <http://wiki.ros.org/catkin/Tutorials/workspace_overlaying>`_, then run
rosa::

    source /opt/ros/hydro/setup.bash
    rosa create_workspace my_workspace
    
If you have a rosintall you're going to use with this workspace, you can add it
up immidiately using the ``-i`` flag. The rosinstall will be merged in to the
workspace (as if using ``wstool merge``), and updated (``wstool update``)::

    rosa create_workspace -i ~/my.rosinstall my_workspace
    
As with ``wstool`` you can also use web URIs directly::

    rosa create_workspace -i http://bit.ly/1xpc6AK my_workspace
    
Specify multiple rosinstall files using multiple ``-i`` flags::

    rosa create_workspace -i ~/my.rosinstall -i http://bit.ly/1xpc6AK my_workspace
    
Adding ROSinstall Files to an Existing Workspace
------------------------------------------------
You can also merge rosinstall files into a workspace that already exists. From
anywhere in the target workspace::

    rosa merge_rosinstall ~/my.rosinstall

Once again, URIs are fair game as are multiple rosinstall files::

    rosa merge_rosinstall ~/my.rosinstall http://bit.ly/1xpc6AK
    
If you're not inside a workspace or you want to merge the rosinstalls into a
different workspace you can specify one using the ``-w`` flag::

    rosa -w ~/my_workspace merge_rosinstall ~/my.rosinstall

License
=======
BSD
