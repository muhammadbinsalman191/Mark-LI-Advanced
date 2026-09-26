from __future__ import annotations

import importlib.util
import json
import py_compile
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "main.py",
    "ui.py",
    "requirements.txt",
    "core/prompt.txt",
]

CRITICAL_MODULES = [
    "PyQt6",
    "sounddevice",
    "google.genai",
    "requests",
    "numpy",
]


def ok(message: str) -> None:
    print(f"[OK] {message}")


def fail(message: str) -> None:
    print(f"[FAIL] {message}")


def check_files() -> bool:
    success = True

    for relative_path in REQUIRED_FILES:
        path = ROOT / relative_path

        if path.exists():
            ok(f"Found {relative_path}")
        else:
            fail(f"Missing required file: {relative_path}")
            success = False

    return success


def check_dependencies() -> bool:
    success = True

    for module in CRITICAL_MODULES:
        try:
            available = importlib.util.find_spec(module) is not None
        except (ImportError, ModuleNotFoundError):
            available = False

        if available:
            ok(f"Dependency available: {module}")
        else:
            fail(
                f"Missing dependency: {module}. "
                "Run: python -m pip install -r requirements.txt"
            )
            success = False

    return success


def check_syntax() -> bool:
    success = True

    for relative_path in ("main.py", "ui.py"):
        path = ROOT / relative_path

        try:
            py_compile.compile(str(path), doraise=True)
            ok(f"Syntax valid: {relative_path}")
        except py_compile.PyCompileError as exc:
            fail(f"Syntax error in {relative_path}: {exc}")
            success = False

    return success


def check_config() -> bool:
    config_path = ROOT / "config" / "api_keys.json"

    if not config_path.exists():
        print(
            "[INFO] config/api_keys.json is not present. "
            "Real API credentials are not required for this smoke test."
        )
        return True

    try:
        data = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"Could not safely parse config/api_keys.json: {type(exc).__name__}")
        return False

    if "gemini_api_key" in data:
        ok("Gemini API key configuration entry detected (value hidden)")
    else:
        print(
            "[INFO] config/api_keys.json exists but gemini_api_key is not configured."
        )

    return True


def check_main_import() -> bool:
    command = [
        sys.executable,
        "-c",
        "import main; print('[OK] main.py imported successfully')",
    ]

    try:
        result = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except subprocess.TimeoutExpired:
        fail("Importing main.py timed out")
        return False

    if result.returncode == 0:
        if result.stdout.strip():
            print(result.stdout.strip())
        return True

    fail("main.py could not be imported")

    if result.stderr.strip():
        print(result.stderr.strip())

    return False


def main() -> int:
    print("Mark-LI Advanced startup smoke test")
    print("=" * 40)

    checks = [
        check_files(),
        check_dependencies(),
        check_syntax(),
        check_config(),
        check_main_import(),
    ]

    print("=" * 40)

    if all(checks):
        print("[PASS] Startup smoke test passed.")
        return 0

    print("[FAIL] Startup smoke test failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
