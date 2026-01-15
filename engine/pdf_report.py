from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(path, report):
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(path)
    story = []

    for line in report:
        story.append(Paragraph(line, styles["BodyText"]))
        story.append(Spacer(1, 6))

    doc.build(story)
