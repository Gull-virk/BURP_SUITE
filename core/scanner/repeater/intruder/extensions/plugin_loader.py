# ============================================================
# File Name : plugin_loader.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Plugin Loader Module:
# - Loads external plugins dynamically
# - Registers extensions
# - Manages plugin lifecycle
# - Supports modular architecture
# ============================================================


import importlib
import os


class PluginLoader:

    def __init__(self, plugin_dir="plugins"):
        self.plugin_dir = plugin_dir
        self.plugins = {}

    # ========================================================
    # LOAD ALL PLUGINS
    # ========================================================
    def load_plugins(self):
        if not os.path.exists(self.plugin_dir):
            os.makedirs(self.plugin_dir)

        for file in os.listdir(self.plugin_dir):

            if file.endswith(".py") and not file.startswith("__"):
                module_name = file[:-3]

                try:
                    module = importlib.import_module(f"{self.plugin_dir}.{module_name}")

                    if hasattr(module, "register"):
                        plugin = module.register()
                        self.plugins[module_name] = plugin

                        print(f"[PLUGIN LOADED] {module_name}")

                except Exception as e:
                    print(f"[PLUGIN ERROR] {module_name} -> {str(e)}")

        return self.plugins

    # ========================================================
    # GET ALL PLUGINS
    # ========================================================
    def get_plugins(self):
        return self.plugins

    # ========================================================
    # RUN SPECIFIC PLUGIN
    # ========================================================
    def run_plugin(self, name: str, *args, **kwargs):
        if name in self.plugins:

            try:
                return self.plugins[name].run(*args, **kwargs)

            except Exception as e:
                return f"Plugin Error: {str(e)}"

        return "Plugin not found"

    # ========================================================
    # LIST PLUGINS
    # ========================================================
    def list_plugins(self):
        print("\n========== PLUGINS ==========")

        for name in self.plugins.keys():
            print(f"- {name}")

        print("=============================\n")


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    loader = PluginLoader()

    loader.load_plugins()
    loader.list_plugins()