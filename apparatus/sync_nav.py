import os
import toml

def get_pages_in_dir(folder):
    pages = []
    if os.path.exists(os.path.join("docs", folder)):
        for root, dirs, files in os.walk(os.path.join("docs", folder)):
            for file in sorted(files):
                if file.endswith(".md"):
                    pages.append(os.path.relpath(os.path.join(root, file), "docs").replace("\\", "/"))
    return pages

def generate_api_sections(directory):
    nav_sections = []
    
    # Process top-level files as 'General'
    overview_pages = []
    if os.path.exists(directory):
        for item in sorted(os.listdir(directory)):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path) and item.endswith(".md"):
                overview_pages.append(os.path.relpath(item_path, "docs").replace("\\", "/"))
    
    if overview_pages:
        nav_sections.append({
            "title": "General",
            "pages": overview_pages
        })
    
    # Process top-level directories as sub-sections
    if os.path.exists(directory):
        for item in sorted(os.listdir(directory)):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                section = {
                    "title": item.replace("-", " ").title(),
                    "pages": []
                }
                
                # Recurse for pages
                for root, dirs, files in os.walk(item_path):
                    for file in sorted(files):
                        if file.endswith(".md"):
                            rel_path = os.path.relpath(os.path.join(root, file), "docs")
                            section["pages"].append(rel_path.replace("\\", "/"))
                
                if section["pages"]:
                    nav_sections.append(section)
                
    return nav_sections

def update_zensical(api_sections):
    print("Updating zensical.toml...")
    
    if os.path.exists("zensical.toml"):
        with open("zensical.toml", "r") as f:
            config = toml.load(f)
    else:
        config = {
            "project": {
                "site_name": "GitHub API Documentation Portal",
                "site_description": "A high-fidelity developer experience for the GitHub Web API."
            },
            "navigation": {
                "index": "index.md"
            }
        }

    # Define the core navigation including Diátaxis
    full_nav = []
    
    # Diátaxis mapping
    diataxis = {
        "Tutorials": "tutorials",
        "How-to Guides": "how-to",
        "Explanation": "explanation"
    }
    
    for title, folder in diataxis.items():
        pages = get_pages_in_dir(folder)
        if pages:
            full_nav.append({
                "title": title,
                "pages": pages
            })
            
    # Include API Reference sections
    full_nav.extend(api_sections)

    # Set navigation
    if "navigation" not in config:
        config["navigation"] = {}
    config["navigation"]["sections"] = full_nav

    with open("zensical.toml", "w") as f:
        toml.dump(config, f)

def run():
    print("Synchronizing navigation for Zensical...")
    api_sections = generate_api_sections("docs/api-reference")
    update_zensical(api_sections)
    print("Navigation synchronized.")

if __name__ == "__main__":
    run()
