================================================================================
                               PricK Interpretter
================================================================================

This folder is based on the files I made for my `code guessing 44`_ entry, which
included the first `PricK interpretter`_ in Python. It also contains some sample
PricK code in the form of stages of writing of my entry, a fibonacci sequence
implementation in the test_ file, and a `subtraction program`_ translated
without optimisation from its BlooP implementation, set to subtract 2 from 5.

Maybe I will add more structure and interpretation to this repo, for now it
serves as a place to find the reference interpretter.

.. _code guessing 44: https://cg.esolangs.gay/44/#3
.. _PricK interpretter: ./prick.py
.. _test: ./test.prick
.. _subtraction program: ./bloop-minus.prick


Interpretter features
=====================

This interpretter recognises all language extensions documented on the
`wiki page`_ of PricK, and an additional debugging builtin ``$`` which prints
out the stacks and memory at the point of its execution.

.. _wiki page: https://esolangs.org/wiki/PricK#Language_extensions
