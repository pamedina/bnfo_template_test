#!/usr/bin/env python

import pyrootutils

ROOT = pyrootutils.setup_root(
    search_from=__file__, indicator="pyproject.toml", pythonpath=True, cwd=True
)

DATA    = ROOT / "data"
FIGURES = ROOT / "figures"
