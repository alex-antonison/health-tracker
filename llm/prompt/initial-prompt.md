I want to stand up a project that can read in a google sheet that looks like 

Date	Symptom	Mobility	Notes
			
10/9/2026	Symtpom1 | Symptom2 | Symptom3	No Assist	A bit anxious
10/10/2026	Symtpom1 | Symptom2 | Symptom3 | Symptom4	No Assist	Ate late on the night of the 9th. 

And can split that into two tables:
1. Expand the symptoms by splitting on |
2. Include all other columns that are single values per cell (currently just Mobility and Notes

Once split out, the Symptoms will go into the "Data Symptoms Table" sheet and then the rest into the "Data Measures Table" sheet in the same Google Sheet.

I have setup My google cloud console with API access to Google Sheets and Drive and have been able to successfully run this python file @src/health_tracker/process_symptom_data.py and it print out records.

I want you to come with a plan to build out a python script that handles this. It needs to be something that I can run about once a week and will read in the table and full replace it each time. No need to worry about doing it incrementally as entries can change over time. Because the dataset will always be small, we can afford to full replace each time.

Put this plan in the @llm/plan/ folder.