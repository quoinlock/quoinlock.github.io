#!/usr/bin/env python3
import re

CSS_VARS = """        :root {
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

"""

# Define all the replacements
REPLACEMENTS = [
    # Hex color replacements
    ('#0f0f1e', 'var(--bg-dark-1)'),
    ('#1a1a2e', 'var(--bg-dark-2)'),
    ('#16213e', 'var(--bg-dark-3)'),
    ('#e4e4e7', 'var(--text-primary)'),
    ('#d4d4d8', 'var(--text-secondary)'),
    ('#a1a1aa', 'var(--text-tertiary)'),
    ('#c7d2fe', 'var(--text-highlight)'),
    ('#6366f1', 'var(--primary-indigo)'),
    ('#8b5cf6', 'var(--primary-purple)'),
    ('#818cf8', 'var(--primary-indigo-light)'),
    ('#a78bfa', 'var(--primary-purple-light)'),
    ('#22c55e', 'var(--success-green)'),
    ('white', 'var(--white)'),  # This one needs special handling for color: white

    # RGBA color replacements
    ('rgba(99, 102, 241, 0.15)', 'color-mix(in srgb, var(--primary-indigo) 15%, transparent)'),
    ('rgba(139, 92, 246, 0.15)', 'color-mix(in srgb, var(--primary-purple) 15%, transparent)'),
    ('rgba(15, 15, 30, 0.8)', 'color-mix(in srgb, var(--bg-dark-1) 80%, transparent)'),
    ('rgba(15, 15, 30, 0.98)', 'color-mix(in srgb, var(--bg-dark-1) 98%, transparent)'),
    ('rgba(15, 15, 30, 0.6)', 'color-mix(in srgb, var(--bg-dark-1) 60%, transparent)'),
    ('rgba(15, 15, 30, 0.95)', 'color-mix(in srgb, var(--bg-dark-1) 95%, transparent)'),
    ('rgba(15, 15, 30, 0.9)', 'color-mix(in srgb, var(--bg-dark-1) 90%, transparent)'),
    ('rgba(99, 102, 241, 0.1)', 'color-mix(in srgb, var(--primary-indigo) 10%, transparent)'),
    ('rgba(99, 102, 241, 0.2)', 'color-mix(in srgb, var(--primary-indigo) 20%, transparent)'),
    ('rgba(99, 102, 241, 0.3)', 'color-mix(in srgb, var(--primary-indigo) 30%, transparent)'),
    ('rgba(99, 102, 241, 0.4)', 'color-mix(in srgb, var(--primary-indigo) 40%, transparent)'),
    ('rgba(99, 102, 241, 0.5)', 'color-mix(in srgb, var(--primary-indigo) 50%, transparent)'),
    ('rgba(99, 102, 241, 0.6)', 'color-mix(in srgb, var(--primary-indigo) 60%, transparent)'),
    ('rgba(139, 92, 246, 0.2)', 'color-mix(in srgb, var(--primary-purple) 20%, transparent)'),
    ('rgba(139, 92, 246, 0.3)', 'color-mix(in srgb, var(--primary-purple) 30%, transparent)'),
]

def update_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Add CSS variables block after <style> if not already present
    if ':root {' not in content:
        content = content.replace('    <style>\n', '    <style>\n' + CSS_VARS)

    # Apply all replacements
    for old, new in REPLACEMENTS:
        content = content.replace(old, new)

    with open(filename, 'w') as f:
        f.write(content)

    print(f"✓ Updated {filename}")

if __name__ == '__main__':
    files = ['faq.html', 'contact.html', 'terms.html', 'privacy.html', 'thanks.html']
    for file in files:
        try:
            update_file(file)
        except Exception as e:
            print(f"✗ Error updating {file}: {e}")
