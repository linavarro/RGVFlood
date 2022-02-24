Platform Instantiation
======================

Container Configuration
-----------------------

RGVFlood is instantiated via a Docker Container stack providing the following services:

:celery: a powerful asynchronous job queue used for running tasks in the background.
:db: an instance of PostGIS, a spatially enabled relational database manager.
:django: a Python web framework upon which RGVFlood is built.
:docs: an nginx static web page server for the documentation.
:geoserver: a geospatial data server.
:gsconf: a service specifically for initially provisioning the geospatial data server.
:letsencrypt: a service for securing and maintaining an SSL certificate
:nginx: a high performance web server.
:rabbitmq: a message proker used by celery for inter-task communication.
:slides: an nginx static web page server for the documentation slides.

GeoNode
-------

The GeoNode application is installed in the **django** container, using the PostGIS database server in the **db** container to store both mode and geospatial data used by the **geoserver** container.

Documentation
-------------

Project documentation is developed in parallel to the application development and produced for deployment simultaneously. Sphinx is used for documentation production, permitting both HTML and PDF deloyment in concert. Hieroglyph is used to co-produce slides from the documentation.

REON
----

The core REON applications, developed and maintained independent of this project, are ingested into the GeoNode application at container instantiation time. RTHS data is provisioned at this time, and updated periodically for currency.

RGVFlood
--------

RGVFlood is the result on integration of all the above elements along with project specific applictions such as the Tier 1 and Tier 2 model integrations, and LRGV-specific analytics.

