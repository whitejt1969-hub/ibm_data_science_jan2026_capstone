# Module 9: Data Collection, Wrangling, EDA & Capstone (SpaceX)

**Author:** Alexander Booth  
**Date:** April 2026  
**Cohort:** IBM-IBSC Jan 28, 2026

---

## Overview

This module is the **project-oriented bridge** from raw information to analysis-ready data for the **SpaceX / “Space Y” capstone scenario**: you **collect** launch data (API and web), **wrangle** it into a consistent tabular form, and perform **exploratory data analysis (EDA)**—including work in **SQL/SQLite**—to understand what drives **first-stage landing success** and reuse.

The core threads:

* **Version control with Git and GitHub** — Why repositories matter for coursework and projects, and how to get started with GitHub in the bootcamp workflow.
* **Data collection** — **REST APIs** (SpaceX `v4` endpoints), **JSON** responses, **flattening** nested structures into DataFrames, and **web scraping** HTML tables with **Beautiful Soup**.
* **Data wrangling** — Enriching IDs via additional endpoints, **filtering** to Falcon 9, handling **nulls** (for example payload mass), and encoding outcomes for downstream modeling.
* **Exploratory data analysis** — Querying and summarizing data in a **database**, visual patterns (launch site, mass, trends over time), **correlation** thinking, and **one-hot encoding** categorical fields for ML prep.

---

## Why This Module Matters

Real projects rarely start with a clean CSV on disk:

* **APIs and scraping** are how you **harvest** data that lives on the web; knowing **requests**, **JSON normalization**, and **HTML parsing** is foundational.
* **Wrangling** turns messy, nested, or incomplete extracts into **one table (or schema)** you can query, plot, and model—this is where many timelines are won or lost.
* **EDA in SQL plus notebooks** mirrors how teams **slice** large or relational data before committing to features and models.

---

## What This Module Covers

### 1. Project Scenario and Business Framing

* **Commercial space and reuse** — Why first-stage recovery matters for **cost** and how predicting **landing success** supports pricing and operations decisions.
* **Capstone narrative** — Acting as a data scientist for a competitor narrative (“Space Y”) using **public SpaceX-oriented data** and dashboards plus ML downstream.

### 2. Collecting Data (API and Web)

* **SpaceX REST API** — Base URL pattern, **past launches** endpoint, **GET** requests with **requests**, and **`.json()`** responses as lists of objects.
* **JSON to tables** — Using **`json_normalize`** (or equivalent) to flatten nested JSON into **pandas**-friendly columns.
* **Web scraping** — **Beautiful Soup** on Wikipedia-style tables, parsing rows into a DataFrame aligned with the API-sourced dataset.

### 3. Data Wrangling

* **Key attributes** — Flight number, date, booster, payload mass, orbit, launch site, outcome, reuse-related fields, landing pad, geolocation, and related identifiers.
* **Enrichment** — When columns hold **IDs** only, **follow-up API calls** (booster, launchpad, payload, core, etc.) to attach meaningful attributes.
* **Sampling and cleaning** — Restricting to **Falcon 9**, imputing or filling **null** payload mass (for example with a **mean**), and preserving meaningful nulls (for example **LandingPad** when unused).
* **Target encoding** — Mapping **landing outcomes** to a **binary class** (failure vs success) for classification.

### 4. Exploratory Data Analysis

* **EDA first** — Summaries and plots before modeling; using a **database** in the first lab and **visual EDA** in the second.
* **Patterns** — Success rates over time, differences by **launch site**, and **combined** effects (for example mass thresholds within a site).
* **Toward modeling** — Identifying attributes associated with successful landings, **correlations**, and **one-hot encoding** of categoricals for ML.

### 5. Git and GitHub (Course Workflow)

* **Concepts** — What **Git** and **GitHub** are and how they support sharing, versioning, and collaboration on notebooks and project assets.

---

## Labs and Notebooks

### 9.03 — GitHub Instructions

* **What are Git and GitHub?** (`9.03 (Github Instructions)/3-dot-1-3-what-are-git-and-github.md`)
* **Getting started with GitHub** (`9.03 (Github Instructions)/Getting_Started_With_Github.pdf`)

### 9.04 — Data Collection and Wrangling (SpaceX)

* **SpaceX data collection via API** (`9.04/jupyter-labs-spacex-data-collection-api.ipynb`)
* **Web scraping launch records** (`9.04/jupyter-labs-webscraping.ipynb`)
* **Data wrangling (JupyterLite-oriented lab)** (`9.04/labs-jupyter-spacex-data wrangling_jupyterlite.ipynb`)

**Supporting data files in `9.04/`:**

* `dataset_part_1.csv`, `dataset_part_2.csv` — Intermediate/partial datasets produced through the collection and wrangling flow.
* `spacex_web_scraped.csv` — Scraped table output for merging or comparison with API data.

### 9.05 — EDA (SQL and Visualization)

* **EDA with SQL (SQLite)** (`9.05/jupyter-labs-eda-sql-edx_sqllite.ipynb`)
* **EDA and visualization** (`9.05/edadataviz.ipynb`)

**Supporting assets in `9.05/`:**

* `dataset_part_3.csv` — Dataset for continued EDA and feature preparation.
* `my_data1.db` — SQLite database used with the SQL EDA notebook.

### 9.07 — Live Session

* Placeholder for live session materials (`9.07 - Live Session/.gitkeep`)

---

## Supporting Materials

### Downloads (Lecture Transcripts / Notes)

Located in `Downloads/`:

* `Data Collection Overview-en.txt`
* `Data Wrangling Overview-en.txt`
* `Exploratory Data Analysis Overview-en.txt`
* `Project Scenario and Overview-en.txt`

---

## Key Takeaways

* **APIs** — Endpoints return **structured JSON**; flatten nested payloads into tables and **join** or enrich when columns are only identifiers.
* **Scraping** — HTML tables are a common source; parse consistently and **reconcile** with API-derived fields before modeling.
* **Wrangling** — **Filter** to the population you care about (Falcon 9), **impute** missing values where justified, and **preserve** meaningful missingness when it carries signal.
* **EDA** — Use **SQL** for aggregation at scale and **notebooks** for visual and multivariate intuition; **encode** categoricals explicitly before ML steps in later modules.
* **GitHub** — Version control keeps your capstone work **reproducible** and **shareable**—adopt it as early as this module.

---

## From Raw Web Data to Modeling-Ready Features

Module 9 is about **closing the gap** between “data lives on the internet” and “I have a defensible feature matrix”: collect, clean, document in Git, explore in SQL and plots—so the **machine learning** stages that follow rest on **data you understand and trust**.
