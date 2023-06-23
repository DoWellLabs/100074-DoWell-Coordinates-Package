=============================
Geometrical Layout Reference
=============================

This page contains specific information on the GeometricalLayout's class, and methods 

class geometrical_layout.GeometricalLayoutApi
==============================================

A client for the Dowell Geometrical Layout of Big Data API.
The API provides endpoints to help users calculate the optimal
arrangement of non-overlaping circles within a given canvas.
By specifying the radius, length, and width, this client help users to determine the number of circles
that can be arranged in a triangular packaging, minimizing wastage of space.
The coordinates of the circle can also be determine.

You can read more about here `Geometrical Layout Api`_



**Example**

.. code-block:: python

    from geometrical_layout import GeometricalLayoutApi
    req = GeometricalLayoutApi()


Methods
-------

post_object
^^^^^^^^^^^^
The endpoint receive a json object of radius, length, width.
Resonse is ``dict`` containing number of circles and coordinates. 


**Parameters**

* ``radius`` - A ``float`` or an ``int`` that identifies a circle radius, is needed
  to make API calls.
 
* ``length`` - An ``int`` denoting the length of the space in canvas

* ``width`` - A ``int`` denoting the length of the space in canvas.
  is the last parameter needed to make API request.


**Examples**

.. code-block:: python

    # Get the number of circles from the response.
    numberOfcircle = req.post_object(radius, length, width)
    print(numberOfcircle)



.. _Geometrical Layout Api: https://github.com/DoWellUXLab/DoWell-Geometrical-layout-of-Big-Data
