import os

# Base project directory (current directory)
BASE_DIR = os.getcwd()

# Folder structure to create
folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "reports",
    "images/charts"
]

# Files to create
files = {
    "README.md": "# Retail Sales Analysis\n\nProject setup initialized.\n",
    "requirements.txt": "pandas\nnumpy\nmatplotlib\nseaborn\njupyter\n",
    ".gitignore": ".ipynb_checkpoints/\n__pycache__/\n.DS_Store\n.env\n",
    "notebooks/01_data_cleaning.ipynb": "",
    "notebooks/02_exploratory_analysis.ipynb": "",
    "notebooks/03_visualization_insights.ipynb": ""
}

def create_folders():
    for folder in folders:
        path = os.path.join(BASE_DIR, folder)
        os.makedirs(path, exist_ok=True)
        print(f"📁 Created folder: {folder}")

def create_files():
    for file_path, content in files.items():
        path = os.path.join(BASE_DIR, file_path)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"📄 Created file: {file_path}")
        else:
            print(f"⚠️ File already exists: {file_path}")

if __name__ == "__main__":
    print("🚀 Setting up Retail Sales Analysis project structure...\n")
    create_folders()
    create_files()
    print("\n✅ Project structure setup complete!")
