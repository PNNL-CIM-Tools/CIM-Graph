# MkDocs Setup Guide

This document explains the MkDocs documentation setup for GitHub Pages alongside the existing Sphinx/ReadTheDocs configuration.

## What Was Set Up

### 1. Configuration Files

- **`mkdocs.yml`** - Main MkDocs configuration with Material theme
  - Configured for dual light/dark mode
  - Navigation tabs matching your existing structure
  - Mermaid diagram support enabled
  - Jupyter notebook rendering enabled

- **`docs/requirements-mkdocs.txt`** - Python dependencies for building MkDocs site
  - MkDocs Material theme
  - mkdocs-jupyter for notebook support
  - pymdown-extensions for mermaid diagrams

- **`docs/index.md`** - New landing page for MkDocs (converted from index.rst)

- **`.github/workflows/docs.yml`** - GitHub Actions workflow for automatic deployment

### 2. GitHub Actions Workflow

The workflow is triggered on:
- Push to `main` or `develop` branches (when docs files change)
- Pull requests to these branches
- Manual trigger via `workflow_dispatch`

**Deployment behavior:**
- `main` branch → Deploys to GitHub Pages at `https://pnnl-cim-tools.github.io/CIM-Graph/`
- `develop` branch → Deploys to gh-pages branch with special marking
- Pull requests → Builds but does not deploy (for validation)

## Local Development

### Install Dependencies

```bash
pip install -r docs/requirements-mkdocs.txt
```

### Build the Site

```bash
# Build the site (outputs to site/ directory)
mkdocs build

# Serve locally with hot reload at http://127.0.0.1:8000
mkdocs serve
```

### Preview Changes

```bash
# Start development server
mkdocs serve

# Open browser to http://127.0.0.1:8000
# Changes to docs will auto-reload
```

## Enabling GitHub Pages

To enable GitHub Pages for your repository:

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under **Source**, select:
   - Source: **GitHub Actions** (NOT "Deploy from a branch")
4. Save

The first deployment will happen when you push changes to the `main` branch that affect the docs.

## Workflow with ReadTheDocs

You now have **dual documentation publishing**:

### ReadTheDocs (Sphinx)
- **Config**: `docs/conf.py` and `docs/.readthedocs.yaml`
- **Build**: Uses nb-sphinx
- **URL**: Your existing ReadTheDocs URL
- **Trigger**: Automatic on ReadTheDocs when you push

### GitHub Pages (MkDocs)
- **Config**: `mkdocs.yml`
- **Build**: Uses mkdocs-jupyter
- **URL**: `https://pnnl-cim-tools.github.io/CIM-Graph/`
- **Trigger**: GitHub Actions workflow on push to main/develop

**Both systems use the same source notebooks**, so you only need to edit once.

## Key Features

### Mermaid Diagrams

Mermaid diagrams in your notebooks will render automatically. Use triple backticks with `mermaid`:

\`\`\`mermaid
graph LR
    A[Start] --> B[Process]
    B --> C[End]
\`\`\`

Your existing mermaid diagrams in the notebooks (like in `01_overview/1_1_overview.ipynb`) will work out of the box.

### Jupyter Notebooks

All your `.ipynb` files are rendered directly without needing to convert them. The `mkdocs-jupyter` plugin handles:
- Code cells with syntax highlighting
- Output cells (text, images, plots)
- Markdown cells
- Mermaid diagrams in markdown cells

### Material Theme Features

- **Search** - Full-text search across all documentation
- **Dark/Light Mode** - Toggle in top-right corner
- **Mobile Responsive** - Works great on all devices
- **Code Copy** - One-click copy for code blocks
- **Navigation** - Tabs, sections, and table of contents

## Customization

### Changing Theme Colors

Edit `mkdocs.yml`:

```yaml
theme:
  palette:
    - scheme: default
      primary: indigo  # Change this color
      accent: indigo   # Change this color
```

Available colors: red, pink, purple, deep purple, indigo, blue, light blue, cyan, teal, green, light green, lime, yellow, amber, orange, deep orange

### Adding Custom CSS

1. Create CSS file at `docs/stylesheets/extra.css` (already exists)
2. Edit `mkdocs.yml` to reference it (already configured)

### Adding New Pages

1. Create new `.ipynb` or `.md` file in appropriate `docs/` subdirectory
2. Add entry to `nav:` section in `mkdocs.yml`

## Testing Before Deployment

Always test locally before pushing:

```bash
# Clean build (removes old site directory)
rm -rf site/
mkdocs build --strict

# Strict mode will fail on warnings
# Verbose mode shows detailed output
mkdocs build --strict --verbose
```

## Troubleshooting

### Build Fails in GitHub Actions

1. Check the Actions tab in your repository
2. Look at the build logs for errors
3. Test locally with `mkdocs build --strict --verbose`

### Mermaid Diagrams Not Rendering

- Ensure you're using triple backticks with `mermaid` language identifier
- Check the diagram syntax at https://mermaid.js.org/

### Notebooks Not Converting

- Verify the notebook is valid JSON (can open in Jupyter)
- Check for execution errors if you enable `execute: true` in config

### GitHub Pages Not Updating

1. Check that GitHub Actions workflow ran successfully
2. Verify GitHub Pages is configured to use **GitHub Actions** (not branch)
3. Wait 1-2 minutes for CDN cache to clear

## Next Steps

Now that the workflow is set up, consider:

1. **Complete Empty Notebooks** - Fill in the 17 minimal/empty notebooks
2. **Add More Mermaid Diagrams** - Enhance existing notebooks with sequence/class diagrams
3. **Create Templates** - Build reusable notebook templates for consistency
4. **Customize Theme** - Adjust colors, fonts, and layout to match your branding
5. **Add Examples** - Include more code examples and use cases

## File Structure

```
CIM-Graph/
├── mkdocs.yml                      # MkDocs configuration
├── docs/
│   ├── index.md                    # Home page (new)
│   ├── requirements-mkdocs.txt     # MkDocs dependencies
│   ├── conf.py                     # Sphinx config (existing)
│   ├── .readthedocs.yaml          # ReadTheDocs config (existing)
│   ├── stylesheets/
│   │   └── extra.css              # Custom CSS
│   └── [sections]/                 # Your existing notebooks
└── .github/
    └── workflows/
        └── docs.yml                # GitHub Actions workflow
```

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [mkdocs-jupyter Plugin](https://github.com/danielfrg/mkdocs-jupyter)
- [Mermaid Diagram Syntax](https://mermaid.js.org/)
