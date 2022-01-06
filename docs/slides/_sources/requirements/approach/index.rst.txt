Approach
========

-   **GeoNode**: The primary user interface platform will rely on the GeoNode
    open-source geospatial content management system. GeoNode will be extended
    with web applications to provide the tools and services described herein.

-   **Data Ingestion**: Server-side scripts will be developed to automate
    ingestion of Data to maintain currency.

-   **WRF-Hydro**: The WRF-Hydro hydrologic forecast model will run continuously in
    the background. The primary interaction between the WRF-Hydro instance and
    the REON.cc interface will be for visualization of forecast data. The long
    term goal of the hydrologic forecasting tool development process is to be
    model agnostic, allowing for ingestion of forecast data from a variety of
    platforms, including the ability to provide ensemble forecasts.

.. nextslide::

-   **HEC-RAS**: Scripts will be developed to extract and transform Data from the
    WRF-Hydro model to be used in HEC-RAS hydraulic models. Elements of this
    process will include extraction of domain data, including topographic and
    hydraulic survey results, along with hydrologic forecasts, all clipped to
    the target domain. The HEC-RAS model will be run on the client-side
    computer, utilizing the analytics and visualization tools available locally,
    however, a long-term goal will be to provide up-load capability for model
    scenarios and outputs to REON.cc for contribution to the knowledge base and
    potential inclusion in server-side analytics and decision support tools.

.. nextslide::

-   **SWMM**: Similar to HEC-RAS, scripts will be developed to extract and transform
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

.. nextslide::

-   **Dashboard**: The web-portal for REON.cc will provide a dashboard,
    providing information tuned to the users' specific interests and needs. The
    dashboard will also allow for execution of analytics, visualization and
    decision support tools as they are added to the platform.

-   **Notifications**: Critical to promoting user collaboration will be the
    integration of a notification and communication system both between users
    and with processes, including the triggering of early warnings based on the
    RTHS network and forecast tools.
