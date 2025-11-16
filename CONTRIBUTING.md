# Contributing

## Quick Start

**To update your resume:**
1. Edit `resume-data.json` (your content)
2. Commit and push
3. Wait 30 seconds
4. Done! HTML, PDF, and README auto-updated

## Files

### ✅ Edit These
- `resume-data.json` - All content (jobs, skills, education)
- `style.css` - Design (colors, fonts, spacing)

### ⛔ Never Touch
- `resume.html` - Auto-generated from template + data
- `README.md` - Auto-generated from JSON
- `Munevver_Aslan_Resume_*.pdf` - Auto-generated

### ⚠️ Advanced Only
- `resume-template.html` - HTML structure (rarely needed)
- `.github/workflows/generate-resume.yml` - Automation

## How It Works

```
resume-data.json + resume-template.html
  ↓ Jinja2
resume.html
  ↓ Playwright
PDF
  ↓ JSON reader
README.md
```

**Timeline:** 30-40 seconds

## Editing resume-data.json

**Add a job:**
```json
{"title": "Job Title", "company": "Company", "location": "Remote",
 "date": "Jan 2025 - Present", "bullets": ["Achievement"]}
```

**Add skills:**
```json
{"category": "Design", "items": "Figma, Adobe XD"}
```

**Note:** First job = "Currently" in README

## Common Mistakes

**Don't:**
- Edit auto-generated files (resume.html, README.md, PDFs)
- Use invalid JSON (missing commas, quotes)

**Do:**
- Validate JSON before committing
- Keep first job as current role
- Use a JSON validator

## Editing Methods

### GitHub Web (Easiest)
1. Go to repo → `resume-data.json`
2. Click pencil icon
3. Edit
4. Commit

### Local
```bash
git clone https://github.com/mnvvr/mnvvr.git
cd mnvvr
# Edit resume-data.json
git add resume-data.json
git commit -m "Update experience"
git push
git pull  # Get generated files
```

## Troubleshooting

**Workflow failed?**
- Check Actions tab for errors
- Verify JSON syntax (no trailing commas)

**PDF looks wrong?**
- Check `style.css` syntax
- Preview `resume.html` locally

## Permissions

Required: Settings → Actions → General → "Read and write permissions"
