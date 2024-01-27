# -*- coding: utf-8 -*-

from mod.common.mod import Mod


@Mod.Binding(name="Script_NeteaseModZcGmj3l4", version="0.0.1")
class Script_NeteaseModZcGmj3l4(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModZcGmj3l4ServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModZcGmj3l4ServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModZcGmj3l4ClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModZcGmj3l4ClientDestroy(self):
        pass
