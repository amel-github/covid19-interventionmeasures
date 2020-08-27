# CCCSL: CSH Covid-19 Control Strategies List

## License
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

## Cite as:
Desvars-Larrive A., Ahne V., Álvarez S., Bartoszek M., Berishaj D., Bulska D., Chakraborty A., Chen E., Chen X., Cserjan D., Dervic A., Dervic E., Di Natale A., Ferreira M.R., Flores Tames E., Garcia D., Garncarek Z., Gliga D.S., Gooriah L., Grzymała-Moszczyńska J., Jurczak A., Haberfellner S., Hadziavdic L., Haug N., Holder S., Korbel J., Lasser J., Lederhilger D., Niederkrotenthaler T., Pacheco A., Pocasangre-Orellana X.M., Reddish J., Reisch V., Roux A., Sorger J., Stangl J., Stoeger L., Takriti H., Ten A., Vierlinger R., Thurner S. CCCSL: Complexity Science Hub Covid-19 Control Strategies List (2020). Version 2.0. https://github.com/amel-github/covid19-interventionmeasures

## Our paper has been published in Scientific Data
Desvars-Larrive, A., Dervic, E., Haug, N. et al. A structured open dataset of government interventions in response to COVID-19. Sci Data 7, 285 (2020). https://doi.org/10.1038/s41597-020-00609-9

## Data
A wide range of different public sources were used to populate, update and curate our dataset, including official government sources, peer-reviewed and non-peer-reviewed scientific papers, webpages of public health institutions (WHO, CDC, and ECDC), press releases, newspaper articles, and government communication through social media. 

**id –** Unique identifier for the implemented measure. ID is also used in the Google Form to report erroneous entries.<br>
**Country –** The country where the NPI measure was implemented.<br>
**ISO3** – Three-letter country code as published by the International Organization for Standardization.<br>
**State** – Subnational geographic area. State where the measure was implemented; the country name otherwise. Used for Germany, India, and USA.<br>
**Region** – Subnational geographic area (e.g. region, department, municipality, city) where the NPI measure has been locally implemented (i.e. the measure was not implemented nationwide as of the mentioned date). The country or the state name otherwise (i.e. measure implemented nationwide).<br>
**Date** – Date of implementation of the NPI. Date of announcement was used when the date of implementation of the NPI could not be found and this was specified in the field Comment.<br>
**L1_Measure** – Theme (L1 of the classification scheme). Eight themes were defined:<br>
(1) Case identification, contact tracing and related measures,<br>
(2) Environmental measures,<br>
(3) Healthcare and public health capacity,<br>
(4) Resource allocation,<br>
(5) Risk communication,<br>
(6) Social distancing,<br>
(7) Travel restriction,<br>
(8) Returning to normal life.<br>
**L2_Measure** – Category (L2 of the classification scheme). See the pdf document for the list of the categories.<br>
**L3_Measure** – Subcategory (L3 of the classification scheme). Provides detailed information on the corresponding category (L2).<br>
**L4_Measure** – Code (L4 of the classification scheme). Corresponds to the finest level of description of the measure.<br>
**Status** – Specifies whether the measure is a prolongation of a previously implemented measure ("Extended") or not ("").<br>
**Comment** – Provides the description of the measure as found in the text data source, translated into English.<br>
**Source** – Provides the reference for each entry.<br>

## Master List of Codes
**Master_list_CCCSL_v2_ordered.csv**: List of all unique combinations of theme/category/subcategory/code that appear in the CCCSL dataset.<br>
**Master-List-with-Unique-LinkType-and-value.csv**: List of the codes providing a better overview of the taxonomy, i.e. type of link parent/child for each pairwise combination of codes and the number of times each link occurs in the dataset (value).

## Glossary of Codes
To promote common understanding and global use of the dataset, we are developping a glossary of the codes used (work in progress).

## Visualisation of the hierarchical coding scheme
Our online interactive tool is available here: http://covid19-interventions.com/CCCSLgraph/ (Author: Sorger J.)

## Open Library
An open library is available (work in progress) that contains all sources used to collect the data: https://www.zotero.org/groups/2488884/cccsl_covid_measure_project.<br>

## Note
The CCCSL is an ongoing collaborative project, built in a time limited by the emergency of the situation. *Version 1* of the CCCSL has not undergone systematic validation and is currently subjected to an extensive data validation process. Our objective is to validate and develop the dataset within the next three months.<br>
We have released *Version 2* of the CCCSL which presents stabilized coding for levels 1, 2, and 3 of the coding scheme.<br>
We are currently developing the labels of the categories/subcategories/codes for the theme "Returning to normal life".

## Contact information
Amélie Desvars-Larrive, [Complexity Science Hub Vienna] (https://www.csh.ac.at)
Email: desvars@csh.ac.at

## Acknowledgements
This work is coordinated by the Complexity Science Hub Vienna, Austria.<br>
This work is supported by the University of Veterinary Medicine Vienna, Austria.

