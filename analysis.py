"""
Bibliometric Analysis of Sustainable Supply Chain Management Research
Dataset: 4441.csv (Scopus publications 2000-2026)

This script performs comprehensive bibliometric analysis on SSCM research trends.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import warnings

warnings.filterwarnings('ignore')

# Set style for visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)

# ============================================================================
# 1. DATA LOADING AND INITIAL EXPLORATION
# ============================================================================

print("=" * 80)
print("BIBLIOMETRIC ANALYSIS: SUSTAINABLE SUPPLY CHAIN MANAGEMENT")
print("=" * 80)

# Load the dataset
df = pd.read_csv('4441.csv', encoding='utf-8-sig')

print(f"\n✓ Dataset loaded successfully")
print(f"  - Total records: {len(df)}")
print(f"  - Total columns: {len(df.columns)}")
print(f"\n  Columns: {list(df.columns)}")

# Basic statistics
print("\n" + "=" * 80)
print("DATASET OVERVIEW")
print("=" * 80)

print(f"\nPublication Year Range: {df['Year'].min():.0f} - {df['Year'].max():.0f}")
print(f"Total Publications: {len(df)}")
print(f"Missing Values per Column:")
print(df.isnull().sum())

# ============================================================================
# 2. TEMPORAL TRENDS
# ============================================================================

print("\n" + "=" * 80)
print("TEMPORAL ANALYSIS")
print("=" * 80)

# Publications by year
pub_by_year = df['Year'].value_counts().sort_index()
print(f"\nPublications by Year:")
print(pub_by_year.tail(10))

# Create visualization
fig, ax = plt.subplots(figsize=(14, 6))
pub_by_year.plot(kind='line', marker='o', linewidth=2, markersize=6, ax=ax)
ax.set_title('Publication Trends Over Time: Sustainable Supply Chain Management Research', 
             fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Publications', fontsize=12)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('temporal_trends.png', dpi=300, bbox_inches='tight')
print("\n✓ Visualization saved: temporal_trends.png")

# ============================================================================
# 3. SOURCE ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("SOURCE AND JOURNAL ANALYSIS")
print("=" * 80)

# Top journals/sources
top_sources = df['Source title'].value_counts().head(15)
print(f"\nTop 15 Publication Sources:")
print(top_sources)

fig, ax = plt.subplots(figsize=(12, 8))
top_sources.plot(kind='barh', ax=ax, color='steelblue')
ax.set_title('Top 15 Publication Sources for SSCM Research', fontsize=14, fontweight='bold')
ax.set_xlabel('Number of Publications', fontsize=12)
plt.tight_layout()
plt.savefig('top_sources.png', dpi=300, bbox_inches='tight')
print("✓ Visualization saved: top_sources.png")

# ============================================================================
# 4. DOCUMENT TYPE ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("DOCUMENT TYPE ANALYSIS")
print("=" * 80)

doc_types = df['Document Type'].value_counts()
print(f"\nDocument Types Distribution:")
print(doc_types)

fig, ax = plt.subplots(figsize=(10, 6))
doc_types.plot(kind='pie', autopct='%1.1f%%', ax=ax, startangle=90)
ax.set_title('Distribution by Document Type', fontsize=14, fontweight='bold')
ax.set_ylabel('')
plt.tight_layout()
plt.savefig('document_types.png', dpi=300, bbox_inches='tight')
print("✓ Visualization saved: document_types.png")

# ============================================================================
# 5. KEYWORD ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("KEYWORD ANALYSIS")
print("=" * 80)

# Author Keywords
author_keywords = []
for keywords_str in df['Author Keywords'].dropna():
    if isinstance(keywords_str, str):
        keywords = [k.strip() for k in keywords_str.split(';')]
        author_keywords.extend(keywords)

keyword_freq = Counter(author_keywords)
top_keywords = keyword_freq.most_common(20)

print(f"\nTop 20 Author Keywords:")
for i, (keyword, count) in enumerate(top_keywords, 1):
    print(f"  {i:2d}. {keyword:<50} ({count})")

# Visualize top keywords
keywords_df = pd.DataFrame(top_keywords, columns=['Keyword', 'Frequency'])
fig, ax = plt.subplots(figsize=(12, 8))
keywords_df.sort_values('Frequency').plot(x='Keyword', y='Frequency', kind='barh', ax=ax, legend=False, color='coral')
ax.set_title('Top 20 Author Keywords in SSCM Research', fontsize=14, fontweight='bold')
ax.set_xlabel('Frequency', fontsize=12)
plt.tight_layout()
plt.savefig('top_keywords.png', dpi=300, bbox_inches='tight')
print("✓ Visualization saved: top_keywords.png")

# ============================================================================
# 6. CITATION ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("CITATION ANALYSIS")
print("=" * 80)

# Convert 'Cited by' to numeric, handling any issues
df['Cited by'] = pd.to_numeric(df['Cited by'], errors='coerce')

cited_stats = df['Cited by'].describe()
print(f"\nCitation Statistics:")
print(cited_stats)

# Most cited papers
top_cited = df.nlargest(10, 'Cited by')[['Title', 'Year', 'Authors', 'Cited by']]
print(f"\nTop 10 Most Cited Papers:")
for idx, (i, row) in enumerate(top_cited.iterrows(), 1):
    print(f"\n  {idx}. {row['Title'][:70]}...")
    print(f"     Authors: {str(row['Authors'])[:60]}")
    print(f"     Year: {row['Year']:.0f}, Citations: {row['Cited by']:.0f}")

# ============================================================================
# 7. OPEN ACCESS ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("OPEN ACCESS TRENDS")
print("=" * 80)

oa_stats = df['Open Access'].value_counts()
print(f"\nOpen Access Distribution:")
print(oa_stats)

fig, ax = plt.subplots(figsize=(10, 6))
oa_stats.plot(kind='pie', autopct='%1.1f%%', ax=ax, startangle=90)
ax.set_title('Open Access Distribution', fontsize=14, fontweight='bold')
ax.set_ylabel('')
plt.tight_layout()
plt.savefig('open_access.png', dpi=300, bbox_inches='tight')
print("✓ Visualization saved: open_access.png")

# ============================================================================
# 8. THEMATIC CLUSTERS (Based on Keywords)
# ============================================================================

print("\n" + "=" * 80)
print("RESEARCH THEMES AND CLUSTERS")
print("=" * 80)

# Define theme keywords for clustering
themes = {
    'Green Innovation & Technology': ['green', 'innovation', 'technology', 'ai', 'artificial intelligence', 'blockchain', 'iot'],
    'Circular Economy': ['circular', 'circular economy', 'reverse logistics', 'recycling', 'waste'],
    'Environmental Performance': ['environmental', 'emissions', 'carbon', 'ghg', 'sustainability'],
    'Supply Chain Resilience': ['resilience', 'risk', 'risk management', 'disruption'],
    'Digital Transformation': ['digital', 'digitalization', 'automation', 'industry 4.0'],
    'Procurement & Sourcing': ['procurement', 'supplier', 'sourcing', 'vendor'],
    'Logistics & Distribution': ['logistics', 'distribution', 'transportation', 'warehouse'],
    'Stakeholder Engagement': ['stakeholder', 'collaboration', 'partnership', 'multi-stakeholder'],
}

# Classify articles by theme
theme_counts = {theme: 0 for theme in themes.keys()}

for keywords_str in df['Author Keywords'].dropna():
    if isinstance(keywords_str, str):
        keywords_lower = keywords_str.lower()
        for theme, theme_keywords in themes.items():
            for keyword in theme_keywords:
                if keyword in keywords_lower:
                    theme_counts[theme] += 1
                    break

print(f"\nResearch Theme Distribution:")
for theme, count in sorted(theme_counts.items(), key=lambda x: x[1], reverse=True):
    percentage = (count / len(df)) * 100
    print(f"  {theme:<40} {count:4d} ({percentage:5.1f}%)")

# Visualize themes
theme_df = pd.DataFrame(list(theme_counts.items()), columns=['Theme', 'Count'])
theme_df = theme_df.sort_values('Count', ascending=True)
fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(theme_df['Theme'], theme_df['Count'], color='mediumseagreen')
ax.set_title('Distribution of Research Themes in SSCM Literature', fontsize=14, fontweight='bold')
ax.set_xlabel('Number of Publications', fontsize=12)
plt.tight_layout()
plt.savefig('research_themes.png', dpi=300, bbox_inches='tight')
print("✓ Visualization saved: research_themes.png")

# ============================================================================
# 9. GEOGRAPHIC ANALYSIS (Based on Affiliations)
# ============================================================================

print("\n" + "=" * 80)
print("GEOGRAPHIC ANALYSIS")
print("=" * 80)

# Extract countries from affiliations (simple approach - look for country patterns)
countries_found = []
for aff in df['Affiliations'].dropna():
    if isinstance(aff, str):
        # Extract last part after comma (often the country)
        parts = aff.split(';')
        for part in parts:
            country_part = part.strip().split(',')[-1].strip()
            if len(country_part) > 0:
                countries_found.append(country_part)

country_freq = Counter(countries_found)
top_countries = country_freq.most_common(15)

print(f"\nTop 15 Countries/Regions by Publication Affiliations:")
for i, (country, count) in enumerate(top_countries, 1):
    print(f"  {i:2d}. {country:<50} ({count})")

# Visualize top countries
countries_df = pd.DataFrame(top_countries, columns=['Country', 'Count'])
fig, ax = plt.subplots(figsize=(12, 8))
countries_df.sort_values('Count').plot(x='Country', y='Count', kind='barh', ax=ax, legend=False, color='lightcoral')
ax.set_title('Top 15 Countries/Regions by Publication Affiliations', fontsize=14, fontweight='bold')
ax.set_xlabel('Number of Affiliations', fontsize=12)
plt.tight_layout()
plt.savefig('top_countries.png', dpi=300, bbox_inches='tight')
print("✓ Visualization saved: top_countries.png")

# ============================================================================
# 10. SUMMARY STATISTICS AND KEY FINDINGS
# ============================================================================

print("\n" + "=" * 80)
print("KEY FINDINGS SUMMARY")
print("=" * 80)

print(f"""
📊 Dataset Scope:
   • Total Publications Analyzed: {len(df):,}
   • Year Range: {df['Year'].min():.0f} - {df['Year'].max():.0f}
   • Unique Sources: {df['Source title'].nunique()}
   • Unique Authors: {df['Authors'].nunique()}

