#!/bin/sh

log (){
  printf "\e[34m $1 \n  \e[0m"
}

log uninstall.... 
pip uninstall -y girepo
log install.... 
pip install -U .


log "the import statment can work?"
sleep 2
python -c "from girepo.extractor import default_mapper; print(default_mapper)"


log "girepo can call as command?"
sleep 8
girepo --help



log uninstall
sleep 2

pip uninstall -y girepo

log "distributions check, normal log removed"
python setup.py sdist >/dev/null
tar ztfv dist/girepo-0.0.2.tar.gz
