# Wisdom

Collaborative decision making is a foundational precept of the REON concept,
requiring an integration between scientific principles and policy drivers
(Gutenson et al, 2020).

-   Decision Support

-   User Collaboration

## Decision Support

Decision Support Tools are generally combinations Analytics and Visualization,
sometimes with inference logic built in, that guide the end-user through
decision logic.

-   Early Warning

-   Inundation Depth

-   Damage Assessment

-   Alternatives Analysis

## User Collaboration

User collaboration is predication on establishment of a COP, ensuring
discussions and collaborative decision making can be made from a common
reference point.

-   Data & Information Sharing

-   Trans-Jurisdictional Knowledge Inventory

# Workflow Implications

The immediate goals for the REON.cc user Interface are to support regional flood
planning and collaborative decision making. REON.cc must:

-   Assimilate available, timely and necessary Data to support all the flood
    planning and decision making functions of REON.cc.

-   Provide key Analytics and Visualization tools to interpret the Data or drive
    further investigations

-   Transform the Data and Information into actionable intelligence to support
    operational decisions and policy making.

-   Serve as a platform for collaborative, multi-jurisdictional decision making.

# Approach

-   **GeoNode**: The primary user interface platform will rely on the GeoNode
    open-source geospatial content management system. GeoNode will be extended
    with web applications to provide the tools and services described herein.

-   **Data Ingestion**: Server-side scripts will be developed to automate
    ingestion of Data to maintain currency.

-   WRF-Hydro: The WRF-Hydro hydrologic forecast model will run continuously in
    the background. The primary interaction between the WRF-Hydro instance and
    the REON.cc interface will be for visualization of forecast data. The long
    term goal of the hydrologic forecasting tool development process is to be
    model agnostic, allowing for ingestion of forecast data from a variety of
    platforms, including the ability to provide ensemble forecasts.

-   HEC-RAS: Scripts will be developed to extract and transform Data from the
    WRF-Hydro model to be used in HEC-RAS hydraulic models. Elements of this
    process will include extraction of domain data, including topographic and
    hydraulic survey results, along with hydrologic forecasts, all clipped to
    the target domain. The HEC-RAS model will be run on the client-side
    computer, utilizing the analytics and visualization tools available locally,
    however, a long-term goal will be to provide up-load capability for model
    scenarios and outputs to REON.cc for contribution to the knowledge base and
    potential inclusion in server-side analytics and decision support tools.

-   SWMM: Similar to HEC-RAS, scripts will be developed to extract and transform
    Data from the WRF-Hydro model to be used in the SWMM urban stormwater
    models. Elements of this process will include extraction of domain data,
    including topographic and hydraulic survey results, along with hydrologic
    forecasts, all clipped to the target domain. The SWMM model will be run on
    the client-side computer, utilizing the analytics and visualization tools
    available locally. Initial deployments will required the client-side
    deployments to provide detailed delineation of the urban stormwater network
    not defined in the existing REON.cc repositories. Future goals will include
    ingestion of the urban stormwater networks for automated generation of the
    input data for client-side execution, and potentially server-side execution
    as well.

-   **Dashboard**: The web-portal for REON.cc will provide a dashboard,
    providing information tuned to the users' specific interests and needs. The
    dashboard will also allow for execution of analytics, visualization and
    decision support tools as they are added to the platform.

-   **Notifications**: Critical to promoting user collaboration will be the
    integration of a notification and communication system both between users
    and with processes, including the triggering of early warnings based on the
    RTHS network and forecast tools.

# Appendices

## Terminology

**Bernoulli**

The Bernoulli equation is a simplification of the Navier-Stokes equations
assuming inviscid fluid and steady (non-time-variant) flow.

**Crowdsource**

Data collection from open, relatively un-controlled, sources.

**Deterministic**

Approaches to describing processes that do not rely on randomness.

**Mechanistic**

Formulations describing physical, biological or chemical processes based on a
theoretical understanding.

**Navier-Stokes**

The Navier–Stokes equations are mathematically representations of conservation
of mass and momentum for simple fluids such as water.

**Stochastic**

Approaches to describing processes in statistical terms.

## Acronyms

COP Common Operating Picture

CUAHSI Consortium of Universities for the Advancement of Hydrologic Science

DHS Department of Homeland Security

DIKW Data, Information, Knowledge, Wisdom

FIF Flood Infrastructure Fund

GIS Geospatial Information System

HEC Hydrologic Engineering Center

HEC-HMS Hydrologic Engineering Center Hydrologic Modeling System

HEC-RAS Hydrologic Engineering Center River Analysis System

