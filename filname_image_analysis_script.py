## Making a script that can alter the name of the files for my experiment to the correct format
#Need to be able to parse through each experiment folder H8 - H13
#Need to be able to insert correct information based on plot such as ; genotype, seed year, plant date, lot #, etc..

# Maybe try dictionaries in python, but might try pearl if unsuccessful.

import os
import re
{Plot_}{Experiment_}{Planted_}{SeedSource_SP21_20207}{SeedYear_21}{Genotype_OH33}{Treatment}{PictureDay_}.nef = {}
{Plot_}{Experiment_}{Planted_}{SeedSource_SP21_20207}{SeedYear_21}{Genotype_OH33}{Treatment}{PictureDay_}.nef =
{Plot_}{Experiment_}{Planted_}{SeedSource_SP21_20207}{SeedYear_21}{Genotype_OH33}{Treatment}{PictureDay_}.nef =
{Plot_}{Experiment_}{Planted_}{SeedSource_SP21_20207}{SeedYear_21}{Genotype_OH33}{Treatment}{PictureDay_}.nef =

{Plot_112}{Experiment_H9}{Planted_10-13-2022}{SeedSource_SP20_20873}{SeedYear_20}{Genotype_PHG50}{Treatment_heat_stress}{PictureDay_8}.nef


def main():
	plot = {}
	experiment = "{}"
	seed_source = "{}"
	seed_year = "{}"
	genotype = "{}"
	treatment = "{}"
	picture_day = "{}"
	i = 0
	path="/Users/propst/Desktop/H11/19-Oct-2022"
	length_path = len(path)
	print(length_path)

	#split the plot name and day
	for filename in os.listdir(path):
		file_num = filename.split("_")
		plot_num = file_num[0]
		plot = plot['plot']: "Plot_" + plot_num.search([0-9][0-9][0-9])

		day_num = file_num[1]
		day = picture_day['day'] : "Day_" + day_num.search([0-9][0-9])

		if plot <= 146:
		experiment = "H9"  

		if plot <= 116:
			treatment = "\{heat_stress\}"
		else:
			next

		if plot <= 126 and if plot >116
			treatment = "\{heat_drought_stress\}"
		else:
			next

		if plot <=136 and if plot >126 :
			treatment = "\{drought\}"
		else:
			next

		if plot >= 137 and plot <= 147
			treatment = "\{control\}"

		genotype = {Genotype_B84 : [107, 117, 127, 137],
		seed_source: "SP20_20399",
		seed_year: "2020"}

		day = "\{Day_" + day + "\}"

		plant_date = ""
		if experiment = "H9":
			plant_date = "\{Planted_10-13-2022\}"




		if plot == 107 or if plot == 117 or if plot == 127 or if plot == 137:
			plot = "\{Plot_" + plot "\}"
			genotype = "\{Genotype_B84\}"
			seed_source = "\{SP20_20399 \}"
			seed_year = "\{2020\}"
			day = "\{Day_" + day + "\}"
		print(plot + experiment + seed_source + seed_year + genotype + treatment + picture_day)






		if plot == 108 or if plot == 118 or if plot == 128:
			genotype = "\{Genotype_OH33\}"




