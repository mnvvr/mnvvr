<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    line-height: 1.6;
    color: #333;
    background: #fff;
}

.container {
    max-width: 850px;
    margin: 0 auto;
    padding: 35px 45px;
}

.header {
    text-align: center;
    margin-bottom: 10px;
    padding-bottom: 8px;
    border-bottom: 2px solid #e91e63;
}

.name {
    font-size: 32px;
    font-weight: 300;
    color: #333;
    margin-bottom: 3px;
    letter-spacing: -0.5px;
}

.name .last-name {
    font-weight: 700;
    color: #333;
}

.title {
    font-size: 11px;
    color: #e91e63;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 4px;
}

.location {
    color: #666;
    font-size: 11px;
    margin-bottom: 5px;
    font-style: normal;
    font-weight: 300;
}

.contact-info {
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 8px;
    font-size: 11px;
    font-weight: 400;
}

.contact-info a {
    color: #34495e;
    text-decoration: none;
}

.contact-info a:hover {
    color: #e91e63;
}

.quote {
    font-style: italic;
    color: #666;
    font-size: 11px;
    margin-top: 6px;
    font-weight: 300;
}

.section {
    margin-bottom: 15px;
}

.section-title {
    font-size: 18px;
    font-weight: 300;
    color: #333;
    margin-bottom: 8px;
    padding-bottom: 4px;
    border-bottom: 2px solid #e5e5e5;
    display: block;
    letter-spacing: -0.3px;
}

.section-title .highlight {
    font-weight: 700;
    color: #e91e63;
}

.summary-text {
    font-size: 11px;
    line-height: 1.65;
    color: #333;
    text-align: justify;
    font-weight: 400;
}

.skills-grid {
    display: grid;
    grid-template-columns: 135px 1fr;
    gap: 6px 18px;
    font-size: 11px;
}

.skill-category {
    font-weight: 700;
    color: #333;
    text-align: right;
}

.skill-items {
    color: #333;
    font-weight: 400;
}

.experience-item {
    margin-bottom: 12px;
    page-break-inside: avoid;
}

.job-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 5px;
}

.job-title {
    font-size: 12px;
    font-weight: 700;
    color: #333;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.job-date {
    font-size: 10px;
    color: #e91e63;
    font-style: italic;
    white-space: nowrap;
    margin-left: 20px;
    font-weight: 400;
}

.company-name {
    font-size: 12px;
    font-weight: 700;
    color: #e91e63;
    margin-bottom: 1px;
}

.job-location {
    font-size: 10px;
    color: #666;
    font-style: normal;
    margin-bottom: 6px;
    font-weight: 300;
}

.job-description {
    margin-left: 0;
    padding-left: 16px;
}

.job-description li {
    margin-bottom: 4px;
    font-size: 11px;
    line-height: 1.55;
    color: #333;
    font-weight: 400;
}

.education-item {
    margin-bottom: 10px;
    page-break-inside: avoid;
    orphans: 2;
    widows: 2;
}

.education-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
}

.school-name {
    font-size: 12px;
    font-weight: 700;
    color: #333;
    margin-bottom: 2px;
}

.degree {
    font-size: 11px;
    color: #333;
    font-weight: 400;
    text-transform: uppercase;
    letter-spacing: 0.2px;
}

.education-date {
    font-size: 10px;
    color: #e91e63;
    font-style: italic;
    white-space: nowrap;
    font-weight: 400;
}

.education-location {
    font-size: 10px;
    color: #666;
    font-style: normal;
    font-weight: 300;
}

@media print {
    body {
        margin: 0;
        padding: 0;
    }
    .container {
        padding: 28px 40px;
    }
    .experience-item {
        page-break-inside: avoid;
    }
    .job-header {
        page-break-after: avoid;
    }
    .job-description {
        page-break-before: avoid;
    }
}

@page {
    margin: 0.35in;
    size: A4;
}
</style>

<div align="center">

# Münevver Aslan

**Digital Product Designer** | Lisbon, Portugal

