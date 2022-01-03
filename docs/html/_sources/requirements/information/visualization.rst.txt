.. slideconf::
   :autoslides: False

Visualization
-------------

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

.. slide:: Visualization
   :level: 3

   Visualization tools can potentially generate **large volumes** of produced data,
   ranging from static **imagery** to **videos**.

   -   **off-loaded** for **client-side execution**

   -   **core tool** for :term:`COP` between **collaborating decision makers**

   -   Changing source data: **balance** between **consistency** and **latency**

   -   **cached** visualization **instances**
