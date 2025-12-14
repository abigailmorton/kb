Document Conventions
====================

This section explains the formatting and terminology used throughout this
documentation set. Use it as a reference when you are not sure what a
particular style or notation means.

Typography
----------

The following typographical conventions are used:

- **Bold text**  
  Used for user interface elements such as button names, menu items, and
  labels. Example: Click **Save** to commit your changes.

- *Italic text*  
  Used for new terms on first use or for emphasis in explanatory text.

- ``monospace``  
  Used for code, commands, configuration keys, JSON keys, and literal
  filenames. Example: The error code is returned in the
  ``goal_value`` field.

- ``PLACEHOLDER`` in ALL CAPS  
  Indicates a value you must replace with a real value. Example:
  ``<INSTITUTION_ID>`` should be replaced with your institution’s identifier.

User interface notation
-----------------------

When describing navigation paths in a user interface, this documentation uses
the following conventions:

- Menu paths are written using a “›” separator, for example:

  ``Settings › Institutions › Connection Profiles``

- Buttons, links, and labeled controls are written in **bold**, for example:
  click **Test Connection**.


Command-line examples
---------------------

Command-line examples assume a Unix-like shell (``bash``, ``zsh``, or similar).

- Command-line examples should work in any shell. The documentation will note if that is not true:

  .. code-block:: bash

     sphinx-build -b html source build/html


Code and configuration examples
-------------------------------

Code and configuration snippets are shown in fenced blocks with syntax
highlighting. For example, JSON structures are shown as:

.. code-block:: json

   {
     "errors": [
       {
         "type": "COMPLETENESS",
         "description": "The request is incomplete.",
         "code": "GOAL_VALUE_BAD"
       }
     ]
   }

Unless otherwise noted, these examples are illustrative. Replace placeholder
values with those appropriate for your environment.

Error codes and identifiers
---------------------------

- Error codes such as ``GOAL_VALUE_BAD`` are shown in ``monospace``.
- Internal reference IDs (for example, ``Ref UCX STU316``) are also shown in
  ``monospace`` and may appear in logs and troubleshooting steps.

Notes, warnings, and other callouts
-----------------------------------

This documentation uses callouts to highlight important information:

.. note::

   Notes provide additional context or tips that may help you complete a
   procedure more efficiently.


.. warning::

   Warnings indicate behavior that may result in data loss, integration
   failure, or other unintended consequences.


When a warning indicates a potential impact to student data or compliance,
follow the instructions carefully before proceeding.

Environment terminology
-----------------------

When a term has a specific meaning in your environment that differs from the
usage above, this documentation will call it out explicitly.
