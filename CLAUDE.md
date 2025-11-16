# Instructions for Claude

When helping with this resume repository, **follow CONTRIBUTING.md exactly**.

## Key Rules

1. **Single source of truth:** `resume-data.json` is the ONLY file users should edit for content
2. **Never edit auto-generated files:** resume.html, README.md, and PDF files are auto-generated
3. **Respect the architecture:** JSON data + HTML template → generated files
4. **When user wants to update resume:** Direct them to edit `resume-data.json`, not HTML
5. **JSON validation:** Always remind users to validate JSON syntax (no trailing commas, proper quotes)

## File Permissions

**User should edit:**
- `resume-data.json` (all content)
- `style.css` (design only)

**Never suggest editing:**
- `resume.html` (auto-generated from template + data)
- `README.md` (auto-generated from JSON)
- `Munevver_Aslan_Resume_*.pdf` (auto-generated)

**Advanced only (rarely):**
- `resume-template.html` (structure changes)
- `.github/workflows/generate-resume.yml` (workflow changes)

## Common User Requests

**"Update my job experience"** → Edit `resume-data.json` experience array
**"Change the design"** → Edit `style.css`
**"Add a skill"** → Edit `resume-data.json` skills array
**"Fix the PDF"** → Check `style.css` or workflow, never edit PDF directly
**"Update README"** → Edit `resume-data.json` (README auto-generates from it)

## Workflow Understanding

```
resume-data.json + resume-template.html
  ↓ Jinja2 template rendering
resume.html
  ↓ Playwright PDF generation
Munevver_Aslan_Resume_HASH.pdf
  ↓ JSON reader (no HTML parsing)
README.md
```

Timeline: 30-40 seconds after push

## When Making Changes

1. Always refer to CONTRIBUTING.md for current practices
2. Validate JSON before committing
3. Test changes don't break the workflow
4. Keep CONTRIBUTING.md under 100 lines
5. Maintain separation of concerns (content, structure, style)

## What NOT to Do

- Don't suggest complex HTML edits (use JSON instead)
- Don't recommend manual PDF generation
- Don't bypass the automation workflow
- Don't make CONTRIBUTING.md verbose (max 100 lines)
- Don't suggest editing generated files

## Architecture Principles

- **Separation:** Content (JSON) ≠ Structure (Template) ≠ Style (CSS)
- **Automation:** Designer edits data, everything else auto-generates
- **Simplicity:** Zero local dependencies, works via GitHub web interface
- **Single source:** JSON is truth, everything derives from it
