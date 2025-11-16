#!/usr/bin/env python3
"""
Resume Generator - Single Source of Truth
Generates resume.html and README.md from resume-data.json
"""

import json
import subprocess
import sys
from pathlib import Path


def load_resume_data():
    """Load resume data from JSON file"""
    with open('resume-data.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_html(data):
    """Generate resume.html from resume data"""

    # Build skills HTML
    skills_html = f"""
                <div class="skill-category">Design Tools</div>
                <div class="skill-items">{data['skills']['designTools']}</div>

                <div class="skill-category">UX Design</div>
                <div class="skill-items">{data['skills']['uxDesign']}</div>

                <div class="skill-category">UI Design</div>
                <div class="skill-items">{data['skills']['uiDesign']}</div>

                <div class="skill-category">Methodology</div>
                <div class="skill-items">{data['skills']['methodology']}</div>

                <div class="skill-category">Languages</div>
                <div class="skill-items">{data['skills']['languages']}</div>
"""

    # Build experience HTML
    experience_html = ""
    for exp in data['experience']:
        responsibilities = "\n".join([f"                    <li>{resp}</li>" for resp in exp['responsibilities']])
        experience_html += f"""
            <div class="experience-item">
                <div class="job-header">
                    <div>
                        <div class="job-title">{exp['title']}</div>
                        <div class="company-name">{exp['company']}</div>
                        <div class="job-location">{exp['location']}</div>
                    </div>
                    <div class="job-date">{exp['startDate']} - {exp['endDate']}</div>
                </div>
                <ul class="job-description">
{responsibilities}
                </ul>
            </div>
"""

    # Build education HTML
    education_html = ""
    for edu in data['education']:
        education_html += f"""            <div class="education-item">
                <div class="education-header">
                    <div>
                        <div class="school-name">{edu['school']}</div>
                        <div class="degree">{edu['degree']}, {edu['faculty']}</div>
                        <div class="education-location">{edu['location']}</div>
                    </div>
                    <div class="education-date">{edu['startDate']} - {edu['endDate']}</div>
                </div>
            </div>
"""

    # Complete HTML template
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['personal']['name']} - Resume</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header class="header">
            <h1 class="name">{data['personal']['name'].split()[0]} <span class="last-name">{data['personal']['name'].split()[1]}</span></h1>
            <div class="title">{data['personal']['title']}</div>
            <div class="location">{data['personal']['location']}</div>
            <div class="contact-info">
                <a href="mailto:{data['personal']['email']}">{data['personal']['email']}</a>
                <span>|</span>
                <a href="{data['personal']['website']}" target="_blank">{data['personal']['website'].replace('https://', '')}</a>
                <span>|</span>
                <a href="{data['personal']['linkedin']}" target="_blank">{data['personal']['linkedin'].split('/')[-1]}</a>
            </div>
            <div class="quote">"{data['personal']['quote']}"</div>
        </header>

        <section class="section">
            <h2 class="section-title">Sum<span class="highlight">mary</span></h2>
            <p class="summary-text">
                {data['summary']}
            </p>
        </section>

        <section class="section">
            <h2 class="section-title">Ski<span class="highlight">lls</span></h2>
            <div class="skills-grid">{skills_html}
            </div>
        </section>

        <section class="section" id="experience">
            <h2 class="section-title">Expe<span class="highlight">rience</span></h2>
{experience_html}
        </section>

        <section class="section">
            <h2 class="section-title">Edu<span class="highlight">cation</span></h2>
{education_html}
        </section>
    </div>
</body>
</html>
"""

    with open('resume.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("✓ Generated resume.html")


def generate_readme(data):
    """Generate README.md from resume data"""

    # Get current experience (first two items)
    igluu = data['experience'][0]
    freelance = data['experience'][1]

    # Build freelance highlights
    freelance_highlights = "\n".join([f"- 🏆 {resp}" if "award" in resp.lower()
                                      else f"- 🎮 {resp}" if "Scrum Poker" in resp
                                      else f"- 🎨 {resp}" if "Bitrick" in resp
                                      else f"- {resp}"
                                      for resp in freelance['responsibilities'][:3]])

    readme = f"""# Hi there, I'm {data['personal']['name']} 👋

