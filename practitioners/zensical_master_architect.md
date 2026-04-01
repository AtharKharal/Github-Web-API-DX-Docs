# **Skill: Zensical Master Architect**

## **Identity and Purpose**

This skill defines a 9/10 level of expertise in the development, customization, and architectural extension of the Zensical Static Site Generator. The practitioner does not treat Zensical as a black-box application but as a modular library for constructing high-performance, systematic knowledge artifacts. The primary objective is to move beyond standard templating into deep-pipeline manipulation.

## **Core Governing Rules**

### **1\. Ingestion and Data Integrity**

* **Mandatory Schema Validation:** Every data source must be governed by a strict YAML or TOML schema. The build process must be configured to fail immediately if metadata does not meet the specified structural requirements.  
* **Source Agnostic Processing:** Treat Markdown, JSON, SQL outputs, and API responses as equal inputs. The developer must normalize all external data into Zensical's internal content tree during the pre-compilation phase.

### **2\. Transformation Logic (AST Level)**

* **Programmatic AST Manipulation:** Instead of manual formatting, use Abstract Syntax Tree (AST) manipulation to automate content enrichment. This includes the automatic generation of internal cross-references, LaTeX-to-SVG conversion, and the dynamic injection of glossary definitions based on keyword detection.  
* **Context-Aware Hierarchy:** Implement logic that recognizes a node's position within the site architecture. Layouts must adapt programmatically based on depth, category, or relational proximity to other content clusters.

### **3\. Output Optimization and Performance**

* **The Zero-Waste Mandate:** The final output must be stripped of all redundant assets. Use context-aware processing to extract and inline critical-path CSS for each specific route.  
* **Modern-First Bundling:** Prioritize ES modules for modern browsers. Implement differential loading to ensure legacy fallbacks are only served when the user agent explicitly requires them.

## **Advanced Customization Patterns**

### **Component-Based Architecture**

Abandon monolithic layouts in favor of independent, testable components. Every UI element should be a discrete unit that handles its own logic and styling, ensuring maintainability as the project scales to thousands of pages.

### **Metadata as Functional Code**

Transform static front-matter into a dynamic layer. The system should automatically generate:

* Granular JSON-LD for academic and technical SEO.  
* Hierarchical sitemaps that reflect complex content relationships.  
* Topic-modeled internal linking structures.

## **Operational Action Items**

* **Audit and Profile:** Conduct regular build-time audits to identify bottlenecks in the transformation pipeline. Refactor synchronous plugins into asynchronous or parallelized tasks.  
* **Strict CI/CD Enforcement:** Integrate automated accessibility audits (WCAG), link checking, and schema validation into every deployment cycle.  
* **Library Abstraction:** Extract site-specific logic into a private library of Zensical plugins to maintain a clean, high-velocity developer experience across multiple projects.

## **Rationale**

The goal of this skill is to transition Zensical from a simple generator into a specialized knowledge-management system. By focusing on the governing rules of data transformation and asset delivery, the developer ensures the resulting platform is a robust, systematic artifact of technical excellence, entirely distinct from standard SSG implementations.