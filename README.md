# Sustainable Supply Chain Management: Bibliometric Research Analysis

A comprehensive bibliometric analysis of **4,441 research publications** on Sustainable Supply Chain Management (SSCM) from 2021-2026, sourced from Scopus database.

## 📊 Project Overview

This repository contains a detailed bibliometric study examining research trends, themes, publication patterns, and geographic distribution in the rapidly growing field of Sustainable Supply Chain Management.

### Key Statistics

| Metric | Value |
|--------|-------|
| **Total Publications** | 4,441 |
| **Year Range** | 2021-2026 |
| **Unique Journals** | 1,414 |
| **Unique Authors** | 4,269 |
| **Countries Represented** | 128 |
| **Average Citations** | 15.4 per paper |
| **Peak Year** | 2025 (1,163 publications) |
| **Growth Rate** | 2.1x from 2021-2025 |

## 📁 Repository Contents

### Data Files
- **`4441.csv`** - Raw Scopus export with 4,441 publications and 33 metadata fields
- **`bibliometric data`** - Template file (placeholder)

### Analysis Scripts
- **`analysis_lightweight.py`** - Main analysis script (uses only Python standard library)
  - Requires only Python 3.11+
  - No external dependencies needed
  - Generates all analysis reports and CSV exports

- **`analysis.py`** - Advanced analysis script with visualizations
  - Requires: pandas, matplotlib, seaborn, numpy
  - Generates PNG visualizations and summary statistics
  - *Note: Requires external library installation*

### Analysis Reports

#### Executive Reports
- **`ANALYSIS_SUMMARY.txt`** - Quick reference summary of key findings
- **`RESEARCH_INSIGHTS.md`** - Comprehensive 12-section analysis report
  - Publication trends
  - Research themes and focus areas
  - Citation impact analysis
  - Global research landscape
  - Research gaps and opportunities
  - Future outlook and recommendations

#### Data Exports (CSV Format)
- **`themes_analysis.csv`** - Research theme distribution
- **`sources_analysis.csv`** - Top 20 publication sources/journals
- **`keywords_analysis.csv`** - Top 30 author keywords and frequency
- **`countries_analysis.csv`** - Geographic distribution (top 20 countries)
- **`analysis_report.json`** - Structured JSON report with complete metrics

## 🚀 Getting Started

### Quick Start (No Setup Required)

1. **Read the executive summary:**
   ```bash
   cat ANALYSIS_SUMMARY.txt
   ```

2. **Read the comprehensive insights:**
   ```bash
   cat RESEARCH_INSIGHTS.md
   ```

3. **Review data exports:**
   ```bash
   cat themes_analysis.csv
   cat keywords_analysis.csv
   ```

### Running the Analysis

#### Using lightweight analysis (recommended):
```bash
python3.11 analysis_lightweight.py
```

**Requirements:** Python 3.11+ (no external libraries)

**Output:**
- Console output with complete analysis
- 5 CSV files with exported data
- JSON structured report
- Text summary

#### Using full analysis with visualizations:
```bash
pip install pandas matplotlib seaborn numpy
python3 analysis.py
```

**Output:**
- All outputs from lightweight analysis
- 7 PNG visualization files
- Console analysis output

## 📈 Key Findings

### Publication Growth
- **Exponential growth:** Publications increased 2.1x from 2021 to 2025
- **2025 Peak:** 1,163 publications (26% growth over 2024)
- **Acceleration:** Growing research focus on SSCM

### Research Themes (Top 8)
1. **Green Innovation & Technology** - 3,732 papers (84.0%)
2. **Environmental Performance** - 1,630 papers (36.7%)
3. **Logistics & Distribution** - 1,375 papers (31.0%)
4. **Circular Economy** - 360 papers (8.1%)
5. **Procurement & Sourcing** - 297 papers (6.7%)
6. **Digital Transformation** - 225 papers (5.1%)
7. **Supply Chain Resilience** - 199 papers (4.5%)
8. **Stakeholder Engagement** - 182 papers (4.1%)

### Top Research Keywords
1. Green Supply Chain Management (593)
2. Sustainability (572)
3. Sustainable Supply Chain Management (510)
4. Green Logistics (422)
5. Supply Chain Management (270)
6. Industry 4.0 (91)
7. Blockchain (90)
8. Artificial Intelligence (84)

### Leading Publication Sources
1. Sustainability (Switzerland) - 328 papers
2. Journal of Cleaner Production - 102 papers
3. Cleaner Logistics and Supply Chain - 60 papers
4. Business Strategy and the Environment - 56 papers
5. Environmental Science and Pollution Research - 51 papers

### Geographic Distribution
- **China:** 1,788 affiliations (40%)
- **India:** 1,341 affiliations (30%)
- **Other leaders:** UK, Indonesia, US (300-500 each)
- **Global:** 128 countries represented

### Open Access Status
- **Open Access:** 2,162 papers (48.7%)
- **Closed Access:** 2,279 papers (51.3%)

## 🔍 Analysis Methodology

### Data Source
- **Database:** Scopus
- **Period:** 2021-2026
- **Collection Date:** June 1, 2026
- **Total Records:** 4,441 publications

### Data Fields Analyzed (33 columns)
- Bibliographic: Authors, Title, Year, DOI
- Publication: Source, Volume, Issue, Pages
- Content: Abstract, Keywords (Author & Index)
- Metadata: Document Type, Publication Stage, Language
- Impact: Citations, Open Access Status
- Geographic: Affiliations, Correspondence Address
- Publisher Information

