# AWM2021 Assignment 1

[www.joelkell.xyz](https://www.joelkell.xyz)

For your assignment, you are required to create and deploy a location-based services (LBS) application which exercises the technologies we have been studying. The main objective of this assignment is to very that you can create, build and deploy an location-based web application to a cloud-facing server in a secure manner.

## To build your application you are required to use:
* Database: PostgreSQL with PostGIS
* Database management: PgAdmin4
* Middle tier(s): Django
* Front-end: Web application which presents well on any device. This is known as responsive design. You can use any framework you like for layout such as jQueryMobile, Ionic, Bootstrap etc. I recommend Bootstrap v4 for simplicity and ease of use.
* Mapping: Leaflet JS with OpenStreetMap
* Deployment (middle tier(s) & database): Use Docker to create an isolated network (subnet), a set of images for your components (Django, PostGIS, PgAdmin4, Nginx) and deploy instances of these making sure that data which is required to be persistent is managed appropriately.. 

## Content
For this phase, the idea is to ensure that you can connect the various components. The idea is to build an application that has a location-based or mapping component. To this end, it is required to:

1. Create/store/manipulate spatial data, hence PostgreSQL/PostGIS.
2. Create a middle layer based on the Model-View-Controller (MVC) pattern, hence Django.
3. Create an application, usable on any platform, hence responsive design.
4. Be accessible securely from the Web, hence cloud deployment