# Resume Setup & Maintenance

This repository contains Münevver Aslan's professional resume in multiple formats, all **automatically generated from a single source of truth**.

## 📁 File Structure

```
.
├── resume-data.json          # 🎯 SINGLE SOURCE OF TRUTH - Edit this file only!
├── generate.py               # 🤖 Generator script - runs automatically
├── style.css                 # 🎨 Resume styling (edit if needed)
│
├── resume.html               # ✨ Auto-generated from resume-data.json
├── README.md                 # ✨ Auto-generated from resume-data.json
└── Munevver_Aslan_Resume.pdf # ✨ Auto-generated from resume.html
```

## 🚀 Quick Start - Update Your Resume

**To update your resume, follow these 3 simple steps:**

1. **Edit** `resume-data.json` with your new information
2. **Run** `python3 generate.py`
3. **Push** to GitHub

```bash
# Example workflow
vim resume-data.json          # Edit your resume data
python3 generate.py           # Generate all files automatically
git add .
git commit -m "Update resume"
git push
```

That's it! Everything else is automated.

## 🔄 How It Works

The `generate.py` script reads `resume-data.json` and automatically generates:

1. **resume.html** - Full HTML resume with all your experience
2. **README.md** - GitHub profile with highlighted current work
3. **Munevver_Aslan_Resume.pdf** - Print-ready PDF using Chrome headless

**Single source of truth:** You only edit `resume-data.json` - everything else is generated from it.

## 📝 What You Can Edit

### Primary Source (Edit This!)
- **resume-data.json** - All your professional information

### Styling (Optional)
- **style.css** - Visual styling, fonts, colors, spacing

### Generator (Advanced)
- **generate.py** - Logic for how HTML/README are generated

## 🛠️ Manual PDF Generation (Optional)

The script automatically generates PDF, but if you need to do it manually:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf="Munevver_Aslan_Resume.pdf" \
  "resume.html"
```

### Command Breakdown:
- `--headless` - Runs Chrome without GUI
- `--disable-gpu` - Disables GPU acceleration (required for headless)
- `--no-pdf-header-footer` - Removes browser-generated headers (date, URL, page numbers)
- `--print-to-pdf="filename.pdf"` - Specifies output PDF file
- Last argument is the input HTML file

### Alternative Methods:

**Using full path:**
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf="/Users/munevver/Desktop/projeler/mnvvr/Munevver_Aslan_Resume.pdf" \
  "/Users/munevver/Desktop/projeler/mnvvr/resume.html"
```

**On Windows:**
```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="Munevver_Aslan_Resume.pdf" "resume.html"
```

**On Linux:**
```bash
google-chrome --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="Munevver_Aslan_Resume.pdf" "resume.html"
```

## ✏️ Making Updates

### Standard Workflow (Recommended):

1. **Edit resume-data.json** - Update your information (new job, skills, etc.)
2. **Run generator** - `python3 generate.py`
3. **Review changes** - Check generated files look correct
4. **Commit & Push** - `git add . && git commit -m "Update resume" && git push`

### Quick Styling Updates:

For visual changes only (colors, fonts, spacing):
1. Edit `style.css`
2. Run `python3 generate.py` (to regenerate PDF with new styles)
3. Commit & Push

### Advanced Updates:

To change how data is displayed:
1. Edit `generate.py` templates
2. Run `python3 generate.py` to test
3. Commit & Push

## 🎨 Styling Notes

- Font: **Outfit** (Google Fonts) with weights 300, 400, 500, 600, 700
- Accent color: **#e91e63** (pink)
- Layout: **2-page A4** format
- Print margins: **0.35in** (set in CSS @page rule)
- Page breaks: Controlled via CSS to avoid splitting experience items

### Key CSS Classes:
- `.name` - Name header (300 weight)
- `.last-name` - Last name (700 weight, bold)
- `.section-title` - Section headers with pink highlight
- `.job-title`, `.company-name` - Bold headers (700 weight)
- `.experience-item` - Uses `page-break-inside: avoid`

## 📋 PDF Print Settings

The CSS includes `@media print` and `@page` rules that control PDF generation:

```css
@media print {
    /* Ensures proper spacing and prevents awkward breaks */
}

@page {
    margin: 0.35in;
    size: A4;
}
```

## 🔗 True Single Source of Truth ✅

**resume-data.json** is the ONLY file you need to edit. Everything else is automatically generated:

- ✅ `resume.html` - Auto-generated from JSON
- ✅ `README.md` - Auto-generated from JSON
- ✅ `Munevver_Aslan_Resume.pdf` - Auto-generated from HTML

**Benefits:**
- Update once, propagate everywhere
- No manual synchronization
- No risk of inconsistency
- Easy to maintain

## 📦 Requirements

- **Python 3** - Already installed on macOS/Linux
- **Chrome/Chromium** - For PDF generation
- No other dependencies needed!

## 🚀 Quick Start for New Users

1. Clone the repository: `git clone https://github.com/mnvvr/mnvvr.git`
2. Edit `resume-data.json` with your changes
3. Run `python3 generate.py`
4. Review generated files
5. Commit and push: `git add . && git commit -m "Update resume" && git push`

**Your updated resume will be live at:**
- GitHub Profile: `https://github.com/mnvvr`
- PDF Download: `https://github.com/mnvvr/mnvvr/blob/main/Munevver_Aslan_Resume.pdf`

## 📄 License

Personal resume - All rights reserved.
