"""Generate Ghana launch PDFs and Gumroad-ready bundles."""

from __future__ import annotations

import json
import shutil
import textwrap
import zipfile
from dataclasses import dataclass
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf"
DIST = ROOT / "dist" / "ghana-launch"
RELEASE_ZIP = ROOT / "dist" / "ai-learners-journal-kit-v3.0.1.zip"
VERSION = "ghana-launch-v1"


@dataclass(frozen=True)
class DocSpec:
    filename: str
    title: str
    subtitle: str
    sections: list[tuple[str, list[str] | list[list[str]]]]


def styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "Title",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=25,
            leading=31,
            textColor=colors.HexColor("#111827"),
            alignment=TA_CENTER,
            spaceAfter=12,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=12.5,
            leading=18,
            textColor=colors.HexColor("#374151"),
            alignment=TA_CENTER,
            spaceAfter=18,
        ),
        "h2": ParagraphStyle(
            "Heading2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=15,
            leading=19,
            textColor=colors.HexColor("#0f766e"),
            spaceBefore=14,
            spaceAfter=8,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=10.2,
            leading=14.5,
            textColor=colors.HexColor("#1f2937"),
            spaceAfter=7,
            alignment=TA_LEFT,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8,
            leading=10,
            textColor=colors.HexColor("#6b7280"),
            alignment=TA_CENTER,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.8,
            leading=13.5,
            textColor=colors.HexColor("#1f2937"),
        ),
    }


def clean(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("'", "&#39;")
    )


def paragraph(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(clean(text), style)


def bullet_list(items: list[str], style: ParagraphStyle) -> ListFlowable:
    return ListFlowable(
        [ListItem(paragraph(item, style), leftIndent=12) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=16,
        bulletFontName="Helvetica",
        bulletFontSize=7,
    )


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#6b7280"))
    footer_text = "AI Learner's Journal Kit | AgenticPPA | Independent learning support resource"
    canvas.drawCentredString(A4[0] / 2, 0.42 * inch, footer_text)
    canvas.drawRightString(A4[0] - 0.55 * inch, 0.42 * inch, f"Page {doc.page}")
    canvas.restoreState()


def build_doc(spec: DocSpec) -> Path:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    out = OUTPUT / spec.filename
    s = styles()
    doc = SimpleDocTemplate(
        str(out),
        pagesize=A4,
        rightMargin=0.58 * inch,
        leftMargin=0.58 * inch,
        topMargin=0.62 * inch,
        bottomMargin=0.72 * inch,
        title=spec.title,
        author="AgenticPPA",
    )

    story = [
        paragraph(spec.title, s["title"]),
        paragraph(spec.subtitle, s["subtitle"]),
        paragraph(
            "Designed for Ghanaian high-school and university learners in coding, AI, data, cybersecurity, and digital-skills programs. Independent resource. Not an official government product.",
            s["small"],
        ),
        Spacer(1, 10),
    ]

    for heading, content in spec.sections:
        story.append(paragraph(heading, s["h2"]))
        if content and isinstance(content[0], list):
            table_data = [[paragraph(str(cell), s["bullet"]) for cell in row] for row in content]  # type: ignore[index]
            table = Table(table_data, colWidths=[1.35 * inch, 4.5 * inch])
            table.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e0f2f1")),
                        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#d1d5db")),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 7),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                        ("TOPPADDING", (0, 0), (-1, -1), 6),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                    ]
                )
            )
            story.append(table)
            story.append(Spacer(1, 8))
        else:
            for block in content:  # type: ignore[assignment]
                if block.startswith("- "):
                    items = [line[2:] for line in block.splitlines() if line.startswith("- ")]
                    story.append(bullet_list(items, s["bullet"]))
                    story.append(Spacer(1, 5))
                else:
                    story.append(paragraph(block, s["body"]))

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    return out


def free_journal() -> DocSpec:
    sections = [
        (
            "How to use this journal",
            [
                "Spend 10 minutes after each learning session. Do not write perfect essays. Capture evidence while it is still fresh.",
                "- Save screenshots of your code, notebook, terminal, app, or design.\n- Record prompts you used with AI tools.\n- Write what you changed after the AI answer.\n- End every day with one next action.",
            ],
        )
    ]
    for day in range(1, 8):
        sections.append(
            (
                f"Day {day}",
                [
                    "Goal for this session: ________________________________________________",
                    "What I learned: _______________________________________________________",
                    "What I built or tried: ________________________________________________",
                    "AI prompt I used: _____________________________________________________",
                    "What confused me: ____________________________________________________",
                    "Proof I saved: ________________________________________________________",
                    "Next step: ____________________________________________________________",
                ],
            )
        )
    sections.append(
        (
            "End-of-week portfolio summary",
            [
                "My strongest learning moment this week: ______________________________",
                "One bug or challenge I solved: _______________________________________",
                "One project or mini-project I can show: ______________________________",
                "One prompt that helped me learn: _____________________________________",
                "What I will build next week: _________________________________________",
            ],
        )
    )
    return DocSpec(
        filename="ghana-ai-coding-journal-7-day-free.pdf",
        title="7-Day AI Coding Journal",
        subtitle="A free starter journal for Ghanaian learners turning coding practice into portfolio proof.",
        sections=sections,
    )


