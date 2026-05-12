# NOTION CONFIGURATION

## Database: Product Discovery — Scout Findings

### Database Fields
| Field | Type | Options |
|-------|------|---------|
| Product Name | Title | — |
| Category | Select | Beauty, Health, Home, Fitness, Kitchen, Pet, Tech, Other |
| Score | Number | 0–100 |
| Recommendation | Select | High Priority, Worth Testing, Medium Potential, Rejected |
| Problem Solved | Text | concise, 1 sentence |
| Emotional Trigger | Text | 1–3 words |
| Why It May Work | Text | 2–3 bullet points |
| Price Range | Select | Fits $39–79, Too Cheap, Too Expensive |
| Competitor Ads | Checkbox | — |
| Competitor Ad Platform | Text | Meta / TikTok / Both |
| Creative Angles Count | Number | 1–5+ |
| Saturation | Select | Low, Medium, High, Extreme |
| Supplier | Text | Alibaba / AliExpress / verified |
| Source | Text | where found |
| Date Added | Date | — |
| Status | Select | New, Under Review, Testing, Rejected, Winner |

## Formatting Rules
- Scannable in under 10 seconds per entry
- No paragraphs — bullets only
- Always fill Score, Recommendation, Status
- High Priority products: add red tag

## Views to Create
1. All Products (sorted by score, desc)
2. High Priority Only (filter: Recommendation = High Priority)
3. Worth Testing (filter: Recommendation = Worth Testing)
4. By Date (sorted by Date Added, desc)
5. By Category (grouped by Category)
