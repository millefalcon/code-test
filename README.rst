code-test
######

Code for Tame of Thrones problem.

Create Gists_ from the command line.

Requires the Requests_ library. Should work on Python 2.7 and 3.3+.

.. _Gists: https://gist.github.com/
.. _Requests: http://docs.python-requests.org/


Prerequisite
============

* Python >= 3.7


Usage
=====

Clone::

   $ git clone https://github.com/millefalcon/code-test
   $ cd code-test/

General usage::

   usage: core.py [-h] infile

   positional arguments:
     infile

   optional arguments:
     -h, --help  show this help message and exit


Run
===

Using input file::

   $ cat input1.txt 
   AIR ROZO
   LAND FAIJWJSOOFAMAU
   ICE STHSTSTVSASOS
   $
   $ python3 core.py input1.txt 
   SPACE AIR LAND ICE
   $
   $ cat input2.txt 
   AIR OWLAOWLBOWLC
   LAND OFBBMUFDICCSO
   ICE VTBTBHTBBBOBAB
   WATER SUMMER IS COMING
   $
   $ python3 core.py input2.txt 
   NONE


Test
====

Run test using unittest::

   $ python3 -m unittest test.py -v
   test_can_rule (test.TameOfThronesTestCase) ... ok
   test_cannot_rule (test.TameOfThronesTestCase) ... ok
   test_load_from_stream (test.TameOfThronesTestCase) ... ok
   test_no_data (test.TameOfThronesTestCase) ... ok
   test_rotate_left (test.TameOfThronesTestCase) ... ok
   test_success (test.TameOfThronesTestCase) ... ok

   ----------------------------------------------------------------------
   Ran 6 tests in 0.001s

   OK