def student_pack() -> DocSpec:
    weeks = []
    for week in range(1, 13):
        weeks.append(
            [
                f"Week {week}",
                "Learning focus: ____  Project evidence: ____  Best prompt: ____  Mistake fixed: ____  Portfolio note: ____",
            ]
        )
    return DocSpec(
        filename="student-portfolio-pack.pdf",
        title="Student Portfolio Pack",
        subtitle="A 12-week system for turning coding, AI, and digital-skills training into visible proof.",
        sections=[
            (
                "Your portfolio operating system",
                [
                    "Use this pack beside any coding or AI course. Each week, capture what you learned, what you built, what broke, how you used AI, and what proof belongs in your portfolio.",
                    "- Keep one folder for screenshots.\n- Keep one GitHub repository or Google Drive folder for projects.\n- Keep one prompt log.\n- Write one short project story every two weeks.",
                ],
            ),
            ("12-week tracker", weeks),
            (
                "AI prompt log",
                [
                    [
                        "Prompt",
                        "What I asked, why I asked it, what the AI suggested, what I changed, and what I learned.",
                    ],
                    ["Prompt 1", "____"],
                    ["Prompt 2", "____"],
                    ["Prompt 3", "____"],
                    ["Prompt 4", "____"],
                    ["Prompt 5", "____"],
                ],
            ),
            (
                "Project case-study template",
                [
                    "Project name: ____",
                    "Problem: What problem did this project solve?",
                    "Tools used: ____",
                    "My role: ____",
                    "How it works: ____",
                    "Screenshots or demo link: ____",
                    "What I learned: ____",
                    "What I would improve next: ____",
                ],
            ),
            (
                "GitHub README starter",
                [
                    "# Project Name",
                    "Short description: ____",
                    "What it does: ____",
                    "How to run it: ____",
                    "What I learned: ____",
                    "Screenshots: ____",
                    "Next improvements: ____",
                ],
            ),
            (
                "Internship and scholarship tracker",
                [
                    ["Opportunity", "Deadline, requirements, portfolio evidence, status, next action"],
                    ["Opportunity 1", "____"],
                    ["Opportunity 2", "____"],
                    ["Opportunity 3", "____"],
                    ["Opportunity 4", "____"],
                ],
            ),
        ],
    )


def facilitator_pack() -> DocSpec:
    return DocSpec(
        filename="facilitator-cohort-license-guide.pdf",
        title="Facilitator Cohort License Guide",
        subtitle="Run coding clubs, bootcamps, and school workshops with a ready-made reflection and portfolio system.",
        sections=[
            (
                "Best use cases",
                [
                    "- 2-hour intro workshop\n- 7-day coding challenge\n- 4-week club sprint\n- 12-week bootcamp or course\n- university tech society portfolio clinic",
                ],
            ),
            (
                "Suggested cohort pricing",
                [
                    "Starter cohort: GHS 300 for up to 25 learners.",
                    "Growth cohort: GHS 750 for up to 100 learners.",
                    "Institution cohort: GHS 1,500 for up to 250 learners.",
                    "Large program: GHS 3,000 for up to 750 learners.",
                ],
            ),
            (
                "Workshop flow",
                [
                    [
                        "Time",
                        "Activity",
                    ],
                    ["0-10 min", "Why portfolio proof matters more than passive course completion."],
                    ["10-25 min", "Show examples of a weak learning note vs a strong project note."],
                    ["25-45 min", "Learners complete their first project reflection."],
                    ["45-65 min", "Prompt log exercise: improve one AI prompt and explain the change."],
                    ["65-90 min", "Pair review: each learner explains one project story."],
                    ["90-120 min", "Commitment: choose one portfolio improvement for the next 7 days."],
                ],
            ),
            (
                "Assessment rubric",
                [
                    [
                        "Area",
                        "What to look for",
                    ],
                    ["Clarity", "Can the learner explain the project problem and outcome?"],
                    ["Evidence", "Are screenshots, links, code, or notes included?"],
                    ["Reflection", "Does the learner explain mistakes and improvements?"],
                    ["AI use", "Does the prompt log show judgment and adaptation?"],
                    ["Next step", "Is there a clear plan for improving the project?"],
                ],
            ),
            (
                "Facilitator CTA",
                [
                    "For a cohort license, email info@agenticppa.com with your cohort size, dates, institution or group name, and whether you need printable files, Google Docs, or a live workshop.",
                ],
            ),
        ],
    )


