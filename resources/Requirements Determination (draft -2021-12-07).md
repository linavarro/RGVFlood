Lower Rio Grande Valley Development Council Flood Infrastructure Fund

Require Determination

Project Deliverable ID: 1.4.1.1

Research Applied Technology, Education and Services Inc.

Andrew Ernest PhD, PE, BCEE, D.WRE

Christopher Fuller PhD

William Kirkey PhD

Linda Navarro

![IMG_3917](media/3c0210f7890ca2397f13b5b5eeeddda5.jpeg)

November 9, 2021

# Approval Page

**Technical Review By:**

Position: Chief Operations Officer

Name: Christopher Fuller, Ph.D.

Signature:

**Final Approval for Submission:**

Position: Chief Executive Officer

Name: Andrew N.S. Ernest, Ph.D., P.E.

Signature:

# Introduction

User Interface Requirements Determination refers to **delineation of** the
**process** to be followed to implement any **enhancements** necessary to
REON.cc to accommodate the goals of REON/WM. The initial deployment of the
REON/WM is to support REON/RGV, **partially funded** by the TWDB/FIF program.

## Need & Philosophical Basis for REON.cc

REON.cc is the user interface for REON. REON, a flagship program of RATES, is
dedicated to the core philosophy of:

*Democratizing Water Intelligence for Knowledge-Enabled Policy & Decision
Making*

Figure: DIKW Pyramid depicts the Data, Information, Knowledge, Wisdom pyramid
espoused by the informatics discipline. As adopted by REON, DIKW refers to:

-   Data: Addressing the monitoring needs of under-served areas to ensure
    technology and monitoring solutions are available to all.

-   Information: Translating water & environmental data into actionable
    intelligence.

-   Knowledge: Educating decision makers and elected officials to promote
    knowledge-based decision making.

-   Wisdom: Supporting implementation through facilitation of collaborative
    efforts between stakeholders such as municipalities, academic institutions,
    not-for-profits, conservancy & environmental groups as well as state and
    federal regulatory agencies.

![](media/bb037f07a017bfff62e2135c3f5258ad.jpeg)

Source: <https://commons.wikimedia.org/wiki/File:DIKW_Pyramid.svg>

Figure: DIKW Pyramid

## The Need for a Common Operating Picture

Figure: Blind Men and Elephant depicts old Indian **fable of the Six Blind Men**
and the Elephant, apropos to the issues of developing of water policy or
collaborative decision making. Each stakeholder or decision maker views the
water “elephant” from their own **parochial perspective**, and argues that
theirs is reality. Being able to provide a **Common Operating Picture** is
critical is multi-jurisdictional decision making is to be both effective and
sustainable. COP has been adopted by several agencies including the DHS and
NOAA's NWS. COP is a Situational Awareness capability designed to ensure that
all participating stakeholder and/or **decision makers possess** the full suite
of **information necessary** for the job at hand.

![](media/de6b31c10d8f4cabff6886826c301ab0.jpeg)

Source: <https://commons.wikimedia.org/wiki/File:Blind_men_and_elephant4.jpg>

Figure: Blind Men and Elephant

# Goals & Objectives of the User Interface

The overarching goal of the REON.cc cyber-collaboratory is to serve as the
**primary end-user interface** for all aspects of **model execution** and **data
analysis**. Specific objectives of REON.cc include:

-   Serve as the **primary user Interface** for all REON related activities.

-   Provide **access** to all available **data** relevant to the REON goals and
    needs of the REON user base.

-   Provide access to the **analytics**, **visualization** and **forecasting**
    tools developed to serve the needs of the user base.

-   Serve as the platform to encourage **engagement** between users and
    facilitate **multi**-**lateral decision making**.

# Description of Development Process

The continued development of the REON.cc User interface will follow the
**standard software development process**:

-   **Requirements Determination**: Determination of the requirements for the
    next version of the User Interface.

-   **Predevelopment Plan**: Establishment of a plan for initiation the
    development process.