### Analysis Methods
1. **Temporal Analysis:** Publication trends over time
2. **Bibliometric Analysis:** Citation counts, impact metrics
3. **Keyword Analysis:** Frequency analysis and clustering
4. **Thematic Analysis:** Research theme identification
5. **Geographic Analysis:** Country/region distribution
6. **Publication Landscape:** Journal, source, and document type analysis

## 💡 Key Insights

### Dominant Trends
- **Technology-focused:** 84% of research focuses on green innovation and technology
- **Asia-Pacific Leadership:** China and India lead with 70% of all affiliations
- **Rapid Growth:** SSCM is one of the fastest-growing research domains
- **Environmental Focus:** Environmental performance in 37% of papers

### Research Gaps (Opportunities)
- Supply Chain Resilience (4.5%) - underrepresented
- Stakeholder Engagement (4.1%) - limited research
- Procurement Sustainability (6.7%) - less studied
- Digital Transformation Integration (5.1%) - emerging area

### Emerging Intersections
- AI + Sustainability
- Blockchain + Supply Chain Transparency
- Industry 5.0 + SSCM
- Circular Economy + Digital Technologies

## 📊 Generated Files Explained

### CSV Files
All CSV files are in standard format, easily importable to Excel, R, Python, or other tools.

**themes_analysis.csv**
```
Theme,Count,Percentage
Green Innovation & Technology,3732,84.0%
Environmental Performance,1630,36.7%
...
```

**sources_analysis.csv**
```
Journal,Publications
Sustainability (Switzerland),328
Journal of Cleaner Production,102
...
```

**keywords_analysis.csv**
```
Keyword,Frequency
green supply chain management,593
sustainability,572
...
```

**countries_analysis.csv**
```
Country/Region,Affiliations
China,1788
India,1341
...
```

### JSON Report
Structured data format suitable for programmatic access and integration.

```json
{
  "title": "Bibliometric Analysis Report...",
  "generated": "2026-06-01T10:13:13",
  "dataset_statistics": {
    "total_publications": 4441,
    "year_range": "2021-2026",
    ...
  },
  "top_themes": [...],
  "top_sources": [...],
  "top_keywords": [...]
}
```

## 🎯 Use Cases

### For Researchers
- Identify research trends in SSCM
- Discover publication venues and citation leaders
- Find research gaps to explore
- Understand global research landscape

### For Practitioners
- Stay updated on SSCM best practices
- Benchmark against research findings
- Identify emerging technologies and trends
- Understand implementation challenges

### For Students
- Learn about SSCM research domain
- Find thesis/research topics
- Understand publication landscape
- Identify leading researchers and institutions

### For Policy Makers
- Understand research priorities
- Inform policy decisions on sustainability
- Identify innovation areas
- Support research funding decisions

## 🔄 Updating the Analysis

To re-run the analysis with updated data:

1. **Export updated data from Scopus** to `4441.csv`
2. **Run the analysis script:**
   ```bash
   python3 analysis_lightweight.py
   ```
3. **Review updated reports** in generated CSV/JSON files

## 📚 Related Research

### Recommended Reading
- **Journal of Cleaner Production** - Leading SSCM publication venue
- **Sustainability (Switzerland)** - Most prolific source in this analysis
- **Business Strategy and the Environment** - Strategy-focused SSCM research

### Key Topics to Explore
- Green Supply Chain Management (GSCM)
- Sustainable Logistics
- Circular Economy in Supply Chains
- Industry 4.0 and Sustainability
- Supply Chain Resilience

## 📋 Data Quality Notes

- **Coverage:** Scopus indexed publications (2021-2026)
- **Language:** Primarily English-language publications
- **Affiliations:** Extracted from author affiliation data
- **Keywords:** Author-supplied and indexed keywords
- **Citations:** Current as of export date (June 1, 2026)

## 🤝 Contributing

This is a static analysis repository. For updates or corrections:

1. Ensure data currency (re-export from Scopus if needed)
2. Run updated analysis scripts
3. Update markdown documentation
4. Commit with meaningful messages

## 📞 Contact & Support

For questions about the analysis:
- Review RESEARCH_INSIGHTS.md for detailed explanations
- Check analysis_report.json for structured data
- Consult ANALYSIS_SUMMARY.txt for quick reference

## 📄 License

This bibliometric analysis is based on Scopus data. Please refer to Scopus terms of use for data usage restrictions.

## 🙏 Acknowledgments

- **Data Source:** Scopus (Elsevier)
- **Analysis Period:** 2021-2026
- **Generation Date:** June 1, 2026
- **Tools:** Python 3.11

---

## Quick Statistics Reference

```
DATASET:
  Total Publications: 4,441
  Year Range: 2021-2026
  Unique Journals: 1,414
  Unique Authors: 4,269
  Countries: 128

GROWTH:
  2021: 550 papers
  2022: 597 papers
  2023: 755 papers
  2024: 922 papers
  2025: 1,163 papers (peak)
  Growth: 2.1x from 2021-2025

THEMES (% of papers):
  Green Innovation & Technology: 84%
  Environmental Performance: 37%
  Logistics & Distribution: 31%
  Circular Economy: 8%
  Digital Transformation: 5%

TOP COUNTRIES:
  China: 1,788 (40%)
  India: 1,341 (30%)
  UK: 466 (11%)
  Indonesia: 463 (10%)
  USA: 386 (9%)

IMPACT:
  Avg Citations: 15.4
  Highly Cited (>10): 1,469
  Max Citations: 464
  Open Access: 48.7%
```

---

*Analysis Generated: June 1, 2026*
*Last Updated: June 1, 2026*
*Next Recommended Update: Q4 2026*