def write_readme(path: Path, title: str, lines: list[str], crlf: bool = False) -> None:
    newline = "\r\n" if crlf else "\n"
    text = "# " + title + newline + newline + newline.join(lines) + newline
    # newline="" disables newline translation so CRLF is preserved exactly.
    path.write_text(text, encoding="utf-8", newline="")


# Minimal runnable subset of the v3 app shipped in the FREE bundle.
# Excludes the paid value (12-week PDFs, facilitator guide, installers, tests,
# visuals, promo, full release bundle) while remaining a working journaling app.
STARTER_MEMBERS = [
    ("ai-journal", "ai-coding-journal-starter/ai-journal"),
    ("Start AI Journal (Web).command", "ai-coding-journal-starter/Start AI Journal (Web).command"),
    ("Start AI Journal (Web).bat", "ai-coding-journal-starter/Start AI Journal (Web).bat"),
    ("Start AI Journal.command", "ai-coding-journal-starter/Start AI Journal.command"),
    ("Start AI Journal.bat", "ai-coding-journal-starter/Start AI Journal.bat"),
    ("scripts/journal_cli.py", "ai-coding-journal-starter/scripts/journal_cli.py"),
    ("scripts/entry_saver.py", "ai-coding-journal-starter/scripts/entry_saver.py"),
    ("scripts/auto_append.py", "ai-coding-journal-starter/scripts/auto_append.py"),
    ("scripts/ai_integration.py", "ai-coding-journal-starter/scripts/ai_integration.py"),
    ("scripts/web_server.py", "ai-coding-journal-starter/scripts/web_server.py"),
    ("web/index.html", "ai-coding-journal-starter/web/index.html"),
    ("requirements.txt", "ai-coding-journal-starter/requirements.txt"),
    ("README.md", "ai-coding-journal-starter/README.md"),
    ("docs/Quick_Start.md", "ai-coding-journal-starter/docs/Quick_Start.md"),
    ("LICENSE", "ai-coding-journal-starter/LICENSE"),
]


