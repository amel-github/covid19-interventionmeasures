CCCSL: Complexity Science Hub COVID-19 Control Strategies List
================
Update 2021-03-01

[Context](#Context)  
[Objectives of the Project](#Objective)  
[Methods](#Methods)  
[Note on the Data](#Note%20on%20the%20Data)  
[Data Sources](#Data%20Sources)  
[CCCSL Fields](#CCCSL%20Fields)  
[Master List of Codes](#Master%20List%20of%20Codes)  
[Glossary of Codes](#Glossary%20of%20Codes)  
[R Codes](#R%20Codes)  
[License](#License)  
[Acknowledgements](#Acknowledgements)  
[Funding](#Funding)  
[Contact](#Contact)  
[List of Contributors](#List%20of%20Contributors)

## Context <a name="Context"></a>

During the COVID-19 pandemic, governments have enforced a broad spectrum
of interventions, under rapidly changing, unprecedented circumstances.
Public health and social measures (PHSMs), also called
non-pharmaceutical interventions (NPIs), aim to prevent the introduction
of infectious diseases, control their spread, and reduce their burden on
the health system. The general concept of containing the initial
(exponential) spread of a disease is called “flattening the
(epi-)curve”. By reducing the growth rate of an epidemic, PHSMs reduce
the stress on the healthcare system and help gaining time to develop and
produce vaccines and specific medications, which is of utmost importance
in the case of emerging infectious diseases.

Monitoring and documenting government strategies during the COVID-19
crisis is crucial to understand the progression of the epidemic and its
impacts, e.g. on the society, the economy, public health, or human
rights.

## Objectives of the Project <a name="Objective"></a>

Started in mid-March 2020, our project aims to generate a comprehensive
structured dataset on government responses to COVID-19, including the
respective time schedules of their implementation.

**Data types**  
Our dataset presents PHSMs but also economic measures (EMs) implemented
in response to COVID-19.

The dataset is readily usable for modelling and machine learning
analyses and exhibits a great analytical flexibility.<br> We also
provide user-friendly documentation and materials (codes, visualisation
interface, and library of sources) along with the dataset, which allow a
maximum understanding of the data and promote its use among non-experts.

## Methods <a name="Methods"></a>

Our methodology is published: Desvars-Larrive, A., Dervic, E., Haug, N.
et al. A structured open dataset of government interventions in response
to COVID-19. *Scientific Data* 7, 285 (2020).
<https://doi.org/10.1038/s41597-020-00609-9>.

## Note on the Data <a name="Note on the Data"></a>

This project is an emergency research project started in response to the
COVID-19 health crisis. The data has been collected in a very limited
time. This dataset is dynamic, continuously updated, and is subjected to
continuous data validation and code curation process.

## Data Sources <a name="Data Sources"></a>

A wide range of different public sources are used to populate, update
and curate our dataset, including official government sources,
peer-reviewed and non-peer-reviewed scientific papers, webpages of
public health institutions (WHO, CDC, and ECDC), press releases,
newspaper articles, and government communication through social media.

An **Open Library of Sources** is available that contains all sources
used to collect the data:
<https://www.zotero.org/groups/2488884/cccsl_covid_measure_project>.  
We also provide various formats of this library that can be imported in
different reference manager software.

## CCCSL Fields <a name="CCCSL Fields"></a>

**id** – Unique identifier for the implemented measure.<br> **Country**
– The country where the measure was implemented.<br> **ISO3** –
Three-letter country code as published by the International Organization
for Standardization.<br> **State** – Subnational geographic area. State
where the measure was implemented; the country name otherwise. Used for
Germany, India, UK, and USA.<br> **Region** – Subnational geographic
area (e.g. region, department, municipality, city) where the measure has
been locally implemented (i.e. the measure was not implemented
nationwide as of the mentioned date). The country or the state name
otherwise (i.e. measure implemented nationwide).<br> **Date** – Date of
implementation of the measure. Date of announcement was used when the
date of implementation of the measure could not be found and this was
specified in the field Comment.<br> **L1\_Measure** – Theme (L1 of the
classification scheme). Eight themes were defined:<br> (1) Case
identification, contact tracing and related measures,<br> (2)
Environmental measures,<br> (3) Healthcare and public health
capacity,<br> (4) Resource allocation,<br> (5) Risk communication,<br>
(6) Social distancing,<br> (7) Travel restriction,<br> (8) Returning to
normal life.<br> **L2\_Measure** – Category (L2 of the classification
scheme). See
[Description\_changes\_v2\_20201216.pdf](Description_changes_v2_20201216.pdf)
document for the list of the categories.<br> **L3\_Measure** –
Subcategory (L3 of the classification scheme). Provides detailed
information on the corresponding category (L2).<br> **L4\_Measure** –
Code (L4 of the classification scheme). Corresponds to the finest level
of description of the measure.<br> **Status** – Specifies whether the
measure is a prolongation of a previously implemented measure
(“Extended”) or a new measure (“New”). When this information has not
been collected, the cell is empty.<br> **Comment** – Provides the
description of the measure as found in the text source, translated into
English.<br> **Source** – Provides the reference(s) for each recorded
measure.<br>

## Master List of Codes <a name="Master List of Codes"></a>

  - [Master\_list\_CCCSL\_v2\_ordered.csv](Master_list_CCCSL_v2_ordered.csv):
    List of all unique combinations of theme/category/subcategory/code
    that appear in the CCCSL dataset.

  - [Master-List-with-Unique-LinkType-and-value.csv](Master-List-with-Unique-LinkType-and-value.csv):
    List of the codes providing a better overview of the taxonomy,
    i.e. type of link parent/child for each pairwise combination of
    codes and the number of times each link occurs in the dataset
    (value).

The Master List of Codes is a dynamic document, updated together with
the dataset, as inductive codes emerge from the text source.

The CCCSL taxonomy can be visualized via our [online interactive
tool](http://covid19-interventions.com/CCCSLgraph/) (Author: Sorger J.).

## Glossary of Codes <a name="Glossary of Codes"></a>

The [Glossary of Codes](CCCSL_Glossary%20of%20codes.docx) provides a
definition for each code used to describe COVID-19 PHSMs and EMs in the
CCCSL.

*Note*  
On 2020-12-16 (commit cd396b3) we have updated the CCCSL with an
improved taxonomy (Categories/Subcategories/Codes). The most important
change concerns the classification of gatherings (theme: Social
distancing). Previous versions discriminated between small (\< 50
persons) and mass gatherings (\> 50 persons). However, this was not
accurate enough with regard to closure of restaurants, shops, short-term
accommodations, or businesses for which we did not know the capacity. We
also wanted to adapt the codes with regard to several PHSMs, e.g. mask
wearing policies and phase-out measures, which, worldwide, discriminate
outdoor and indoor settings. Therefore, the theme “Social distancing”
has new categories “Indoor gathering restriction”, “Outdoor gathering
restriction” and “Indoor and outdoor gathering restriction”. See our
[Glossary of Codes](CCCSL_Glossary%20of%20codes.docx) for more details.

## R Codes <a name="R Codes"></a>

R codes for exploring the dataset and reproducing the figures of our
[publication](https://doi.org/10.1038/s41597-020-00609-9) as well as
some graphs displayed on our
[webpage](https://covid19-interventions.com/) are available on
[GitHub](https://github.com/amel-github/CCCSL-Codes) and
[Zenodo](https://doi.org/10.5281/zenodo.3949808).

## License <a name="License"></a>

This project is licensed under the CC BY-SA 4.0 License - see the [CC
BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en) file
for details.

## Acknowledgements <a name="Acknowledgements"></a>

This work is coordinated by the [Complexity Science Hub Vienna,
Austria](https://www.csh.ac.at). <br> This work is supported by the
[University of Veterinary Medicine Vienna,
Austria](https://www.vetmeduni.ac.at/).

![](Vetmed_Logo3.png)             ![](CSH_Logo3.png)

 

## Funding <a name="Funding"></a>

EOSCsecretariat.eu has received funding from the European Union’s
Horizon Programme call H2020-INFRAEOSC-05-2018-2019, grant Agreement
number 831644.

![Screenshot](eosc_logo2.png)  

## Contact <a name="Contact"></a>

Amélie Desvars-Larrive (Complexity Science Hub Vienna, Austria /
University of Veterinary Medicine Vienna, Austria). <br> Email:
[desvars@csh.ac.at]()

## List of Contributors (alphabetical order) <a name="List of Contributors"></a>

Ahne Verena *(Complexity Science Hub Vienna)*<br> Álvarez Francisco S.
*(Fundación Naturaleza El Salvador)*<br> Bartoszek Marta *(Institute of
Psychology, Jagiellonian University, Kraków, Poland / University of
Veterinary Medicine Vienna)*<br> Berishaj Dorontinë *(Independent
Scholar)*<br> Bulska Dominika *(Institute for Social Studies, University
of Warsaw, Poland)*<br> Chakraborty Abhijit *(Complexity Science Hub
Vienna)*<br> Chen Jiaying *(Section for Science of Complex Systems,
Medical University of Vienna / Complexity Science Hub Vienna)*<br> Chen
Xiao *(Independent Scholar)*<br> Cserjan David *(Complexity Science Hub
Vienna)*<br> Dervic Alija *(Institute of Electrodynamics, Microwave and
Circuit Engineering, Vienna University of Technology, Austria)*<br>
Dervic Elma *(Section for Science of Complex Systems, Medical University
of Vienna / Complexity Science Hub Vienna)*<br> Desvars-Larrive Amélie
*(University of Veterinary Medicine Vienna / Complexity Science Hub
Vienna)*<br> Di Natale Anna *(Section for Science of Complex Systems,
Medical University of Vienna / Complexity Science Hub Vienna)*<br> El
Goukhi Jasmin *(University of Vienna / University of Veterinary Medicine
Vienna)*<br> Ferreira Marcia R. *(Complexity Science Hub Vienna)*<br>
Flores Tames Erwin *(Complexity Science Hub Vienna)*<br> Garcia David
*(Section for Science of Complex Systems, Medical University of Vienna /
Complexity Science Hub Vienna)*<br> Garncarek Zuzanna *(Institute of
Psychology, Jagiellonian University, Kraków, Poland)*<br> Gliga Diana S.
*(Independent Scholar)*<br> Gooriah Leana *(German Centre for
Integrative Biodiversity Research (iDiv), Leipzig, Germany)*<br> Gruber
Michael *(University of Veterinary Medicine)*<br> Grzymała-Moszczyńska
Joanna *(Institute of Psychology, Jagiellonian University, Kraków,
Poland)*<br> Jurczak Anna *(Institute of Psychology, Jagiellonian
University, Kraków, Poland)*<br> Haberfellner Simon *(Independent
Scholar)*<br> Hadziavdic Lamija *(Independent Scholar)*<br> Haug Nils
*(Section for Science of Complex Systems, Medical University of Vienna /
Complexity Science Hub Vienna, Austria)*<br> Holder Samantha
*(Independent Scholar)*<br> Korbel Jan *(Section for Science of Complex
Systems, Medical University of Vienna / Complexity Science Hub
Vienna)*<br> Lasser Jana *(Section for Science of Complex Systems,
Medical University of Vienna / Complexity Science Hub Vienna)*<br>
Lederhilger Diana *(Independent Scholar)*<br> Niederkrotenthaler Thomas
*(Unit Suicide Research & Mental Health Promotion, Medical University of
Vienna, Austria / Complexity Science Hub Vienna)*<br> Pacheco Andrea
*(German Centre for Integrative Biodiversity Research (iDiv), Leipzig,
Germany)*<br> Pocasangre-Orellana Xochilt María *(Fundación Naturaleza
El Salvador)*<br> Reddish Jenny *(Seshat: The Global History Databank /
Complexity Science Hub Vienna)*<br> Reisch Viktoria *(Independent
Scholar)*<br> Roux Alexandra *(CERMES3, Ecole des Hautes Etudes en
Sciences Sociales, Villejuif / Gender, Sexuality, Health, CESP, INSERM,
Paris-Saclay University, Villejuif, France)*<br> Schueller William
*(Complexity Science Hub Vienna)*<br> Sorger Johannes *(Complexity
Science Hub Vienna)*<br> Stangl Johannes *(Independent Scholar)*<br>
Stoeger Laura *(Complexity Science Hub Vienna)*<br> Takriti Huda
*(Complexity Science Hub Vienna)*<br> Ten Alexandr *(Flowers
project-team, National Research Institute for Digital Sciences (INRIA),
Talence, France)*<br> Thurner Stefan *(Section for Science of Complex
Systems, Medical University of Vienna / Santa Fe Institute, Santa Fe,
USA / Complexity Science Hub Vienna)*<br> Vierlinger Rainer
*(Independent Scholar)*
