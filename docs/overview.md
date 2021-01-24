# Microblot Overview

This is the Microblot codebase overview.


## Major Components

Microblot is comprised by several distinct parts:

- CMS app, powering the blogs
- main app, powering the www site
- Slack integration
- built-in URL shortener


### CMS

The visitor side of the application—the various workspace blogs—is powered by a fairly simple CMS living in the `cms` app.
It holds the relevant models (`Blog`, `Author`, `Post`, and `Category`) and views (blog home page, post page, author page, category page, and feeds).


### Main App

The www site houses the project's home page, as well as the requisite flat pages like Terms of Service, Privacy Policy, etc.
It also houses the global blog and its feed and global category pages.


### Slack Integration

The Slack integration is the only input into the system.
It provides endpoints for the various Slack commands (e.g., `/microblot new`) and events (e.g., user profile update), respondes to the interactions as needed (in real-time or via asynchronous worker tasks), and manages CMS relevant content.


### URL Shortener

The built-in URL shortener is just a redirect to full individual posts.