-   **Requirements Validation**: Validation of the User Interface Requirements
    by stakeholders and sponsor.

-   **Implementation**: Development & implementation of the User Interface.

-   **Quality Assurance Demonstration**: Demonstration of operational integrity
    of the interface components and identification of methodologies for
    capturing un-intended outcomes. Equivalent to Alpha-Testing.

-   **End-User Acceptance Testing**: Rigorous testing of the beta version of the
    User Interface by stakeholders, with immediate feedback for refinement as
    needed.

-   **End-User Interface Development Report**: Production and provision of a
    final report documenting the User Interface development and implementation.

# Platform Identification

The current implementation of REON.cc (Figure: REON.cc User Interface) utilizes
a nominally modified instance of the **Open Source** Geospatial Content
Management System GeoNode. From the provider:

*GeoNode is a web-based application and platform for developing geospatial
information systems (GIS) and for deploying spatial data infrastructures (SDI).*

*It is designed to be extended and modified, and can be integrated into existing
platforms.*

With a **robust user-management system**, integration with the well-established
GeoServer **geospatial data server** platform for hosting GIS data, and reliance
on the Django web framework for the Python programming language, GeoNode is
ideally suited to being adapted for addressing the Goals and Objectives of the
REON.cc platform.

![](media/acb21bb1f699165196fd529147531669.jpeg)

Figure: REON.cc User Interface

# End-User Needs Identification

Based on feedback during initial end-user meetings, the Figure: REON.cc
Information Flow depicts the information flow necessary to meet the end-user
needs. End-user needs are, in order of priority:

1.  **Hydrologic Extremes**: Immediate needs for REON.cc are to support policy
    and operational decision making for **flood response and resiliency**.
    Shortly after flood management application, user is expected to need
    inclusion of **drought preparedness and management** as core functionality.

2.  **Water Supply**: As support is provided for floods and droughts, decision
    makers are expected to turn their attention to utilizing REON.cc for water
    supply applications, including mid-term **storage predictions** and
    **inter-basin transfer** decisions.

3.  **Ecosystem Services**: Increased expansion of water supply needs are
    coupled to **water quality** implications on **source water**. In parallel,
    applications of REON.cc are expected to expand to address ecosystem
    services, including **Freshwater** and **instream flows** management.

![](media/5efccee44494dc1b4b630564f9e93169.jpeg)

Figure: REON.cc Information Flow

# Data

Data is the lowest, most fundamental, tier of the DIKW pyramid. Data Input needs
include processes for recruiting data specific to the REON.cc end-uses. This
includes user entered, warehoused and cloud stored data.

-   Crowdsource Data

-   Observed Data

-   Domain Data

-   Processed Data

## Crowdsource Data

Effective data input will rely on a **balance** between **quality assured** data
from known sources, to **crowdsourced** data, that while potentially meeting
only nominal quality assurance standards, may often be of **higher volumes** and
potentially possess **unique intrinsic value**.

-   Crowdsource data can consume **significant storage capacity**.

-   For example, **photographs** from **social media** platforms, **geolocated**
    and **time-stamped** have been shown to provide potentially **quantitative**
    insights into flood inundation depths to **correlate** against
    **forecasting** tools.

## Observed Data

Of particular interest is RTHS and **real-time data** from other providers,
along with other observations such as **physical grab samples**,
**meteorological measurements** and others that could serve as **forcing data**
for mechanistic models, analytics and decision support tools.

-   The current **RTHS database** is CUAHSI ODM 1.1.1 compliant. Additional data
    is stored in different databases to accommodate the needs of the source data
    structures.

-   Where possible **cloud-sourced** data should be retrieved **on demand**
    rather than being stored locally in order to **ensure currency**.
    **Caching** and **buffering** technologies should be used to prevent data
    access **latency** when needed for processing by analytics, visualization
    and forecast tools.

## Domain Data

This includes **geographic**, **hydrographic**, **socio-economic**,
**socio-political** and other data that defines the **geospatial extent** of the
application domain.

