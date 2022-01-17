Identification of Critical Software & Hardware Components
=========================================================

.. ifnotslides::

   .. figure:: rgvflood-sequence.png
       :name: rgvflood-sequence

       Components of the RGVFlood Platform

   :numref:`rgvflood-sequence` depicts the components of RGVFlood. Primary user interaction is through :term:`REON.cc` for decision support, although emergency managers and first responders may be provided alerts directly from :term:`RTHS` stations. Access to :term:`REON/WM` will also be provided for research purposes.

   :term:`RGVFlood` is an instantiation of :term:`REON` cyberinfrastructure specific to :term:`LRGV`, utilizing  the :term:`REON.cc` framework of :term:`REON` analytic & decision support applications. :term:`REON.cc` utilizes the :term:`GeoNode` geospatial content management server, which serves and stores geospatial and :term:`RTHS` station metadata.

   :term:`REON/WM` refers to the ecosystem of hydrologic, hydraulic & stormwater forecast models, pulling geospatial data from :term:`GeoNode` and forcing data from :term:`RTHS.us`, the :term:`RTHS` network server, which collects real-time hydrologic and water quality data, and serve forcing data and station metadata to the models and flood early warning information to emergency managers and first responders.

.. ifslides::

   .. figure:: rgvflood-sequence.png
       :class: full

       Components of the RGVFlood Platform

.. slide:: RGVFlood Components
   :level: 3

   :term:`RGVFlood`
       Instantiation of :term:`REON` cyberinfrastructure specific to :term:`LRGV`

   Primary User Interaction
       Through :term:`REON.cc` for decision support

   :term:`REON.cc`
       Framework of :term:`REON` analytic & decision support applications

   :term:`GeoNode`
       Geospatial content management server, serving & storing geospatial and :term:`RTHS` station metadata

   .. nextslide::
      :increment:

   :term:`REON/WM`
       Ecosystem of hydrologic, hydraulic & stormwater forecast models, pulling geospatial data from :term:`GeoNode` and forcing data from :term:`RTHS.us`

   :term:`RTHS.us`
       :term:`RTHS` Network Server, serving forcing data, station metadata, and flood early warning information
