.. slideconf::
   :autoslides: False

Component Interactions
======================

.. figure:: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/RATESResearch/RGVFlood/main/docsrc/uml/rgvflood-component-interactions.uml

   RGVFlood Component Interactions

.. todo::

   Explain figure and components

.. slide:: Component Interactions
   :level: 3

   .. figure:: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/RATESResearch/RGVFlood/main/docsrc/uml/rgvflood-component-interactions.uml
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
  
   .. todo::
      
      GeoNode components