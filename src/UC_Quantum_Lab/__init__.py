import os, json, sys
from atexit import register as __register

_config_dir = ".UCQ_config"
_layout_file = os.path.join(_config_dir, "layout.json")
_trigger_file = ".trigger"
_master_show = False
_show_plt = False
_states = {}
_circs = []
_hists = []

__version__ = "0.1.8"

# cleans up the config directory on init of this python module
if _config_dir in os.listdir():
    _master_show = True
    #print("cleaning up config dir")
    for item in os.listdir(_config_dir):
        # deletes png html or the trigger file from the config dir
        if item.endswith(".png") or item.endswith(".html") or item == _trigger_file:
            os.remove(os.path.join(_config_dir, item))

def register():
    if _config_dir in os.listdir():
        with open(os.path.join(_config_dir, "config.json"), 'w') as f:
            f.write(json.dumps({"python" : sys.executable}, indent=2))

from .layout import _layout_at_exit, _exit
from .commands import _show_at_exit
# need to be in this order
__register(_layout_at_exit)
__register(_exit)
__register(_show_at_exit)