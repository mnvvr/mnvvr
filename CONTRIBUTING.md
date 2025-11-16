# Contributing to This Resume Repository

This repository uses a **single source of truth** system with automated PDF and README generation. Understanding what to edit and what to leave alone is crucial.

---

## 🎯 Quick Start for Designers

**To update your resume:**

1. Edit `resume-data.json` (your content - jobs, skills, education)
2. Edit `style.css` (if you want design changes)
3. Commit and push
4. Wait 30-40 seconds
5. Done! HTML, PDF, and README are automatically updated

**That's it.** Never touch the generated files manually.

---

## 📁 File Structure

### ✅ Files You Should Edit

| File | Purpose | When to Edit |
|------|---------|-------------|
| `resume-data.json` | **Your resume content** - All text, experience, skills, education in JSON format | Every time you update your resume content |
| `style.css` | **Visual styling** for the PDF - Colors, fonts, spacing, layout | When you want to change the design/appearance |

### ⚠️ Files You Might Edit (Advanced)

| File | Purpose | When to Edit |
|------|---------|-------------|
| `resume-template.html` | HTML structure template with placeholders | When you want to change HTML structure/layout (rare) |

### ⛔ Files You Should NEVER Touch

| File | Purpose | Why Not to Touch |
|------|---------|------------------|
| `resume.html` | Auto-generated from template + data | Regenerated from resume-data.json on every push |
| `README.md` | Auto-generated GitHub profile page | Regenerated from resume-data.json on every push |
| `Munevver_Aslan_Resume_*.pdf` | Auto-generated versioned PDF | Created by workflow, commit hash in filename |
| `.github/workflows/generate-resume.yml` | Automation script | Only edit if you understand GitHub Actions |

---

## 🔄 How the Automation Works

When you push changes to `resume-data.json`:

```
1. GitHub Actions triggers
2. Template + Data → resume.html (Jinja2 templating)
3. resume.html → PDF (Playwright with full CSS support)
4. Data → README.md (direct JSON reading)
5. Old PDF deleted automatically
6. HTML, PDF, and README committed back to repo
```

**Timeline:** ~30-40 seconds from push to completion

---

## ✏️ Editing Your Resume

### Option 1: GitHub Web Interface (Easiest)

1. Go to https://github.com/mnvvr/mnvvr
2. Click `resume-data.json`
3. Click the pencil icon (✏️ Edit)
4. Make your changes
5. Click "Commit changes"
6. Wait ~30-40 seconds

### Option 2: Local Editing

```bash
git clone https://github.com/mnvvr/mnvvr.git
cd mnvvr
# Edit resume-data.json in your editor
git add resume-data.json
git commit -m "Update work experience"
git push origin main
git pull  # Get generated files
```

---

## 📝 resume-data.json Structure

### Adding a New Job
```json
{
  "experience": [
    {
      "title": "Your Job Title",
      "company": "Company Name",
      "location": "City, Country or Remote",
      "date": "Month Year - Present",
      "bullets": [
        "Achievement or responsibility",
        "Another achievement"
      ]
    }
  ]
}
```

### Adding a Skill Category
```json
{
  "skills": [
    {
      "category": "Category Name",
      "items": "Tool 1, Tool 2, Tool 3"
    }
  ]
}
```

**Note:** The FIRST experience item appears in README.md as "Currently"

---

## 🎨 Styling Guide (style.css)

### Key Variables
- **Accent color:** `#e91e63` (pink used in highlights, company names, dates)
- **Text color:** `#333` (main text)
- **Light text:** `#666` (secondary text like locations)
- **Font:** 'Outfit' from Google Fonts

### Common Changes

**Change accent color:**
```css
/* Find and replace #e91e63 with your color */
.highlight { color: #YOUR_COLOR; }
.company-name { color: #YOUR_COLOR; }
```

**Change font:**
```css
@import url('https://fonts.googleapis.com/css2?family=YourFont&display=swap');
body { font-family: 'YourFont', -apple-system, sans-serif; }
```

