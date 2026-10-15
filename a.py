from pathlib import Path

# Folder containing this script
ROOT_FOLDER = Path(__file__).resolve().parent

# Blockbench model file extension
TARGET_EXTENSIONS = {".blockymodel", ".bbmodel"}


def replace_with_markdown(file_path: Path) -> None:
    original_name = file_path.name
    markdown_path = file_path.with_name(original_name + ".md")

    # Never overwrite an existing Markdown file
    if markdown_path.exists():
        print(f"SKIPPED (replacement exists): {file_path}")
        return

    content = (
        f"# This used to be {original_name}\n\n"
        "Original file type: bbmodel\n\n"
        "This file has been removed for memory space. "
        "Treat it as if it were the original one.\n"
    )

    try:
        # Create the placeholder first
        markdown_path.write_text(content, encoding="utf-8")

        # Delete the original only after successful creation
        file_path.unlink()

        print(f"REPLACED: {file_path} -> {markdown_path}")

    except OSError as error:
        print(f"ERROR processing {file_path}: {error}")


def main() -> None:
    print(f"Scanning: {ROOT_FOLDER}")

    files = [
        path
        for path in ROOT_FOLDER.rglob("*")
        if path.is_file()
        and path.suffix.lower() in TARGET_EXTENSIONS
    ]

    print(f"Found {len(files)} .bbmodel files.")

    for file_path in files:
        replace_with_markdown(file_path)

    print("Done!")


if __name__ == "__main__":
    main()
