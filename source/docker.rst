============
Docker Guide
============

.. toctree::
    :maxdepth: 4

*************************
Install Docker Components
*************************

This section explains the initial setup, installation, and start up of Docker on a Debian machine. For this example, we will be installing RSSHub.

Prerequisites
=============

- Fresh Debian system
- User with ``sudo``
- Outbound internet access
- Port 1200 available (RSSHub default)

.. note:: All commmands below are run as your normal user unless otherwise noted.

Update the system
=================

.. code-block:: bash

    sudo apt update
    sudo apt upgrade -y

**Optional**, but recommended on truly fresh installs:

.. code-block:: bash

   sudo apt install -y ca-certificates curl gnupg lsb-release

Install Docker Engine
=====================

Add Docker GPG Key
------------------

.. code-block:: bash

    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg

Add Docker's Repository
-----------------------

.. code-block:: bash

    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
       https://download.docker.com/linux/debian \
       $(. /etc/os-release && echo "$VERSION_CODENAME") stable" \
    | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Install Docker + Compose plugin
-------------------------------

.. code-block:: bash

    sudo apt update
    sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

Enable Docker and Allow Non-root Usage
======================================

Enable and Start Docker
-----------------------

.. code-block:: bash

    sudo systemctl enable --now docker

Add Your User to the Docker Group
---------------------------------

.. code-block:: bash

    sudo usermod -aG docker $USER

.. warning::

    **Important**: Log out and log back in again so group membership applies

Verify:

.. code-block:: bash

    docker run --rm hello-world

If that works, then Docker is correctly installed.

**************
Install RSSHub
**************

Create Directory for RSSHub
===========================

.. code-block:: bash

    mkdir -p ~/services/rsshub
    cd ~/services/rsshub


Create docker-compose.yml
=========================

Create the file:

.. code-block:: bash

    nano docker-compose.yml

The following is for a **minimal, clean configuration**:

.. code-block:: yaml

    services:
    rsshub:
        image: diygod/rsshub:latest
        container_name: rsshub
        restart: unless-stopped
        ports:
        - "1200:1200"
        environment:
        NODE_ENV: production
        CACHE_TYPE: memory
        healthcheck:
        test: ["CMD", "curl", "-f", "http://localhost:1200/health"]
        interval: 30s
        timeout: 10s
        retries: 3

Save and Exit.


Start RSSHub
============

.. code-block:: bash

    docker compose up -d

Check status:

.. code-block:: bash

    docker compose ps

Check logs:

.. code-block:: bash

    docker compose logs -f

Verify RSSHub is working
========================

From the same machine:

.. code-block:: json

    {"status":"ok"}

From a browser (or remote machine):

.. code-block:: cpp

    http://<server-ip>:1200

Optional: Basic Firewall Opening
================================

If you use ``ufw``:

.. code-block:: bash

    sudo apt install -y ufw
    sudo ufw allow 1200/tcp
    sudo ufw enable

Updating RSSHub Later
=====================

From the RSSHub dirctory:

.. code-block:: bash

    docker compose pull
    docker compose up -d