**{data['personal']['title']}** based in {data['personal']['location']}

*"{data['personal']['quote']}"*

{data['summary']}

## 💼 Currently

**{igluu['title']} at [IGLUU](https://www.igluu.cz/)** *({igluu['startDate']} - {igluu['endDate']})*
{igluu['responsibilities'][0]}

**{freelance['title']}** *({freelance['startDate']} - {freelance['endDate']})*
{freelance_highlights}

## 🎨 What I Do

- **Design Systems:** Building scalable component libraries and design systems from scratch
- **AI-Powered Workflows:** Leveraging Midjourney, Cursor, and AI tools for rapid prototyping and design-to-code workflows
- **Product Design:** Translating complex technical requirements into intuitive, accessible interfaces
- **Branding:** Creating comprehensive visual identities and brand systems

## 🛠️ Tools & Skills

**Design:** {data['skills']['designTools']}
**UX/UI:** {data['skills']['uxDesign']}
**Methodology:** {data['skills']['methodology']}
**Languages:** {data['skills']['languages']}

## 🌱 Exploring

{chr(10).join([f"- {focus}" for focus in data['currentFocus']])}

## 📫 Connect With Me

- Portfolio: [{data['personal']['website'].replace('https://', '')}]({data['personal']['website']})
- LinkedIn: [{data['personal']['linkedin'].split('/')[-1]}]({data['personal']['linkedin']})
- X (Twitter): [@{data['personal']['twitter'].split('/')[-1]}]({data['personal']['twitter']})
- Email: {data['personal']['email']}

---

📄 [View Full Resume](./Munevver_Aslan_Resume.pdf) | 💾 [Resume Data (JSON)](./resume-data.json)

*Designing the future, one pixel (and line of code) at a time!*
"""

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme)

    print("✓ Generated README.md")


def generate_pdf():
    """Generate PDF from HTML using Chrome headless"""
    chrome_paths = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",  # macOS
        "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",     # Windows
        "google-chrome",                                                   # Linux
        "chromium"                                                         # Linux alternative
    ]

    chrome_path = None
    for path in chrome_paths:
        if Path(path).exists() or subprocess.run(['which', path], capture_output=True).returncode == 0:
            chrome_path = path
            break

    if not chrome_path:
        print("⚠ Chrome/Chromium not found. Skipping PDF generation.")
        print("  To generate PDF manually, run:")
        print('  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="Munevver_Aslan_Resume.pdf" "resume.html"')
        return

    try:
        subprocess.run([
            chrome_path,
            '--headless',
            '--disable-gpu',
            '--no-pdf-header-footer',
            f'--print-to-pdf=Munevver_Aslan_Resume.pdf',
            'resume.html'
        ], check=True, capture_output=True)
        print("✓ Generated Munevver_Aslan_Resume.pdf")
    except subprocess.CalledProcessError as e:
        print(f"⚠ PDF generation failed: {e}")
        print("  You can generate it manually using the command above.")


def main():
    """Main function to orchestrate resume generation"""
    print("🚀 Generating resume from resume-data.json...\n")

    try:
        # Load data
        data = load_resume_data()
        print("✓ Loaded resume-data.json")

        # Generate files
        generate_html(data)
        generate_readme(data)
        generate_pdf()

        print("\n✅ All done! Your resume has been generated from single source of truth.")
        print("\nNext steps:")
        print("  1. Review the generated files")
        print("  2. git add .")
        print("  3. git commit -m 'Update resume'")
        print("  4. git push")

    except FileNotFoundError:
        print("❌ Error: resume-data.json not found!")
        print("   Make sure you're running this script from the repository root.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in resume-data.json: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
