"""Every module under here is imported once, so every restaurant registers itself."""
import importlib
import pkgutil


def load_all():
    for m in pkgutil.walk_packages(__path__, __name__ + "."):
        importlib.import_module(m.name)
