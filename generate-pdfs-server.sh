#!/bin/bash

# PDF Generation Script with Local Server
# Starts Jekyll server and generates PDFs from http://localhost

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo "======================================"
echo "SAIL PDF Generator (Server Mode)"
echo "======================================"
echo ""

# Check for Node.js and Playwright
if ! command -v node &> /dev/null; then
    echo -e "${RED}ERROR: Node.js not installed${NC}"
    echo "Install with: brew install node"
    exit 1
fi

if [ ! -d "node_modules/playwright" ]; then
    echo -e "${RED}ERROR: Playwright not installed${NC}"
    echo "Install with: npm install playwright"
    exit 1
fi

echo -e "${GREEN}✓ Node.js and Playwright found${NC}"
echo ""

# Check for bundle
if ! command -v bundle &> /dev/null; then
    echo -e "${RED}ERROR: bundler is not installed${NC}"
    echo "Install with: gem install bundler"
    exit 1
fi

# Clean old PDFs
echo "Cleaning old PDFs..."
rm -rf pdfs/risk-assessments/*.pdf
rm -rf pdfs/safe-work-procedures/*.pdf
echo -e "${GREEN}✓ Cleaned${NC}"
echo ""

# Create PDF directories
mkdir -p pdfs/risk-assessments pdfs/safe-work-procedures

# Start Jekyll server in background
echo "Starting Jekyll server..."
bundle exec jekyll serve --detach --port 4000 > /dev/null 2>&1

# Wait for server to start
echo "Waiting for server to start..."
sleep 3

# Check if server is running
if ! curl -s http://localhost:4000 > /dev/null; then
    echo -e "${RED}ERROR: Jekyll server failed to start${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Jekyll server running at http://localhost:4000${NC}"
echo ""

# Create Playwright PDF generator
cat > generate-pdf-server.js << 'JSEOF'
const { chromium } = require('playwright');

async function generatePDF(url, outputPath) {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Load from web server
  await page.goto(url, { waitUntil: 'networkidle' });

  // Generate PDF with print media emulation
  await page.pdf({
    path: outputPath,
    format: 'A4',
    margin: { top: '15mm', right: '15mm', bottom: '15mm', left: '15mm' },
    printBackground: true,
    preferCSSPageSize: false
  });

  await browser.close();
}

const [,, url, outputPath] = process.argv;
generatePDF(url, outputPath).catch(console.error);
JSEOF

# Function to generate PDFs
generate_pdf() {
    local slug="$1"
    local type="$2"
    local url="$3"
    local output="$4"

    echo -e "${BLUE}Processing: ${slug}${NC}"

    if node generate-pdf-server.js "$url" "$output" 2>/dev/null; then
        size=$(du -h "$output" | cut -f1)
        echo -e "${GREEN}✓ Generated: $output ($size)${NC}"
        echo ""
        return 0
    else
        echo -e "${RED}✗ Failed: $slug${NC}"
        echo ""
        return 1
    fi
}

# Generate Risk Assessment PDFs
echo "======================================"
echo "Generating Risk Assessment PDFs..."
echo "======================================"
echo ""

ra_count=0
for dir in _risk_assessments/*.md; do
    if [ -f "$dir" ]; then
        filename=$(basename "$dir" .md)
        url="http://localhost:4000/SAIL-RA-SWP/risk-assessments/${filename}/"
        output="pdfs/risk-assessments/SAIL-RA-${filename}.pdf"

        if generate_pdf "$filename" "RA" "$url" "$output"; then
            ((ra_count++))
        fi
    fi
done

# Generate Safe Work Procedure PDFs
echo "======================================"
echo "Generating Safe Work Procedure PDFs..."
echo "======================================"
echo ""

swp_count=0
for dir in _safe_work_procedures/*.md; do
    if [ -f "$dir" ]; then
        filename=$(basename "$dir" .md)
        url="http://localhost:4000/SAIL-RA-SWP/safe-work-procedures/${filename}/"
        output="pdfs/safe-work-procedures/SAIL-SWP-${filename}.pdf"

        if generate_pdf "$filename" "SWP" "$url" "$output"; then
            ((swp_count++))
        fi
    fi
done

# Stop Jekyll server
echo "Stopping Jekyll server..."
pkill -f "jekyll serve" 2>/dev/null || true
echo -e "${GREEN}✓ Server stopped${NC}"
echo ""

# Cleanup temp files
rm -f generate-pdf-server.js

# Summary
echo "======================================"
echo "Summary"
echo "======================================"
echo ""
echo -e "${GREEN}PDF Engine: Playwright (Chromium)${NC}"
echo -e "${GREEN}Risk Assessments:      ${ra_count} PDFs generated${NC}"
echo -e "${GREEN}Safe Work Procedures:  ${swp_count} PDFs generated${NC}"
echo ""

if [ $ra_count -gt 0 ] || [ $swp_count -gt 0 ]; then
    echo "Generated files:"
    echo ""

    if [ $ra_count -gt 0 ]; then
        echo -e "${BLUE}Risk Assessments:${NC}"
        ls -lh pdfs/risk-assessments/*.pdf 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'
        echo ""
    fi

    if [ $swp_count -gt 0 ]; then
        echo -e "${BLUE}Safe Work Procedures:${NC}"
        ls -lh pdfs/safe-work-procedures/*.pdf 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'
        echo ""
    fi
fi

echo -e "${GREEN}✓ PDF generation complete!${NC}"
echo ""

read -p "Open PDFs folder? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        open pdfs/
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        xdg-open pdfs/
    fi
fi
