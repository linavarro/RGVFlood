Determination of Component Interactions
=======================================

.. ifnotslides::

   .. figure:: rgvflood-component-interactions.png
       :name: rgvflood-component-interactions

       RGVFlood Component Interactions

   Three components make :term:`RGVFlood` application ecosystem specific to the :term:`LRGV` (:numref:`rgvflood-component-interactions`).  Hydrologic data specific to the :term:`LRGV`, includes national & state level data, along with locally collected data as well as local forcings from :term:`RTHS.us`. This *RGV Hydrography* is stored in a :term:`REON` :term:`PostgreSQL` database (:term:`REON/db`). The *RGV Water Model* (:term:`REON/WM`), is driven by *RGV Hydrography* and tuned using local forcings from :term:`RTHS.us`. The interface to :term:`REON.cc`, tuned to the specific needs of the :term:`LRGV` users, is accessed from :term:`RGVFlood.com`.

   :term:`RGVFlood` relies on the :term:`REON` cyberinfrastructure, which includes the :term:`RTHS.us` network serving forcing data, station metadata and flood early warning information from the :term:`RTHS` stations. :term:`REON/WM` refers to the ecosystem of hydrologic, hydraulic & stormwater forecast models. These models are defined in Tiers - with Tier I representing the continuous running real-time regional hydrologic forecast model (:term:`WRF-Hydro`), Tier II being an on-demand hydraulic model (:term:`HEC-RAS`), applied to a subset of the region, Tier III being an on-demand hydrologic charactgerization model (:term:`HEC-HMS`), and Tier IV being urban stormwater models such as :term:`SWMM`. Primary user interaction with :term:`RGVFlood` is through the :term:`REON.cc` cybercollaboratory, whic includes a framework of analytic & decision support applications, pulling data through the :term:`GeoNode` :term:`Django` interface as needed. The entire :term:`REON` cyberinfrastructure is data driven, relying on a :term:`PostgreSQL` database server (:term:`REON/db`) with :term:`PostGIS` extensions, storing :term:`REON` specific data for :term:`RTHS`, :term:`REON/WM` and :term:`REON.cc`.
   
   Geospatial content and collaborative services are provided by a :term:`GeoNode` instance. :term:`GeoNode` relies on a geospatial data server (:term:`GeoServer`) to host the data layers, and a :term:`Python` web framework (:term:`Django`) to serve the base user interface. The :term:`Django` user interface is extended with the :term:`REON.cc` web applications. As with :term:`REON`, the :term:`GeoNode` ecosystem is served by a :term:`PostgreSQL` database server (:term:`GeoNode/db`) with :term:`PostGIS` extensions, storing :term:`GeoNode` :term:`Django` and :term:`GeoServer` data. :term:`Django` uses a task scheduling and messaging application (:term:`Celery`) to maximize parallel task processing. The :term:`RGVFlood` instance of :term:`GeoNode` relies on the :term:`NGINX` high performance web server to serve its components.      

.. ifslides::

   .. figure:: rgvflood-component-interactions.png
       :class: full

       RGVFlood Component Interactions

.. slide:: :term:`LRGV`
   :level: 3

   RGV Hydrography
       Hydrologic data specific to the :term:`LRGV`. Includes national & state level data, along with locally collected data as well as local forcings from :term:`RTHS.us`. Data stored in :term:`REON` :term:`PostgreSQL` database

   RGV Water Model
      :term:`REON/WM` driven by RGV Hydrography and tuned using local forcings

   :term:`RGVFlood.com`
       User interface to :term:`REON.cc` tuned to the specific needs of the :term:`LRGV` users.

.. slide:: :term:`RGVFlood`
   :level: 3

   :term:`RTHS.us`
       :term:`RTHS` Network Server, serving forcing data, station metadata and flood early warning information.

   :term:`REON/WM`
       Ecosystem of hydrologic, hydraulic & stormwater forecast models.

   :term:`REON.cc`
       Framework of :term:`REON` analytic & decision support applications, pulling data through the :term:`GeoNode` :term:`Django` interface as needed.

   :term:`REON/db`
       :term:`PostgreSQL` with :term:`PostGIS` extensions database server storing :term:`REON` specific data for :term:`RTHS`, :term:`REON/WM` & :term:`REON.cc` data.

.. slide:: :term:`GeoNode`
   :level: 3

   :term:`Django`
       :term:`Python` web framework upon which :term:`GeoNode` is built.

   :term:`NGINX`
       High performance web server used to serve :term:`GeoNode` components.

   :term:`Celery`
       A task scheduling and messaging application used to maximize parallel task processing.

   :term:`GeoServer`
       Geospatial data server for sharing to :term:`GeoNode` and end-users directly.

   :term:`GeoNode/db`
       :term:`PostgreSQL` with :term:`PostGIS` extensions database server storing :term:`GeoNode` :term:`Django` and :term:`GeoServer` data.
