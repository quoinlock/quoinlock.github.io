# LetterPress Tools

Professional tools for letterpress typesetters, brought to you by [Quoinlock](https://quoinlock.com).

Live at: [quoinlock.com/letterpress](https://quoinlock.com/letterpress)

## Overview

This collection of web-based tools is designed specifically for letterpress printers and typesetters. Each tool addresses common challenges in traditional letterpress printing, from calculating character counts for case sorting to mixing custom PMS ink colors.

## Tools

### 1. Character Counter

Analyzes text to count character frequency - essential for planning type case layouts and determining how many of each character you'll need.

**Features:**
- Real-time character frequency analysis
- Automatic categorization (uppercase, lowercase, numbers, punctuation, spaces)
- Two-column layout for easy reading
- Print-friendly output
- Perfect for:
  - Planning type case organization
  - Estimating character needs for a project
  - Sorting foundry type
  - Case layout optimization

**Usage:**
1. Paste or type your text
2. View instant character frequency breakdown
3. Print results for reference while sorting type

---

### 2. Leading Calculator

Calculates the leading (line spacing) needed to fill a specific height with a given number of lines.

**Features:**
- Supports multiple units (points, picas, inches)
- Shows text height, leading per line, and total leading
- Displays traditional typographic notation (e.g., "12/14")
- Provides spacing recommendations
- Useful for:
  - Filling a specific form height
  - Balancing page layout
    - Calculating furniture and spacing needs

**Usage:**
1. Enter your type size in points
2. Specify number of lines
3. Enter available height (space to fill)
4. Get exact leading calculations

**Example:**
- Type size: 12pt
- Lines: 20
- Available height: 40 picas
- Result: Leading calculations for perfect fit

---

### 3. PMS Ink Mixer

Converts PANTONE (PMS) ink formulas from percentages to practical parts and weights for mixing letterpress inks.

**Features:**
- Supports both current (11-color) and legacy (18-color) PMS base ink systems
- Converts percentages to simplified parts ratios
- Calculates exact weights based on your scale accuracy
- Handles trace amounts intelligently
- Shareable formulas via URL
- Print-friendly mixing sheets
- Accounts for:
  - Scale accuracy (0.1g, 0.25g, or 0.5g)
  - Desired ink yield
  - Paper type (coated/uncoated)
  - Normalization when percentages don't sum to 100%

**Ink Systems:**
- **Current Base Inks** (11 colors, post-2023): Black, Green, Orange 016, Pink, Process Blue, Purple v2, Real Purple, Rubine Red, Violet v2, Warm Red, Yellow PY12
- **Legacy Base Inks** (18 colors, pre-2023): Black, Blue 072, Bright Red, Dark Blue, Green, Med. Purple, Orange 021, Pink, Process Blue, Purple, Red 032, Reflex Blue, Rhod. Red, Rubine Red, Violet, Warm Red, Yellow 012, Yellow
- **Mixing Colors**: Opaque White, Transparent White

**Usage:**
1. Select your ink system (current or legacy)
2. Enter color name and PMS code (optional)
3. Specify paper type and ink yield
4. Enter percentage for each base ink
5. Click "Calculate" to get parts and weights
6. Print or share the formula

**Smart Features:**
- Automatically simplifies ratios (targets 8 or 16 parts)
- Supports quarter-part increments (0.25, 0.5, 0.75)
- Rounds weights to your scale's accuracy
- Shows "trace" for amounts too small to measure
- Normalizes percentages that don't sum to 100%

---

### 4. Unit Converter

Quick conversion between typographic measurement units.

**Features:**
- Converts between points, picas, inches, and millimeters
- Real-time conversion as you type
- Reference chart included
- Essential for:
  - Converting design measurements
  - Working with mixed measurement systems
  - Quick reference lookup

**Conversions:**
- 1 inch = 72 points = 6 picas = 25.4mm
- 1 pica = 12 points = 1/6 inch = 4.23mm
- 1 point = 1/72 inch = 0.35mm

---

## Technical Details

### Browser Support
- Modern browsers (Chrome, Firefox, Safari, Edge)
- Fully responsive design for mobile and tablet
- Print-optimized output

### Print Functionality
All tools include print-friendly layouts:
- Character Counter: Clean character frequency tables
- Leading Calculator: Results only (no input fields)
- PMS Ink Mixer: Professional mixing formula sheets with all settings
- Unit Converter: Reference chart

### URL Sharing
The PMS Ink Mixer supports sharing formulas via URL parameters, making it easy to save and share recipes with colleagues.

---

## Development

### File Structure
```
letterpress/
├── index.html          # Single-page application with all tools
└── README.md          # This file
```

### Styling
- Custom CSS with Quoinlock branding
- Dark theme with purple/indigo gradient accents
- Glassmorphic UI elements
- Fully responsive grid layouts

### JavaScript
- Vanilla JavaScript (no dependencies)
- Tab-based interface for tool switching
- Real-time calculations and conversions
- URL parameter handling for sharing

---

## Credits

Built with care by [Quoinlock](https://quoinlock.com) for the letterpress community.

## License

© 2026 Quoin LLC. All rights reserved.

---

## Support

Questions or suggestions? Contact us at [quoinlock.com/contact](https://quoinlock.com/contact)
