"""
Bibliometric Analysis of Sustainable Supply Chain Management Research
Using Built-in Python Libraries (No External Dependencies)
"""

import csv
import json
from collections import Counter, defaultdict
from datetime import datetime

# ============================================================================
# 1. DATA LOADING
# ============================================================================

print("=" * 80)
print("BIBLIOMETRIC ANALYSIS: SUSTAINABLE SUPPLY CHAIN MANAGEMENT")
print("=" * 80)

data = []
headers = []

try:
    with open('4441.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        for row in reader:
            data.append(row)
    
    print(f"\n✓ Dataset loaded successfully")
    print(f"  - Total records: {len(data)}")
    print(f"  - Total columns: {len(headers)}")
    
except Exception as e:
    print(f"Error loading data: {e}")
    exit(1)

# ============================================================================
# 2. BASIC STATISTICS
# ============================================================================

print("\n" + "=" * 80)
print("DATASET OVERVIEW")
print("=" * 80)

years = []
sources = []
doc_types = []
authors_list = []
keywords_list = []
citations = []
affiliations = []

for record in data:
    try:
        year = int(float(record.get('Year', 0) or 0))
        if year > 0:
            years.append(year)
    except:
        pass
    
    if record.get('Source title'):
        sources.append(record['Source title'])
    
    if record.get('Document Type'):
        doc_types.append(record['Document Type'])
    
    if record.get('Authors'):
        authors_list.append(record['Authors'])
    
    if record.get('Author Keywords'):
        keywords_list.append(record['Author Keywords'])
    
    if record.get('Affiliations'):
        affiliations.append(record['Affiliations'])
    
    try:
        cited = int(float(record.get('Cited by', 0) or 0))
        if cited >= 0:
            citations.append(cited)
    except:
        pass

if years:
    print(f"\nYear Range: {min(years)} - {max(years)}")
    print(f"Total Publications: {len(data)}")
    print(f"Unique Journals: {len(set(sources))}")
    print(f"Unique Authors: {len(set(authors_list))}")

# ============================================================================
# 3. TEMPORAL TRENDS
# ============================================================================

print("\n" + "=" * 80)
print("TEMPORAL ANALYSIS")
print("=" * 80)

pub_by_year = Counter(years)
print(f"\nPublications by Year (Last 10 Years):")
for year in sorted(pub_by_year.keys())[-10:]:
    count = pub_by_year[year]
    bar = "█" * (count // 5)
    print(f"  {year}: {count:4d} {bar}")

# ============================================================================
# 4. SOURCE/JOURNAL ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("TOP PUBLICATION SOURCES")
print("=" * 80)

source_freq = Counter(sources)
print(f"\nTop 15 Journals/Sources:")
for i, (source, count) in enumerate(source_freq.most_common(15), 1):
    print(f"  {i:2d}. {source[:65]:<65} ({count})")

# ============================================================================
# 5. DOCUMENT TYPE
# ============================================================================

print("\n" + "=" * 80)
print("DOCUMENT TYPE DISTRIBUTION")
print("=" * 80)

doc_type_freq = Counter(doc_types)
total_docs = len(data)
print(f"\nDocument Types:")
for doc_type, count in doc_type_freq.most_common():
    pct = (count / total_docs) * 100
    bar = "▓" * int(pct / 5)
    print(f"  {doc_type:<25} {count:5d} ({pct:5.1f}%) {bar}")

# ============================================================================
# 6. KEYWORD ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("KEYWORD ANALYSIS")
print("=" * 80)

all_keywords = []
for kw_str in keywords_list:
    if kw_str:
        keywords = [k.strip().lower() for k in kw_str.split(';')]
        all_keywords.extend(keywords)

keyword_freq = Counter(all_keywords)
print(f"\nTop 25 Author Keywords:")
for i, (keyword, count) in enumerate(keyword_freq.most_common(25), 1):
    print(f"  {i:2d}. {keyword[:50]:<50} ({count})")

# ============================================================================
# 7. CITATION ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("CITATION ANALYSIS")
print("=" * 80)

if citations:
    avg_citations = sum(citations) / len(citations)
    max_citations = max(citations)
    highly_cited = sum(1 for c in citations if c > 10)
    
    print(f"\nCitation Statistics:")
    print(f"  - Average Citations per Paper: {avg_citations:.2f}")
    print(f"  - Max Citations: {int(max_citations)}")
    print(f"  - Papers with >10 Citations: {highly_cited}")
    print(f"  - Papers with >50 Citations: {sum(1 for c in citations if c > 50)}")
    print(f"  - Total Citation Count: {int(sum(citations))}")

# ============================================================================
# 8. THEMATIC ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("RESEARCH THEMES")
print("=" * 80)

themes = {
    'Green Innovation & Technology': ['green', 'innovation', 'technology', 'ai', 'artificial intelligence', 'blockchain', 'iot', 'industry 4.0'],
    'Circular Economy': ['circular', 'circular economy', 'reverse logistics', 'recycling', 'waste', 'remanufacturing'],
    'Environmental Performance': ['environmental', 'emissions', 'carbon', 'ghg', 'sustainability', 'eco-'],
    'Supply Chain Resilience': ['resilience', 'risk', 'risk management', 'disruption', 'agility'],
    'Digital Transformation': ['digital', 'digitalization', 'automation', 'industry 5.0', 'cyber-physical'],
    'Procurement & Sourcing': ['procurement', 'supplier', 'sourcing', 'vendor', 'buying', 'purchasing'],
    'Logistics & Distribution': ['logistics', 'distribution', 'transportation', 'warehouse', 'delivery', 'routing'],
    'Stakeholder Engagement': ['stakeholder', 'collaboration', 'partnership', 'multi-stakeholder', 'governance'],
}

theme_counts = defaultdict(int)
for kw_str in keywords_list:
    if kw_str:
        kw_lower = kw_str.lower()
        for theme, theme_keywords in themes.items():
            for keyword in theme_keywords:
                if keyword in kw_lower:
                    theme_counts[theme] += 1
                    break

print(f"\nResearch Theme Distribution:")
for theme in sorted(theme_counts.items(), key=lambda x: x[1], reverse=True):
    theme_name, count = theme
    pct = (count / len(data)) * 100
    bar = "▒" * int(pct / 5)
    print(f"  {theme_name:<40} {count:4d} ({pct:5.1f}%) {bar}")

# ============================================================================
# 9. GEOGRAPHIC ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("GEOGRAPHIC ANALYSIS")
print("=" * 80)

countries_found = []
for aff in affiliations:
    if aff:
        parts = aff.split(';')
        for part in parts:
            country_part = part.strip().split(',')[-1].strip()
            if len(country_part) > 2:
                countries_found.append(country_part)

country_freq = Counter(countries_found)
print(f"\nTop 15 Countries/Regions by Affiliations:")
for i, (country, count) in enumerate(country_freq.most_common(15), 1):
    bar = "░" * min(int(count / 10), 30)
    print(f"  {i:2d}. {country:<40} {count:4d} {bar}")

# ============================================================================
# 10. OPEN ACCESS ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("OPEN ACCESS STATUS")
print("=" * 80)

open_access_count = 0
for record in data:
    oa = record.get('Open Access', '')
    if oa and 'Open Access' in oa:
        open_access_count += 1

oa_pct = (open_access_count / len(data)) * 100
print(f"\nOpen Access Publications: {open_access_count} ({oa_pct:.1f}%)")
print(f"Closed Access Publications: {len(data) - open_access_count} ({100 - oa_pct:.1f}%)")

# ============================================================================
# 11. KEY FINDINGS SUMMARY
# ============================================================================

print("\n" + "=" * 80)
print("KEY FINDINGS SUMMARY")
print("=" * 80)

top_theme = sorted(theme_counts.items(), key=lambda x: x[1], reverse=True)[0]
top_journal = source_freq.most_common(1)[0]
top_keyword = keyword_freq.most_common(1)[0]
top_country = country_freq.most_common(1)[0] if country_freq else ('N/A', 0)

print(f"""
📊 RESEARCH LANDSCAPE:
   • Total Publications Analyzed: {len(data):,}
   • Year Range: {min(years)} - {max(years)}
   • Unique Journals/Sources: {len(set(sources))}
   • Unique Authors: {len(set(authors_list))}
   • Average Citations per Paper: {avg_citations:.1f}

📈 PUBLICATION TRENDS:
   • Peak Publication Year: {max(pub_by_year, key=pub_by_year.get)}
   • Publications in 2026: {pub_by_year.get(2026, 0)}
   • Highly Cited Papers (>10 citations): {highly_cited}

📚 RESEARCH FOCUS:
   • Most Studied Theme: {top_theme[0]} ({top_theme[1]} papers)
   • Top Journal: {top_journal[0][:50]} ({top_journal[1]} papers)
   • Most Frequent Keyword: {top_keyword[0]} ({top_keyword[1]} mentions)
   • Common Document Type: {doc_type_freq.most_common(1)[0][0]}

🌍 GLOBAL RESEARCH:
   • Leading Geographic Region: {top_country[0]} ({top_country[1]} affiliations)
   • Countries Represented: {len(country_freq)}
   • International Collaboration Indicator: {len([a for a in affiliations if a and ';' in a])} papers

📖 OPEN SCIENCE:
   • Open Access Publications: {open_access_count} ({oa_pct:.1f}%)
   • Supporting Greater Accessibility: {'Yes' if oa_pct > 50 else 'Moderate'}
""")

# ============================================================================
# 12. EXPORT RESULTS
# ============================================================================

print("\n" + "=" * 80)
print("GENERATING REPORTS")
print("=" * 80)

# Export theme analysis
theme_report = []
for theme in sorted(theme_counts.items(), key=lambda x: x[1], reverse=True):
    theme_report.append({'Theme': theme[0], 'Count': theme[1], 'Percentage': f"{(theme[1]/len(data)*100):.1f}%"})

# Export top sources
sources_report = []
for source, count in source_freq.most_common(20):
    sources_report.append({'Journal': source, 'Publications': count})

# Export top keywords
keywords_report = []
for keyword, count in keyword_freq.most_common(30):
    keywords_report.append({'Keyword': keyword, 'Frequency': count})

# Export top countries
countries_report = []
for country, count in country_freq.most_common(20):
    countries_report.append({'Country/Region': country, 'Affiliations': count})

# Write JSON report
report = {
    'title': 'Bibliometric Analysis Report: Sustainable Supply Chain Management',
    'generated': datetime.now().isoformat(),
    'dataset_statistics': {
        'total_publications': len(data),
        'year_range': f"{min(years)}-{max(years)}",
        'unique_journals': len(set(sources)),
        'unique_authors': len(set(authors_list)),
        'average_citations': round(avg_citations, 2),
        'max_citations': int(max_citations),
        'open_access_percentage': round(oa_pct, 1)
    },
    'top_themes': theme_report[:10],
    'top_sources': sources_report[:15],
    'top_keywords': keywords_report[:25],
    'top_countries': countries_report[:15]
}

with open('analysis_report.json', 'w') as f:
    json.dump(report, f, indent=2)

print("✓ Generated: analysis_report.json")

# Write CSV reports
def write_csv(filename, data, fieldnames):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

write_csv('themes_analysis.csv', theme_report, ['Theme', 'Count', 'Percentage'])
print("✓ Generated: themes_analysis.csv")

write_csv('sources_analysis.csv', sources_report, ['Journal', 'Publications'])
print("✓ Generated: sources_analysis.csv")

write_csv('keywords_analysis.csv', keywords_report, ['Keyword', 'Frequency'])
print("✓ Generated: keywords_analysis.csv")

write_csv('countries_analysis.csv', countries_report, ['Country/Region', 'Affiliations'])
print("✓ Generated: countries_analysis.csv")

# Write text summary
with open('ANALYSIS_SUMMARY.txt', 'w') as f:
    f.write("=" * 80 + "\n")
    f.write("BIBLIOMETRIC ANALYSIS: SUSTAINABLE SUPPLY CHAIN MANAGEMENT\n")
    f.write("=" * 80 + "\n\n")
    f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    f.write("EXECUTIVE SUMMARY\n")
    f.write("-" * 80 + "\n\n")
    
    f.write(f"Dataset Scope:\n")
    f.write(f"  • Total Publications: {len(data):,}\n")
    f.write(f"  • Year Range: {min(years)} - {max(years)}\n")
    f.write(f"  • Unique Sources: {len(set(sources))}\n")
    f.write(f"  • Unique Authors: {len(set(authors_list))}\n\n")
    
    f.write(f"Publication Metrics:\n")
    f.write(f"  • Average Citations: {avg_citations:.2f}\n")
    f.write(f"  • Highly Cited (>10): {highly_cited}\n")
    f.write(f"  • Open Access: {oa_pct:.1f}%\n\n")
    
    f.write(f"Top Research Theme: {top_theme[0]}\n")
    f.write(f"Leading Journal: {top_journal[0]}\n")
    f.write(f"Most Common Keyword: {top_keyword[0]}\n")
    f.write(f"Leading Country: {top_country[0]}\n\n")
    
    f.write("RESEARCH THEMES\n")
    f.write("-" * 80 + "\n\n")
    for i, (theme, count) in enumerate(sorted(theme_counts.items(), key=lambda x: x[1], reverse=True), 1):
        pct = (count / len(data)) * 100
        f.write(f"{i:2d}. {theme}: {count} ({pct:.1f}%)\n")
    
    f.write("\n\nTOP 20 KEYWORDS\n")
    f.write("-" * 80 + "\n\n")
    for i, (keyword, count) in enumerate(keyword_freq.most_common(20), 1):
        f.write(f"{i:2d}. {keyword}: {count}\n")
    
    f.write("\n\nTOP 15 SOURCES\n")
    f.write("-" * 80 + "\n\n")
    for i, (source, count) in enumerate(source_freq.most_common(15), 1):
        f.write(f"{i:2d}. {source}: {count}\n")
    
    f.write("\n\nTOP 15 COUNTRIES/REGIONS\n")
    f.write("-" * 80 + "\n\n")
    for i, (country, count) in enumerate(country_freq.most_common(15), 1):
        f.write(f"{i:2d}. {country}: {count}\n")

print("✓ Generated: ANALYSIS_SUMMARY.txt")

print("\n" + "=" * 80)
print("✓ ANALYSIS COMPLETE")
print("=" * 80)
print("\nGenerated Files:")
print("  1. analysis_report.json - Complete structured report")
print("  2. themes_analysis.csv - Research themes breakdown")
print("  3. sources_analysis.csv - Top publications sources")
print("  4. keywords_analysis.csv - Keyword frequency analysis")
print("  5. countries_analysis.csv - Geographic distribution")
print("  6. ANALYSIS_SUMMARY.txt - Executive summary")
print("\n" + "=" * 80 + "\n")
