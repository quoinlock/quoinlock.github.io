#!/bin/bash

# Script to update CSS files with CSS variables

CSS_VARS_BLOCK='        :root {
            /* Primary Colors */
            --primary-indigo: #6366f1;
            --primary-purple: #8b5cf6;
            --primary-indigo-light: #818cf8;
            --primary-purple-light: #a78bfa;

            /* Dark Purple Shades */
            --purple-dark: #4c1d95;
            --purple-mid: #7c3aed;
            --purple-mid-alt: #6d28d9;

            /* Background Colors */
            --bg-dark-1: #0f0f1e;
            --bg-dark-2: #1a1a2e;
            --bg-dark-3: #16213e;

            /* Text Colors */
            --text-primary: #e4e4e7;
            --text-secondary: #d4d4d8;
            --text-tertiary: #a1a1aa;
            --text-highlight: #c7d2fe;

            /* Utility Colors */
            --success-green: #22c55e;
            --white: #ffffff;
            --black: #000000;

            /* Light Grays (for book pages, etc.) */
            --gray-light-1: #f5f5f5;
            --gray-light-2: #e8e8e8;
            --gray-light-3: #dadada;
        }

'

for file in faq.html contact.html terms.html privacy.html thanks.html; do
    if [ -f "$file" ]; then
        echo "Processing $file..."

        # Insert CSS variables after <style> tag
        sed -i '/<style>/a\'"$(echo -e "$CSS_VARS_BLOCK")" "$file"

        # Replace color values with CSS variables
        sed -i \
            -e 's/#0f0f1e/var(--bg-dark-1)/g' \
            -e 's/#1a1a2e/var(--bg-dark-2)/g' \
            -e 's/#16213e/var(--bg-dark-3)/g' \
            -e 's/#e4e4e7/var(--text-primary)/g' \
            -e 's/#d4d4d8/var(--text-secondary)/g' \
            -e 's/#a1a1aa/var(--text-tertiary)/g' \
            -e 's/#c7d2fe/var(--text-highlight)/g' \
            -e 's/#6366f1/var(--primary-indigo)/g' \
            -e 's/#8b5cf6/var(--primary-purple)/g' \
            -e 's/#818cf8/var(--primary-indigo-light)/g' \
            -e 's/#a78bfa/var(--primary-purple-light)/g' \
            -e 's/#22c55e/var(--success-green)/g' \
            -e 's/rgba(99, 102, 241, 0\.15)/color-mix(in srgb, var(--primary-indigo) 15%, transparent)/g' \
            -e 's/rgba(139, 92, 246, 0\.15)/color-mix(in srgb, var(--primary-purple) 15%, transparent)/g' \
            -e 's/rgba(15, 15, 30, 0\.8)/color-mix(in srgb, var(--bg-dark-1) 80%, transparent)/g' \
            -e 's/rgba(15, 15, 30, 0\.98)/color-mix(in srgb, var(--bg-dark-1) 98%, transparent)/g' \
            -e 's/rgba(15, 15, 30, 0\.6)/color-mix(in srgb, var(--bg-dark-1) 60%, transparent)/g' \
            -e 's/rgba(99, 102, 241, 0\.2)/color-mix(in srgb, var(--primary-indigo) 20%, transparent)/g' \
            -e 's/rgba(99, 102, 241, 0\.3)/color-mix(in srgb, var(--primary-indigo) 30%, transparent)/g' \
            -e 's/rgba(99, 102, 241, 0\.4)/color-mix(in srgb, var(--primary-indigo) 40%, transparent)/g' \
            -e 's/rgba(99, 102, 241, 0\.5)/color-mix(in srgb, var(--primary-indigo) 50%, transparent)/g' \
            -e 's/rgba(99, 102, 241, 0\.6)/color-mix(in srgb, var(--primary-indigo) 60%, transparent)/g' \
            -e 's/rgba(99, 102, 241, 0\.1)/color-mix(in srgb, var(--primary-indigo) 10%, transparent)/g' \
            -e 's/rgba(139, 92, 246, 0\.2)/color-mix(in srgb, var(--primary-purple) 20%, transparent)/g' \
            -e 's/rgba(139, 92, 246, 0\.3)/color-mix(in srgb, var(--primary-purple) 30%, transparent)/g' \
            -e 's/color: white/color: var(--white)/g' \
            "$file"

        echo "✓ Completed $file"
    else
        echo "✗ File $file not found"
    fi
done

echo "All files processed!"
