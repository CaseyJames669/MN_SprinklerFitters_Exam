# MN Sprinkler Fitters Exam Study Guide

A comprehensive, scripted dataset of questions and answers for studying for the Minnesota Sprinkler Fitters Exam. This project sources material from NFPA standards and Minnesota state codes, then cleans, processes, and formats it for various study applications, including a web-based quiz app and an interactive mind map.

---

## Project Structure

The repository is organized into the following directories:

- **`/src/`**: Contains the source code for the web application.
- **`/scripts/`**: Houses all Python scripts used for the data processing pipeline.
- **`/data/`**: Contains the JSON data files, separated into `raw/` and `processed/` subdirectories.
- **`/reference/`**: Stores the raw source material (the "PDF Study Guide"), including `nfpa/` and `minnesota/` codes and standards.
- **`/output/`**: Holds the generated output files, such as formatted text for Quizlet or data for the mind map.
- **`/visualization/`**: Contains the HTML, CSS, and JavaScript for the interactive mind map.
- **`/docs/`**: Includes project documentation.
- **`/archive/`**: Stores archived files, such as saved web pages, that are not part of the main data flow but are preserved for reference.

Other important files in the root directory:

- **`JSON Analysis.md`**: A detailed report on the structure, integrity, and quality of the JSON data.

---

## Data Flow & Usage

The project's workflow takes raw data, processes it through a series of Python scripts, and generates clean, usable study guides and applications.

**1. Source Materials & Raw Data**
- The process begins with the source documents in `/reference/` and the initial dataset in `/data/raw/`.

**2. Initial Processing**
- The scripts in `/scripts/` are used to clean, validate, and enhance the raw data, resulting in `Quizlet Full - Enhanced.json`.

**3. AI-Powered Verification**
- The `Quizlet Full - Enhanced.json` file is manually processed using the Grok4 AI model to generate `Grok4 accuracy verification results.json`. This file contains the original data along with AI-suggested corrections.

**4. Applying Corrections**
- The `scripts/apply_corrections.py` script takes the verification file and programmatically applies the corrections to create the final, canonical dataset: `Grok4 applied corrections.json`.

**5. Generating Outputs**
- Other scripts in the `/scripts/` directory use the final, corrected data to generate various outputs, such as the Quizlet import file (`output/Quizlet Full - CorrectedImport.txt`) and the data for the mind map.

**6. Applications**
- **Web App:** The Flask application in `/src/web_app/` serves the processed data as an interactive quiz.
- **Mind Map:** The files in `/visualization/` create an interactive mind map of the study material.

---

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages (see `requirements.txt`)

### Usage

To run the web application:

```bash
python src/web_app/app.py
```

To regenerate the processed data, run the relevant scripts from the `/scripts/` directory.

---

## Interactive Mind Map

✨ **Explore the dataset interactively as a mind map, hosted on GitHub Pages:**

**[Launch Interactive Mind Map](http.caseyjames669.github.io/MN_SprinklerFitters_Exam/visualization/)**

---

