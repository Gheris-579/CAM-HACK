# CAM-HACK

## Description

This repository contains CAM-HACK, a Python script that automates discovery of publicly-exposed IP camera streams by parsing Insecam’s more or less country pages. The tool fetches the country index as JSON, lists countries with counts of devices, and (when run interactively) scrapes the selected country’s bycountry pages to extract IP:PORT stream


---

## Dependencies

The script uses the following Python libraries:

* `requests`
* `colorama`



---

## Installation

```
git clone https://github.com/tuo-utente/CAM-HACK.git
cd CAM-HACK
pip install -r requirements.txt # or: pip install requests colorama
```


## RUN


```
python cam-hack.py
```

## Prompt example:

`(IT) Italy (532)` `(US) United States (1420)` `(FR) France (210)` 


┌─[CAM-HACK~@HOME] 

└──╼$   it

---



## SCREEN

<img width="1180" height="902" alt="Screenshot 2025-09-29 004904" src="https://github.com/user-attachments/assets/a4d8b03d-69d1-48a4-a1cc-3980ba5d015b" />




<img width="1132" height="671" alt="Screenshot 2025-09-29 011720" src="https://github.com/user-attachments/assets/d559334e-78a8-41a4-b3e1-57ac19824555" />


## Contatti

Author: Gheris


