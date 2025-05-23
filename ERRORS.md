ERROR: ImportError: cannot import name 'appengine' from 'urllib3.contrib'


You're encountering a **compatibility issue** with `twine` (or `requests_toolbelt`) and the installed version of `urllib3`. Specifically, the error is:

```
ImportError: cannot import name 'appengine' from 'urllib3.contrib'
```

### 💥 Why this is happening:

* Older versions of `requests_toolbelt` rely on `urllib3.contrib.appengine`, which has been removed in recent versions of `urllib3`.
* This typically breaks `twine upload`.

---

### ✅ Solution: Upgrade `twine` and `requests_toolbelt`

You likely have an old `twine` installed globally that's incompatible with the latest `urllib3`.

Run this in your **virtual environment** or as a user install:

```bash
pip install --upgrade twine requests_toolbelt
```

To avoid using the globally installed (and possibly broken) version of `twine`, consider using it inside your virtual environment or via `python -m`.

---

### ✅ Alternative: Use `build` and `twine` via Python module

Instead of calling `twine` directly, run:

```bash
python -m build  # Builds both .tar.gz and .whl
python -m twine upload dist/*
```

If `python -m twine` still fails after upgrading, uninstall the global one:

```bash
pip uninstall twine requests_toolbelt
```

Then reinstall it only in your venv:

```bash
python -m pip install --upgrade twine requests_toolbelt
```

---

### 🔄 Optional Cleanup

You might want to clear the cache and reinstall dependencies if issues persist:

```bash
rm -rf ~/.cache/pip
pip install --force-reinstall twine requests_toolbelt
```

Let me know if you'd like a clean `pyproject.toml` + `build` setup to replace your `setup.py`.
