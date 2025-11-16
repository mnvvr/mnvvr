# Resume Setup & Maintenance

This repository contains Münevver Aslan's professional resume in multiple formats, all generated from a single source of truth.

## 📁 File Structure

```
.
├── resume-data.json          # Single source of truth - all professional data
├── resume.html               # HTML resume (generated from resume-data.json)
├── style.css                 # Resume styling
├── Munevver_Aslan_Resume.pdf # PDF resume (generated from HTML)
└── README.md                 # GitHub profile (uses data from resume-data.json)
```

## 🔄 How It Works

1. **resume-data.json** - Contains all professional information (experience, skills, education, etc.)
2. **resume.html** - HTML resume that displays the data with proper formatting
3. **style.css** - All styling separated from HTML for maintainability
4. **Munevver_Aslan_Resume.pdf** - Generated from HTML using Chrome headless
5. **README.md** - GitHub profile that references the same data

## 🛠️ Generating PDF from HTML

To regenerate the PDF after making changes to the HTML or CSS:

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

### Update Professional Information:

1. **Edit resume-data.json** - Update your data (new job, skills, etc.)
2. **Update resume.html** - Reflect changes in HTML structure
3. **Update README.md** - Update GitHub profile with new information
4. **Regenerate PDF** - Run the Chrome command above
5. **Commit & Push** - Save changes to GitHub

### Quick Updates:

For small changes (typos, formatting):
1. Edit the relevant file directly (HTML, CSS, or README)
2. Regenerate PDF if HTML/CSS changed
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

## 🔗 Single Source of Truth

All professional information should ultimately come from **resume-data.json**. Currently:
- JSON data is manually synced with HTML and README
- Future improvement: Generate HTML/README automatically from JSON

## 📦 Dependencies

- **Chrome/Chromium** - Required for PDF generation
- No other external dependencies (pure HTML/CSS)

## 🚀 Quick Start for New Contributors

1. Clone the repository
2. Make changes to desired files
3. If HTML/CSS changed, regenerate PDF using Chrome command
4. Commit and push changes
5. PDF will be available at: `https://github.com/mnvvr/mnvvr/blob/main/Munevver_Aslan_Resume.pdf`

## 📄 License

Personal resume - All rights reserved.
