import json
import os
import re
from jinja2 import Environment, FileSystemLoader

# Initialization
COLLECTION_PATH = "GitHub Web API Reference.postman_collection.json"
TEMPLATES_DIR = "templates"
OUTPUT_DIR = "docs/api-reference"
NAV_TOML = "zensical.toml"

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
endpoint_template = env.get_template("api_endpoint.md.j2")
overview_template = env.get_template("api_overview.md.j2")

def slugify(text):
    return re.sub(r'[\s/]+', '-', text.lower().strip().replace('{', '').replace('}', ''))

def parse_url(url_obj):
    if isinstance(url_obj, str):
        return url_obj
    return url_obj.get('raw', '')

def extract_parameters(request):
    params = []
    url = request.get('url', {})
    
    # Path Variables
    for var in url.get('variable', []):
        params.append({
            "name": var.get('key'),
            "type": "string",
            "location": "Path",
            "required": True,
            "description": var.get('description', '')
        })
    
    # Query Parameters
    for query in url.get('query', []):
        params.append({
            "name": query.get('key'),
            "type": "string",
            "location": "Query",
            "required": False,
            "description": query.get('description', '')
        })
    
    return params

def extract_responses(responses):
    extracted = []
    for resp in responses:
        extracted.append({
            "code": resp.get('code'),
            "status": resp.get('status'),
            "description": resp.get('name', ''),
            "example": resp.get('body', '')
        })
    return extracted

def process_item(item, parent_path=""):
    name = item.get('name')
    slug = slugify(name)
    current_path = os.path.join(parent_path, slug)
    
    # If it's a folder
    if 'item' in item:
        os.makedirs(os.path.join(OUTPUT_DIR, parent_path), exist_ok=True)
        endpoints_in_folder = []
        
        for sub_item in item['item']:
            result = process_item(sub_item, slug if not parent_path else os.path.join(parent_path, slug))
            if result:
                endpoints_in_folder.append(result)
        
        # Generate Overview for folder
        if endpoints_in_folder:
            overview_content = overview_template.render(
                category={
                    "name": name,
                    "description": item.get('description', f"API endpoints for {name}."),
                    "endpoints": endpoints_in_folder
                }
            )
            overview_filename = os.path.join(OUTPUT_DIR, parent_path, slug, "index.md")
            os.makedirs(os.path.dirname(overview_filename), exist_ok=True)
            with open(overview_filename, "w", encoding="utf-8") as f:
                f.write(overview_content)
                
        return {
            "name": name,
            "path": f"{slug}/index.md",
            "description": item.get('description', '')
        }
    
    # If it's a request (endpoint)
    request = item.get('request')
    if request:
        endpoint_data = {
            "name": name,
            "description": request.get('description', ''),
            "method": request.get('method'),
            "url": parse_url(request.get('url')),
            "parameters": extract_parameters(request),
            "request_example": request.get('body', {}).get('raw', ''),
            "responses": extract_responses(item.get('response', []))
        }
        
        content = endpoint_template.render(endpoint=endpoint_data)
        filename = f"{slug}.md"
        full_path = os.path.join(OUTPUT_DIR, parent_path, filename)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        return {
            "name": name,
            "path": filename,
            "summary": request.get('description', '')[:100] + "...",
            "method": request.get('method'),
            "url": endpoint_data['url']
        }

def run():
    print(f"Loading collection from {COLLECTION_PATH}...")
    with open(COLLECTION_PATH, 'r', encoding='utf-8') as f:
        collection = json.load(f)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("Generating API reference...")
    for item in collection.get('item', []):
        process_item(item)
    
    print("Generation complete.")

if __name__ == "__main__":
    run()