**Adjust spacing:**
```css
.section { margin-bottom: 15px; }  /* Space between sections */
.experience-item { margin-bottom: 12px; }  /* Space between jobs */
```

---

## 🚨 Common Mistakes

### ❌ Don't

- Edit `resume.html`, `README.md`, or PDF files (auto-generated)
- Use invalid JSON syntax (missing commas, unmatched brackets)
- Forget quotes around string values in JSON

### ✅ Do

- Edit `resume-data.json` for all content changes
- Validate JSON before committing (use a JSON validator)
- Keep the first experience item as your current role

---

## 📤 Sharing Your Resume

### Latest PDF Location

After any update, your latest PDF is:
```
Munevver_Aslan_Resume_XXXXXXX.pdf
```
Where `XXXXXXX` is the 7-character commit hash.

### Download Link

Share this GitHub raw URL (updates automatically):
```
https://github.com/mnvvr/mnvvr/raw/main/Munevver_Aslan_Resume_XXXXXXX.pdf
```

**Note:** Update the commit hash when you make changes.

### README Link

Your README always links to the latest PDF:
```markdown
📄 [Download Resume (PDF)](./Munevver_Aslan_Resume_XXXXXXX.pdf)
```

---

## 🐛 Troubleshooting

### Workflow Failed

1. Go to https://github.com/mnvvr/mnvvr/actions
2. Click the failed workflow run
3. Check the error logs
4. Common issues:
   - **HTML syntax error:** Fix in `resume.html`
   - **Missing class names:** Parser expects specific classes
   - **Permission error:** Check workflow permissions in Settings → Actions

### PDF Looks Wrong

1. Check `style.css` for syntax errors
2. Preview `resume.html` locally in a browser
3. Check browser console for CSS errors

### README Missing Content

1. Verify the HTML structure in `resume.html`
2. Check that class names match what the parser expects:
   - `summary-text` for summary
   - `skill-category` and `skill-items` for skills
   - `experience-item` for jobs

---

## 🔧 Advanced: Modifying the Workflow

**Only edit `.github/workflows/generate-resume.yml` if you need to:**

- Change PDF generation settings (margins, page size)
- Modify README structure or content extraction
- Add new automation steps
- Change file naming conventions

**Before editing:**
1. Understand GitHub Actions syntax
2. Test in a fork repository first
3. Be prepared to debug Python and shell scripts

**Key workflow steps:**
1. **Setup:** Node.js and Playwright installation
2. **PDF generation:** Chromium headless rendering
3. **README generation:** Python HTML parser
4. **Git operations:** Auto-commit and push

---

## 📋 Workflow Permissions

Required repository settings (Settings → Actions → General):

- ✅ **Workflow permissions:** "Read and write permissions"
- ✅ **Allow GitHub Actions to create and approve pull requests:** Enabled

Without these, the workflow cannot commit generated files.

---

## 🎓 Learning Resources

- **HTML basics:** https://developer.mozilla.org/en-US/docs/Learn/HTML
- **CSS styling:** https://developer.mozilla.org/en-US/docs/Learn/CSS
- **GitHub Actions:** https://docs.github.com/en/actions
- **Git basics:** https://git-scm.com/book/en/v2/Getting-Started-Git-Basics

---

## 💡 Tips for Best Results

1. **Preview locally** before pushing:
   - Open `resume.html` in your browser
   - Check that everything looks correct
   - Test print preview (Cmd/Ctrl + P)

2. **Make small, focused commits:**
   ```
   Good: "Update current job description"
   Bad: "Changed stuff"
   ```

3. **Keep the first experience item current:**
   - This appears in README as "Currently"
   - List jobs in reverse chronological order (newest first)

4. **Use consistent formatting:**
   - Date format: "Month Year - Present" or "Month Year - Month Year"
   - Location format: "City, Country" or "Remote"

---

## 📞 Getting Help

If something breaks or you need help:

1. Check the Actions tab for error messages
2. Review this guide for common issues
3. Check `resume.html` for HTML syntax errors
4. Verify class names haven't been accidentally removed

**Remember:** The system is designed to be simple. Edit `resume.html`, push, and let automation handle the rest!
