import os
import toml
import yaml

def generate_nav(directory):
    nav_sections = []
    
    # Process top-level files as an 'Overview' section
    overview_pages = []
    for item in sorted(os.listdir(directory)):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path) and item.endswith(".md"):
            overview_pages.append(os.path.relpath(item_path, "docs").replace("\\", "/"))
    
    if overview_pages:
        nav_sections.append({
            "title": "General",
            "pages": overview_pages
        })
    
    # Process top-level directories as sections
    for item in sorted(os.listdir(directory)):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            section = {
                "title": item.replace("-", " ").title(),
                "pages": []
            }
            
            # Recurse for pages
            for root, dirs, files in os.walk(item_path):
                for file in files:
                    if file.endswith(".md"):
                        rel_path = os.path.relpath(os.path.join(root, file), "docs")
                        section["pages"].append(rel_path.replace("\\", "/"))
            
            if section["pages"]:
                nav_sections.append(section)
                
    return nav_sections

def update_mkdocs(nav_sections):
    print("Updating mkdocs.yml...")
    
    # Map TOML sections to MkDocs nav format string
    nav_lines = ["nav:", "  - Home: index.md"]
    
    # Add Diátaxis sections if they exist
    diataxis = {
        "Tutorials": "tutorials/",
        "How-to Guides": "how-to/",
        "Explanation": "explanation/"
    }
    
    for title, folder in diataxis.items():
        if os.path.exists(os.path.join("docs", folder)):
            pages = []
            for root, dirs, files in os.walk(os.path.join("docs", folder)):
                for file in files:
                    if file.endswith(".md"):
                        pages.append(os.path.relpath(os.path.join(root, file), "docs").replace("\\", "/"))
            if pages:
                nav_lines.append(f"  - {title}:")
                for page in sorted(pages):
                    nav_lines.append(f"      - {page}")

    # Add API Reference
    nav_lines.append("  - API Reference:")
    for section in nav_sections:
        nav_lines.append(f"      - {section['title']}:")
        for page in section['pages']:
            nav_lines.append(f"          - {page}")

    with open("mkdocs.yml", "r") as f:
        lines = f.readlines()

    # Find where nav starts
    new_lines = []
    for line in lines:
        if line.strip().startswith("nav:"):
            break
        new_lines.append(line)
    
    new_lines.extend([l + "\n" for l in nav_lines])
    
    with open("mkdocs.yml", "w") as f:
        f.writelines(new_lines)

def run():
    print("Synchronizing navigation...")
    with open("zensical.toml", "r") as f:
        config = toml.load(f)
        
    nav_sections = generate_nav("docs/api-reference")
    config["navigation"]["sections"] = nav_sections
    
    with open("zensical.toml", "w") as f:
        toml.dump(config, f)
    
    update_mkdocs(nav_sections)
    print("Navigation synchronized.")

if __name__ == "__main__":
    run()
