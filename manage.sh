#!/bin/sh

if [ $# -eq 0 ]
then
	django-admin.py help --pythonpath=`pwd` --settings=settings.devel
else
	django-admin.py $@ --pythonpath=`pwd` --settings=settings.devel
fi
