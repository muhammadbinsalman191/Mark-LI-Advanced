import subprocess
import sys
import platform
from pathlib import Path

REQUIRED_PYTHON = (3, 12)

if sys.version_info[:2] != REQUIRED_PYTHON:
    current = platform.python_version()
    print(
        f"ERROR: Mark-LI Advanced currently targets Python 3.12.x. "
        f"You are running Python {current}."
    )
    print("Install Python 3.12 and run setup.py with that interpreter.")
    raise SystemExit(1)

print(f"Using Python {platform.python_version()} (tested target: 3.12.x)")

print("Installing requirements...")
subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)

print("Installing Playwright browsers...")
subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)

if platform.system() == "Windows":
    try:
        import win32com.client  # noqa: F401
    except ImportError:
        postinstall = Path(sys.executable).parent / "Scripts" / "pywin32_postinstall.py"
        print(
            "\n⚠️  pywin32 did not install correctly — desktop shortcut creation "
            "will fall back to a slower method that may not work on this machine.\n"
            "    Try fixing it manually with:\n"
            f'    "{sys.executable}" -m pip install --force-reinstall pywin32\n'
            f'    "{sys.executable}" "{postinstall}" -install\n'
        )

print("\n✅ Setup complete! Run 'python main.py' to start MARK LI.")