📄 [Download PDF Resume](./Munevver_Aslan_Resume.pdf) | 💼 [LinkedIn](https://linkedin.com/in/munevveraslan) | 🌐 [Portfolio](https://munevver.netlify.app)

</div>

---

    <div class="container">
        <header class="header">
            <h1 class="name">Münevver <span class="last-name">Aslan</span></h1>
            <div class="title">Digital Product Designer</div>
            <div class="location">Lisbon, Portugal</div>
            <div class="contact-info">
                <a href="mailto:munevveraslan2@gmail.com">munevveraslan2@gmail.com</a>
                <span>|</span>
                <a href="https://munevver.netlify.app" target="_blank">munevver.netlify.app</a>
                <span>|</span>
                <a href="https://linkedin.com/in/munevveraslan" target="_blank">munevveraslan</a>
            </div>
            <div class="quote">"Everything is design. Everything!"</div>
        </header>

        <section class="section">
            <h2 class="section-title">Sum<span class="highlight">mary</span></h2>
            <p class="summary-text">
                Product Designer with Industrial Design background, specializing in UI/UX for digital products and AI-powered design workflows. Experienced in building design systems from scratch and leading 0-to-1 product launches. Expert in leveraging AI tools (Midjourney, Cursor) for rapid prototyping, development, and design-to-code workflows. Passionate about translating complex technical requirements into intuitive, accessible interfaces through close collaboration with engineering teams.
            </p>
        </section>

        <section class="section">
            <h2 class="section-title">Ski<span class="highlight">lls</span></h2>
            <div class="skills-grid">
                <div class="skill-category">Design Tools</div>
                <div class="skill-items">Figma (Advanced), Adobe Creative Suite (Photoshop, Illustrator, Lightroom), Midjourney, Cursor, Sketch, Adobe XD</div>

                <div class="skill-category">UX Design</div>
                <div class="skill-items">User Experience Design, User Research, Information Architecture, User Flows, Journey Mapping, Persona Development</div>

                <div class="skill-category">UI Design</div>
                <div class="skill-items">User Interface Design, Visual Design, Wireframing, Prototyping, Design Systems, Component Libraries</div>

                <div class="skill-category">Methodology</div>
                <div class="skill-items">Agile/Scrum, AI-Powered Design Workflows, Branding, Visual Identity</div>

                <div class="skill-category">Languages</div>
                <div class="skill-items">Turkish (Native), English (Professional Working Proficiency)</div>

            </div>
        </section>

        <section class="section" id="experience">
            <h2 class="section-title">Expe<span class="highlight">rience</span></h2>

            <div class="experience-item">
                <div class="job-header">
                    <div>
                        <div class="job-title">UX UI Designer</div>
                        <div class="company-name">IGLUU</div>
                        <div class="job-location">Remote</div>
                    </div>
                    <div class="job-date">Oct. 2025 - Present</div>
                </div>
                <ul class="job-description">
                    <li>Designing product interfaces for a Czech real estate platform, working on broker tools, rental application flows, and ČSOB bank insurance partnership</li>
                    <li>Iterating on designs through detailed feedback cycles with Product Owners and senior designers</li>
                    <li>Working within established design system while identifying and proposing improvements to responsive design approaches</li>
                    <li>Collaborating with developers on implementation, ensuring designs translate effectively across multiple breakpoints</li>
                </ul>
            </div>

            <div class="experience-item">
                <div class="job-header">
                    <div>
                        <div class="job-title">Digital Product Designer</div>
                        <div class="company-name">Freelancer</div>
                        <div class="job-location">Remote</div>
                    </div>
                    <div class="job-date">Oct. 2023 - Present</div>
                </div>
                <ul class="job-description">
                    <li>Won branding award at Octant foundation's design competition for the Argot Collective Act Project, creating comprehensive logo design and brand identity system selected from international submissions</li>
                    <li>Building Scrum Poker application from concept to deployment using AI-assisted development (Cursor), demonstrating end-to-end product design and full-stack development capability</li>
                    <li>Delivering UI design, branding, and visual identity solutions for diverse clients, managing complete design lifecycle from discovery to final delivery</li>
                    <li>Developing Bitrick, an AI-generated visual narrative series exploring advanced Midjourney techniques for maintaining character consistency across sequential storytelling</li>
                    <li>Leveraging AI tools to accelerate design iteration cycles while maintaining high visual fidelity and user-centered design principles</li>
                </ul>
            </div>

            <div class="experience-item">
                <div class="job-header">
                    <div>
                        <div class="job-title">UX UI Designer</div>
                        <div class="company-name">Prove Us Wrong</div>
                        <div class="job-location">Remote</div>
                    </div>
                    <div class="job-date">Jan. 2022 - Oct. 2023</div>
                </div>
                <ul class="job-description">
                    <li>Led user interface design for Truthpost platform (Kleros Incubator), establishing comprehensive design system and visual identity from ground up</li>
                    <li>Created scalable design system in Figma with reusable component library, enabling consistent cross-platform experiences and efficient designer-developer handoff</li>
                    <li>Collaborated with distributed international teams across multiple time zones on governance and coordination tools, translating complex technical requirements into intuitive user interfaces</li>
                    <li>Produced visual assets using hybrid workflow combining AI tools (Midjourney) with traditional design software (Illustrator, Photoshop, Lightroom)</li>
                    <li>Conducted user research and usability testing sessions to validate design decisions and inform iterative improvements throughout product development</li>
                </ul>
            </div>

            <div class="experience-item">
                <div class="job-header">
                    <div>
                        <div class="job-title">UX UI Designer</div>
                        <div class="company-name">Lumhar Design</div>
                        <div class="job-location">İzmir, Turkey</div>
                    </div>
                    <div class="job-date">Jul. 2021 - Jan. 2022</div>
                </div>
                <ul class="job-description">
                    <li>Designed visually engaging, responsive, and modular interfaces tailored specifically for gaming audiences</li>
                    <li>Applied user research insights to create intuitive user flows that enhanced overall user experience and engagement</li>
                    <li>Collaborated closely with development team to ensure design feasibility and maintain visual quality through implementation</li>
                </ul>
            </div>

            <div class="experience-item">
                <div class="job-header">
                    <div>
                        <div class="job-title">UX UI Designer</div>
                        <div class="company-name">Artysmm Technology and Digital Consultancy Company</div>
                        <div class="job-location">Remote</div>
                    </div>
                    <div class="job-date">Jun. 2020 - Jan. 2021</div>
                </div>
                <ul class="job-description">
                    <li>Conducted comprehensive website audit and recommended strategic improvements to enhance user experience and modern aesthetics</li>
                    <li>Redesigned key website pages focusing on improved usability, visual hierarchy, and responsive design principles</li>
                    <li>Worked with cross-functional team to implement design improvements while maintaining brand consistency</li>
                </ul>
            </div>

        </section>

        <section class="section">
            <h2 class="section-title">Edu<span class="highlight">cation</span></h2>
            <div class="education-item">
                <div class="education-header">
                    <div>
                        <div class="school-name">Gazi Üniversitesi</div>
                        <div class="degree">B.S. Industrial Product Design, Faculty of Architecture</div>
                        <div class="education-location">Ankara, Turkey</div>
                    </div>
                    <div class="education-date">Sep. 2013 - Jul. 2019</div>
                </div>
            </div>

        </section>
    </div>
