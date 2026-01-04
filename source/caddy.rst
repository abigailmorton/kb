===============
Caddy Migration
===============

*******
Purpose
*******

Migrate a Debian host from Nginx to Caddy, preserving existing sites, ensuring ports 80/443 are clean, and validating Caddy service health before configuring production hosts.

***********
Assumptions
***********

- Debian-based system using systemd
- DNS already points to the host
- Ports 80 and 443 are available

***********
Preparation
***********

Snapshot
========

Files in smersh:/etc/nginx are backed up to DARPA/archive/nginx

.. code-block:: bash

    rsync -ahq --no-links \
    abby@smersh.local:/etc/nginx/ \
    /media/abby/DARPA/archive/nginx/

Before shutdown, this is what's listening now:

.. raw:: html

    <a href="https://notes.cloverdalelane.com/guides/docs_caddy/listening.out" target="_blank" rel="noopener noreferrer">Listening output</a>

*****
Nginx
*****

Stop and disable Nginx
============================

Nginx prevents it from grabbing ports on boot

.. code-block:: bash

    sudo systemctl stop nginx
    sudo systemctl disable nginx

.. code-block:: text

    Synchronizing state of nginx.service with SysV service script with /usr/lib/systemd/systemd-sysv-install.
    Executing: /usr/lib/systemd/systemd-sysv-install disable nginx
    Removed '/etc/systemd/system/multi-user.target.wants/nginx.service'.


Confirm ports are free
======================

.. code-block:: bash

    sudo ss -ltnp | egrep ':(80|443)\b' || echo "80/443 free"

.. code-block:: text

    80/443 free

*************
Install Caddy
*************

Install Caddy from upstream repo
================================

.. raw:: html

    <a href="https://caddyserver.com/docs/install#debian-ubuntu-raspbian" target="_blank" rel="noopener noreferrer">Caddy Install Documentation</a>


.. code-block:: bash

    sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https curl
    curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
    sudo chmod o+r /usr/share/keyrings/caddy-stable-archive-keyring.gpg
    sudo chmod o+r /etc/apt/sources.list.d/caddy-stable.list
    sudo apt update
    sudo apt install caddy

.. raw:: html

    <a href="https://notes.cloverdalelane.com/guides/docs_caddy/caddy_install.out" target="_blank" rel="noopener noreferrer">Caddy install commands</a>

Start Caddy
===========

.. code-block:: bash

    sudo systemctl enable --now caddy


.. code-block:: text

    sudo systemctl status caddy --no-pager
    ● caddy.service - Caddy
        Loaded: loaded (/usr/lib/systemd/system/caddy.service; enabled; preset: enabled)
        Active: active (running) since Sat 2026-01-03 10:48:34 CST; 7min ago
    Invocation: 96de21dd3abb4a83b803f25174541c39
        Docs: https://caddyserver.com/docs/
    Main PID: 2519125 (caddy)
        Tasks: 10 (limit: 18889)
        Memory: 14.1M (peak: 14.6M)
            CPU: 128ms
        CGroup: /system.slice/caddy.service
                └─2519125 /usr/bin/caddy run --environ --config /etc/caddy/Caddyfile

    Jan 03 10:48:34 smersh caddy[2519125]: {"level":"warn","ts":1767458914.5065043,"logger":"http.auto_https","msg":"server is listening onl…p_port":80}
    Jan 03 10:48:34 smersh caddy[2519125]: {"level":"info","ts":1767458914.5066855,"logger":"tls.cache.maintenance","msg":"started backgroun…00070ca80"}
    Jan 03 10:48:34 smersh caddy[2519125]: {"level":"warn","ts":1767458914.5067377,"logger":"http","msg":"HTTP/2 skipped because it requires…ddr":":80"}
    Jan 03 10:48:34 smersh caddy[2519125]: {"level":"warn","ts":1767458914.5067523,"logger":"http","msg":"HTTP/3 skipped because it requires…ddr":":80"}
    Jan 03 10:48:34 smersh caddy[2519125]: {"level":"info","ts":1767458914.50676,"logger":"http.log","msg":"server running","name":"srv0","p…"h2","h3"]}
    Jan 03 10:48:34 smersh caddy[2519125]: {"level":"info","ts":1767458914.5071228,"msg":"autosaved config (load with --resume flag)","file"…save.json"}
    Jan 03 10:48:34 smersh caddy[2519125]: {"level":"info","ts":1767458914.5071929,"msg":"serving initial configuration"}
    Jan 03 10:48:34 smersh systemd[1]: Started caddy.service - Caddy.
    Jan 03 10:48:34 smersh caddy[2519125]: {"level":"info","ts":1767458914.543985,"logger":"tls","msg":"cleaning storage unit","storage":"Fi…are/caddy"}
    Jan 03 10:48:34 smersh caddy[2519125]: {"level":"info","ts":1767458914.5775955,"logger":"tls","msg":"finished cleaning storage units"}
    Hint: Some lines were ellipsized, use -l to show in full.

**************************
Initial Site Configuration
**************************

Reverse Proxy
=============

.. code-block:: text

    blog.example.com {
        reverse_proxy 127.0.0.1:PORT
    }


Basic auth protected site
=========================

.. code-block:: text

    notes.cloverdalelane.com {
        root * /var/www/abbynet/notes/site
        file_server

        basic_auth {
            abby <PASSWORD_HASH>
        }
    }

.. raw:: html

    <a href="https://notes.cloverdalelane.com/guides/docs_caddy/Caddyfile" target="_blank" rel="noopener noreferrer">Caddyfile</a>