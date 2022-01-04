.. slideconf::
   :autoslides: False

Components
==========

.. figure:: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/RATESResearch/RGVFlood/main/docsrc/uml/rgvflood-sequence.uml

   Components of the RGVFlood Platform

.. todo:: 
   
   Explain figure

.. :term:`RGVFlood` is the instantiation of the :term:`REON` Cyberinfrastructure specific to the :term:`LRGV`. :term:`REON.cc` is the framework of :term:`REON` analytic and decision support applications.

.. slide:: Components
   :level: 3
   
   .. figure:: http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/RATESResearch/RGVFlood/main/docsrc/uml/rgvflood-sequence.uml
      :class: full

      Components of the RGVFlood Platform
      
.. slide:: Components
   :level: 3

   :term:`RGVFlood`
      Instantiation of :term:`REON` cyberinfrastructure specific to :term:`LRGV`
   Primary User Interaction 
      Through :term:`REON.cc` for decision support
   :term:`REON.cc`
      Framework of :term:`REON` analytic & decision support applications
   :term:`GeoNode`
      Geospatial content management server, serving & storing geospatial and :term:`RTHS` station metadata
      
.. slide:: Components
   :level: 3
      
   :term:`REON/WM`
      Ecosystem of hydrologic, hydraulic & stormwater forecast models, pulling geospatial data from :term:`GeoNode` and forcing data from :term:`RTHS.us`
   :term:`RTHS.us`
      :term:`RTHS` Network Server, serving forcing data, station metadata and flood early warning information
