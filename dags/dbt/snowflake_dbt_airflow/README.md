# Snowflake DBT Project

This is a DBT project designed to transform raw data into clean, analytics-ready datasets on Snowflake.

## 📁 Project Structure

```
.
├── analyses/          # One-off analysis SQL files (not part of DAG)
├── dbt_packages/      # Auto-generated packages from dbt deps
├── logs/              # Logs generated during DBT runs
├── macros/            # Custom Jinja macros
├── models/            # Core transformation logic
│   ├── staging/       # Source-aligned raw models (clean + rename)
│   └── marts/         # Final fact/dimension tables for reporting
├── seeds/             # Static CSV files materialized as tables
├── snapshots/         # Historical snapshot models (SCD)
├── tests/             # Custom data quality tests (if needed)
├── .gitignore         # Files/folders ignored by Git
├── dbt_project.yml    # Main DBT project configuration
├── packages.yml       # DBT packages used (e.g., dbt_utils)
├── package-lock.yml   # Lock file for package dependencies
└── README.md          # Project documentation (this file)
```

---

## 📦 DBT Packages

This project uses [`dbt_utils`](https://hub.getdbt.com/dbt-labs/dbt_utils/latest/) for enhanced macros such as:

- `generate_surrogate_key`
- `union_relations`
- `date_spine`
- `pivot` / `unpivot`
- `star`

To install packages:

```bash
dbt deps
```

---

## 🚀 DBT Commands

Here are the most common commands to use this project:

```bash
dbt run            # Run all models
dbt test           # Run all tests
dbt seed           # Load seed CSVs as tables
dbt snapshot       # Apply snapshot logic
dbt docs generate  # Generate project documentation
dbt docs serve     # View documentation in the browser
```

---

## 🔧 Configuration

Edit `dbt_project.yml` to:

- Set project name and version
- Configure model materializations (table/view/incremental)
- Control folder structure
- Enable or disable features (e.g., quoting, persist_docs)

---

## ✅ Best Practices

- Keep staging models 1:1 with source tables
- Use `ref()` for all model dependencies
- Organize marts into `core`, `reporting`, `finance`, etc.
- Add `tests` and `docs` to all important models

---

## 📚 References

- [DBT Documentation](https://docs.getdbt.com/)
- [Snowflake Adapter](https://docs.getdbt.com/reference/warehouse-profiles/snowflake-profile)
- [dbt_utils Package](https://hub.getdbt.com/dbt-labs/dbt_utils/latest/)

---

## 🧑‍💻 Maintainers

- Project Owner: [Your Name or Team]
- Contact: [email@example.com]

## Demo

- Staging tables are 1:1 to the source tables and we can aggregate the data to create the fact tables.
- Fact table is the dimensional modeling technique which contains the numeric measures produced by an operational measurement event which has lowest grain and always contains foriegn keys for each of its associated dimensions.