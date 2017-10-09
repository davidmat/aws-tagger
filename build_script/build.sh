#!/bin/bash

if [ ! -d "/tmp/boto_env" ]
then
  mkdir /tmp/boto_env
  cd /tmp/boto_env
  virtualenv /tmp/boto_env/
  . /tmp/boto_env/bin/activate
  pip install boto
  pip install pyYAML
  cd -
fi

. /tmp/boto_env/bin/activate

cd ${bamboo.build.working.directory}
python tagger.py
