==================
geniatagger-python
==================

Python library for GeneiaTagger

-------
License
-------

GPL version 3 or later. Please read ``LICNESE``.

-------
Install
-------

Run ``pip install -e .``


----------
How to use
----------

::

  from geniatagger import Geniatagger

  tagger = GeniaTagger('.../path_to_geniatagger/geniatagger')
  print tagger.parse('This is a pen.')
  
