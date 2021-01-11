# Microblot Overview

High level overview of the major parts and flows making up Microblot.


## Architectural Diagram

```
                                                                      ┌───────────────────────────────┐   
                                                                      │                               │   
                                                                      │           Database            │   
                                                  ┌──────────────────▶│       (Heroku Postgres)       │◀─┐
                                                  │                   │                               │  │
                                                  │                   └───────────────────────────────┘  │
                                                  │                                                      │
                                                  │                   ┌───────────────────────────────┐  │
                                                  │                   │                               │  │
                                                  │                   │  www.microblot.io build hook  │  │
                                                  │                ┌─▶│           (Netlify)           │◀─┤
                                                  │                │  │                               │  │
                                                  │                │  └───────────────────────────────┘  │
                                                  │                │                                     │
┌────────────────────────────┐     ┌────────────────────────────┐  │  ┌───────────────────────────────┐  │
│                            │     │                            │  │  │                               │  │
│    /microblot [command]    │     │    api.microblot.io web    │  │  │  foo.microblot.io build hook  │  │
│          (Slack)           │◀───▶│          (Heroku)          │◀─┼─▶│           (Netlify)           │◀─┤
│                            │     │                            │  │  │                               │  │
└────────────────────────────┘     └────────────────────────────┘  │  └───────────────────────────────┘  │
                                                                   │                                     │
                                                                   │  ┌───────────────────────────────┐  │
                                                                   │  │                               │  │
                                                                   │  │  bar.microblot.io build hook  │  │
                                                                   └─▶│           (Netlify)           │◀─┤
┌────────────────────────────┐     ┌────────────────────────────┐     │                               │  │
│                            │     │                            │     └───────────────────────────────┘  │
│         Slack API          │     │  api.microblot.com worker  │                                        │
│          (Slack)           │◀────│          (Heroku)          │────────────────────────────────────────┘
│                            │     │                            │                                         
└────────────────────────────┘     └────────────────────────────┘                                         
```


## User Flow

1. User runs `/microblot [command]`.
2. Slack makes a request to `api.microblot.io`.
3. `api.microblot.io` coordinates the Slack interaction, using the database as needed.
4. If there's a data change, `api.microblot.io` sends requests to relevant build hooks.
5. Individual sites rebuild.


## Worker Flow

1. Scheduled worker runs.
2. It interacts with Slack as needed.
3. It updates the database as needed.
4. It sends requests to relevant build hooks.
5. Individual sites rebuild.


## Code Change Flow

1. Changes are made to the `main` branch of the Microblot repository.
2. `api.microblot.io` deploys automatically.
3. Upon successful deployment, `api.microblot.io` sends requests to all build hooks:
    1. `www.microblot.io`
    2. individual blogs
4. All sites rebuild.