📈 Publication Trends:
   • Latest Year Data: {pub_by_year.tail(1).values[0]} publications
   • Average Citations per Paper: {df['Cited by'].mean():.1f}
   • Highly Cited Papers (>10 citations): {(df['Cited by'] > 10).sum()}

📚 Research Landscape:
   • Most Common Document Type: {doc_types.index[0]}
   • Leading Research Theme: {sorted(theme_counts.items(), key=lambda x: x[1], reverse=True)[0][0]}
   • Top Author Keyword: {top_keywords[0][0] if top_keywords else 'N/A'}

🌍 Global Research Activity:
   • Leading Region/Country: {top_countries[0][0] if top_countries else 'N/A'}
   • International Collaboration: {(df['Affiliations'].notna() & (df['Affiliations'].str.contains(';', na=False))).sum()} papers

📖 Open Science:
   • Open Access Publications: {(df['Open Access'].notna() & (df['Open Access'].str.contains('Open Access', na=False))).sum()}
   • Percentage: {((df['Open Access'].notna() & (df['Open Access'].str.contains('Open Access', na=False))).sum() / len(df)) * 100:.1f}%
""")

# ============================================================================
# 11. EXPORT SUMMARY REPORT
# ============================================================================

summary_data = {
    'Metric': [
        'Total Publications',
        'Year Range',
        'Unique Journals',
        'Average Citations',
        'Most Common Theme',
        'Top Country',
        'Leading Document Type'
    ],
    'Value': [
        f"{len(df):,}",
        f"{df['Year'].min():.0f} - {df['Year'].max():.0f}",
        f"{df['Source title'].nunique()}",
        f"{df['Cited by'].mean():.2f}",
        sorted(theme_counts.items(), key=lambda x: x[1], reverse=True)[0][0],
        top_countries[0][0] if top_countries else 'N/A',
        doc_types.index[0]
    ]
}

summary_df = pd.DataFrame(summary_data)
summary_df.to_csv('analysis_summary.csv', index=False)
print("\n✓ Summary exported to: analysis_summary.csv")

print("\n" + "=" * 80)
print("✓ ANALYSIS COMPLETE")
print("=" * 80)
print("\nGenerated Files:")
print("  1. temporal_trends.png - Publication trends over time")
print("  2. top_sources.png - Leading journals/sources")
print("  3. document_types.png - Document type distribution")
print("  4. top_keywords.png - Most frequent author keywords")
print("  5. open_access.png - Open access publication status")
print("  6. research_themes.png - Research theme distribution")
print("  7. top_countries.png - Leading geographic regions")
print("  8. analysis_summary.csv - Summary statistics")
print("\n" + "=" * 80)
