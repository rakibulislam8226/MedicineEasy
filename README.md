<div align="center">
  <h2>MedicineEasy</h2>
</div>

### MedicineEasy is mainly to help users for any medicine's with additional data. 

## Introduction

Welcome to the official repository of MedicineEasy, the transformative app revolutionizing drug information access for pharmacists. Designed for professionals in community pharmacies, hospital pharmacies, and clinics, MedicineEasy is committed to streamlining the medication dispensing process and enhancing patient care.

## Features

MedicineEasy is packed with features designed to empower pharmacists:

- **Effortless Search**: Quickly find medication details by brand, generic name, or classification.
- **Comprehensive Information**: Get info on usage, symptoms, interactions, pediatric guidelines, indications, pharmacology, dosage, and side effects.
- **Regular Updates**: Stay current with the latest in drug information and industry standards.
---

<div align="center">
  <h3>Setup guide.</h3>
</div>

## Getting Started

To start using MedicineEasy:

1. **Clone the Repository**:
 ```shell
git clone git@github.com:rakibulislam8226/MedicineEasy.git
  ```

**Go to the directory file**
```
cd MedicineEasy
```
---
**Create virtual environment based on your operating system**
 * **For ubuntu**
 ```shell
python3.10 -m venv venv
  ```

  ###### Activate the virtual environment
 ```shell
source venv/bin/activate
  ```
 * **For windows**
 ```shell
python -m venv venv
  ```

---
**Copy .example.env file to .env:**

  * For linux
    ```shell
    cp .example.env .env
    ```
  * For windows
    ```shell
    copy .example.env .env
    ```
##### Fill the .env with proper data
---
### Install the requirements file.
```
pip install -r requirements.txt
```
#### Go the the src directory
```
cd src/
```

  ###### Migrate the project
 ```shell
python manage.py migrate
  ```
  ###### If needed create superuser with proper data
  ```
  python manage.py createsuperuser
  ```
  ###### Run the server
 ```shell
python manage.py runserver
  ```
---

### Project Structure
