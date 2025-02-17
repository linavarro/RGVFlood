Specification of Use Case Scenarios
===================================

.. ifnotslides::

   .. figure:: rgvflood-use-cases.png
       :name: rgvflood-use-cases

       RGVFlood Use Cases

   :numref:`rgvflood-use-cases` depicts the most commonly anticipated user-cases for :term:`RGVFlood`. The primary intended use for :term:`RGVFlood` is to facilitate multi-jurisdictional decision making, with jurisdictions of varying sizes, needs and capacities being able to participate with equal impact or influence. Represented in :numref:`rgvflood-use-cases` are 2 jurisdictions, *JurisdictionA* and *JurisdictionB*. *JurisdictionA* represents a local government with significant capacity, including in-house engineering, whereas *JurisdictionB* represents one of lesser capacity or resources, where the elected officials perform operational duties in addition to decision and/or policy-making. *JurisdictionB* also relies on consultants for engineering services. Within each jurisdiction are also local or regional planners, and first responders and/or emergency managers.

   Decision makers are typically elected officials on whom the burden of inter-jurisdictional decision making rests. While their primary responsibility is to the constituents who elected them to public office, effective flood management requires adoption of a supra-jurisdictional perspective to accommodate implementation strategies that maximize regional values first before local or parochial priorities. Both decision maker and constituency education is a requirement for sustaining this approach, the first to enable knowledge-based decision making and the second in order to protect the elected officials' credibility with their voters. Elected officials' incentives are two-fold, first to protect the life and property of thier constituents from the impacts of floods, and second to recruit additional (i.e. external) resources and funds to effect this. Both of these are promoted by instantiating policies that promote regional strategies and by pursuing large-scale capital improvement projects to effect regional flood management while taking advantage of economies of scale.

   Federal agencies such as :term:`FEMA` and :term:`USACE`, and state agencies such as :term:`TGLO` and :term:`TWDB`, provide financial and technical resources for flood response, recovery and resiliency planning. Jurisdictional and multi-jurisdictional planners needing to make both operational and strategic decisions in coordination with elected officials looking towards these agencies for access to these resources, need regional flood intelligence and inter-jurisdictional collaborative tools provided by :term:`RGVFlood` in order to be competitive.

   Hydrologic and hydraulic modeling are data intensive efforts, requiring the collection and ground-truthing of domain data as a precursor to model execution and calibration. A key goal for the Tier I (:term:`WRF-Hydro`) :term:`REON/WM` infrastructure is the provision of both baseline domain data and forecast-driven forcing data for the Tier II (:term:`HEC-RAS`), Tier III (:term:`HEC-HMS`) & Tier IV (:term:`SWMM`) supported models for design development or review. Research engineers and hydrologists are likely use the :term:`REON/WM` :term:`WRF-Hydro` instance directly, along with real time data from :term:`RTHS.us`.

   Emergency management agencies and first responders will be able to utilize early warning information generated by the :term:`RTHS` stations themselves, or from :term:`REON.cc` utilizing higher order analytics. Simple triggers built into the :term:`RTHS` stations themselves wl be able to notify relevant authorities upon the detection of a critical event such as a rapid rise in water level. Higher order analytics embedded in :term:`REON.cc` will allow more sophisticated alerts such as earlier warnings based on travel times between sequential :term:`RTHS` stations.
       
.. slide:: Use Cases
   :level: 3

   .. figure:: rgvflood-use-cases.png
      :class: full

      RGVFlood Use Cases

.. slide:: Stakeholders
   :level: 3

   Decision Makers
      Elected officials responsible for regional policy making and recruitment of state & federal funds.

   Planners
      Jurisdictional and multi-jurisdictional planners needing to make both operational and strategic decisions in coordination with Elected officials.

   Federal Agencies
      Agencies such as :term:`FEMA` and :term:`NWS` that provide financial and technical resources for flood response, recovery & resiliency planning.

   State Agencies
      Agencies such as :term:`TGLO` and :term:`TWDB` that provide financial and technical resources for flood response, recovery & resiliency planning.

.. slide:: Stakeholders
   :level: 3

   First Responders
      Emergency Management Agencies and First Responders utilizing Early Warning information generated by the :term:`RTHS` stations themselves, or from :term:`REON.cc` utilizing higher order analytics.

   Engineers
      Both public sector and private sector engineers, relying on the :term:`REON/WM` Tier II (:term:`HEC-RAS`), Tier III (:term:`HEC-HMS`) & Tier IV (:term:`SWMM`) supported models for design development or review.

   Researchers
      Research engineers and hydrologists are likely use the :term:`REON/WM` :term:`WRF-Hydro` instance directly, along with real time data from :term:`RTHS.us`.
