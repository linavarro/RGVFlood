RATES Station Benchmark Site Surveying
=========================================

A 3D model of the RATES Station Benchmark Site Surveying shall be conducted with the requested two methods.

Method 1- Unmanned Aircraft System (UAS)
=========================================

A UAS utilizes hardward and software to generate a 3D point cloud Digital Surface Model (DSM) of the RATES Station Benchmark Site. Only 14 CFR FAA 107 Certified Remote Piolts for commericial operation shall have conduct UAS Surveys.  The Operations Over People rule became effective on April 21, 2021. Drone pilots operating under Part 107 may fly at night, over people and moving vehicles without a waiver as long as they meet the requirements defined in the rule. Airspace authorizations are still required for night operations in controlled airspace under 400 feet.  Certified Remote Pilots are full responsible for opperation of UAS for RATES Station Benchmark Site Surveying.

Equipment
------------

UAS 
 - UAS equipment used shall be capibile of working with Pix4Dcapture that can be found at `Suported Drones Pix4Dcapture <https://support.pix4d.com/hc/en-us/articles/203991609-Supported-drones-cameras-and-controllers-PIX4Dcapture>`_
 - Smartphone suport Pix4Dcapture

GNSS
 - GNSS equipment used for Ground Control Points (GCPs) shall be a Real Time Kinematic (RTK) GNSS rover equipment, operating at centimeter-level (i.e. survey-grade) 
accuracy.

Ground Targets
 - GCPs are a points with of known coordinates in the area of interest. Coordinates are measured with GNSS RTK surveying methods and used to georeference the generated point cloud.
 - 10 GCP Targes shall be set at the RATES Station Benchmark Site to obtain the coordinates needed to georeference and check the generated point cloud.


Software
---------

Pix4Dcapture
RATE Pix4D account or consultant Pix4D account should be used to login intitate Pix4Dcapture. Logging in requires Internet connection. It can be skipped up to five times so that the app can be temporarily used without login. The Login screen has several items.

Suncalc
`SunCalc <https://www.suncalc.org/>`_ should be used to determine the best sun angle to reduce the shadows that effect the 3D modeling

Workflow
-----------

The following is the general workflow.  Please refer to the Pix4Dcapture manual details.

.. code-block:: yaml
1. Optain 14 CFR FAA 107 Certified Remote Piolts
2. Complete the RATE's Tutorial on UAS Station Benchmark Surveying Training
3. Verify all equipment is 
4. Utilize a Fixed Height Pole with proper tripod legs
5. Scout the location and set a Station Mark
 - Marks are defined IN USGS TM3A19 or `NGS Special Application Mark Description <https://geodesy.noaa.gov/marks/descriptors.shtml#setting>`_
 - The mark must be durable, have a stable setting, and good satellite visibility.
 - Follow safety procedures and sign notification when occupying location.
 - Obtain pictures of mark for OPUS Shared Observer Field Log
6. Place GNSS level on RATES Station Benchmark Contorl Point
7. Start Survey: Collect RINEX 3 data (Conversion from Vendor format to Rinx may occur in office download) for 4 hours and 15 minutes.
8. Occationally check level of instrument and note time checked.  If off more then half bubble stop measuring.  Level and restart 4 hours and 15 minutes.
9. Complete `Observer Field Log for GNSS Surveys <https://geodesy.noaa.gov/surveys/forms/obslog-OPUS.pdf?>`_
  - Obtain pictures of setup
  - Obtain measurments and description to find RATES Station Control
10. Optional: `Complete Visibility Obstruction Diagram <https://geodesy.noaa.gov/surveys/forms/#visibility>`_
11. End Survey: Stop Collecting after 4 hours and 15 minutes
12. Occupy RATES Station Benchmark Control Point with your RTK GPS twice with a complete loss of lock between occupations
13. Download to RATE Shared Site under \Station\01_BM\RINEX
  - If collected in Vendor format please place Vendor format file in RATE Shared Site under \Station\01_BM\RINEX
13. DO NOT UPLOAD to OPUS Shared Solutions
14. Upload to regular OPUS and submit PDF of email results to \Station\01_BM\OPUS_RESULTS
15. Place all Images and Observation Feild Logs in \Station\01_BM\FIELD_NOTES
16. Place the two (2) RATES Station Benchmark Control Point RTK GPS Solutions:
  - In X,Y, Z (m); Lat, Lon, ellipsoidal height (ftus); Northing, Easting, Orthometric Height (ftus) with RMS in File format outlined in Geospatial Data Model document in the \Station\01_BM\RTK directory 
  - In any raw vendor data format \Station\01_BM\RTK directory 
  
.. note::
 
Your shared solution must be a high-quality solution:
≥ 70% observations used and ambiguities fixed
≤ 3 cm RMS
≤ 4 cm peak-to-peak error ranges for latitude and longitude
≤ 8 cm peak-to-peak error range for ellipsoid height
