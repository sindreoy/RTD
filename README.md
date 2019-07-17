
# Prelude

The experiment is legacy from a long time ago in a galaxy far away.
What do I mean about that?
Well, mainly that it uses the window system "WX" to comply with legacy code.
This was later abandoned in favour of "Qt" in order to to adhere to the system used in ALL other experiments...

# Install

## Dependencies

```
sudo apt install python-pip libgtk-3-dev
sudo apt install python-{setuptools,matplotlib}
sudo pip install {minimalmodbus,wxPython,wxmplot}
```

## Modules

```
git clone
python setup.py build
sudo python setup.py install
```

the experiment can now be run as a module:

```
python -m RTD
```

This is the current setup, but the "setuptools" option "entry_point" should probably be used in thr future.

