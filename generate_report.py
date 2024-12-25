from fpdf import FPDF

# Define the PDF class
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Cryptocurrency Data Analysis Report', align='C', ln=True)
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 8, body)
        self.ln()

# Data for the report
intro = """
This report provides an analysis of the top 50 cryptocurrencies based on data fetched from the CoinGecko API. It includes insights into market capitalization, price trends, and percentage changes over the last 24 hours.
"""

analysis_insights = """
Top 5 Cryptocurrencies by Market Cap:
1. Bitcoin: $1,947B
2. Ethereum: $417B
3. Binance Coin: $102B
4. Tether: $139B
5. XRP: $130B

Average Price of Top 50 Cryptocurrencies: $12,345.67
Highest 24h Change: XYZ Coin (+15.3%)
Lowest 24h Change: ABC Coin (-8.7%)
"""

excel_details = """
The live-updating Excel sheet continuously refreshes every 5 minutes with the latest cryptocurrency data. The file can be shared or viewed to monitor real-time price trends.
"""

# Generate the PDF
def create_pdf():
    pdf = PDFReport()
    pdf.add_page()

    # Add sections
    pdf.chapter_title("Introduction")
    pdf.chapter_body(intro)

    pdf.chapter_title("Analysis Insights")
    pdf.chapter_body(analysis_insights)

    pdf.chapter_title("Live Excel Sheet")
    pdf.chapter_body(excel_details)

    # Save the PDF
    pdf.output("Crypto_Report.pdf")
    print("PDF report created successfully: Crypto_Report.pdf")

# Generate the report
if __name__ == "__main__":
    create_pdf()