## Fire Sprinkler Code References
| ID | Original Answer/Source | Verified (Yes/No) | Correction (if any) | Verification Method/Tools Used |
|---|---|---|---|---|
-------
| 0 | Annually or after each operation (NFPA 25 2023 Edition, Section 7.3.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 1 | Residential occupancies up to and including four stories in height (NFPA 13R 2022 Edition, Section 1.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 2 | 130 square feet (NFPA 13 2025 Edition, Table 11.2.3.1.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 3 | 225 square feet (NFPA 13 2025 Edition, Table 11.2.3.1.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 4 | 100-130 square feet (NFPA 13 2025 Edition, Table 11.2.3.1.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 5 | 100 square feet (NFPA 13 2025 Edition, Section 29.3.2) | No | Corrected Answer: 100 square feet. Corrected Source: NFPA 13 2025 Edition, Table 17.2.3.1. Reasoning: Section 29.3.2 is about acceptance tests; coverage is in Table 17.2.3.1 for ESFR. Verified via web_search 'NFPA 13 2025 ESFR coverage area', snippet from nfpa.org blog on 2025 edition changes confirming 100 sq ft max for K-16.8 ESFR. | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 6 | 100 or 130 square feet (NFPA 13 2025 Edition, Tables 18.1(a)-(d)) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 7 | 75 psi (NFPA 20 2022 Edition, Section 4.32.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 8 | 1" for horizontal runs up to 20'; 1¼" for 20' to 80'; 1½" for runs over 80' (NFPA 14 2022 Edition, Table 7.3.1.1) | No | Corrected Answer: 1" for up to 100 ft; 1 1/4" for up to 150 ft; 1 1/2" for up to 200 ft. Corrected Source: NFPA 14 2022 Edition, Table 7.3.1.1. Reasoning: The lengths are incorrect; table shows different lengths for pipe sizes. Verified via web_search 'NFPA 14 2022 Table 7.3.1.1 hose lines pipe sizes', snippet from NFPA link confirming 1" up to 100 ft, etc. | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 9 | Ordinary: Orange/Red; Intermediate: Yellow/Green; High: Blue; Extra High: Purple (NFPA 13 2025 Edition, Table 7.2.4.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 10 | False (Minnesota State Fire Code 2020, Section 903.4) | No | Corrected Answer: True | Corrected Source: Minnesota State Fire Code 2020, Section 903.4, Exception 2 | Reasoning: The statement is true; limited area systems with <20 sprinklers are exempt from electrical supervision (monitoring). Locking is not mandatory if not supervised. Verified via web_search 'Minnesota State Fire Code 2020 Section 903.4 control valves supervision exception', snippet from dps.mn.gov confirming exception for <20 sprinklers. No 2025 update found in search. | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 11 | Every 5 years; every 3 years without corrosion protection (NFPA 25 2023 Edition, Section 9.3.5) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 12 | 5 years (NFPA 25 2023 Edition, Section 6.3.2.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 13 | 10 (NFPA 13 2025 Edition, Section 8.3.3.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 14 | 1": 3'; 1¼": 4'; 1½"+: 5' (NFPA 13 2025 Edition, Section 18.5.5.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 15 | 7-10 minutes for one/two-family dwellings (NFPA 13D 2022 Edition, Section 6.5.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 16 | To prevent evaporation of priming water into system (NFPA 13 2025 Edition, Section 8.3.2.3) | No | Corrected Answer: To allow for drainage of condensation and to prevent false trips | Corrected Source: NFPA 13 2025 Edition, Section 8.3.2.3 | Reasoning: The reason is to drain condensation above the dry valve; the file's answer is incorrect. Verified via web_search 'NFPA 13 check valve with hole in clapper freezer', snippet from NFPA confirming for drainage to prevent freezing. | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 17 | 5 minutes (NFPA 13 2025 Edition, Section 8.17.1.5) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 18 | 50 gpm at system pressure (NFPA 14 2022 Edition, Section 7.10.1.2.1) | No | Corrected Answer: 100 gpm @ 65 psi | Corrected Source: NFPA 14 2022 Edition, Section 7.10.1.2.1 | Reasoning: For Class II (occupant use with 1.5" hose), it's 100 gpm @ 65 psi. The file has 50 gpm, which is incorrect. Verified via web_search 'NFPA 14 1.5 inch hose stations pressure flow', snippet confirming 100 gpm @ 65 psi for Class II. | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 19 | 250 gpm @ 100 psi (NFPA 14 2022 Edition, Section 7.6) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 20 | 100 gpm @ 65 psi (NFPA 14 2022 Edition, Section 7.6.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 21 | Hydro test, air test, alarm test (NFPA 13 2025 Edition, Chapter 29) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 22 | At least 250 gpm (NFPA 14 2022 Edition, Section 3.3.17) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 23 | 8 hours, 2" diameter (NFPA 22 2023 Edition, Section 14.2.11) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 24 | 5 seconds (NFPA 13 2025 Edition, Section 16.9.5.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 25 | To prevent air pockets (NFPA 20 2022 Edition, Section 4.15.6.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 26 | Frame arms typically chrome/brass; temp by bulb (NFPA 13 2025 Edition, no frame color code) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 27 | Up to 50% (Minnesota State Fire Code 2020, Section 906.1) | No | Corrected Answer: 100% if hose stations are provided in accordance with Section 905 | Corrected Source: Minnesota State Fire Code 2020, Section 906.1 Exception | Reasoning: The code allows omission of extinguishers where hose stations are provided. The file has 'up to 50%', which is incorrect. Verified via web_search 'Minnesota State Fire Code 2020 Section 906.1 extinguishers hose lines', snippet confirming exception for hose stations. | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 28 | Rack storage (NFPA 13 2025 Edition, Chapter 25) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 29 | Aluminum or other pipe not listed (NFPA 13D 2022 Edition, Section 5.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 30 | When pressures exceed 175 psi (NFPA 13 2025 Edition, Section 10.3.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 31 | System acceptance (NFPA 13 2025 Edition, Section 29.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 32 | Systems connected to non-potable water supplies (NFPA 13 2025 Edition, Section 8.16.4.2) | No | Corrected Answer: For pendent sprinklers on dry systems | Corrected Source: NFPA 13 2025 Edition, Section 8.4.7 | Reasoning: Return bends are for pendent sprinklers on dry systems to prevent sediment trapping. The file's answer is incorrect. Verified via web_search 'NFPA 13 return bends use', snippet confirming for dry pendent. | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 33 | Increaser couplings (NFPA 13 2025 Edition, Section 18.5.3.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 34 | K-5.6 or listed (NFPA 17A 2024 Edition, Section 4.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 35 | Ordinary (NFPA 13 2025 Edition, Section 7.3.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
-------
| 36 | Sloped ceilings or ceilings that aren't flat (NFPA 13 2025 Edition, Section 12.1.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 37 | All but single-story buildings that are less than 2000 sq ft (NFPA 13R 2022 Edition, Section 6.6.4) | No | Corrected Answer: Yes, except for systems with less than 20 sprinklers | Corrected Source: NFPA 13R 2022 Edition, Section 6.6.4 | Reasoning: FDC required unless the system has less than 20 sprinklers or is in a single-story building <2000 sq ft. The file is partially correct but incomplete. Verified via web_search 'NFPA 13R FDC requirements', snippet confirming exceptions. | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 38 | Yes (NFPA 20 2022 Edition, Section 4.12.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 39 | 1":2, 1¼":3, 1½":5, 2":10, etc. (NFPA 13 2025 Edition, Schedule Tables) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
-------
| 40 | 60 seconds (NFPA 13 2025 Edition, Section 8.3.3.7) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 41 | 1"/1¼":12', 1½"-8":15' (NFPA 13 2025 Edition, Table 18.4.1(a)) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 42 | 12' (NFPA 13 2025 Edition, Table 18.4.1(a)) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 43 | ¾"-1":8', 1¼"-1½":10', 2"-3":12', 3.5"-8":15' (NFPA 13 2025 Edition, Table 18.4.1(b)) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 44 | ¾":5'6", 1":6', 1¼":6'6", 1½":7', 2":8', 2½":9', 3":10' (NFPA 13 2025 Edition, Table 18.4.1(c)) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 45 | 25 feet (NFPA 13 2025 Edition, Section 18.5.6.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 46 | Within 24" (NFPA 13 2025 Edition, Section 18.5.3.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 47 | Between dry pipe valve and control valve (NFPA 13 2025 Edition, Section 16.12.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 48 | High if within 7' radius (NFPA 13 2025 Edition, Table 7.3.2.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 49 | Annually (NFPA 25 2023 Edition, Section 5.2.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 50 | 130 ft hose reach (NFPA 14 2022 Edition, Section 7.3.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 51 | 299M (MN Statutes Chapter 299M) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 52 | Misdemeanor, up to $1,000/90 days (MN Statutes 609.02 Subd. 3; 299M) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 53 | 52,000 sq ft (NFPA 13 2025 Edition, Section 5.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 54 | 52,000 sq ft (NFPA 13 2025 Edition, Section 5.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 55 | 40,000 sq ft for hydraulically calculated systems and 20,000 sq ft for scheduled systems (NFPA 13 2025 Edition, Section 5.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 56 | 40,000 sq ft (NFPA 13 2025 Edition, Section 5.5) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 57 | OS&Y valve (NFPA 20 2022 Edition, Section 4.16) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 58 | Listed check or backflow then an indicating valve (NFPA 20 2022 Edition, Section 4.17) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 59 | Must not (NFPA 13 2025 Edition, Section 10.3.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 60 | ½" per 10 feet for mains and lines (NFPA 13 2025 Edition, Section 8.2.2.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 61 | 1 inch (NFPA 13 2025 Edition, Section 8.2.3.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 62 | Single and two-family dwellings (NFPA 13D 2022 Edition, Section 1.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 63 | No (NFPA 13D 2022 Edition, Section 5.5) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 64 | Up to 12" (NFPA 13 2025 Edition, Section 11.2.5.2.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 65 | Light hazard (NFPA 13 2025 Edition, Section 4.3.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 66 | 12 feet (NFPA 13 2025 Edition, Table 18.4.1(a)) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 67 | 3 feet (NFPA 13 2025 Edition, Section 14.2.4.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 68 | Preaction system (NFPA 13 2025 Edition, Section 3.3.19) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 69 | Detection system must be activated (NFPA 13 2025 Edition, Section 8.3.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 70 | 40°F (4°C) or above (NFPA 20 2022 Edition, Section 4.32.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 71 | True (NFPA 13 2025 Edition, Section 18.5.3.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 72 | 60 minutes (NFPA 13 2025 Edition, Section 13.1.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 73 | 175 psi or 10 psi over maximum system pressure (NFPA 13 2025 Edition, Section 8.1.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 74 | June 30th (MN Rules 7512.0200 Subp. 2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 75 | Local Health Department (NFPA 13 2025 Edition, Section 5.3.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 76 | 7 psi (NFPA 13 2025 Edition, Section 7.5.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 77 | Ductile iron pipe allowed if listed (NFPA 14 2022 Edition, Section 5.1.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 78 | When there is more than 20 heads (NFPA 13 2025 Edition, Section 8.17.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 79 | 5.6 or 8.0 K factor (NFPA 13 2025 Edition, Section 21.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 80 | 18" (NFPA 13 2025 Edition, Section 11.1.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 81 | 18" (MN Rules 7512.0100 Subp. 36) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 82 | 18" and 48" (MN Fire Code 2020, Section 912.2.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 83 | Monthly (NFPA 25 2023 Edition, Section 9.3.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 84 | Quarterly (NFPA 25 2023 Edition, Section 6.2.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 85 | Quarterly (NFPA 25 2023 Edition, Section 13.3.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 86 | Quarterly (NFPA 25 2023 Edition, Section 13.8.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 87 | Monthly (NFPA 96 2024 Edition, Section 12.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 88 | Diesel = Weekly for a minimum of 30-minute run time Electric = Weekly for a minimum of 10-minute run time Steam = Weekly (NFPA 25 2023 Edition, Section 8.3.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 89 | Up to 2": ¾"; 2½" to 3½": 1¼"; 4" and larger: 2" (NFPA 13 2025 Edition, Table 29.2.1.15) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 90 | 30 minutes (NFPA 13 2025 Edition, Section 8.2.6.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 91 | Farthest head from the riser (NFPA 13 2025 Edition, Section 27.2.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 92 | Remote end head (NFPA 13 2025 Edition, Section 27.2.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 93 | 4 continuous heads (NFPA 13 2025 Edition, Section 27.2.4.6) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 94 | 3' to 5' (NFPA 14 2022 Edition, Section 7.3.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 95 | When they are constantly attended (NFPA 13 2025 Edition, Section 16.9.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 96 | Intermediate or high temperature (NFPA 13 2025 Edition, Table 7.3.2.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 97 | Max ceiling temp = 150°F Temperature rating = 175°F to 225°F (NFPA 13 2025 Edition, Table 7.3.2.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 98 | At least ⅔ full (NFPA 25 2023 Edition, Section 9.3.4.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 99 | Steel - 1 foot Copper - 6" CPVC - 6" (NFPA 13 2025 Edition, Section 18.5.5.10) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 100 | Yes (NFPA 14 2022 Edition, Section 9.1.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 101 | ½" per 10 feet for mains ¼" per 10 feet for branch lines (NFPA 13 2025 Edition, Section 8.2.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 102 | Single head design = 18 gpm Two head design = 13 gpm (NFPA 13D 2022 Edition, Section 11.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 103 | 12 feet or 144 sq ft (NFPA 13D 2022 Edition, Section 10.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 104 | 4" (NFPA 13 2025 Edition, Section 18.5.9.6) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 105 | Blue (NFPA 13 2025 Edition, Table 7.2.4.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 106 | 8 feet (NFPA 13D 2022 Edition, Section 10.2.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 107 | A. Bathrooms less than 55 sq ft B. Closets less than 24 sq ft and least dimension under 3 feet C. Porches and balconies D. Attics and concealed spaces (NFPA 13R 2022 Edition, Section 6.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 108 | ½ inch (NFPA 13 2025 Edition, Table 18.5.9.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 109 | 100 feet (NFPA 14 2022 Edition, Section 7.3.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 110 | Intermediate (NFPA 13 2025 Edition, Table 7.3.2.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 111 | Up to 3 ft off center (NFPA 13 2025 Edition, Section 12.1.1.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 112 | <24 sq ft and <3 ft dim (NFPA 13 2025 Edition, Section 9.5.5.13) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 113 | Every 40 feet (NFPA 13 2025 Edition, Section 18.5.10.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 114 | No max specified (NFPA 13 2025 Edition, Section 16.12.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 115 | 0-299 heads = 6 spare heads 300-999 heads = 12 spare heads 1000+ heads = 24 spare heads (NFPA 13 2025 Edition, Section 7.3.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 116 | At least six (NFPA 20 2022 Edition, Section 14.2.5) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 117 | 6" but not <2" (NFPA 22 2023 Edition, Section 5.3.1) | No | Corrected Answer: The size of the discharge pipe or pipes shall be such that the velocity of water flow shall not exceed values given in Table 5.3.1 for the available storage listed. Corrected Source: NFPA 22 2023 Edition, Section 5.3.1. Reasoning: The answer is not accurate; it's about velocity limits, not a fixed size. Verified via web_search 'NFPA 22 2023 Section 5.3.1 tank discharge size', snippet confirming velocity table, no '6" but not <2"'. | web_search and browse_page on nfpa.org and dps.mn.gov |
| 118 | 8 inches (NFPA 13 2025 Edition, Section 9.5.3.1.5) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 119 | >36" equal space (NFPA 13 2025 Edition, Section 11.1.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 120 | Uprights, sidewalls no trap, listed dry, return bends (NFPA 13 2025 Edition, Section 8.4.8) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 121 | 3 psi max loss in 24 hrs at 40 psi (NFPA 13 2025 Edition, Section 29.2.1.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 122 | None NFPA 13; 40 gal 13D/13R (NFPA 13 2025 Edition, Section 5.3.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 123 | Hazen Williams (Standard hydraulic method) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 124 | Water-filled +250 lbs (NFPA 13 2025 Edition, Section 18.1.1.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 125 | At least 2 (NFPA 13 2025 Edition, Section 16.13) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 126 | Up to max four (NFPA 13R 2022 Edition, Section 11.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 127 | Unobstructed <800 sq ft enclosed (NFPA 13 2025 Edition, Section 11.1.7) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 128 | 40 feet (NFPA 24 2022 Edition, Section 6.3.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 129 | UFC, IBC, IFC (Various jurisdictions) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 130 | 80 sq ft (NFPA 13 2025 Edition, Table 17.2.3.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 131 | A copy of NFPA 25, data sheets, and instructions for proper operation and maintenance (NFPA 13 2025 Edition, Section 29.6) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 132 | 1 inch (NFPA 20 2022 Edition, Section 4.13) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 133 | 8 max light hazard (NFPA 13 2025 Edition, Figure 11.1.1.2.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 134 | 20 (NFPA 13 2025 Edition, Section 16.12.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 135 | Relies on pressure boost from fire department pumper truck via FDC (NFPA 14 2022 Edition, Section 3.3.18) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 136 | Glycerin (NFPA 13 2025 Edition, Section 5.3.3.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 137 | 32-40" (NFPA 24 2022 Edition, Section 6.3.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 138 | 4 inch (NFPA 14 2022 Edition, Section 5.4.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 179 | Brass, copper, or stainless steel ½" (NFPA 20 2022 Edition, Section 4.32) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 180 | ⅝" (NFPA 13 2025 Edition, Table 18.5.12.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 181 | 18 inches (NFPA 14 2022 Edition, Section 9.1.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 182 | 4" for completely sprinkled buildings otherwise 6" (NFPA 14 2022 Edition, Section 5.4.1.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 183 | 1¼" (NFPA 14 2022 Edition, Table 6.3.1.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 184 | 6" under/around; 2 ft above (NFPA 24 2022 Edition, Section 10.9) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 185 | Intermediate or high temperature (NFPA 13 2025 Edition, Table 7.3.2.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 186 | 15 psi (NFPA 13 2025 Edition, Section 27.2.4.6.5) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 187 | Varies by arrangement (NFPA 13 2025 Edition, Section 25.9) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 188 | 18" (NFPA 13 2025 Edition, Section 11.1.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 189 | 1" to 4" (NFPA 13D 2022 Edition, Section 10.3.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 190 | 2 feet (NFPA 22 2023 Edition, Section 4.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 191 | 5 sprinkler heads (NFPA 13 2025 Edition, Schedule) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 192 | 15 psi (Calculation per NFPA 13 2025 Edition, Section 8.2.3.7) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 193 | 10 psi (NFPA 13 2025 Edition, Section 8.1.2.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 194 | 175 psi, 150 psi (NFPA 13 2025 Edition, Section 6.1.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 195 | 175 psi (NFPA 13 2025 Edition, Section 27.2.4.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 196 | 15 psi (NFPA 13 2025 Edition, Section 27.2.4.6.5) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 197 | 8000 (MN Statutes 299M) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 198 | 13 (NFPA 13 2025 Edition) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 199 | 13D (NFPA 13D 2022 Edition) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 200 | 13R (NFPA 13R 2022 Edition) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 201 | 14 (NFPA 14 2022 Edition) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 202 | 24 (NFPA 24 2022 Edition) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 203 | 25 (NFPA 25 2023 Edition) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 204 | 20 (NFPA 20 2022 Edition) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 205 | 22 (NFPA 22 2023 Edition) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 206 | 72 (NFPA 72 2024 Edition) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 207 | 96 (NFPA 96 2024 Edition) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 208 | 17A (NFPA 17A 2024 Edition) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 209 | Class I (NFPA 14 2022 Edition, Section 4.1.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 210 | Class II (NFPA 14 2022 Edition, Section 4.1.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 211 | Class III (NFPA 14 2022 Edition, Section 4.1.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 212 | 80 inches (10x diameter) (NFPA 20 2022 Edition, Section 4.15.3.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 213 | Not Allowed (NFPA 13 2025 Edition, no provision) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 214 | Concentric Reducer (NFPA 20 2022 Edition, Section 4.15.6.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 215 | Dry System (NFPA 13 2025 Edition, Section 17.17.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 216 | 40°F (NFPA 13 2025 Edition, Section 5.4.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 217 | No (NFPA 13 2025 Edition, Section 17.17.1.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 218 | 3 inches (NFPA 13 2025 Edition, Section 10.3.5.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 219 | Parallel (NFPA 13 2025 Edition, Section 10.2.6) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 220 | False (NFPA 20 2022 Edition, Section 10.3.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 221 | 10 psi (NFPA 13 2025 Edition, Section 8.1.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 222 | 1/2 inch (NFPA 13 2025 Edition, Section 16.10.5.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 223 | Condensate ¾" (NFPA 13 2025 Edition, Section 8.16.2.5.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 224 | 1 inch (NFPA 13 2025 Edition, Section 8.16.2.5.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 225 | 24 hours (NFPA 13 2025 Edition, Section 29.2.1.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 226 | 28 inches (NFPA 13D 2022 Edition, Section 6.2.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 227 | False (MN Fire Code 2020, Section 903.3.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 228 | Deluge (NFPA 13 2025 Edition, Section 3.3.15) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 229 | longer time (NFPA 13 2025 Edition, A.7.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 230 | 4 ft (NFPA 13 2025 Edition, Section 14.2.4.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 231 | 2 ft (NFPA 13 2025 Edition, Section 12.1.1.3.9) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 232 | high (NFPA 13 2025 Edition, Table 7.3.2.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 233 | intermediate (NFPA 13 2025 Edition, Table 7.3.2.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 234 | 225 sq ft (NFPA 13 2025 Edition, Table 11.2.3.1.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 235 | 6 (NFPA 13 2025 Edition, Table 7.3.1.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 236 | 12 (NFPA 13 2025 Edition, Table 7.3.1.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 237 | 24 (NFPA 13 2025 Edition, Table 7.3.1.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 238 | location (NFPA 13 2025 Edition, Section 5.4.1.5) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 239 | 3" (NFPA 13 2025 Edition, Section 16.12.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 240 | 5 minutes (NFPA 13 2025 Edition, Section 17.17) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 241 | 90 seconds (NFPA 72 2024 Edition, Section 17.13.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 242 | 3 (NFPA 13 2025 Edition, Section 8.3.3.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 243 | 1000 (NFPA 13 2025 Edition, Section 8.3.2.9) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 244 | 52,000 sq ft (NFPA 13 2025 Edition, Section 5.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 245 | Intermediate (NFPA 13 2025 Edition, Table 7.3.2.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 246 | 225-300°F (NFPA 13 2025 Edition, Table 7.2.4.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 247 | 135-170°F (NFPA 13 2025 Edition, Table 7.2.4.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 248 | 3 inches (NFPA 13 2025 Edition, Section 10.2.6.1.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 249 | 4 ft (NFPA 13 2025 Edition, Section 13.2.8.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 250 | 3 in (NFPA 13 2025 Edition, Section 13.2.8.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 251 | 32 (NFPA 13 2025 Edition, Section 9.3.16) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 252 | 10 (NFPA 13 2025 Edition, Section 9.3.16) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 253 | 400 sq ft (NFPA 13 2025 Edition, Table 11.2.3.1.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 254 | 225 sq ft (NFPA 13 2025 Edition, Table 11.2.3.1.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 255 | 130 (NFPA 13 2025 Edition, Table 11.2.3.1.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 256 | 4 in (NFPA 13 2025 Edition, Section 10.2.5.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 257 | 6 ft (NFPA 13 2025 Edition, Section 10.2.5.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 258 | 1 to 12 in (NFPA 13 2025 Edition, Section 10.2.6.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 259 | 60 (NFPA 13 2025 Edition, Section 13.2.9.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 260 | 18 in (NFPA 13 2025 Edition, Section 9.5.5.2) | No | Corrected Answer: 18" clearance. Corrected Source: NFPA 13 2025 Edition, Section 9.5.5.2. Reasoning: The answer is about clearance, not sq ft size. The file has '___ sq ft in size', but it's 18" clearance from top of storage to sprinkler deflector. Verified via web_search. | web_search and browse_page on nfpa.org and dps.mn.gov |
| 261 | 1000 (NFPA 13 2025 Edition, Section 9.3.17) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 262 | 6 (NFPA 13 2025 Edition, Section 10.3.4.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 263 | 24 ft (NFPA 13 2025 Edition, Section 10.3.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 264 | Ball valve (NFPA 13 2025 Edition, Section 16.9.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 265 | True (NFPA 13 2025 Edition, Section 16.15.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 266 | 1/2 in (NFPA 13 2025 Edition, Section 16.11) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 267 | 32-40 inches (NFPA 24 2022 Edition, Section 6.3.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 268 | 20 (NFPA 13 2025 Edition, Section 25.9.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 269 | 3/4" (NFPA 13 2025 Edition, Section 16.10.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 270 | 1 1/4" (NFPA 13 2025 Edition, Section 16.10.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 271 | 2" (NFPA 13 2025 Edition, Section 16.10.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 272 | 1" (NFPA 13 2025 Edition, Section 16.10.5) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 273 | 1" (MN Fire Code 2020, Section 912.5) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 274 | 1/4" (NFPA 13 2025 Edition, Section 16.13) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 275 | 6 ft (NFPA 13 2025 Edition, Section 18.4.8.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 276 | 1 in (NFPA 13 2025 Edition, Section 18.5.7.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 277 | 1 1/2" (NFPA 13 2025 Edition, Section 18.5.7.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 278 | 6 ft (NFPA 13 2025 Edition, Section 18.5.5.6) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 279 | 36 in (NFPA 13 2025 Edition, Section 18.5.5.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 280 | 48 in (NFPA 13 2025 Edition, Section 18.5.5.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 281 | 60 in (NFPA 13 2025 Edition, Section 18.5.5.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 282 | 18 in (NFPA 13 2025 Edition, Section 18.5.5.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 283 | 24 in (NFPA 13 2025 Edition, Section 18.5.5.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 284 | 30 in (NFPA 13 2025 Edition, Section 18.5.5.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 285 | 24 in (NFPA 13 2025 Edition, Section 18.5.5.9) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 286 | 12 in (NFPA 13 2025 Edition, Section 18.5.5.9) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 287 | 12 ft (NFPA 13 2025 Edition, Table 18.4.1(a)) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 288 | 12 ft (NFPA 13 2025 Edition, Table 18.4.1(a)) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 289 | 15 ft (NFPA 13 2025 Edition, Table 18.4.1(a)) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 290 | 15 ft (NFPA 13 2025 Edition, Table 18.4.1(a)) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 291 | Lowest level and every other floor (NFPA 14 2022 Edition, Section 9.1.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 292 | 2" (NFPA 13 2025 Edition, Table 18.4.10.1) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 293 | 18 and 48 (MN Fire Code 2020, Section 912.2.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 294 | ≤2/12 (NFPA 13 2025 Edition, Section 3.3.22) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 295 | 40 psi 24 hrs ≤3 psi loss (NFPA 25 2023 Edition, Section 13.5.1.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 296 | anti-vortex plate (NFPA 22 2023 Edition, Section 8.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 297 | 6 (NFPA 22 2023 Edition, Section 8.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 298 | Listed (NFPA 13 2025 Edition, Section 7.4.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 299 | 5 sec (NFPA 13 2025 Edition, Section 16.9.5.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 300 | 3" (NFPA 13 2025 Edition, Section 16.12.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 301 | 6 (NFPA 13 2025 Edition, Section 8.2.3.3) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 302 | 1" steel, ¾" plastic (NFPA 13D 2022 Edition, Section 6.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 303 | 100 ft (NFPA 14 2022 Edition, Section 6.4.5.4) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 304 | 800 (NFPA 13 2025 Edition, Section 3.3.199) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
| 305 | 130 (NFPA 13 2025 Edition, Table 11.2.3.1.2) | Yes | None | web_search and browse_page on nfpa.org and dps.mn.gov |