HEC-RTS Hydrologic Engineering Center Real Time Simulation

LLM/BSC Lower Laguna Madre/Brownsville Ship Channel watershed.

LRGVDC Lower Rio Grande Valley Development Council

LSM Land Surface Models focus on describing the processes driving the exchange
of terrestrial water with atmospheric.

NLDAS North American Land Data Assimilation System

NOAA National Oceanic and Atmospheric Agency

NWC National Water Center

NWM National Water Model

NWS National Weather Service

ODM Observations Data Model

Primo Parallel raster inundation model

RATES Research, Applied Technology, Education and Service, Inc., a non-profit
technology-based company.

REON The River and Estuary Observation Network. A partnership of organizations,
supported by cloud software, committed to furthering the Democratization of
Water Intelligence by sharing water data, analytics and models for local and
regional decision making.

REON.cc Cloud-based cyber-infrastructure that supports REON's goals.

REON/RGV Instantiation of REON with specific application to the Lower Rio Grande
Valley - this includes the collection of RTHS stations, the REON partners with a
stake in the LRGV, and the application of the REON/WM to the LRGV.

REON/WM The REON Water Model

RTHS Real Time Hydrologic System

RWRAC Regional Water Resources Advisory Committee

SA Situational Awareness

TWDB Texas Water Development Board

TWDB/FIF The Texas Water Development Board Flood Infrastructure Fund.

USACE United States Army Corps of Engineers

VIC Variable Infiltration Capacity (VIC) Macroscale Hydrologic Model

WPS WRF Preprocessing System

WRF-Hydro Weather Research and Forecasting Model Hydrological modeling system

SWMM Stormwater Management Model

SPRNT Simulation Program for River Networks

## Assets

**Eeyore**

URL: Eeyore.ratesresearch.org

CPU: Dual Intel(R) Xeon(R) E-2124 CPU @ 3.30GHz

Memory: 16GB

HD: 4TB

OS: Ubuntu Linux 20.04

**Tigger**

URL: Tigger.water-wizard.org

CPU: Dual Intel(R) Xeon(R) CPU E3-1245 v3 @ 3.40GHz

Memory: 16GB

HD: 4TB

OS: Ubuntu Linux 20.04

## Bibliography

GeoNode

<https://geonode.org/>

Gutenson et al, 2020

<http://www.jeiletters.org/index.php?journal=mys&page=article&op=view&path%5B%5D=202000048>

Django

<https://www.djangoproject.com/>

HEC-HMS

<https://www.hec.usace.army.mil/software/hec-hms/>

HEC-RAS

<https://www.hec.usace.army.mil/software/hec-ras/>

InfoWorks ICM

<https://www.innovyze.com/en-us/products/infoworks-icm>

MIKE Urban+

<https://www.mikepoweredbydhi.com/download/mike-2019/mike-urban-plus?ref=%7B5399F5D6-40C6-4BB2-8311-37B615A652C6%7D>

National Water Center

<https://water.noaa.gov/about/nwc>

National Water Model

<https://water.noaa.gov/about/nwm>

Navarro et al, 2021

<https://www.mdpi.com/2071-1050/13/20/11186>

Exhausted Grape Marc Derived Biochars: Effect of Pyrolysis Temperature on the
Yield and Quality of Biochar for Soil Amendment

<https://www.mdpi.com/2071-1050/13/20/11187>

Eco-Efficiency for the G18: Trends and Future Outlook

<https://www.mdpi.com/2071-1050/13/20/11196>

Corporate Social Responsibility Reporting in the Casino Industry: A Content
Analysis

<https://www.mdpi.com/2071-1050/13/20/11185>

Analytical Models for Seawater and Boron Removal through Reverse Osmosis

<https://www.mdpi.com/2071-1050/13/16/8999>

NOAA-OWP/ngen: Next Generation Water Modeling Engine and Framework Prototype

<https://github.com/NOAA-OWP/ngen>

PRIMo: Parallel raster inundation model

<https://www.sciencedirect.com/science/article/abs/pii/S0309170818308698>

Python

<https://www.python.org/>

Simulation Program for River Networks

<https://github.com/frank-y-liu/SPRNT>

Storm Water Management Model (SWMM) \| US EPA

<https://www.epa.gov/water-research/storm-water-management-model-swmm>

VIC

<https://vic.readthedocs.io/en/master/>

WRF-Hydro

<https://ral.ucar.edu/projects/wrf_hydro/overview>

Setting Up an Ubuntu Linux Cluster

<https://www.particleincell.com/2020/ubuntu-linux-cluster/>
