API Reference
=============

This section provides detailed API documentation for the ``gitig`` package.

Main Module
-----------

.. automodule:: gitig
   :members:
   :undoc-members:
   :show-inheritance:

Core Functions
~~~~~~~~~~~~~~

.. autofunction:: gitig.main

.. autofunction:: gitig.async_main

.. autofunction:: gitig.patch_with_diff

Context Managers
~~~~~~~~~~~~~~~~

.. autofunction:: gitig.input_file

.. autofunction:: gitig.output_file

Network Module
--------------

.. automodule:: gitig.net
   :members:
   :undoc-members:
   :show-inheritance:

Template Operations
~~~~~~~~~~~~~~~~~~~

.. autofunction:: gitig.net.get_template

.. autofunction:: gitig.net.get_latest_sha

HTTP Client Management
~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: gitig.net.httpx_client

Exceptions
~~~~~~~~~~

.. autoexception:: gitig.net.NoCommitError
   :members:
   :show-inheritance:

Logging Module
--------------

.. automodule:: gitig._logging
   :members:
   :undoc-members:
   :show-inheritance:

Structured Logging
~~~~~~~~~~~~~~~~~~

.. autoclass:: gitig._logging.StructLogAdapter
   :members:
   :show-inheritance:

Formatters
~~~~~~~~~~

.. autoclass:: gitig._logging.ExtraFormatter
   :members:
   :show-inheritance:

Logging Configuration
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: gitig._logging.LoggingType
   :members:
   :show-inheritance:

.. autofunction:: gitig._logging.make_logging_handler

Constants Module
----------------

.. automodule:: gitig.consts
   :members:
   :undoc-members:

Utilities Module
----------------

.. automodule:: gitig.utils
   :members:
   :undoc-members:
   :show-inheritance:

Metaclasses
~~~~~~~~~~~

.. autoclass:: gitig.utils.FinalMeta
   :members:
   :show-inheritance:

Type Annotations
----------------

Common Types
~~~~~~~~~~~~

The following types are commonly used throughout the codebase:

.. code-block:: python

   from typing import Sequence, TextIO, Generator
   from pathlib import Path
   
   # Template content and SHA
   TemplateResult = tuple[Sequence[str], str]
   
   # File content as lines
   FileLines = Sequence[str]

Error Handling
--------------

Exception Hierarchy
~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   BaseException
   └── Exception
       └── RuntimeError
           └── NoCommitError

Custom Exceptions
~~~~~~~~~~~~~~~~~

All custom exceptions inherit from standard Python exceptions and provide
additional context for debugging.

Constants and Configuration
---------------------------

GitHub Integration
~~~~~~~~~~~~~~~~~~

.. data:: gitig.consts.OWNER_REPO
   
   The GitHub repository containing gitignore templates.

.. data:: gitig.consts.RAW_BASE_URL
   
   Base URL for fetching raw template files.

.. data:: gitig.consts.API_ENDPOINT
   
   GitHub API endpoint for repository operations.

Regular Expressions
~~~~~~~~~~~~~~~~~~~

.. data:: gitig.MARKER_RE
   
   Regular expression pattern for matching template marker comments.

Internal APIs
-------------

.. note::
   
   The following APIs are considered internal and may change without notice.
   Use at your own risk.

Argument Parsing
~~~~~~~~~~~~~~~~

.. autofunction:: gitig._build_argparser

These functions are used internally by the command-line interface and are
not intended for direct use by library consumers.