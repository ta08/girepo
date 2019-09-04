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
sleep 4
girepo --help



log uninstall
sleep 2

pip uninstall -y girepo

log "distributions check, normal log removed"

python setup.py sdist >/dev/null

version=$(cat girepo/__init__.py | grep version | sed -E 's/.*([0-9]+\.[0-9]+\.[0-9]+).*/\1/g')

log "contents of tar gz"
tar ztfv dist/girepo-${version}.tar.gz

sleep 4
log "contents of wheel"
tar ztfv dist/girepo-${version}-py3-none-any.whl
