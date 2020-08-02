# Final Assignment

### Status

Once you are finished with the final assignment, edit this readme and add "x" to the correct box:

* [x] Submitted

* [] I'm still working on my final assignment. 

### Instructions

Read the final assignment instructions from the course webpages [https://autogis.github.io](https://automating-gis-processes.github.io/site/lessons/FA/final-assignment.html). Remember to write readable code, and to provide adequate documentation using inline comments and markdown. Organize all your code(s) / notebook(s) into this repository and **add links to all relevant files to this `README.md`file**. In sum, anyone who downloads this repository should be able to **read your code and documentation** and understand what is going on, and **run your code** in order to reproduce the same results :) 

**Modify this readme so that anyone reading it gets a quick overview of your final work topic, and finds all the necessary input data, code and results.** Add short descriptions, and provide links to relevant files under the topics below (modify the titles according to your topic). You can delete this intro text if you like. 

*Note: If your code requires some python packages not found in the csc notebooks environment, please mention them also in this readme and provide installation instrutions.*

*Note: Don't upload large files into GitHub! If you are using large input files, provide downloading instructions and perhaps a small sample of the data in this repository for demonstrating your workflow.*

## Topic:

The program creates a new Folium map which contains statistical data from different districts in the HRI area and results from the 2019 governmental election. The goal is to compare how different sosioeconomic attributes such as education and employment correlate with the distribution of votes to different political parties. Cities covered are Helsinki, Espoo and Vantaa. Kauniainen was left out due to lack of data.

The code consists of importing the required Python libraries and files, cleaning and merging the datasets to be suitable for the analysis and creating the Folium map instance with map elements presenting different data on the map.

### Input data:

Districts as a KML-file: https://hri.fi/data/fi/dataset/paakaupunkiseudun-aluejakokartat

Voting areas as a shapefile: https://hri.fi/data/fi/dataset/paakaupunkiseudun-aanestysaluejako

Amount of votes by voting area in the 2019 elections: http://pxnet2.stat.fi/PXWeb/pxweb/fi/StatFin/StatFin__vaa__evaa__evaa_2019/130_evaa_2019_tau_103.px/

Unemployment rates and education levels by districts from the year 2017: http://www.aluesarjat.fi/  

### Analysis steps:
1. Add the required Python modules and import the data.
2. Clean the election results, districts and voting area dataframes from unnecessary data and merge the election results to correct voting areas.
3. Clean and merge the unemployment and education data together from different cities.
4. Create new code columns to unemployment and education dataframes which are used to merge them to correct districts
4. Create the Folium map eith different map elements and layers.
### Results:
An interactive Folium map with districts, voting areas, unemployment rates and education levels as optional map layers. Winning parties by voting area are displayed as Folium Circle elements with different colors and a Vincent pie chart as a popup containing the distribution of votes in the voting area.