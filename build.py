from pathlib import Path
import shutil
import zipfile

ADDON_ID = "plugin.video.aiobridge"
VERSION = "0.1.0"

ROOT = Path(__file__).parent
DIST = ROOT / "dist"

FILES = [
    "addon.xml",
    "default.py",
    "router.py",
    "LICENSE",
    "README.md",
]

DIRS = [
    "lib",
    "resources",
]


def build():
    DIST.mkdir(exist_ok=True)

    zip_path = DIST / f"{ADDON_ID}-{VERSION}.zip"

    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:

        # File nella root dell'addon
        for file in FILES:
            src = ROOT / file
            if src.exists():
                z.write(src, arcname=f"{ADDON_ID}/{file}")

        # Cartelle ricorsive
        for directory in DIRS:
            base = ROOT / directory
            if not base.exists():
                continue

            for file in base.rglob("*"):
                if file.is_file():
                    relative = file.relative_to(ROOT)
                    z.write(file, arcname=f"{ADDON_ID}/{relative}")

    print(f"Build completata:\n{zip_path}")


if __name__ == "__main__":
    build()