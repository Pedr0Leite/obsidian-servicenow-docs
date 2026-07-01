---
title: General guidelines for agentic development
description: General guidelines for agentic development on the ServiceNow AI Platform cover prompt writing, context management, compliance validation, and development environment setup.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/vibe-cooding-guidelines.html
release: australia
topic_type: concept
last_updated: "2026-06-05"
reading_time_minutes: 1
keywords: [agentic development, prompt writing, context management, compliance validation, development environment, build agent, developer sandboxes, iterative development, vault console]
breadcrumb: [Explore, Agentic development, Agentic development on the ServiceNow AI Platform, Building applications]
tags:
  - application-development
  - type-concept
---

# General guidelines for agentic development

General guidelines for agentic development on the ServiceNow AI Platform cover prompt writing, context management, compliance validation, and development environment setup.

## Agentic development guidelines

-   Use clear, focused prompts with as much detail as possible to generate more accurate and relevant output.
-   If you're using [[build-agent|Build Agent]], include as much context as possible in your first prompt to enable more robust development. Include roles, data requirements, and success criteria.
-   When switching between two separate applications in Build Agent, specify the new [[c_ApplicationContext|application context]].
-   Save your successful prompts to repurpose and reuse. For more information, see [[vibe-coding-example-prompts|Example prompts for vibe coding and AI-assisted development]].
-   Save your session to quickly resume working where you stopped.
-   Use the Build Agent chat panel for iterative development.
-   Validate compliance using Vault Console to check audit trails and security settings before [[get-started-deployment|deployment]].
-   Develop in a sandbox using [[sandboxes-landing|Developer Sandboxes]] for isolation and safety, or use a Personal Development Instance \(PDI\) or a non-production instance to avoid production deployment.

## Related

- [[vibe-coding-example-prompts|Example prompts for vibe coding and AI-assisted development]]
- [[build-agent|Build Agent]]
- [[c_ApplicationContext|Application context]]
- [[get-started-deployment|Deployment]]
- [[sandboxes-landing|Developer Sandboxes]]
