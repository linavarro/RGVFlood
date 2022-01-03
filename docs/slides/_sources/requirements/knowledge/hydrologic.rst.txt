Hydrologic Modeling
-------------------

Hydrologic modeling focuses on simulation of water quantity in the environment.
Some key elements of hydrologic modeling include:

-   Conservation of Mass: A focus on balancing the amount, or mass, of water in
    the system.

-   Stochastic Processes: Hydrologic processes are often represented as
    Stochastic.

.. nextslide::

-   Land Surface Models: LSM's are critical in rigorous hydrologic forecasting,
    since forecasts can be significantly influenced by meteorological processes.

.. nextslide::

-   Groundwater Models: Groundwater Models are necessary components if
    significant interaction is expected between surface water and groundwater.
    Groundwater timescales are often orders of magnitude higher than surface
    water. Exceptions such as Karst formations will often require coupled
    Surface and Groundwater modeling.

.. nextslide::

-   Hydrologic Routing: Hydrologic routing of surface water is necessary to
    translate land surface Models into lateral transport through defined
    channels. While grid-based land surface Models will allow for lateral
    transport between cells, simulation of channelized flow is necessary under
    most topographic conditions where channelized flow dominates.

.. nextslide::

-   Hydrologic Models: Several hydrologic models were considered for initial
    incorporation into the REON/WM, including:

    -   WRF-Hydro

    -   HEC-HMS

    -   VIC

.. nextslide::

**TIER I Real-Time Hydrologic Model**: WRF-Hydro was selected for the initial deployment within the REON/WM system for Tier I modeling because:

-   It is an open-source, community-supported framework, allowing for extensibility.

-   It is what the NWC uses for the NWM.

-   Facilitates a pathway for contribution to, and the adoption of, the Nextgen-NWM as it matures.