-   **National** and **local data** sources such as NLDAS can be **ingested**
    with existing **Metadata** specifications, while topographic survey results,
    such as those generated during the placement of RTHS stations will required
    specification of **quality assurance standards** and other Metadata
    requirements as additional data inputs.

-   As with cloud-sourced observed data, **cloud-sourced domain data** should be
    retrieved **on demand** rather than being stored locally in order to
    **ensure currency** and **minimize local storage** needs through
    **caching**.

## Processed Data

Processed Data is produced when **raw data** is **transformed** through
**analytic** or **deterministic** tools.

-   Unless carefully produced, processed Data can contribute to extremely **high
    storage** volume needs.

-   **Balancing** the **computational effort** needed to produce the processed
    data against **storage volumes** needed to store it is critical to
    **efficiency**.

-   **Tuning** the **analytic** and **deterministic** tools to limit the
    production of processed data to only that needed to serve the decision
    making end can minimize both processing and storage needs.

-   In some cases, **high computational** effort and **high processed storage
    volumes** cannot be avoided, in which case, processed may be **condensed**
    through further analytic processing to reduce the volume of storage needed
    while **maintaining** the **intrinsic value** of the processing.

-   **Caching** should be used to reduce the **volume** for **storage** over
    **time**.

# Information

**Information** is a key product of REON.cc. It results from the transformation
of raw data into actionable intelligence.

-   Processing capacity needs are driven by the complexity and volume of data
    needed for the particular analytic and visualization tool being used, but in
    general, they are significantly lower that the mechanistic tools used in
    Knowledge: Processing Needs.

-   Storage needs for information are driven by the outputs of the analytic and
    procedural tools that act on the raw data.

-   Determination of the need to store these outputs is driven by a balance
    between the computation effort required to reproduce and the volume of
    storage associated with the output data.

-   Some caching and buffering must be considered for remote and cloud-served
    data, such as National data sources, to ensure timely utilization in the
    Processing elements of REON.cc.

-   The REON.cc cyberinfrastructure has been implemented for water quality
    applications (Navarro et al, 2021).

-   Tools involved in transformation of Date into Information include:

    -   Analytics

    -   Visualization

## Analytics

Most analytic tools are unlikely to require output data storage, as the
**computational effort** needed to process the tool are likely to be
**nominal**, and as such can be executed **on-demand**, allowing for outputs
reflective of the current state of available data.

-   For **example**, a simple analytic tool that takes stage height data from
    hydrologically connected RTHS stations, and produces travel time estimates
    between the two, produces a single data point for each execution.

-   Both the computational **cost** and the storage cost are **nominal**.

-   However, travel time **estimates** for two RTHS stations can **change over
    time** as the bathymetry of the intervening channel evolves, and under
    deferring upstream and downstream flow conditions.

-   **Storage** of the different travel time estimates **can be useful over
    time** to provide insights into the changing topography of the region.

## Visualization

Visualization tools can potentially generate **large volumes** of produced data,
ranging from static **imagery** to **videos**.

-   Visualization tools can also be **off-loaded** for **client-side
    execution**, in which case server-side storage of outputs is not applicable.

-   Visualization is a **core tool** for establishing COP between
    **collaborating decision makers**, and is anticipated to be critical
    component of the operational functionality of REON.cc.

-   Except in the case of large volumes of source data, the **computational
    effort** required to produce the visualization outputs is generally
    **nominal**.

-   A **balance** between ensuring **consistency** in source data between runs,
    and minimizing **latency** between requests for visuals and their
    production, and minimizing storage volumes must be drawn.

-   The **likely approach** will be to establish visualization "**instances**"
    that are **cached** for a prescribed period to ensure all participating
    entities have access to the COP.

# Knowledge

Knowledge refers to the **transformation** of Data and Information through a
fundamental understanding of the **physical**, **chemical** and **biological**
mechanisms into **Actionable Intelligence**.

-   These mechanisms are **represented** as **mathematical** or **statistical
    transformations**, with the resulting outputs being **reproducible**.

-   Several **processing components** are integrated into REON.cc:

    -   Assimilation

    -   Forecasting