def build_bundles(files: list[Path]) -> dict[str, str]:
    DIST.mkdir(parents=True, exist_ok=True)
    free_zip = DIST / "AI-Coding-Journal-Ghana-Free-7-Day.zip"
    paid_zip = DIST / "AI-Learners-Journal-Kit-Student-Portfolio-Pack.zip"
    facilitator_zip = DIST / "AI-Learners-Journal-Kit-Facilitator-Cohort-Pack.zip"

    free_pdf = OUTPUT / "ghana-ai-coding-journal-7-day-free.pdf"
    student_pdf = OUTPUT / "student-portfolio-pack.pdf"
    facilitator_pdf = OUTPUT / "facilitator-cohort-license-guide.pdf"

    readme_free = DIST / "README-free.txt"
    readme_paid = DIST / "README-student-pack.txt"
    readme_facilitator = DIST / "README-facilitator.txt"
    write_readme(
        readme_free,
        "Free 7-Day AI Coding Journal + Starter App",
        [
            "Thank you for downloading the free starter from AgenticPPA.",
            "",
            "WHAT IS IN THIS ZIP",
            "1. ghana-ai-coding-journal-7-day-free.pdf  - a printable, fillable 7-day journal.",
            "2. ai-coding-journal-starter (folder)      - a small app that saves your learning entries on your computer.",
            "3. README.txt                              - this file.",
            "",
            "OPTION A - JUST USE THE JOURNAL (no setup)",
            "Open the PDF and fill it in for seven learning sessions. That is all you need to start.",
            "",
            "OPTION B - RUN THE APP IN YOUR BROWSER (recommended, needs Python 3)",
            "This opens a friendly page with buttons - no commands to type.",
            "Open the ai-coding-journal-starter folder, then:",
            "Mac: double-click \"Start AI Journal (Web).command\".",
            "Windows: double-click \"Start AI Journal (Web).bat\".",
            "Your web browser opens automatically. Keep the little window open while you write;",
            "press Ctrl-C in it when you are done. Your notes are saved on your own computer.",
            "",
            "THE FIRST TIME, YOUR COMPUTER MAY WARN YOU (this is normal - the file is safe):",
            "Mac (\"Apple could not verify...\"): click Done (NOT Move to Trash). Then open",
            "     System Settings > Privacy & Security, scroll down to the Security section, and",
            "     click \"Open Anyway\" next to the launcher. Enter your password if asked, then",
            "     click Open. After this, the double-click works normally.",
            "Windows (\"Windows protected your PC\"): click \"More info\", then \"Run anyway\".",
            "",
            "OPTION C - TEXT MENU IN THE TERMINAL (always works)",
            "Prefer the classic menu? Use \"Start AI Journal.command\" (Mac) or",
            "\"Start AI Journal.bat\" (Windows). Or run it by hand:",
            "1. Open the Terminal app (press Cmd+Space, type Terminal, press Return).",
            "2. Type these letters and a space - do NOT press Return yet:  cd ",
            "3. Drag the ai-coding-journal-starter folder onto the Terminal window. Its",
            "   location is filled in for you. Now press Return.",
            "4. Type this and press Return:  python3 scripts/journal_cli.py menu",
            "   (For the browser version instead, type:  python3 scripts/web_server.py )",
            "",
            "Your entries are saved in a folder called AI-Journal in your home directory.",
            "",
            "NEED PYTHON?",
            "Install it free from https://www.python.org/downloads/ then try Option B again.",
            "",
            "ASKING THE AI",
            "Beginner questions (like \"what is an API?\") are answered offline for free by the",
            "built-in Starter Guide - no setup needed. For AI answers to any question, see the",
            "README's \"Turn on AI answers\" section (free key options included).",
            "",
            "WANT THE FULL SYSTEM?",
            "The paid Student Portfolio Pack adds the 12-week portfolio journal, prompt log, project",
            "case-study and GitHub README templates, an internship and scholarship tracker, and the",
            "complete toolkit. See https://agenticppa.com/ghana-ai-coding-journal",
            "",
            "Support: agbe@udel.edu",
            "Independent learning resource. Not an official government product.",
        ],
        crlf=True,
    )
    write_readme(
        readme_paid,
        "Student Portfolio Pack",
        [
            "Thank you for getting the AI Learner's Journal Kit Student Portfolio Pack.",
            "Begin with student-portfolio-pack.pdf, then unpack the included v3.0.1 release bundle if you want the CLI journal tools.",
            "Support: info@agenticppa.com",
        ],
    )
    write_readme(
        readme_facilitator,
        "Facilitator Cohort Pack",
        [
            "Use this pack for coding clubs, school workshops, bootcamps, and university tech societies.",
            "For larger cohort licensing or customization, contact info@agenticppa.com.",
        ],
    )

    def zip_files(zip_path: Path, members: list[tuple[Path, str]]) -> None:
        with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for source, arcname in members:
                if source.exists():
                    zf.write(source, arcname)

    zip_files(
        free_zip,
        [
            (free_pdf, free_pdf.name),
            *[(ROOT / src, arc) for src, arc in STARTER_MEMBERS],
            (readme_free, "README.txt"),
        ],
    )
    zip_files(
        paid_zip,
        [
            (free_pdf, "01-free-7-day-journal.pdf"),
            (student_pdf, "02-student-portfolio-pack.pdf"),
            (facilitator_pdf, "03-facilitator-notes-preview.pdf"),
            (RELEASE_ZIP, "04-ai-learners-journal-kit-v3.0.1.zip"),
            (ROOT / "PRIVACY.md", "policies/PRIVACY.md"),
            (ROOT / "REFUND_POLICY.md", "policies/REFUND_POLICY.md"),
            (ROOT / "SUPPORT.md", "policies/SUPPORT.md"),
            (readme_paid, "README.txt"),
        ],
    )
    zip_files(
        facilitator_zip,
        [
            (facilitator_pdf, "facilitator-cohort-license-guide.pdf"),
            (student_pdf, "student-portfolio-pack.pdf"),
            (free_pdf, "free-7-day-journal.pdf"),
            (ROOT / "docs" / "Workshop_Facilitator_Guide.md", "workshop-facilitator-guide.md"),
            (readme_facilitator, "README.txt"),
        ],
    )

    manifest = {
        "version": VERSION,
        "generated_files": [str(p.relative_to(ROOT)) for p in files],
        "bundles": {
            "free": str(free_zip.relative_to(ROOT)),
            "student_paid": str(paid_zip.relative_to(ROOT)),
            "facilitator": str(facilitator_zip.relative_to(ROOT)),
        },
    }
    manifest_path = DIST / "ghana-launch-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest["bundles"]


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    specs = [free_journal(), student_pack(), facilitator_pack()]
    files = [build_doc(spec) for spec in specs]
    bundles = build_bundles(files)
    print(json.dumps({"pdfs": [str(p) for p in files], "bundles": bundles}, indent=2))


if __name__ == "__main__":
    main()
