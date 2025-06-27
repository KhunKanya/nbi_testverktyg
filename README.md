# 📊 NBI Testverktyg - Statistical Data Validation Framework  
**Automated Data Quality Assurance for Sweden's National Bank**  
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?logo=pandas)](https://pandas.pydata.org)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-black?logo=githubactions)](https://github.com/features/actions)

Production-grade validation framework for statistical data processing at Sveriges Riksbank (National Bank of Sweden). Implements automated data quality checks, anomaly detection, and compliance verification for financial datasets.

## 🔍 Project Overview
This framework ensures data integrity through:
- **Statistical Validation Rules**
- **Data Anomaly Detection**
- **Automated Report Generation**
- **Version-controlled Validation Logic**
- **CI/CD Pipeline Integration**

## 🧩 Core Features
### Data Validation Engine
```python
# validators/economic.py
class EconomicValidator:
    def validate_inflation(self, df: pd.DataFrame) -> ValidationResult:
        """Validate inflation rate dataset"""
        result = ValidationResult("Inflation Data")
        
        # Rule: Valid value range
        result.add_check(
            name="Value Range",
            check=df['rate'].between(-5.0, 20.0).all(),
            message="Inflation rate out of expected range"
        )
        
        # Rule: Year-over-year consistency
        yoy_change = df['rate'].pct_change() * 100
        result.add_check(
            name="YoY Change Threshold",
            check=(yoy_change.abs() < 10).all(),
            message="Extreme YoY changes detected"
        )
        
        return result



