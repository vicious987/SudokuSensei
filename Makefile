.PHONY:pylint

PYLINT = pylint
#PYLINTFLAGS = #-rn #--disable=C0326
PYTHONFILES := $(wildcard *.py)

pylint:
	#$(PYLINT) $(PYLINTFLAGS) *.py
	$(PYLINT) $(PYTHONFILES)
