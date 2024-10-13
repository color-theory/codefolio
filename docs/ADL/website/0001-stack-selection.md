---
# These are optional metadata elements. Feel free to remove any of them.
status: "proposed"
date: {10-12-2024}
decision-makers: {John Stringer}
consulted: {Myself, The internet, Colleagues}
---

# {Use MERN Stack for Website}

## Context and Problem Statement

Need to decide what stack to use for front end and backend for the website.

<!-- This is an optional element. Feel free to remove. -->
## Decision Drivers

* Needs to be lightweight enough to host on my limited AWS creds.
* Performance is important. Caching?
* Modernity and Popularity of stack are important for this project.
* Allows me to show off my full-stack skills.

## Considered Options

* MERN
* Serverless
* LAMP
* Hybrid

## Decision Outcome

Chosen option: Hybrid because it combines some of the most popular front and backend technologies,
allows me to show that I can design systems that integrate multiple frameworks, and allows me to show off my full-stack chops.
I will likely use nginx for reverse proxy, load balancing, and general front end static web hosting. This will allow me to
point to any type of service I can create on the backend, and provides strong configuration for Security.

Instead of using express for the backend, I will likely use a combination of technologies where it matters.
For example, in order to leverage kafka streams, I will probably use Java. But for some standard web api, I will probably use
.NET or express. 

### Consequences

* Good, because it will cover a lot of the technologies for which I may be required to know at a new job. The frameworks available
for this stack are modern and widely supported.
* Good, because it gives me the flexibility to change my mind and settle with one tech if I decide to do so.
* Bad, because it is a bit overkill for a single website, it will require more boilerplate to implement, may cost a bit more to host
than other alternatives, and will require me to completely overhaul my current server configuration.
* Bad, because there is a risk that showing how I can leverage all kinds of languages may be detrimental in applications
where someone wishes to see expertise in one language.
