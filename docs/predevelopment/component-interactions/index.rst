Component Interactions
======================

.. ifnotslides::

   .. figure:: rgvflood-component-interactions.png
       :name: rgvflood-component-interactions

       RGVFlood Component Interactions

   Three components make :term:`RGVFlood` application ecosystem specific to the :term:`LRGV` (:numref:`rgvflood-component-interactions`).  Hydrologic data specific to the :term:`LRGV`, includes national & state level data, along with locally collected data as well as local forcings from :term:`RTHS.us`. This *RGV Hydrography* is stored in a :term:`REON` :term:`PostgreSQL` database. The *RGV Water Model* (:term:`REON/WM`), is driven by RGV Hydrography and tuned using local forcings from :term:`RTHS.us`. The user interface to :term:`REON.cc` tuned to the specific needs of the :term:`LRGV` users is accessed from :term:`RGVFlood.com`.
   
   :term:`RGVFlood` relies on the :term:`REON` cyberinfrastructure, which includes the :term:`RTHS.us` serving forcing data, station metadata and flood early warning information from the :term:`RTHS` stations.
   
   :term:`REON/WM`
       Ecosystem of hydrologic, hydraulic & stormwater forecast models.

   :term:`REON.cc`
       Framework of :term:`REON` analytic & decision support applications, pulling data through the :term:`GeoNode` :term:`Django` interface as needed.

   :term:`REON/db`
       :term:`PostgreSQL` with :term:`PostGIS` extensions database server storing :term:`REON` specific data for :term:`RTHS`, :term:`REON/WM` & :term:`REON.cc` data.

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
