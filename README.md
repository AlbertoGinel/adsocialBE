# adSocial Backend

This is a Django-based backend using **Django REST Framework** for API functionality. The backend is deployed on [Railway.app](http://railway.app), and I've already set up an account there.

## Project Structure

Since this is a small app, I kept all the main components within a single file for simplicity and ease of review. The key components of the backend are:

- **Models**: The core of the application is centered around **Influencers**, who can have multiple **Social Media Accounts** and a **Manager**.
- **Views**: All views are handled within a single file, divided into sections for **Influencers**, **Accounts**, and **Managers**.
- **Serializers**: These are used to convert complex data types like Django models into JSON and vice versa.
- **URLs**: The URLs are also defined in this file to route the incoming requests to the correct views.

## Key Models

The main model structure revolves around **Influencers**, each of which can have multiple **Accounts** (social media accounts) and may be assigned a **Manager**. Here are the main models in the application:

1. **Influencer**:
   - Has a `first_name`, `last_name`, and a reference to a **Manager**.
   - Can have multiple **Social Media Accounts**.

2. **Social Media Account**:
   - Linked to an **Influencer**.
   - Stores details about the social media account, including `social_network`, `title`, `username`, `account_url`, and `followers`.

3. **Manager**:
   - Represents an individual who manages one or more **Influencers**.

## CRUD Functionality

The CRUD functionality is basic but fully covers the necessary operations to manage influencers, their accounts, and their managers.

## Views

The views are all handled in a single file and are organized into the following sections:

- **Influencers**: Includes functionality to manage influencers—creating new influencers, fetching them, updating, and deleting them.
- **Accounts**: Includes endpoints for managing social media accounts related to influencers.
- **Managers**: Includes functionality for managing managers and assigning them to influencers.
