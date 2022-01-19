function deploy {
    rm -rf apiaudio.egg-info build dist
    pip3 install twine wheel
    python3 setup.py sdist bdist_wheel
    echo '============'
    echo 'In order to obtain the username/pass; contact Core team devs'
    echo '%%%%%%%%%%%%'
    python3 -m twine upload dist/*
}

while true; do
    read -p "Do you wish to publish a new version $(sed -n '6p' < apiaudio/__init__.py | cut -d '"' -f 2) to PyPI? " yn
    case $yn in
        [Yy]* ) deploy; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no. Its not a game. Its not a kindergarden.";;
    esac
done
