# ============================================================
# File Name : extension_sdk.py
# Project   : CyberSecuritySuite
# Author    : Gull Virk
# Version   : 1.0.0
#
# Description:
# Extension SDK Module:
# - Defines plugin interface
# - Standardizes extensions
# - Provides lifecycle hooks
# - Safe execution wrapper for plugins
# ============================================================


class ExtensionBase:
    """
    Base class for all extensions/plugins.
    Every plugin must inherit this class.
    """

    def __init__(self, name="Unnamed Extension"):
        self.name = name

    # ========================================================
    # LIFECYCLE METHODS
    # ========================================================
    def on_load(self):
        """Called when plugin is loaded"""
        pass

    def on_unload(self):
        """Called when plugin is unloaded"""
        pass

    def run(self, *args, **kwargs):
        """Main execution method"""
        raise NotImplementedError("Plugin must implement run()")


# ============================================================
# EXTENSION MANAGER
# ============================================================
class ExtensionManager:

    def __init__(self):
        self.extensions = {}

    # ========================================================
    # REGISTER EXTENSION
    # ========================================================
    def register(self, name: str, extension: ExtensionBase):
        try:
            self.extensions[name] = extension
            extension.on_load()
            print(f"[EXTENSION LOADED] {name}")
        except Exception as e:
            print(f"[ERROR] Failed to load extension {name}: {str(e)}")

    # ========================================================
    # UNREGISTER EXTENSION
    # ========================================================
    def unregister(self, name: str):
        if name in self.extensions:
            try:
                self.extensions[name].on_unload()
                del self.extensions[name]
                print(f"[EXTENSION REMOVED] {name}")
            except Exception as e:
                print(f"[ERROR] Unload failed {name}: {str(e)}")

    # ========================================================
    # RUN EXTENSION
    # ========================================================
    def run(self, name: str, *args, **kwargs):
        if name not in self.extensions:
            return {"error": "Extension not found"}

        try:
            return self.extensions[name].run(*args, **kwargs)
        except Exception as e:
            return {"error": str(e)}

    # ========================================================
    # LIST EXTENSIONS
    # ========================================================
    def list_extensions(self):
        return list(self.extensions.keys())


# ============================================================
# SAMPLE EXTENSION (DEMO)
# ============================================================
class SampleExtension(ExtensionBase):

    def __init__(self):
        super().__init__("SampleExtension")

    def on_load(self):
        print("[SampleExtension] Loaded successfully")

    def on_unload(self):
        print("[SampleExtension] Unloaded")

    def run(self, data):
        return f"Processed: {data}"


# ============================================================
# TEST RUN
# ============================================================
if __name__ == "__main__":

    manager = ExtensionManager()

    sample = SampleExtension()

    manager.register("sample", sample)

    print(manager.run("sample", "Hello CyberSecurity"))

    print("Installed Extensions:", manager.list_extensions())

    manager.unregister("sample")