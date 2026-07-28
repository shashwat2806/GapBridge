from fpdf import FPDF
from datetime import date


class GapBridgeReport(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, "GapBridge Policy Analysis Report", ln=True, align="C")
        self.set_font("Helvetica", "", 9)
        self.cell(0, 6, date.today().strftime("%B %d, %Y"), ln=True, align="C")
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def section_title(self, text):
        self.set_font("Helvetica", "B", 12)
        self.set_fill_color(230, 230, 230)
        self.cell(0, 8, text, ln=True, fill=True)
        self.ln(2)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 6, text)
        self.ln(2)


def export_pdf(policy_name, scorecard, roadmap, filepath):
    pdf = GapBridgeReport()
    pdf.add_page()

    pdf.section_title("Summary")
    pdf.body_text(
        f"Policy analyzed: {policy_name}\n"
        f"Overall maturity: {scorecard['overall_pct']}% ({scorecard['maturity_label']})\n"
        f"Weighted maturity: {scorecard['weighted_pct']}%\n\n"
        f"Full per-control gap details, roadmap items, and the RAG-grounded "
        f"revised policy are available in the accompanying markdown and JSON/CSV exports."
    )

    pdf.section_title("Coverage by NIST Function")
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(60, 7, "Function", border=1)
    pdf.cell(35, 7, "Coverage", border=1)
    pdf.cell(45, 7, "Controls Met", border=1)
    pdf.ln()
    pdf.set_font("Helvetica", "", 10)
    for fn, data in scorecard["by_function"].items():
        pdf.cell(60, 7, fn, border=1)
        pdf.cell(35, 7, f"{data['pct']}%", border=1)
        pdf.cell(45, 7, f"{data['met']}/{data['total']}", border=1)
        pdf.ln()
    pdf.ln(4)

    pdf.section_title("Improvement Roadmap")
    pdf.body_text(
        f"Short term (0-3 months): {len(roadmap['short_term_0_3_months'])} items\n"
        f"Mid term (3-6 months): {len(roadmap['mid_term_3_6_months'])} items\n"
        f"Long term (6-12 months): {len(roadmap['long_term_6_12_months'])} items"
    )

    pdf.output(filepath)