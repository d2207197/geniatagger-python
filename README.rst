==================
geniatagger-python
==================

Python Wrapper for `GeniaTagger`_ (part-of-speech tagging, shallow parsing, and named entity recognition for biomedical text)


.. _GeniaTagger: http://www.nactem.ac.uk/GENIA/tagger/

-------
License
-------

GPL version 3 or later. Please read ``LICNESE``.

-------
Install
-------

Download/Clone and run ``pip install -e .``

or

Run ``pip install https://github.com/d2207197/geniatagger-python/archive/master.zip``



----------
How to use
----------

Local mode

.. code:: python

  # python3
  from geniatagger import GeniaTagger
  
  tagger = GeniaTagger('.../path_to_geniatagger/geniatagger')
  print(tagger.parse('This is a pen.'))
  # output:
  #((u'This', u'This', u'DT', u'B-NP', u'O'),
  # (u'is', u'be', u'VBZ', u'B-VP', u'O'),
  # (u'a', u'a', u'DT', u'B-NP', u'O'),
  # (u'pen', u'pen', u'NN', u'I-NP', u'O'),
  # (u'.', u'.', u'.', u'O', u'O'))
  
  tagger = GeniaTagger('.../path_to_geniatagger/geniatagger', ['-nt'])
  print(tagger.parse('This is a pen.'))
  # output:
  # ((u'This', u'This', u'DT', u'B-NP', u'O'),
  #  (u'is', u'be', u'VBZ', u'B-VP', u'O'),
  #  (u'a', u'a', u'DT', u'B-NP', u'O'),
  #  (u'pen.', u'pen.', u'NN', u'I-NP', u'O'))

  
Server mode

.. code:: console
  
  $ geniatagger-server --help
  $ geniatagger-server ~/tools/geniatagger-3.0.1/geniatagger -- -nt
   * Running GeniaTagger with: /Users/joe/tools/geniatagger-3.0.1/geniatagger -nt
   * Listening on: localhost:9595
   
.. code:: python

  # python3
  from geniatagger import GeniaTaggerClient
  
  tagger = GeniaTaggerClient(9595)
  print(tagger.parse('This is a pen.'))
  
  
