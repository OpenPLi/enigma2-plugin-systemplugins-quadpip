from __future__ import print_function
from . import _, PLUGIN_NAME, PLUGIN_VERSION
from Plugins.Plugin import PluginDescriptor
from .qpip import QuadPipScreen


def main(session, **kwargs):
	session.open(QuadPipScreen)


def Plugins(**kwargs):
	return [(
		PluginDescriptor(name=_("Enable Quad PiP"),
		description=_("Quad Picture in Picture"),
		where=[PluginDescriptor.WHERE_EXTENSIONSMENU],
		fnc=main))]
