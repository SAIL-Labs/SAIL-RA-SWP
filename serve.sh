#!/bin/bash

# SAIL Laboratory Safety Documentation - Local Testing Script
# Regenerates the RA/SWP pages from documents/*.yaml, then runs Jekyll locally.

set -e

echo "SAIL safety docs — local server"
echo "================================"
echo ""

# --- Python: generate the collection markdown from documents/*.yaml ----------
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed."
    exit 1
fi

VENV=docgen/.venv
if [ ! -d "$VENV" ]; then
    echo "Creating Python venv and installing docgen dependencies..."
    python3 -m venv "$VENV"
    "$VENV/bin/pip" install -q -r docgen/requirements.txt
fi

echo "Generating web pages from documents/*.yaml..."
"$VENV/bin/python" docgen/render.py --all --web
echo ""

# If Word/PDF outputs have been rendered (render.py --all --pdf), copy them into
# the site tree so the Download buttons work locally like they do on the live site.
if [ -d docgen/out/pdfs ]; then
    mkdir -p pdfs docx
    cp -r docgen/out/pdfs/. pdfs/
    [ -d docgen/out/docx ] && cp -r docgen/out/docx/. docx/
    echo "Copied rendered PDFs/Word docs into ./pdfs and ./docx (served locally)."
else
    echo "NOTE: no local PDFs yet — Download buttons will 404 locally until you run:"
    echo "      $VENV/bin/python docgen/render.py --all --pdf   (needs LibreOffice)"
    echo "      (the deployed site always has them — CI generates PDFs on every push)"
fi
echo ""

# --- Ruby: Jekyll ------------------------------------------------------------
if ! command -v bundle &> /dev/null; then
    echo "Error: Bundler is not installed."
    echo "Please install it with: gem install bundler"
    exit 1
fi

if [ ! -f "Gemfile.lock" ]; then
    echo "Installing dependencies..."
    bundle install
    echo ""
fi

echo "Starting server at http://localhost:4000/SAIL-RA-SWP/"
echo "NOTE: pages are generated from documents/*.yaml — edit the YAML, then"
echo "re-run 'docgen/.venv/bin/python docgen/render.py --all --web' (livereload"
echo "picks up the regenerated markdown automatically)."
echo "Press Ctrl+C to stop the server"
echo ""

bundle exec jekyll serve --livereload