## Assimilation

The Assimilation tools are used import or transform Observed Data into the
required format for ingestion into Analytics or other Forecasting tools. The key
application is for "nudging" deterministic tools using timely forcing data.

-   They include routines that retrieve and ingest domain and forcing data for
    themechanistic forecasting tools.

-   Processing capacity needs can be significant, and can increase exponentially
    with the scale of the domain

-   Storage needs can be orders of magnitude greater than the input Data and
    Information used, especially with time-variant computations.

-   Reduction of output storage needs can be significantly reduced by
    transforming it through analytic tools.

## Forecasting

Forecasting tools are differentiated from Analytics primarily in scope and
rigor. Both types of tools can be either Stochastic or Mechanistic, however
forecasting tools are more likely to be both Mechanistic and Deterministic.
Within the context of REON.cc, the immediate application of forecasting tools
will fall under the following categories:

-   Hydrologic Modeling

-   Hydraulic Modeling

-   Urban Stormwater Modeling

## Hydrologic Modeling

Hydrologic modeling focuses on simulation of water quantity in the environment.
Some key elements of hydrologic modeling include:

-   Conservation of Mass: A focus on balancing the amount, or mass, of water in
    the system.

-   Stochastic Processes: Hydrologic processes are often represented as
    Stochastic.

-   Land Surface Models: LSM's are critical in rigorous hydrologic forecasting,
    since forecasts can be significantly influenced by meteorological processes.

-   Groundwater Models: Groundwater Models are necessary components if
    significant interaction is expected between surface water and groundwater.
    Groundwater timescales are often orders of magnitude higher than surface
    water. Exceptions such as Karst formations will often require coupled
    Surface and Groundwater modeling.

-   Hydrologic Routing: Hydrologic routing of surface water is necessary to
    translate land surface Models into lateral transport through defined
    channels. While grid-based land surface Models will allow for lateral
    transport between cells, simulation of channelized flow is necessary under
    most topographic conditions where channelized flow dominates.

-   Hydrologic Models: Several hydrologic models were considered for initial
    incorporation into the REON/WM, including:

    -   WRF-Hydro

    -   HEC-HMS

    -   VIC

### TIER I Real-Time Hydrologic Model

WRF-Hydro was selected for the initial deployment within the REON/WM system for
Tier I modeling because:

-   It is an open-source, community-supported framework, allowing for
    extensibility.

-   It is what the NWC uses for the NWM.

-   Facilitates a pathway for contribution to, and the adoption of, the
    Nextgen-NWM as it matures.

## Hydraulic Modeling

Hydraulic modeling is typically differentiated from Hydrologic Modeling in that
formulations balance system energy rather than mass. This is typically required
in situations where the timescales of transport and transformation phenomena are
short.

Some key elements of hydrologic modeling include:

-   Conservation of Energy: A focus on balancing energy in the system.

-   Mechanistic Processes: Hydraulic systems are often represented as
    combinations of Mechanistic processes.

-   Hydraulic Models: Several hydraulic models were considered for initial
    incorporation into the REON/WM, including:

    -   HEC-RAS

    -   SPRNT

    -   Primo

### Tier II On-Demand Hydraulic Modeling

HEC-RAS was selected for initial deployment in the REON/WM as the Tier II model
because:

-   It is extensively used by practitioners

-   Though closed-source, it is freely available for use by end-users.

-   It enjoys strong and stable development support by the USACE/HEC

## Urban Stormwater Modeling

Urban stormwater modeling typically includes facets of both Hydrologic Modeling
and Hydraulic Modeling, and will often incorporate rudimentary water quality
modeling as well. These models simulate rainfall-runoff, open channel flow and
underground pipe flow to try to capture as much of the urban stormwater
environment as possible. These are complex models requiring a significant amount
of domain data to be effective and useful.

### Tier III Urban Stormwater Modeling

Due to the complexity of the data requirements, urban stormwater modeling is not
expected to be directly linked or embedded into REON.cc.

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
