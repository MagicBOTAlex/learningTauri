# src-tauri/src-python/main.py
_tauri_plugin_functions = ["greet_python"] # make "greet_python" callable from UI
def greet_python(rust_var):
    return str(rust_var) + " from python"